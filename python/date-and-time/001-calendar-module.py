""" 
Task
You are given a date. Your task is to find what the day is on that date.

Input Format
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

Constraints
→ 2000 < year < 3000

Output Format
Output the correct day in capital letters.

Sample Input
08 05 2015

Sample Output
WEDNESDAY

Explanation
The day on August 5ᵗʰ 2015 was WEDNESDAY.
 """




# Solution:
import datetime
import calendar
m, d, y = list(map(int, input().split()))
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())
