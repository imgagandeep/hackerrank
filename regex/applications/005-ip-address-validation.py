""" 
You will be provided with N lines of what are possibly IP addresses. You need to detect if the text contained in each of the lines represents an (a)IPv4 address (b)IPv6 address or (c)None of these.
IPv4 was the first publicly used Internet Protocol which used 4 byte addresses which permitted for 232 addresses. The typical format of an IPv4 address is A.B.C.D where A, B, C and D are Integers lying between 0 and 255 (both inclusive).
IPv6, with 128 bits was developed to permit the expansion of the address space. To quote from the linked article: The 128 bits of an IPv6 address are represented in 8 groups of 16 bits each. Each group is written as 4 hexadecimal digits and the groups are separated by colons (:). The address 2001:0db8:0000:0000:0000:ff00:0042:8329 is an example of this representation. Consecutive sections of zeros will be left as they are.
An IPv6 value such as "...:0:..." or "...:5:..." is address-wise identical to "...:0000:..." or "...:0005:....". Leading zeros may be omitted in writing the address.

Input Format
An integer N such that N <= 50. This is followed by N lines such that each the text in each line is either an IPv4 address or an IPv6 address, or a chunk of text which does not equal either of these. There will be no extra text or whitespace leading or trailing the IP address in a line (if it is an IP address). The number of characters in each line will not exceed 500.

Output Format
N lines.
The iᵗʰ output line should equal (a)IPv4 or (b)IPv6 or (c)Neither depending on what you detected the ith input line to be.

Sample Input
3
This line has junk text.
121.18.19.20
2001:0db8:0000:0000:0000:ff00:0042:8329

Sample Output
Neither
IPv4
IPv6
 """




# Solution:
import re

ipv4 = re.compile('^(((2[0-5][0-5])|(1[0-9][0-9])|([1-9][0-9])|(\d))\.){3}((2[0-5][0-5])|(1[0-9][0-9])|([1-9][0-9])|(\d))$')
ipv6 = re.compile('^([a-f0-9]{1,4}:){7}[a-f0-9]{4}$')
n = int(input())
for i in range(n):
    string = str(input())
    if (len(re.findall(ipv4, string)) != 0):
        print("IPv4")
    elif(len(re.findall(ipv6, string)) != 0):
        print("IPv6")
    else:
        print("Neither")
