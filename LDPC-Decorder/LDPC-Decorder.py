def LDPC_decording():
                 #101011001010110011010100110010101101001101011001010100110101010011010110010110100110101001011010011
    codeword = '11111010010111001111101001011100011011011100010001011100111110100110110101010011111101011010100111110101010100111111010111000100011011011010011011110101111110101010011011111010111101011111101010100110'
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
    print("Transpose of P :", Transpose_P)

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

    print("Identity Matrix: ", identity_matrix)

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

    for j in range(0, 25):
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
    
    for j in range(0, 25):
        a = []
        if Syndrome[j] == [0, 0, 0, 0]: #Has no errors
            x=segments[j]
            c = [int(digit) for digit in str(x)]
            #print(c)
            a = c
            #a.append(segments[j])
            #print(a)
    
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

LDPC_decording()
