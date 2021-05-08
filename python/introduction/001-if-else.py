""" 
Task:
Given an integer, n, perform the following conditional actions:
→ If n is odd, print Weird
→ If n is even and in the inclusive range of 2 to 5, print Not Weird
→ If n is even and in the inclusive range of 6 to 20, print Weird
→ If n is even and greater than 20, print Not Weird

Input Format:
A single line containing a positive integer, n.

Constraints
→ 1 ≤ n ≤ 100

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input:
3

Sample Output:
Weird

Explanation
n = 3
n is odd and odd numbers are weird, so print Weird.
 """




# Solution:
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2) != 0:
        print("Weird")
    else:
        if (n >= 2) and (n <= 5):
            print("Not Weird")
        elif (n >= 6) and (n <= 20):
            print("Weird")
        elif (n > 20):
            print("Not Weird")
