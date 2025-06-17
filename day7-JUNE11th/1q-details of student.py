students={}
n=int(input("Enter how many students: "))
for i in range(n):
    name=input("ENTER THE NAME OF STUDENT: ")
    first_name=input("enter the first name: ")
    last_name=input("enter the last name: ")
    gender=input("enter the Gender: ")
    contact=int(input("enter the contact number: "))
    Dob=input("enter the DOB: ")
    highest_qualification=input("enter the highest qualification: ")
    current_qualification=input("enter the current ongoing qualification: ")
    mail_ID=input("enter the mail-ID: ")
    password=input("enter the password: ")
students[name]={"FIRST NAME":first_name,"LAST NAME":last_name
               ,"GENDER":gender,"CONTACT NUMBER":contact,"DATE OF BIRTH":Dob,"HIGHEST QUALIFICATION":highest_qualification
               ,"CURRENT QUALIFICATION":current_qualification,"EMAIL ID":mail_ID,"PASSWORD":password}
print("\nSTUDENT DETAILS ENTERED ARE:")
for student,details in students.items():
    print(f"\n STUDENT NAME:{students}")
