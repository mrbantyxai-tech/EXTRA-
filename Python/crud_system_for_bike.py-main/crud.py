#CRUD
#C = Create
#R = Read/Retriew
#U = Update
#D = Delete

print()
print("Welcome to The CRUD System For Bike")
print()

bikes = []
while True:
    print()
    print("Enter 1 For Add Your Bike Name")
    print("Enter 2 For Read Specs of All Bikes")
    print("Enter 3 For Update Your Bike Info")
    print("Enter 4 For Delete info Of Your Bike")
    print("Enter 5 For Exit...!")
    print()
    print()
    bchoice = int(input("Select What You Want to do (1/5):- "))
    print()
    print()

    if (bchoice == 1):
        name = input("Enter Your Bike Model Name :- ")
        hp = int(input("Enter Your Bike's HorsePower :- "))
        cc = float(input("Enter Your Bike's Engine CC Capacity :- "))
        bike = {"name":name,"hp":hp,"cc":cc}
        bikes.append(bike)
    elif (bchoice == 2):
        print("Name    |HP     |CC      ")
        for bk in bikes:
            print(f'{bk['name']}    |{bk['hp']}     |{bk['cc']}')
    elif (bchoice == 3):
        print("")
    elif (bchoice == 4):
        print("")
    elif (bchoice == 5):
        print("You're Exit...!")
        break
    else:
        print("Abe Bhai Please Options Ke Hisab Se Daal (1/5)!")
