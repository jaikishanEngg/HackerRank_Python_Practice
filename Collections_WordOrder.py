'''
Problem Statement:
https://www.hackerrank.com/challenges/word-order
'''


#word order

ordered_dict = {}
n = int(input())
for i in range(n):
    inp = input()
    if(inp in ordered_dict):
        ordered_dict[inp] += 1
    else:
        ordered_dict[inp] = 1

#print(ordered_dict)
print(len(ordered_dict))

for i in ordered_dict:
    print(ordered_dict[i], end=" ")
