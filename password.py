import random
import array

digits=["0","1","2","3","4","5","6","7","8","9"]

low_chars=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

up_chars=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols=['@', '#', '$']

all_pass = digits + low_chars + up_chars + symbols

ran_digits = random.choice(digits)
ran_lowchars = random.choice(low_chars)
ran_upchars = random.choice(up_chars)
ran_syms = random.choice(symbols)

print("Password Generator!","\n")
len=int(input("Enter the length for your password:"))

password = ''.join(random.choices(all_pass, k=len))

print("Your Password: ", password)