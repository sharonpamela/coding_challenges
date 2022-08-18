'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Examples:

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''


def is_valid_str(s):

    res = []

    for char in s:
        if char == "(":
            res.append(')')
        elif char == "{":
            res.append("}")
        elif char == '[':
            res.append(']')
        else:
            if len(res) == 0 or char != res.pop():
                return False
    return len(res) == 0


s = ")()[]{}}"
print(is_valid_str(s))