'''
Problem statement:
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
'''

def average(array):
    # your code goes here
    s = set(array)
    avg = float(sum(s)/len(s))
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)