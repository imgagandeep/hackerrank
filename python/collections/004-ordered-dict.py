""" 
Task
You are the manager of a supermarket. You have a list of N items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.
                    item_name = Name of the item. 
                    net_price = Quantity of the item sold multiplied by the price of each item.

Input Format
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space. 

Constraints
0 < N ≤ 100

Output Format
Print the item_name and net_price in order of its first occurrence.

Sample Input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation
BANANA FRIES: Quantity bought: 1, Price: 12
Net Price: 12
POTATO CHIPS: Quantity bought: 2, Price: 30
Net Price: 60
APPLE JUICE: Quantity bought: 2, Price: 10
Net Price: 20
CANDY: Quantity bought: 4, Price: 5
Net Price: 20
 """




# Solution:
from collections import OrderedDict

order = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(None, 1)
    order[item] = order.get(item, 0) + int(price)
for item, price in order.items():
    print(item, price)
