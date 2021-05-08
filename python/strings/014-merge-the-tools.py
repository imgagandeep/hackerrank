""" 
Consider the following:
→ A string, s, of length n where s = c₀ c₁ .... c(n-1).
→ An integer, k, where k is a factor of n.

We can split s into n/k substrings where each substring, tᵢ to create string uᵢ such that:
→ The characters in uᵢ are a subsequence of the characters in tᵢ.
→ Any repeat occurrence of a character is removed from the string such that each character in uᵢ occurs exactly once. 
   In other words, if the character at some index j in tᵢ occurs at a previous index < j in tᵢ, then do not include the character in string uᵢ.
Given s and k, print n/k lines where each line i denotes string uᵢ.

Example
s = 'AAABCADDE'
k = 3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u₁ = 'A'. 
The second substring has all distinct characters, so u₂ = 'BCA'. The third substring has 2 different characters, so u₃ = 'DE'. 
Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

Function Description
Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:
→ string s: the string to analyze
→ int k: the size of substrings to analyze

Prints
Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format:
The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.

Constraints
→ 1 ≤ n ≤ 10⁴, where n is the length of s
→ 1 ≤ k ≤ n
→ It is guaranteed that n is a multiple of k.

Sample Input:
AABCAAADA
3

Sample Output:
AB
CA
AD

Explanation
Split s into n/k = 9/3 = 3 equal parts of length k = 3. 
Convert each tᵢ to uᵢ by removing any subsequent occurrences of non-distinct characters in tᵢ:
1. t₀ = "AAB" → u₀ = "AB"
2. t₁ = "CAA" → u₁ = "CA"
3. t₂ = "ADA" → u₂ = "AD"
Print each uᵢ on a new line.
 """





# Solution 1:
import textwrap
def merge_the_tools(string, k):
    for i in textwrap.wrap(string, k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in i if c not in d]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)



# Solution 2:
# def merge_the_tools(string, k):
#     temp = []
#     len_temp = 0
#     for item in string:
#         len_temp += 1
#         if item not in temp:
#             temp.append(item)
#         if len_temp == k:
#             print (''.join(temp))
#             temp = []
#             len_temp = 0

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
