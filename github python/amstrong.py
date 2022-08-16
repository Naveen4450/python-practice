#amstrong number
print("enter a number")
x=int(input())
sum1=0
sum2=0
z=y=x
while x!=0:
    sum1=sum1+1
    x=x//10
while y!=0:
    r=x%10
    sum2=sum2+pow(r,sum1)
    y=y//10
if(sum2==x):
    print(str(z)+'is the amstrong number')
else:
    print(str(z)+'is not amstrong number')
