'''
Problem statement:
https://www.hackerrank.com/challenges/python-lists/problem
'''
if __name__ == '__main__':
    N = int(input())
    l = []
    while(N>0):
        cmd_l = input().split()
        if(len(cmd_l) == 3 and cmd_l[0] == "insert"):
            #insert statement
            l.insert(int(cmd_l[1]),int(cmd_l[2]))
        elif(len(cmd_l) == 2 and (cmd_l[0] == "remove" or cmd_l[0] == "append")):
            if(cmd_l[0] == "remove"):
                l.remove(int(cmd_l[1]))
            elif(cmd_l[0] == "append"):
                l.append(int(cmd_l[1]))
        elif(len(cmd_l) == 1):
            if(cmd_l[0] == "sort"):
                l.sort()
            elif(cmd_l[0] == "reverse"):
                l.reverse()
            elif(cmd_l[0] == "pop"):
                l.pop()                
            elif(cmd_l[0] == "print"):
                print(l)
        N -= 1
