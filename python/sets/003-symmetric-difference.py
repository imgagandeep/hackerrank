""" 
Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format
Output the symmetric difference integers in ascending order, one per line.

Sample Input:
4
2 4 5 9
4
2 4 11 12

Sample Output:
5
9
11
12
 """




# Solution 1:
input()
aset = set(map(int, input().split()))
input()
bset = set(map(int, input().split()))
adiff = aset.difference(bset)
bdiff = bset.difference(aset)
for i in bdiff:
    adiff.add(i)
for i in sorted(adiff):
    print(i)



# Solution 2:
# if __name__ == "__main__":
#     M = int(input().strip())
#     set_m = set(map(int, input().strip().split(' ')))
    
#     N = int(input().strip())
#     set_n = set(map(int, input().strip().split(' ')))
    
#     for i in sorted(set_m ^ set_n):
#         print(i)
