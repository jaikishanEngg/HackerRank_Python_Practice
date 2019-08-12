'''
Problem statement:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr) #convert it to list
    m = max(arr) #find top marks
    while(m in arr):
        #remove the top marks from the list with duplicates
        arr.remove(m)
    print(max(arr)) #print the runner-up marks