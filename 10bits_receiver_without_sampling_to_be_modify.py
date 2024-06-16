from machine import ADC, Pin
import utime

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

def edge_detection():
    previous_voltage = read_voltage()
    utime.sleep_ms(10)
    
    while True:
        current_voltage = read_voltage()
        print(current_voltage)
        if current_voltage > previous_voltage + 5:  # Edge rise threshold
            print("Rising edge detected")
            break
        previous_voltage = current_voltage
        utime.sleep_ms(100)

def calculate_threshold(voltages):
    # Calculate threshold from the first 5 values
    first_five_average = sum(voltages[:5]) / 5
    threshold = first_five_average - (0.5625 * first_five_average)
    return threshold

def main():
    voltages = []  # Array to store voltage values

    # Collect 10 voltage readings
    while len(voltages) < 10:
        input_voltage = read_voltage()
        print("Input Voltage = ", input_voltage)
        voltages.append(input_voltage)
        utime.sleep_ms(100)
        
    print("Voltages_array = ", voltages)
    threshold = calculate_threshold(voltages)
    print("Threshold Value = {:.2f}".format(threshold))
    Bits = []
    for voltage in voltages:
        if voltage > threshold:
            print("Bit: 1")
            Bits.append("1")
        else:
            print("Bit: 0")
            Bits.append("0")
    print("Binary Values = ", Bits)

    # Collect and process the data word
    voltages = []  # Reset the array to store new voltage values

    # Collect 99 voltage readings
    for _ in range(99):
        input_voltage = read_voltage()
        voltages.append(input_voltage)
        print("Input Voltage = ", input_voltage)
        utime.sleep_ms(100)
            
    # Convert collected voltage values to binary based on the threshold
    Bits = []
    for voltage in voltages:
        if voltage > threshold:
            print("Bit: 1")
            Bits.append("1")
        else:
            print("Bit: 0")
            Bits.append("0")

    received_bits = ''.join(Bits)
    print("Received Bits: [", received_bits, "]", sep='')

if __name__ == "__main__":
    print("Starting edge detection...")
    edge_detection()
    print("Starting main function...")
    main()

