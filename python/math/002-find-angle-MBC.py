""" 
ABC is a right angled triangle. ∠ABC = 90 degree. Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC. Your task is to find ∠MBC in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
→ 0 < AB ≤ 100
→ 0 < BC ≤ 100
→ Lengths AB and BC are natural numbers.

Output Format
Output ∠MBC in degrees. 
Note: Round the angle to the nearest integer.

Sample Input:
10
10

Sample Output:
45°
 """




# Solution:
import math
ab, bc = int(input()), int(input())
print(str(round((math.degrees(math.atan2(ab, bc))))) + '°')
