import random
characters = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()_-+[]{};/';.,"
password_length = int(input("enter length of required password"))
password = "".join(random.sample(characters,password_length))
print(password.upper())
print(password.lower())
answer = input("Do you like the password? Enter yes or no: ")
if answer == "yes":
    print("Thank You!")
elif answer == "no":
    password = "".join(random.sample(characters,password_length))
    print(password.upper())
    print(password.lower())
else:
    print("Please enter yes or no.")
