'''
Write a function that takes an unsigned integer 
and returns the number of '1' 
bits it has (also known as the Hamming weight).
'''

def hammingWeight(n):
    bits_count = 0
    num = n
    while num > 0:
        if num%2 == 1:
            bits_count+=1
        num = num >> 1
    return bits_count

print(hammingWeight(3))