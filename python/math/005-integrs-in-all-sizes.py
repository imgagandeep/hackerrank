""" 
Task
Read four numbers, a, b, c, and d, and print the result of aᵇ + cᵈ.

Input Format
Integers a, b, c, and d are given on four separate lines, respectively.

Constraints
1 ≤ a ≤ 1000
1 ≤ b ≤ 1000
1 ≤ c ≤ 1000
1 ≤ d ≤ 1000

Output Format
Print the result of aᵇ + cᵈ on one line.

Sample Input:
9
29
7
27

Sample Output:
4710194409608608369201743232  

Note: This result is bigger than 2⁶³ - 1. Hence, it won't fit in the long long int of C++ or a 64-bit integer.
 """




# Solution:
a, b, c, d = (int(input()) for i in range(4))
print(a ** b + c ** d)
