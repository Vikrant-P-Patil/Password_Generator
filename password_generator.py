import random

    #what does import random do? 
    #ans : import random provides functions for generating pseudo-random numbers and making random selections, such as random.random() for floats between 0 and 1, random.choice() for selecting items from a sequence, and random.randint() for random integers

import string

    #what does import string do?
    #ans : import string provides access to string constants like string.ascii_letters, string.digits, and string.punctuation, which define predefined sets of characters used as sources for generating random strings or processing text.

def generate_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters
    # string.ascii is a constant that holds all the 52 english letters in a single string(lowercase and uppercas)
    digits = string.digits
    special = string.punctuation
    #string.punctuation is also a constant that holds all the special charachers in a string together

    characaters = letters
    if numbers:
        characaters += digits

    if special_characters:
        characaters += special

    pwd = ""
    criteria = False
    number= False
    has_special = False

    while not criteria or len(pwd) < min_lenght:
        char = random.choice(characaters)
        #random.choice chooses random elemetents from the character string
        pwd += char

        if char in digits:
            number=True

        elif char in special:
            has_special = True

        criteria = True

        if numbers:
            criteria = number

        if special_characters:
            criteria=criteria  and has_special

    return pwd

min_length=int(input("Enter the minimum length for your password : "))
number = input("Do you want to have numbers in your password? (y/n) : ").lower() == "y"
has_special = input("Do you want to have special characters in your password to make it more stronger? (y/n) : ").lower() == "y"
pwd = generate_password(min_length, number, has_special)
print("Your generated password is:",pwd) 