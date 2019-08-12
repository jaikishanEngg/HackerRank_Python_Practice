'''
Problem statement:
https://www.hackerrank.com/challenges/py-if-else
'''

#!/bin/python3
if __name__ == '__main__':
    n = int(input().strip())
    if(n>0 & n<=100):
        if(n%2 == 1):
            #when n is odd print weird
            print("Weird")
        elif(n%2 == 0):
            #when n is even
            if(n>=2 and n<=5):
                print("Not Weird")
            elif(n>=6 and n<=20):
                print("Weird")
            elif(n>20):
                print("Not Weird")
