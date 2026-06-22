import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# empty list to store the password in
rand_list = []

# Loops to add the random letters, symbols, and numbers based on user input
for _ in range(nr_letters):
    rand_list.append(random.choice(letters))

for _ in range(nr_symbols):
    rand_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    rand_list.append(random.choice(numbers))

# to make the list random will use shuffle()
random.shuffle(rand_list)

new_pass = ""
for password in rand_list:
    new_pass += password

print(f"your new password is: {new_pass}")
