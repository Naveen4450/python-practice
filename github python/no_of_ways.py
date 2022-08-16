#no of ways
def fact(n):
    if(n!=1):
        return n*fact(n-1)
        print('hi')
    else:
        return 1
print("enter the no of shoes")#m
m=int(input())
print("print to no of shoes we should select")#s
s=int(input())
w=fact(m)//(fact(m-s)*fact(s))
print("the no of ways are"+ str(w))
