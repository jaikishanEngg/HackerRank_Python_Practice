cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    li = list()
    #li.append(0);     li.append(1)
    if(n == 0):
        return []
    elif(n==1):
        return [0]
    else:
        li.extend([0,1])
        for i in range(2,n):
            li.append(li[i-1]+li[i-2])
        return li
    # return a list of fibonacci numbers


