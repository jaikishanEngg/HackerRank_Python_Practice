'''
Problem statement:
https://www.hackerrank.com/challenges/py-the-captains-room
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
from sys import stdin
k = int(stdin.readline())

room_nums = list(map(int,stdin.readline().split()))

count_group = Counter(room_nums)
#print(count_group)
#print(type(count_group))


count_group = dict(count_group)
#print(count_group)
#print(type(count_group))

r_count_group = dict((v,k) for k,v in count_group.items())

print(r_count_group[1])

