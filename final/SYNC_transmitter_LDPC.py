import machine
import utime

#Define GPIO pins
led_pin = machine.Pin(16, machine.Pin.OUT)

initial_word = '1111100000'

def send_data_word(output_status_array):
    
    
    a = output_status_array[:150]
    b = output_status_array[150:300]
    c = output_status_array[300:450]
    d = output_status_array[450:]

    for bit in initial_word:  # Transmit initial 10 bits
        led_pin.value(int(bit))  # Set the LED state base3d on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)  
    print()
    
    for bit in a:  
        led_pin.value(int(bit))  # Set the LED state based on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)
    print()
    led_pin.value(0)
    utime.sleep_ms(200)
    for bit in initial_word:  # Transmit initial 10 bits
        led_pin.value(int(bit))  # Set the LED state base3d on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)  
    print()
    
    for bit in b:  
        led_pin.value(int(bit))  # Set the LED state based on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)
    print()
    led_pin.value(0)
    utime.sleep_ms(200)
    for bit in initial_word:  # Transmit initial 10 bits
        led_pin.value(int(bit))  # Set the LED state base3d on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)  
    print()
    
    for bit in c:  
        led_pin.value(int(bit))  # Set the LED state based on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)
    print()
    led_pin.value(0)
    utime.sleep_ms(200)
    for bit in initial_word:  # Transmit initial 10 bits
        led_pin.value(int(bit))  # Set the LED state base3d on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)  
    print()
    
    for bit in d:  
        led_pin.value(int(bit))  # Set the LED state based on the bit
        print(bit, end='')  # Print the transmitting bit
        utime.sleep_ms(100)
    print()
#Data(data_word)
led_pin.value(0)  # Turn off the LED



def process_data(dataword):
    # Function to process the dataword using the given logic

    # Define the initial states and arrays
    Current_status = [0, 0, 0]
    output_status_array = []


    separate_arrays = []
    for i in range(0, len(dataword), 3):
        separate_arrays.append(dataword[i:i+3])
        
    #print("Separate Array:", separate_arrays)

    # Process each separate array
    for input_codeword in separate_arrays:
        input_codeword.extend([0, 0, 0]) 
        #print("Input Codeword:", input_codeword)

        # Process each input codeword
        for Input in input_codeword:
            if Current_status == [0, 0, 0] and Input == 0:
                Output_status = [0, 0, 0]
                Current_status = [0, 0, 0]
                output_status_array.extend(Output_status)

            elif Current_status == [0,0,0] and Input == 1:
                Output_status = [1,1,1]
                Current_status = [1,0,0]
                output_status_array.extend(Output_status)
        
            ############## 
        
            elif Current_status == [0,0,1] and Input == 0:
                Output_status = [1,0,1]
                Current_status = [0,0,0]
                output_status_array.extend(Output_status)
        
            elif Current_status == [0,0,1] and Input == 1:
                Output_status = [0,1,0]
                Current_status = [1,0,0]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [0,1,0] and Input == 0:
                Output_status = [1,1,1]
                Current_status = [0,0,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [0,1,0] and Input == 1:
                Output_status = [0,0,0]
                Current_status = [1,0,1]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [0,1,1] and Input == 0:
                Output_status = [0,1,0]
                Current_status = [0,0,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [0,1,1] and Input == 1:
                Output_status = [1,0,1]
                Current_status = [1,0,1]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,0,0] and Input == 0:
                Output_status = [1,1,0]
                Current_status = [0,1,0]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,0,0] and Input == 1:
                Output_status = [0,0,1]
                Current_status = [1,1,0]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,0,1] and Input == 0:
                Output_status = [0,1,1]
                Current_status = [0,1,0]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,0,1] and Input == 1:
                Output_status = [1,0,0]
                Current_status = [1,1,0]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,1,0] and Input == 0:
                Output_status = [0,0,1]
                Current_status = [0,1,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,1,0] and Input == 1:
                Output_status = [1,1,0]
                Current_status = [1,1,1]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,1,1] and Input == 0:
                Output_status = [1,0,0]
                Current_status = [0,1,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,1,1] and Input == 1:
                Output_status = [0,1,1]
                Current_status = [1,1,1]
                output_status_array.extend(Output_status)

        #print("Input:", Input)
        #print("Current Status:", Current_status)
        #print("------------------------")

    print("------------------------")
    print("Output Status Array:", output_status_array)
    print("------------------------")

    separate_encoded_arrays = []
    for i in range(0, len(output_status_array), 18):
        separate_encoded_arrays.append(output_status_array[i:i+18])
        
    print("Separate encoded Array:", separate_encoded_arrays)

    #for input_encoded_codeword in separate_encoded_arrays:
    #    print("Input Codeword:", input_encoded_codeword)
    #for index, input_encoded_codeword in enumerate(separate_encoded_arrays, start=1):
        #print(f"Input Codeword{index}: {input_encoded_codeword}")
    
    send_data_word(output_status_array)

data_word = '101011001010110011010100110010101101001101011001010100110101010011010110010110100110101001011010110'
dataword = [int(bit) for bit in data_word]
print("dataword",dataword)
# Test the function with a sample dataword
#dataword = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]#dataword = [1, 0, 1, 1, 0, 1]
process_data(dataword)
print("Bit transmission finished")




