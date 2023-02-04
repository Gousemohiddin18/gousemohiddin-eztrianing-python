q1=""" what is your favorite bike company ?
a.Kawasaki
b.BMW
c.KTM
d.TVS"""

q2="""who is your favorite character in marvel ?
a.Thor
b.iron man
c.hulk
d.captain america"""

q3="""who is the only player to score a century in all formates of cricket ?
a.dhoni
b.sachin
c.virat kohli
d.rohith sharma"""

q4="""which  metal available in wakanda ?
a.adamantium
b.vaibranium
c.cryptonium
d.uru"""

questions={q1:"a",q2:"b",q3:"c",q4:"b"}

name=input("hi whats your name :")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    x1=input("do you want to skip this question (yes/no) :")
    if x1=="yes":
        continue
    ans=input("enter your answer :")
    if ans==questions[i]:
        print("Wow! you got one point")
        score=score+1
        print("your current score is :",score)
    else:
        print("Wrong answer,u lost 1 point")
        score=score-1
        print("your current score is ",score)
    x2=input("Do you want to Quit? type(yes/no) :")
    if x2=="yes":
        break
print("your total score is",score)
