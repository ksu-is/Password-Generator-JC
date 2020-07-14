import random
characters = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()_-+[]{};/';.,"
password_length = int(input("enter length of required password"))
password = "".join(random.sample(characters,password_length))
print(password)
