print("Name- Adarsh Singh, Roll No.- 17, Sec- A, PPS Practical-3")
number = int(input("Enter the integer number: "))
# Initiate value to null
revs_number = 0
# reverse the integer number using the while loop
while (number > 0):
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10
# Display the result
print("The reverse number is : ",revs_number)