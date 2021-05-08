""" 
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format
A single line containing a string S.

Constraints
0 < len(S) ≤ 1000

Output Format
Print the modified string S.

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
 """




# Solution:
def change(s):
    if str.islower(s):
        return str.upper(s)
    else:
        return str.lower(s)
def swap_case(s):
    return ('').join(map(change,s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
