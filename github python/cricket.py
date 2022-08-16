def batting(runs,sk,four,six):
    c=0
    if(runs>=50):
        c=c+5
    if(runs>=100):
        c=c+10
    while(runs>1):
        c=c+1
        runs=runs-2
    if(sk>=80 & sk<=100):
        c=c+2
    if(sk>100):
        c=c+4
    while(four!=0):
        c=c+1
        four=four-1
    while(six!=0):
        c=c+2
        six=six-1
    return c
def bowling(wickets,economy):
    c=0
    if(wickets==3 | wickets==4):
        c=c+5
    if(wickets==5):
        c=c+10
    while(wickets!=0):
        c=c+10
        wickets=wickets-1
    if(economy<=4.5 and economy>=3.5):
        c=c+4
    if(economy<=3.5 and economy>=2):
        c=c+7
    if(economy<2):
        c=c+10
    return c
def feilding(feild):
    b=0
    while(feild!=0):
        b=b+10
        feild=feild-1
    return b
