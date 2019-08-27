import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    timedelta = t2 - t1
    return timedelta.days * 24 * 3600 + timedelta.seconds
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        print("{}\n{}".format(t1,t2))
        date1 = datetime.strptime(t1,'%a %d %b %Y %X %z')
        date2 = datetime.strptime(t2,'%a %d %b %Y %X %z')

        delta = time_delta(date1, date2)

        fptr.write(str(abs(delta)) + '\n')

    fptr.close()
