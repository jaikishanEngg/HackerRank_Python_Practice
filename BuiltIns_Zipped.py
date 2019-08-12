'''
Problem statement:
https://www.hackerrank.com/challenges/zipped
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

s,no_sub = map(int,stdin.readline().split())
subjects = list()
for i in range(no_sub):
    subjects.append(list(map(float,stdin.readline().split())))

marks = list()

marks = zip(*subjects)
#print(list(marks))

average = list() #average of each student

for student_marks in marks:
    average.append(sum(student_marks)/no_sub)

for i in average:
    print(i)

