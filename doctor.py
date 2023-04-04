print('name : Adarsh Singh \n Roll No-17 \n Sec : A \n PPS Exp-7')
doctor_detail={'Name' : ' ' , 'Address' : ' ' , 'contact' : ' ' , 'Personal Number' : ' ' , 'Qualification' : ' ' , 'mail': ' '
,'Specification' : ' '}
print("___________")
print("Enter the Details of Doctor below ")
doctor_detail['Name']=(input("Name of your Doctor : "))
doctor_detail['Address']=(input("Address :"))
doctor_detail['contact']=(input("Contact :"))
doctor_detail['Personal Number']=(input("Clinic Contact Number : "))
doctor_detail['Qualification']=(input("Qualifications :"))
doctor_detail['mail']=(input("Doctor Id : "))
doctor_detail['Specification']=(input("Doctor Specialization : "))
print("\nInformation of your Doctor: ")
print("___________")
print(doctor_detail)
print("____DOCTOR INFORMATION___( using items() method )\n")
for x,y in doctor_detail.items():
print(x,y)
print("____Printing Values___( using iteration )\n")
for i in doctor_detail:
print(doctor_detail[i])
print("____Printing Values___( using values() method )\n")
for x in doctor_detail.values():
print(x)
print("____Printing Keys___( using keys() method )\n")
for i in doctor_detail.keys():
print(i)
print("____Printing Keys___( using iteration )\n")
for i in doctor_detail:
print(i)