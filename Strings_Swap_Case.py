'''
Problem statement:
https://www.hackerrank.com/challenges/swap-case
'''

def swap_case(s):
    s = list(s)
    for i in range(0,len(s)):
        if(s[i].isupper()):
            s[i]=s[i].lower()
        else:
            s[i]=s[i].upper()
    return "".join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)