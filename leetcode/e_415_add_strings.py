'''
Given two non-negative integers, num1 and num2 
represented as string, return the sum of num1 and 
num2 as a string.

You must solve the problem without using any 
built-in library for handling large integers 
(such as BigInteger). You must also not convert 
the inputs to integers directly.
'''

def add_strings(num1, num2):
    n1 = [n for n in num1]
    n2 = [n for n in num2]
    carry = 0
    res = []

    while len(n1) or len(n2):
        digit1 = int(n1.pop()) if len(n1) > 0 else 0
        digit2 = int(n2.pop()) if len(n2) > 0 else 0
        sum = carry + digit1 + digit2
        # store last digit of sum if there is more to compute
        # else store whole number
        keep  = str(sum%10) if len(n1)>0 or len(n2)>0 else str(sum) 
        res.append(keep) # whole div rounds down
        carry =  1 if sum>9 else 0
    res.reverse()
    return "".join(res)


    
n1, n2 = "119", "92"
# n1, n2 = "456", "77"
# n1, n2 = "1", "9"

print(add_strings(n1, n2))