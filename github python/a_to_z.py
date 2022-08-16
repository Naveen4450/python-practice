#code to check whether we have all alphabets are not
print("enter the string")
string1=input()
k=len(string1)
alpha1='A'
alpha2='a'
i=0
j=0
print(k)
while i<26:
    if(alpha1 in string1 or alpha2 in string1):
        print(alpha1)
    b=bytes(alpha1,'utf-8')
    b=b[0]+1
    alpha1=chr(b)
    c=bytes(alpha2,'utf-8')
    c=c[0]+1
    alpha2=chr(c)
    i=i+1
    j=0
        
            
