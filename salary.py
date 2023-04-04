print("NAME=Adarsh Singh,ROLL NO=17,SEC=A,CSE,PPS EXPERIMENT-2:")
a=input("ENTER YOUR NAME HERE: ")
b=int(input("ENTER YOUR SALARY HERE: "))
c=input("ENTER YOUR GENDER HERE(M/F): ")
if b<10000 and c=="M":
print(str(a)+", YOUR SALARY WITH BONUS IS "+str(b+(b*0.07)))
elif b<10000 and c=="F":
print(str(a)+", YOUR SALARY WITH BONUS IS "+str(b+(b*0.12)))
if b>=10000 and c=="M":
print(str(a)+", YOUR SALARY WITH BONUS IS "+str(b+(b*0.05)))
elif b>=10000 and c=="F":
print(str(a)+", YOUR SALARY WITH BONUS IS "+str(b+(b*0.1)))