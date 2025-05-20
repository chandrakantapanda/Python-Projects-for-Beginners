import random
import string

def generate_password(length=12):
    letters = string.ascii_letters #a-zA-z
    digits = string.digits #0-9
    symbols = string.punctuation #!@#$%^
    #combine all the characters
    all_chrs = letters+ digits + symbols
    password = ''.join(random.choice(all_chrs) for _ in range(length))
    return password

#usage
length = int(input("Enter desired password length:"))
print("your secure password is:",generate_password(length))


