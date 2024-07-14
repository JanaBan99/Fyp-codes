import machine
import utime

# Define GPIO pins
led_pin = machine.Pin(16, machine.Pin.OUT)

def LDPC_encoding(codeword):
    # Initialize 
    P = [
        [1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1]
    ]

    # Identity matrix generation
    identity_matrix = []
    for i in range(len(P[0])):
        row = []
        for j in range(len(P[0])):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        identity_matrix.append(row)

    # Generator Matrix
    Generator_Matrix = []
    for k in range(len(P[1])):
        P[k].extend(identity_matrix[k])
        Generator_Matrix.append(P[k])

    encoded_word = []

    # Multiply codeword with Generator_Matrix
    for j in range(len(Generator_Matrix[0])):
        result = (
            int(codeword[0]) * Generator_Matrix[0][j] ^
            int(codeword[1]) * Generator_Matrix[1][j] ^
            int(codeword[2]) * Generator_Matrix[2][j] ^
            int(codeword[3]) * Generator_Matrix[3][j]
        )
        encoded_word.append(result)

    binary_str_list = [str(digit) for digit in encoded_word]
    binary_string = ''.join(binary_str_list)
    return binary_string

a = '1010110010101100110101001100101011010011010110010101001101010100110101100101101001101010010110100110'
sets_of_4 = [a[i:i+4] for i in range(0, len(a), 4)]

encoded_sets = []
for i in range(len(sets_of_4)):
    encoded_sets.append(LDPC_encoding(sets_of_4[i]))

result = ''.join(encoded_sets)
print("Encoded Result:", result)


print("starting initializing bits")
initial_word = '1111100000'
for bit in initial_word:  # Transmit initial 10 bits
    led_pin.value(int(bit))  # Set the LED state based on the bit
    print(bit, end='')  # Print the transmitting bit
    utime.sleep_ms(100)  # Wait for 1000 milliseconds (1 second)
print()

for bit in result:
    led_pin.value(int(bit))
    print(bit, end='')
    utime.sleep_ms(100)
led_pin.value(0)



