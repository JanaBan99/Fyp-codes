import machine
import random
import time
# Use this to get random bits
def generate_99_binary_bits():
    return ''.join(random.choice(['0', '1']) for _ in range(99))

# Define GPIO pins
led_pin = machine.Pin(16, machine.Pin.OUT)

# Uncomment this and send to send a random bit stream
#data_word = generate_99_binary_bits() # 99-bit data word to send

data_word = '101011001010110011010100110010101101001101011001010100110101010011010110010110100110101001011010110'
#data_word='101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101'
initial_word = '11111100000'  # Initial 10-bit word to send before data_word
try:
    # Timer callback function
    def send_bit(timer):
        
        global bit_index, initial_word, data_word, led_pin
        if bit_index < len(initial_word):
            bit = initial_word[bit_index]
        else:
            bit = data_word[bit_index - len(initial_word)]
        
        led_pin.value(int(bit))  # Set the LED state based on the bit
        print(bit, end='')  # Print the transmitting bit
        bit_index += 1
        
        # Stop the timer once all bits are sent
        if bit_index >= len(initial_word) + len(data_word):
            timer.deinit()
            time.sleep(0.01)
            led_pin.value(0)  # Turn off the LED

    # Global bit index
    bit_index = 0

    # Initialize the hardware timer
    timer = machine.Timer()
    timer.init(period=10, mode=machine.Timer.PERIODIC, callback=send_bit)  # Adjust frequency as needed

    # The main loop will keep the script running
    while bit_index < len(initial_word) + len(data_word):
        pass
except:
    timer.deinit() 
