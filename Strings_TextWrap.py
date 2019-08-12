'''
Problem statement:
https://www.hackerrank.com/challenges/text-wrap
'''

import textwrap

def wrap(string, max_width):
    paragraphs = []
    while(len(string)>max_width):
        paragraphs.append(string[:max_width])
        string = string[max_width:]
    if(len(string)>0):
        return "\n".join(paragraphs)+"\n"+(string[:])
    else:
        return "\n".join(paragraphs)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)