import random
def answer(number):
    if number==1:
        return "it is certain"
    elif number==2:
        return "it is decidedly so "
    elif number==3:
        return "yes"
    elif number==4:
        return "reply hazy try again"
    elif number==5:
        return "ask again later"
    elif number==6:
        return "concentrate and try again"
    elif number==7:
        return "my reply is no"
    elif number==8:
        return "outlook not good"
    elif number==9:
        return "very doubtful"
numb=random.randint(1,9)
print(answer(numb))

