import sys
blue=[sys.argv[2]]
red=[sys.argv[1]]
print('enter the red size')
print(sys.argv[1])
print('enter the blue size')
print(sys.argv[2])
c=0
for i in range(3,3+int(sys.argv[1])+int(sys.argv[2])):
    print(sys.argv[i])
    c+=1
print(c)
#first five is red second five is blue
print('enter r=red first row or b=b first row')
print(sys.argv[c+3])
for i in range(3,(c//2)+3):
    red.append(int   (sys.argv[i]))
for i in range((c//2)+3,c+3):
    blue.append(int(sys.argv[i]))
for i in range(0,(c//2)-3):
    print(red[i])
for i in range(0,(c//2)-3):
    print(blue[i])
if(sys.argv[c+3] is 'r'):
    red.sort()
    
elif(sys.argv[c+3] is 'b'):
    blue.sort()
for i in range (0,(c//2)-3):
    if(sys.argv[c+3]=='r'):
        if(red[i]<blue[i]):
            print('valid')
        else:
            print('try again')
    if(sys.argv[c+3]=='b'):
        if(blue[i]<red[i]):
            print('valid')
        else:
            print('try again')
    
        
