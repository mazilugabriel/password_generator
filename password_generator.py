import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

print("This is my first python Password Generator app!")

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like in your password? \n"))

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
    print(password)
    

