from collections import Counter

def minion_game(string):
    kevin_score = 0  #initialize Kevin and Stuart scores
    stuart_score = 0
    string = string.upper()
    l = len(string)
    for i in range(l):
        if(string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or string[i]=='U'):
            #kevin
            kevin_score +=  (l - i)
        else:
            #stuart
            stuart_score += (l - i)
    if(kevin_score == stuart_score):
        print("Draw")
    elif(kevin_score > stuart_score):
        print("Kevin {}".format(kevin_score))
    else:
        print("Stuart {}".format(stuart_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)