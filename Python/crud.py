#CRUD
#C = Create
#R = Read/Retriew
#U = Update
#D = Delete

print()
print("Welcome to The CRUD System For Bike")
print()

bikes = []
cno = 1
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
        bike = {"id":cno,"name":name,"hp":hp,"cc":cc}
        bikes.append(bike)
        cno += 1
    elif (bchoice == 2):
        print("CNO.     |Name    |HP     |CC      ")
        for bk in bikes:
            print(f'{bk['id']}    |{bk['name']}    |{bk['hp']}     |{bk['cc']}')
    elif (bchoice == 3):
       edit = int(input("Choose a Option WHat You Want to Edit"))
       print()
       if edit == bike['id']:
            print()
       
            
    elif (bchoice == 4):
        rmov = int(input("Enter The CNO. Of Bike For Remove"))
        for bike in bikes:
            if rmov == bike['id']:
                bikes.remove(bike)
                print("Removed Succesfully")
                break
    elif (bchoice == 5):
        print("You're Exit...!")
        break
    else:
        print("Abe Bhai Please Options Ke Hisab Se Daal (1/5)!")
