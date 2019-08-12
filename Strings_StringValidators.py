'''
Problem statement:
https://www.hackerrank.com/challenges/string-validators
'''

if __name__ == '__main__':
    s = input()
    isalnum = isalpha = isdigit = islower = isupper = False
    for i in s:
        if(i.isalnum()):
            isalnum = True
        if(i.isalpha()):
            isalpha = True
        if(i.isdigit()):
            isdigit = True
        if(i.islower()):
            islower = True
        if(i.isupper()):
            isupper = True
    print("{0}\n{1}\n{2}\n{3}\n{4}".format(isalnum,isalpha,isdigit,islower,isupper))


