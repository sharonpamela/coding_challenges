#   // i: two integers
#   // o: one integer comprised of alternating digits from a and b (if one runs out, 
#           append remainder of other as rest)
#   // c: input nums > 0, < 100,000,000 (positives only)
#   // e: repeating nums, single nums, single zeros, if c > 100,000,000, return -1

from collections import deque
def decimalZip(a, b):
    num1 = deque([ i for i in str(a)])
    num2 = deque([ i for i in str(b)])
    res = []
    
    if a == 0:
        return b
    elif b == 0:
        return a

    while num1 or num2:
        if len(num1):
            res.append(num1.popleft())
        if len(num2):
            res.append(num2.popleft())
    r = int("".join(res))
    
    return r if r < 100000000 else -1

  


# var result, a, b;
# a = 12
# b = 56 # 1526
# a = 56
# b = 12 #5162

a = 12345
b = 678 #16273845

a = 0
b = 1234 # 1234

a = 1234 # 1234
b = 0

a = 123456789
b = 123456789 #1234
result = decimalZip(a, b)
print(result)