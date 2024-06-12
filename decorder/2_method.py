

# Decording_bits  1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1
Decording_bits = [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1] #[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]

# Split Decording_bits into arrays with 3 elements each


############## decode the bits in the first stage ################

if Decording_bits == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
                    #         #       #        #        #
    decode_bits = [0, 0, 0, 0, 0, 0]
    print("decode_bits:", decode_bits)
    
elif Decording_bits == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]:#corrected
                    #         #       #        #        #
    decode_bits = [0, 0, 1, 0, 0, 0]
    print("decode_bits:", decode_bits)
    
elif Decording_bits == [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0]:#corrected
    decode_bits = [0, 1, 0, 0, 0, 0]
    print("decode_bits:", decode_bits)#####
    
elif Decording_bits == [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]:#corrected
                    #         #       #        #        #
    decode_bits = [0, 1, 1, 0, 0, 0]
    print("decode_bits:", decode_bits)
    
elif Decording_bits == [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]:#checked
    decode_bits = [1, 0, 0, 0, 0, 0]
    print("decode_bits:", decode_bits)
    
elif Decording_bits == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]:#d
    decode_bits = [1, 0, 1, 0, 0, 0]
    print("decode_bits:", decode_bits)
    
elif Decording_bits == [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]:#d
    decode_bits = [1, 1, 0, 0, 0, 0]
    print("decode_bits:", decode_bits)
    
elif Decording_bits == [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]:#d
    decode_bits = [1, 1, 1, 0, 0, 0]
    print("decode_bits:", decode_bits)
    
else:
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
    c = [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0]
    d = [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    e = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    f = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    g = [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
    h = [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
    
    hamming_dist_a = sum(1 for x, y in zip(Decording_bits, a) if x != y)
    hamming_dist_b = sum(1 for x, y in zip(Decording_bits, b) if x != y)
    hamming_dist_c = sum(1 for x, y in zip(Decording_bits, c) if x != y)
    hamming_dist_d = sum(1 for x, y in zip(Decording_bits, d) if x != y)
    hamming_dist_e = sum(1 for x, y in zip(Decording_bits, e) if x != y)
    hamming_dist_f = sum(1 for x, y in zip(Decording_bits, f) if x != y)
    hamming_dist_g = sum(1 for x, y in zip(Decording_bits, g) if x != y)
    hamming_dist_h = sum(1 for x, y in zip(Decording_bits, h) if x != y)
    
    values = [x for x in (hamming_dist_a, hamming_dist_b, hamming_dist_c, hamming_dist_d, hamming_dist_e, hamming_dist_f, hamming_dist_g, hamming_dist_h) if x != 0]
    min_hamming_dist = min(values)
    
    if min_hamming_dist == hamming_dist_a:
        decode_bits = [0, 0, 0, 0, 0, 0]
        print("decode_bits:", decode_bits)
        
    elif min_hamming_dist == hamming_dist_b:
        decode_bits = [0, 0, 1, 0, 0, 0]
        print("decode_bits:", decode_bits)
        
    elif min_hamming_dist == hamming_dist_c:
        decode_bits = [0, 1, 0, 0, 0, 0]
        print("decode_bits:", decode_bits)#####
        
    elif min_hamming_dist == hamming_dist_d:
        decode_bits = [0, 1, 1, 0, 0, 0]
        print("decode_bits:", decode_bits)
        
    elif min_hamming_dist == hamming_dist_e:
        decode_bits = [1, 0, 0, 0, 0, 0]
        print("decode_bits:", decode_bits)
        
    elif min_hamming_dist == hamming_dist_f:
        decode_bits = [1, 0, 1, 0, 0, 0]
        print("decode_bits:", decode_bits)
        #result_array = c
    elif min_hamming_dist == hamming_dist_g:
        decode_bits = [1, 1, 0, 0, 0, 0]
        print("decode_bits:", decode_bits)
        
    elif min_hamming_dist == hamming_dist_h:
        decode_bits = [1, 1, 1, 0, 0, 0]
        print("decode_bits:", decode_bits)