'''
Problem statement:
https://www.hackerrank.com/challenges/list-comprehensions
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    m = max(x,y,z)
    res = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k != n):
                    t = []
                    t.append(i)
                    t.append(j)
                    t.append(k)
                    res.append(t)
                
    print(res)
