data = 120
bit_prev = "0111100001101111"
bits = [8,9,10,11,12,13,14,15]
    
data = bytes([data])
bit_data = ''.join(f'{x:b}' for x in data)
bit_data = '0' * (len(bits) - len(bit_data)) + bit_data

print(f"Data to insert : {bit_data}, Head: {bit_prev[:bits[0]]}, Tail: {bit_prev[bits[-1]+1:]} {bits[-1]+1:}")
new_bits = bit_prev[:bits[0]] + bit_data + bit_prev[bits[-1]+1:]


print(f"Result:\n{bit_prev}\n{new_bits}")
