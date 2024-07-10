from machine import ADC, Pin
import time
import utime
from machine import RTC
import os

# Define analog inputs
ANALOG_IN_PIN = 28

# Floats for resistor values in divider (in ohms)
R1 = 30000.0
R2 = 7500.0

# Float for Reference Voltage
ref_voltage = 3.3
all_bits =[]
# Setup ADC
adc = ADC(Pin(ANALOG_IN_PIN))

def Data(received_bits, differences):
    file_path = "without_encoding_10.csv"
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
        file.write(f"{received_bits},{differences}\n")

    file.close()

def read_voltage():
    # Read the analog input
    adc_value = adc.read_u16()
    
    # Determine voltage at ADC input
    adc_voltage = (adc_value / 65535) * ref_voltage
    
    # Calculate voltage at divider input
    in_voltage = adc_voltage * (R1 + R2) / R2
    
    return in_voltage

def edge_detection():
    previous_voltage = read_voltage()
    
    time.sleep(0.01)
    
    while True:
        current_voltage = read_voltage()
        print(current_voltage)
        if current_voltage > previous_voltage+5:  # value was 5 up to 60 cm Edge rise threshold
            print("Rising edge detected")
            break
        previous_voltage = current_voltage
        time.sleep(0.1)

def main():
    voltages = []  # Array to store voltage values
    Bits = []
    #threshold_value=False 
    while len(voltages) < 10:
        #start_time = time.time()

        #while len(samples) < 10:
        input_voltage = read_voltage()
        #print(" >>>>>>>>>>>>>>>>>>>>Input Voltage = {:.2f}".format(input_voltage))
        voltages.append(input_voltage)
        #print("Received voltages :",voltages)
        time.sleep(0.1)

    #print("123")
    print("Received voltages :",voltages)
    # Calculate threshold from last 5 values
    first_five_average = sum(voltages[:5]) / 5
    threshold = first_five_average - (0.58 * first_five_average)
    #threshold = 0.42 * first_five_average
    print("Threshold Value = {:.6f}".format(threshold))
    threshold_value=True
    
    # Array to store binary values based on threshold comparison
    binary_values = []

    # Compare voltage values with threshold
    for voltage in voltages:
        if voltage > threshold:
            binary_values.append(1)
        else:
            binary_values.append(0)

    print("Binary values based on threshold comparison:", binary_values)

    # Check if the binary sequence matches the specified pattern
    if binary_values == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]:
        print("Proceeding to the next part...")
    else:
        print("Session terminated.")
        #return

    
        # Sampling and calculating average for 1 second
        #samples = []
        #start_time = time.time()
    if threshold_value==True:
        voltages = []  # Array to store voltage values
        binary_values = []
        while len(voltages) <150:
            #start_time = time.time()
           
            input_voltage = read_voltage()
            
            #print(" >>>>>>>>>>>>>>>>>>>>Input Voltage = {:.2f}".format(input_voltage))
            voltages.append(input_voltage)
            time.sleep(0.1)
        print("dataword Voltage =",voltages)
        for voltage in voltages: 
            if voltage > threshold:
                binary_values.append(1)
            else:
                binary_values.append(0)

    print("Binary values based on threshold comparison:", binary_values)
            
    #print("Received Bits: ", Bits)
    received_bits = ''.join(map(str, binary_values))
    all_bits.append(received_bits)
    print(received_bits)
    
    print("Received Bits:    [", received_bits, "]", sep='')

def main2():
    voltages = []  # Array to store voltage values
    Bits = []
    #threshold_value=False 
    while len(voltages) < 10:
        #start_time = time.time()

        #while len(samples) < 10:
        input_voltage = read_voltage()
        #print(" >>>>>>>>>>>>>>>>>>>>Input Voltage = {:.2f}".format(input_voltage))
        voltages.append(input_voltage)
        #print("Received voltages :",voltages)
        time.sleep(0.1)

    #print("123")
    print("Received voltages :",voltages)
    # Calculate threshold from last 5 values
    first_five_average = sum(voltages[:5]) / 5
    threshold = first_five_average - (0.58 * first_five_average)
    #threshold = 0.42 * first_five_average
    print("Threshold Value = {:.6f}".format(threshold))
    threshold_value=True
    
    # Array to store binary values based on threshold comparison
    binary_values = []

    # Compare voltage values with threshold
    for voltage in voltages:
        if voltage > threshold:
            binary_values.append(1)
        else:
            binary_values.append(0)

    print("Binary values based on threshold comparison:", binary_values)

    # Check if the binary sequence matches the specified pattern
    if binary_values == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]:
        print("Proceeding to the next part...")
    else:
        print("Session terminated.")
        #return

    
        # Sampling and calculating average for 1 second
        #samples = []
        #start_time = time.time()
    if threshold_value==True:
        voltages = []  # Array to store voltage values
        binary_values = []
        while len(voltages) <144:
            #start_time = time.time()
           
            input_voltage = read_voltage()
            
            #print(" >>>>>>>>>>>>>>>>>>>>Input Voltage = {:.2f}".format(input_voltage))
            voltages.append(input_voltage)
            time.sleep(0.1)
        print("dataword Voltage =",voltages)
        for voltage in voltages: 
            if voltage > threshold:
                binary_values.append(1)
            else:
                binary_values.append(0)

    print("Binary values based on threshold comparison:", binary_values)
            
    #print("Received Bits: ", Bits)
    received_bits = ''.join(map(str, binary_values))
    all_bits.append(received_bits)
    print(received_bits)
    
    print("Received Bits:    [", received_bits, "]", sep='')

if __name__ == "__main__":
    print()
    print("Starting 1st edge detection...")
    edge_detection()
    print("Starting main function...")
    main()
    #utime.sleep_ms(100)
    print()
    print("Starting 2nd edge detection...")
    edge_detection()
    print("Starting main function...")
    main()
    #utime.sleep_ms(100)
    print()
    print("Starting 3rd edge detection...")
    edge_detection()
    print("Starting main function...")
    main()
    #utime.sleep_ms(100)
    print()
    
    
    
    print("Starting 4th edge detection...")
    edge_detection()
    print("Starting main function...")
    main2()
    print()
    print("all bits:", all_bits)
    
    bitstream = ''.join(all_bits)

    print("Total Bitstream:",bitstream)



