'''
Problem statement:
https://www.hackerrank.com/challenges/python-string-formatting/problem
'''

def print_formatted(number):
    # your code goes here
    format_value = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        print("".join(str(i)).rjust(format_value),end="")
        print("".join(list(oct(i))[2:]).rjust(format_value+1),end="")
        print("".join(list(hex(i).upper())[2:]).rjust(format_value+1),end="")
        print("".join(list(bin(i))[2:]).rjust(format_value+1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)