from machine import ADC, Pin
import time

# Define analog input
ANALOG_IN_PIN = 28

# Floats for resistor values in divider (in ohms)
R1 = 30000.0
R2 = 7500.0

# Float for Reference Voltage
ref_voltage = 3.3

# Setup ADC
adc = ADC(Pin(ANALOG_IN_PIN))

def read_voltage():
    # Read the analog input
    adc_value = adc.read_u16()
    
    # Determine voltage at ADC input
    adc_voltage = (adc_value / 65535) * ref_voltage
    
    # Calculate voltage at divider input
    in_voltage = adc_voltage * (R1 + R2) / R2
    
    return in_voltage

def run():
    voltages = []  # Array to store voltage values

    while len(voltages) < 10:
        start_time = time.time()
        samples = []

        while len(samples) < 10:
            input_voltage = read_voltage()
            samples.append(input_voltage)
            print("Received sample: {:.2f}".format(input_voltage))
            time.sleep(0.1)
        
        average_voltage = sum(samples) / len(samples)
        voltages.append(average_voltage)
        
        print(" >>>>>>>>>>>>>>>>>>>>Input Voltage = {:.2f}".format(average_voltage))
        
        elapsed_time = time.time() - start_time
        if elapsed_time < 1:
            time.sleep(1 - elapsed_time)

    # Calculate threshold from last 5 values
    last_five_average = sum(voltages[5:]) / 5
    threshold = last_five_average + (0.3 * last_five_average)
    print(">>>>>>>>>>>>>>>>>>>>>>>Threshold Value = {:.2f}".format(threshold))

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
        return

    while True:
        # Sampling and calculating average for 1 second
        samples = []
        start_time = time.time()

        while time.time() - start_time < 1:
            input_voltage = read_voltage()
            samples.append(input_voltage)

        average = sum(samples) / len(samples)
        print("Average Voltage for 1 second = {:.2f}".format(average))

        # Compare average with threshold
        if average > threshold:
            print("Bit: 1")
        else:
            print("Bit: 0")

if __name__ == "__main__":
    run()



