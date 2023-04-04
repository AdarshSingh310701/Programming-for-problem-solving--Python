print("Name-Adarsh Singh, Roll No.-17, Sec-A, CSE, PPS Exp-4")
str=input("Enter a string: ")
print("Length of the entered string is: ",len(str))
print("Reversed string is",str[::-1])
str1=input("Enter another string: ")
if(str1==str):
print("The strings are the same")
else:
print("The strings are not the same")
if(str==str[::-1]):
print("The string is a palindrome")
else:
print("The string is not a palindrome")