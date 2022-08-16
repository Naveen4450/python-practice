import cricket
p1=input("enter player1 name")
p2=input("enter player2 name")
p3=input("enter player3 name")
p4=input("enter player4 name")
p5=input("enter player5 name")
role1=input("enter player1 role")
role2=input("enter player2 role")
role3=input("enter player3 role")
role4=input("enter player4 role")
role5=input("enter player5 role")
ball1=int(input("enter player1 balls"))
ball2=int(input("enter player2 balls"))
r1=int(input("enter player1 runs"))
r2=int(input("enter player2 runs"))
r3=int(input("enter player3 runs"))
r4=int(input("enter player4 runs"))
r5=int(input("enter player5 runs"))
four1=int(input("enter player1 four"))
four2=int(input("enter player2 four"))
six1=int(input("enter player1 six"))
six2=int(input("enter player2 six"))
feild1=int(input("enter player1 feild"))
feild2=int(input("enter player2 feild"))
feild3=int(input("enter player3 feild"))
feild4=int(input("enter player4 feild"))
feild5=int(input("enter player5 feild"))
wickets3=int(input("enter player3 wickets"))
wickets4=int(input("enter player4 wickets"))
wickets5=int(input("enter player5 wickets"))
ska=94
skb=107
economy3=7.1
economy4=4.5
economy5=3.1
pts1=0
pts2=0
pts3=0
pts4=0
pts5=0
pts1=cricket.batting(r1,ska,four1,six1)+cricket.feilding(feild1)
pts2=cricket.batting(r2,skb,four2,six2)+cricket.feilding(feild2)
pts3=cricket.bowling(wickets3,economy3)+cricket.feilding(feild3)
pts4=cricket.bowling(wickets4,economy4)+cricket.feilding(feild4)
pts5=cricket.bowling(wickets5,economy5)+cricket.feilding(feild5)
print("{'name':",p1,"'batscore':",pts1,)
print("{'name':",p2,"'batscore':",pts2,)
print("{'name':",p3,"'bowlscore':",pts3,)
print("{'name':",p4,"'bowlscore':",pts4,)
print("{'name':",p5,"'bowlscore':",pts5,)
