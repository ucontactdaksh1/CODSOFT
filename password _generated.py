import random
import string
def generate_password (length):
    characters=string.ascii_lowercase + string.digits
    password=''.join(random.choice(characters) for i in range (length))
    return password
try:
    ch = 1
    while (ch!=0):
        password_length=int (input("enter the desired password length:"))
        if password_length<=0:
            print("please enter a positive length.")
        print("Generated password:",generate_password(password_length))
        ch= int(input("Enter a value: "))
except ValueError:
    print ("invalid input.please enter a valid positive integer for the password length.")    