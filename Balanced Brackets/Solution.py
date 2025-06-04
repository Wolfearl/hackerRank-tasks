#!/bin/python3

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    brackets = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for word in s:
        if word in brackets:
            stack.append(word)
        elif not stack or brackets[stack.pop()] != word:
            return "NO"
    return "YES" if not stack else "NO"
