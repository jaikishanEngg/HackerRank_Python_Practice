'''
Problem statement:
https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

from collections import OrderedDict
def merge_the_tools(string, k):
    i=0 #start index
    slicers = list()    #slice the string into k pieces
    while(i<len(string)):
        slicers.append(string[i:i+k])
        i+=k
    for ele in slicers:
        print("".join(OrderedDict.fromkeys(ele)))

        



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)