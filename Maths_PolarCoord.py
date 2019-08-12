'''
Problem statement:
https://www.hackerrank.com/challenges/polar-coordinates
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from cmath import phase
c = complex(input())

print(math.sqrt((c.real*c.real)+(c.imag*c.imag)))    #print r value
print(phase(c))


