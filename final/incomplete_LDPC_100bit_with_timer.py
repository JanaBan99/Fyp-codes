from machine import ADC, Pin, Timer
import time
import utime
from machine import RTC
import os

decoded_bit_string = []
voltages = []
adc_values = []
threshold_adc = 850
threshold=[]
binary_values=[]
# Define analog input pin
ANALOG_IN_PIN = 28

# Floats for resistor values in the divider (in ohms)
R1 = 30000.0
R2 = 7500.0

# Float for Reference Voltage
ref_voltage = 3.3

# Setup ADC
adc = ADC(Pin(ANALOG_IN_PIN))

# Timer define
timer_edge_detection = Timer()
timer_adc_sampling = Timer()

def Data(bit_stream_2,differences):
    file_path = "without_encoding_100.csv"
    file_exists = False
    try:
        with open(file_path, "r"):
            file_exists = True
    except OSError:
        file_exists = False
    
    with open(file_path, "a") as file:
        # Write header if file is empty
        if not file_exists:
            file.write("Received Bits,Differences\n")
        # Write data and differences
        file.write(f"{bit_stream_2},{differences}\n")

    file.close()
    
def read_adc_value():
    # Read the analog input
    return adc.read_u16()

def edge_detection(timer):
    global previous_adc_value
    #print(previous_adc_value)
    current_adc_value = read_adc_value()
    if current_adc_value > previous_adc_value + threshold_adc:# Edge rise threshold
        print(current_adc_value)
        print("Rising edge detected")
        timer_edge_detection.deinit()
        timer_adc_sampling.init(period=10, mode=Timer.PERIODIC, callback=check)
    previous_adc_value = current_adc_value
        #print(previous_adc_value)
def check(timer):
    global adc_values
    
    if len(adc_values) <210:
        input_adc_value = read_adc_value()
        print(f"ADC Read: {input_adc_value}")
        adc_values.append(input_adc_value)
    else:
        timer_adc_sampling.deinit()  # Deinitialize the timer after collecting 109 readings
        print("ADC values:", adc_values)
        calculate_voltages(adc_values)

def calculate_voltages(adc_values):
    voltages = [(adc_value / 65535) * ref_voltage for adc_value in adc_values]
    in_voltages = [adc_voltage * (R1 + R2) / R2 for adc_voltage in voltages]
    print("Voltages:", in_voltages)
    calculate_threshold(in_voltages)

def calculate_threshold(in_voltages):
    global threshold, binary_values
    first_five_average = sum(in_voltages[:5]) / 5
    threshold = first_five_average - (0.58 * first_five_average)
    print("Threshold Value = {:.6f}".format(threshold))

    binary_values=[1 if adc_voltage > threshold else 0 for adc_voltage in in_voltages]
    print("Binary values based on threshold comparison:", binary_values)
    initialization_bits=binary_values[:10]
    data_bits=binary_values[10:]
    bit_stream_1 = ''.join(map(str, initialization_bits))
    #print("Initialization_Bits", bit_stream_1)
    print()
    bit_stream_2=''.join(map(str, data_bits))
    print("Data_Bits:", bit_stream_2)
    LDPC_decording(bit_stream_2)
    checkBits(bit_stream_2)
    

def checkBits( bit_stream_2):
    global decoded_bit_string
    transmittedBits= '11111010010111001111101001011100011011011100010001011100111110100110110101010011111101011010100111110101010100111111010111000100011011011010011011110101111110101010011011111010111101011111101010100110'
    #transmittedBits= '101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101'
    print()
    print("Transmitted_Bits:",transmittedBits)
    print()
    print("Transmitted bits length:", len(transmittedBits))
    print("Received Bits length:", len(bit_stream_2))

    if len(transmittedBits) != len(bit_stream_2):
        raise ValueError("Bit streams must have the same length")

    difference1 = sum(1 for b1, b2 in zip(transmittedBits, bit_stream_2) if b1 != b2)
    print("Number of differences between the two bit streams:", difference1)
    print('************************************************************')
    #Data(bit_stream_2,differences)

    EncodedBits= '101011001010110011010100110010101101001101011001010100110101010011010110010110100110101001011010110'
    #transmittedBits= '101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101'
    total_decoded_string = decoded_bit_string[0]
    print()
    print("Original_Bits:",EncodedBits)
    print("Received_decoded_Bits:", total_decoded_string)
    print()
    print("Transmitted bits length:", len(EncodedBits))
    print("Received Bits length:", len(total_decoded_string))

    if len(EncodedBits) != len(total_decoded_string):
        raise ValueError("Bit streams must have the same length")

    difference2 = sum(1 for b1, b2 in zip(EncodedBits, total_decoded_string) if b1 != b2)
    print("Number of differences between the two bit streams:", difference2)
    print('************************************************************')


