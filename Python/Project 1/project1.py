print("Welcome To The Interactive Personal Data Collecter!")
print(" ")

name = input("Please Enter Your Name:")
age = int(input("Please Enter Your Age:"))
height = float(input("Please Enter Your Height in Meters:"))
fav_num = int(input("PLease Enter Your Favorite Number:"))

print(" ")

print("Thanks You! Here is The Information we Collected:")

print("Name:", name,end=" ")
print(("(Type:"),type(name),end=" ")
print(",Memory Address:",id(name))

print("Age:", age,end=" ")
print("(Type:",type(age),end=" ")
print(",Memory Address:",id(age))

print("Height:", height,end=" ")
print(("(Type:"),type(height),end=" ")
print(",Memory Address:",id(height))

print("Favorite Number:",fav_num,end=" ")
print(("(Type:"),type(fav_num),end=" ")
print(",Memory Address:",id(fav_num))

print(" ")

age_sum = 2025 - age

print("Your Birth Year is Approximately:",(age_sum),end=" ")
print("(Based On Your Age:",age)

print(" ")

print("Thank You For Using The Personal Data Collecter, Goodbye!")




