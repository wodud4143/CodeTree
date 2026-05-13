y = int(input())

# Please write your code here.

def year(n):
    if n % 4 == 0 :
        if n % 100 == 0 and n % 400 != 0 :
            return False
        else :
            return True
    else :
        return False

if year(y) :
    print('true')
else :
    print('false')