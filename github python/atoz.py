print("enter the string")
string1=input()
alpha1="a"
alpha2="A"
i=0
while i<26:
    if(alpha1 in string1 or alpha2 in string1):
        print(alpha2)
    elif(alpha1 not in string1 or alpha2 not in string1):
        break
    b=bytes(alpha1,'utf-8')
    b=b[0]+1
    alpha1=chr(b)
    c=bytes(alpha2,'utf-8')
    c=c[0]+1
    alpha2=chr(c)
    i=i+1
    
        
    
  
        
