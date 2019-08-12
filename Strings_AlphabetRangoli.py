'''
Problem statement:
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''

def print_rangoli(size):
    # your code goes here
    i = 97 + size -1
    line = []
    s= ''
    while(i>=97):
        temp = s.rjust((size-1)*2,'-')+chr(i)+"".join(reversed(s.rjust((size-1)*2,'-')))
        line.append(temp);
        s += chr(i)+'-'
        i -= 1

    for l in range(0,len(line)):
        print(line[l])
    length = len(line)-2
    while(length>=0):
        print(line[length])
        length -= 1
   

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)