""" 
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
N = 4
append 1
append 2
insert 3 1
print

→ append 1: Append 1 to the list, arr = [1].
→ append 2: Append 2 to the list, arr = [1, 2].
→ insert 3 1: Insert 3 at index 1, arr = [1, 3, 2].
→ print: Print the array.
Output:
[1, 3, 2]

Input Format
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints
→ The elements added to the list must be integers.

Output Format
For each command of type print, print the list on a new line.

Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
 """




# Solution:
if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(0, N):
        cmd = input().split()
        if cmd[0] == "insert":
            list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "append":
            list.append(int(cmd[1]))
        elif cmd[0] == "pop":
            list.pop()
        elif cmd[0] == "print":
            print(list)
        elif cmd[0] == "remove":
            list.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            list.sort()
        else:
            list.reverse()


""" Test Case -> 1
29
append 1
append 6
append 10
append 8
append 9
append 2
append 12
append 7
append 3
append 5
insert 8 66
insert 1 30
insert 6 75
insert 4 44
insert 9 67
insert 2 44
insert 9 21
insert 8 87
insert 1 75
insert 1 48
print
reverse
print
sort
print
append 2
append 5
remove 2
print

Output -> 1
[1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
[5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
[1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
[1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]




Test Case -> 2
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print


Output -> 2
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1] """