def LDPC_decording(codeword):
    global decoded_bit_string
                 #101011001010110011010100110010101101001101011001010100110101010011010110010110100110101001011010011
    #codeword = '11111010010111001111101001011100011011011100010001011100111110100110110101010011111101011010100111110101010100111111010111000100011011011010011011110101111110101010011011111010111101011111101010100110'
    P = [[1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1]]

    def transpose(X):
        transpose = [[0, 0, 0, 0] for _ in range(len(X))]

        try:
            cols_A = len(X[0])
        except TypeError:
            cols_A = len(X)

        # Compute the transpose
        for i in range(len(X)):
            for j in range(cols_A):
                transpose[j][i] = X[i][j]

        return transpose

    Transpose_P = transpose(P)
    #print("Transpose of P :", Transpose_P)

    #Identity matrix generation
    identity_matrix = []
    for i in range(4):
        # Initialize an empty row
        row = []
        # Loop over each column in the current row
        for j in range(len(P[1])):
            # If row index is equal to column index, set element to 1
            if i == j:
                row.append(1)
            # Otherwise, set element to 0
            else:
                row.append(0)
                # Append the row to the matrix
        identity_matrix.append(row)

    #print("Identity Matrix: ", identity_matrix)

    Parity_check_matrix = []
    for k in range(4):
        identity_matrix[k].extend(Transpose_P[k])
        Parity_check_matrix.append(identity_matrix[k])

    print("Parity check Matrix: ", Parity_check_matrix) 

    def transpose_matrix(matrix):
    # Get the number of rows and columns in the original matrix
        rows = len(matrix)
        cols = len(matrix[0])
    
        # Create a new matrix with the dimensions swapped
        transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
        # Fill the new matrix with transposed values
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]
    
        return transposed

    Transpose_Parity_check_matrix = transpose_matrix(Parity_check_matrix)
    print("Transpose of the Parity Check Matrix", Transpose_Parity_check_matrix)
    
    Syndrome = []
    segments = [codeword[i:i+8] for i in range(0, len(codeword), 8)]
    print("segment: ", segments)
    # Convert each 8-bit segment into a list of integers
    r = [[int(bit) for bit in segment] for segment in segments]

    for j in range(len(r)):
        a = []  # Initialize a new list for each syndrome calculation
        for i in range(0, 4):
            a.append(
                r[j][0] * Transpose_Parity_check_matrix[0][i] ^ 
                r[j][1] * Transpose_Parity_check_matrix[1][i] ^ 
                r[j][2] * Transpose_Parity_check_matrix[2][i] ^ 
                r[j][3] * Transpose_Parity_check_matrix[3][i] ^ 
                r[j][4] * Transpose_Parity_check_matrix[4][i] ^ 
                r[j][5] * Transpose_Parity_check_matrix[5][i] ^ 
                r[j][6] * Transpose_Parity_check_matrix[6][i] ^ 
                r[j][7] * Transpose_Parity_check_matrix[7][i]
            )
        Syndrome.append(a)

    print("Syndrome: ", Syndrome)
    
    Corrected_bits = []
    
    for j in range(len(r)):
        a = []
        if Syndrome[j] == [0, 0, 0, 0]: #Has no errors
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            #print(c)
            a = c
            #a.append(segments[j])
            #print(a)
            
        elif Syndrome[j][0]== 1 & Syndrome[j][1] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[0, 0, 0, 0, 0, 1, 0, 0]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)
            
        elif Syndrome[j][1]== 1 & Syndrome[j][2] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[0, 0, 0, 0, 0, 0, 1, 0]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)
            
        elif Syndrome[j][2]== 1 & Syndrome[j][3] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[0, 0, 0, 0, 0, 0, 0, 1]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)
            
        elif Syndrome[j][0]== 1 & Syndrome[j][3] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[0, 0, 0, 0, 1, 0, 0, 0]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)
    
        elif Syndrome[j][3] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[0, 0, 0, 1, 0, 0, 0, 0]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)
        
        elif Syndrome[j][2] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[0, 0, 1, 0, 0, 0, 0, 0]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)    
            
        elif Syndrome[j][1] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[0, 1, 0, 0, 0, 0, 0, 0]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)
            
        elif Syndrome[j][0] == 1:
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            print("****************************")
            print(c)
            b=[1, 0, 0, 0, 0, 0, 0, 0]
            a = [x ^ y for x, y in zip(c, b)]
            print(a)
            print(j)        
        
        Corrected_bits.append(a)
    #print("Corrected bits: ", Corrected_bits)
    
    print("Corrected bits: ",Corrected_bits)
    decoded_bit_string.append(Corrected_bits)

def Data(LDPC_encoded_bits,difference2,transmitted_codeword,difference1):
    file_path = "LDPC_with.csv"
    file_exists = False
    try:
        with open(file_path, "r"):
            file_exists = True
    except OSError:
        file_exists = False
    
    with open(file_path, "a") as file:
        # Write header if file is empty
        if not file_exists:
            file.write("Received_bits,Error_received,Decoded_bits,Error_decoded\n")
            
        # Write data and differences
        file.write(f"{LDPC_encoded_bits},{difference2},{transmitted_codeword},{difference1}\n")
    file.close()

try:
    def main():
        global previous_adc_value
        previous_adc_value = read_adc_value()
        #print(previous_adc_value)
        # Initialize the edge detection timer
        timer_edge_detection.init(period=10, mode=Timer.PERIODIC, callback=edge_detection)

        print("Starting edge detection...")
except:
    timer.deinit()
    print("error occured")
    
if __name__ == "__main__":
    main()







