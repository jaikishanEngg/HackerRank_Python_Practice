'''
Problem statement:
https://www.hackerrank.com/challenges/find-a-string
'''

def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        index = string.find(sub_string)   #index of substring
        if(index != -1):    #sub-string found
            count += 1  #count of substring
            string = string[index+1 : ] #slice
        else:
            break;
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)