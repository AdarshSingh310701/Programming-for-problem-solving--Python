print ("Name- Adarsh Singh, Sec-A, Roll No.-17")
def display (name, roll_no, *marks):
print ("Name of Student”, name)
print ("Roll no. of student”, roll_no)
for m in marks:
sum=m1+m2+m3+m4+m5+m6
per=(sum/600) *100
print ("Percentage of student”, per)
cgpa=per/9.5
print ("CGPA of student”, cgpa)
if(cgpa>7.9):
print ("Congratulations you got Distinction")
elif(cgpa>6.3 and cgpa<7.9):
print ("Congratulations you got 1st division")
elif(cgpa>5.26 and cgpa<6.3):
print ("You achieved 2nd division")
elif(cgpa>4.2 and cgpa<5.26):
print ("You achieved 3rd division")
elif(cgpa<4.2):
print ("You failed, pls try harder next time")
print ("Student Result Portal")
name=input ("Enter name of student")
roll_no=int (input ("Enter Roll No. of student"))
m1=int (input ("Enter Marks of Maths"))
m2=int (input ("Enter Marks of PPS"))
m3=int (input ("Enter Marks of Communication Skills"))
m4=int (input ("Enter Marks of Japanese Language"))
m5=int (input ("Enter Marks of Chemistry"))
m6=int (input ("Enter Marks of Physics"))
display (name, roll_no, m1, m2, m3, m4, m5, m6)