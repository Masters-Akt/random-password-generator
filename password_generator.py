import random
import array
n = int(input("Enter length of passowrd to generated: "))
while n<4:
    print("Minimum password length must be 4. Try again.")
    n = int(input("Enter length of passowrd to generated: "))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lcase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ucase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', ':', ';', '<', '>', '?', '/', '.', ',']

combined_list = digits + lcase_chars + ucase_chars + symbols

rand_digits = random.choice(digits)
rand_upper = random.choice(ucase_chars)
rand_lower = random.choice(lcase_chars)
rand_sym = random.choice(symbols)

temp_password = rand_digits + rand_upper + rand_lower + rand_sym

for x in range(n-4):
    temp_password = temp_password + random.choice(combined_list)
    temp_pass_list = array.array('u', temp_password)
    random.shuffle(temp_pass_list)

temp_pass_list = array.array('u', temp_password)
random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x

print(password)