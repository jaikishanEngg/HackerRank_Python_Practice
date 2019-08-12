'''
Problem statement:
https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''

import math
if __name__ == '__main__':
    n = int(input())    #no of students
    student_marks = {}  #student marks Maths, Physics, Chemistry
	no_of_subs = 3 #Maths, Physics, Chemistry
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = round((math.fsum(student_marks[query_name]))/no_of_subs,2)	#round to 2 decimals
    print("{:.2f}".format(avg))	
	
	
'''
To notice the difference between round() and format(), please run the following code:

import math	
print(3.149898)						#3.149898
print(round(3.149898,2))			#3.15
print("{:.2f}".format(3.149898))	#3.15

#Both results in same result, so you can use either of them

'''