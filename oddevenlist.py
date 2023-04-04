print("Name- Adarsh Singh, Sec-A, Roll No.-17, PPS Exp-6")
import random
randomlist = random.sample(range(10, 30), 5)
print(randomlist)
even=[]
odd=[]
for j in randomlist:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)