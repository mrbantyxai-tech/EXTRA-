print()
print("Welcome to The Student Data Organizer! :)")
print()
print()
students = []
sid = 1
while True:
    print("Select an Option :-")
    print("--------------------------------------")
    print("| 1. Add Student                     |")
    print("| 2. Display All Subjects            |")
    print("| 3. Update Student Information      |")
    print("| 4. Delete Student                  |")
    print("| 5. Display Subjects Offered        |")
    print("| 6. Exit                            |")
    print("--------------------------------------")
    schoice = int(input("Enter Your Choice :- "))
    print()
    print()
    if schoice == 1:
        print("Student ID :-",sid)
        name = input("Name :- ")
        age = int(input("Age :- "))
        grade = input("Grade :- ")
        dob = input("Date of Birth (YYYY-MM-DD) :- ")
        sub = input("Subjects (comma-separated) :- ")
        subset = {sub}
        student = {
                    "id":sid,
                    "name":name,
                    "age":age,
                    "grade":grade,
                    "dob":dob,
                    "sub":sub
                }
        students.append(student)
        sid += 1
        print()
        print()
        print("Student added Succesfully!")
        print()
        print()
    elif schoice == 2:
        if(len(students)==0):
            print('The Record Is Empty...!!')
            print()
            print()
        for stud in students:
            print(f"Student ID :- {stud["id"]} |  Name :- {stud["name"]} | Age :- {stud["age"]} | Grade :- {stud["grade"]} |   DOB :- {stud["dob"]}  Subjects :- {stud["sub"]}")
    elif schoice == 3:
        sid = int(input("Enter Student's id which you edit :- "))
        for student in students:
            if student['id'] == sid:
                print()
                print('--------------------------------------------------------')
                print('| Enter a For Edit Student Name.                       |')
                print('| Enter b For Edit Student Age.                        |')
                print('| Enter c For Edit Student Grade.                      |')
                print('--------------------------------------------------------')
                print()
                print()
                cho  = input('Enter Your Choice For Update Student Details :- ')
                if cho == 'a':
                    student['name'] = input('Enter The New Name Of Student :- ')
                    print('Deatils Updated Successfully....!!')
                    break
                elif cho == 'b':
                    student['age'] = int(input('Enter The New age Of Student :- '))
                    print('Deatils Updated Successfully....!!')
                    break
                elif cho == 'c':
                    student['grade'] = input('Enter The New Grade Of Student :- ')
                    print('Deatils Updated Successfully....!!')
                    break
    elif schoice == 4:
        if(len(students)==0):
            print('The Record Is Empty...!!')
        else:    
            sid = int(input("Enter Student's id which you remove :- "))
            for student in students:    
                if sid == student['id']:
                    students.remove(student)
                    print('Student Removed Successfully...!!')
                    break
                else:
                    print('No Student Found With This ID ... !!')
    elif schoice == 5:
        print("-------We Are Offered These Subjects-------")
        print("Biology,Computer Science,Urdu,Russian,Japanese,Chinese,")
    elif schoice == 6:
        print("Exit")
        break
    else:
        print("Enter Valid Number")
