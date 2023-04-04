print("Name- Adarsh Singh, Sec-A, Roll No.-17, PPS Exp-8")
file=open("input1.txt","r+")
print("\nName of the File:", file.name)
print("\nFile is Closed:", file.closed)
print("\nFile has been opened in", file.mode, "Mode")
print(file.readlines())
print("\nFile is closed",file.closed)
with open("input1.txt","rb") as file1:
with open("input2.txt","wb") as file2:
buf = file1.read(500)
file2.write(buf)

with open("input1.txt","r") as file1:
buf = file1.read(500).swapcase()
buff = buf.replace(".",",")
print(buff)