'''
Problem statement:
https://www.hackerrank.com/challenges/python-loops
'''

if __name__ == '__main__':
    n = int(input())
    if(n>0 and n<=20):
        i = 0
        while(i<n):
            print(i*i)
            i+=1
