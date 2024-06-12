import machine
import utime

def run():
    
    # Define GPIO pins
    led_pin = machine.Pin(16, machine.Pin.OUT)

    data_word = '1010110010101100110101001100101011010011010110010101001101010100110101100101101001101010010110101'  # 99-bit data word to send
    initial_word = '1111100000'  # Initial 10-bit word to send before data_word

    # Function to send the data word
    def send_data_word(initial_word, data_word):
        for bit in initial_word:  # Transmit initial 10 bits
            led_pin.value(int(bit))  # Set the LED state based on the bit
            print(bit, end='')  # Print the transmitting bit
            utime.sleep_ms(1000)  # Wait for 1000 milliseconds (1 second)
        print()
        utime.sleep_ms(25)
        
        for bit in data_word:  # Transmit the 99-bit data word
            led_pin.value(int(bit))  # Set the LED state based on the bit
            print(bit, end='')  # Print the transmitting bit
            utime.sleep_ms(1000)  # Wait for 1000 milliseconds (1 second)

    send_data_word(initial_word, data_word)
    led_pin.value(0)  # Turn off the LED





