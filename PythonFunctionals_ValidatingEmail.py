def evaluate_user(user):
    user = str(user)
    for e in user:
        if(not(e.isalnum()) and (e not in('_','-'))):
            return False
            break
    else:
        return True

def fun(s):
    # return True if s is a valid email, else return False
    #username@web.ext
    #len(ext)<=3; username: alnum() - _     web: alnum()
    s = str(s)
    try:
        index_at = s.index('@')     #may evaluate to  ValueError
        username = s[:index_at]
        index_dot = s.index('.')    #may evaluate to  ValueError
        web = s[index_at+1:index_dot]
        ext = s[index_dot+1:]
    except ValueError:
        return False
    if(username == ""):
        return False
    else:
        username_res = evaluate_user(username)
        if(len(ext)>3 or not(web.isalnum()) or not(username_res)):
            return False
        else:
            return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)