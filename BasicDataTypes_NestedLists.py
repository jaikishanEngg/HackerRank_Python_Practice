'''
Problem statement:
https://www.hackerrank.com/challenges/nested-list
'''

def key_s(students):
    return students[1]

if __name__ == '__main__':
    students = []
    sec_low_list = []
    #input no.of testcases and iterate 
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])   #adding name,score pair to the students list
    
    min_marks = min(students,key = key_s)[1]   #find the minimum marks
    
    l = len(students)
    j = 0

    while(j<l): #Remove the min marks from the list (including duplicates)
        if(students[j][1] == min_marks):
            del students[j]
            l -= 1
        else:
            j += 1

    sec_minMarks = min(students, key = key_s)[1]
    for i in students:
        if(i[1] == sec_minMarks):
            sec_low_list.append(i[0])
    sec_low_list.sort()
    for i in sec_low_list:
        print(i)
