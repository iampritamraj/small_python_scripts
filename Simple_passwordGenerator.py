import random 

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + number + symbols

length = input("Enter password length OR Press Enter to use default length:")
if len(length) == 0:
    length = 16
else:
    length = int(length)
password = "".join(random.sample(all, length))
print(password)