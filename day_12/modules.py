# Day 12 - 30DaysOfPython Challenge

import random
import string

## LEVEL 1

# Write a function which generates a six digit/character random_user_id.
def random_user_id():
    chars = string.ascii_letters + string.digits
    rand_user_id = ""
    for _ in range(6):
        rand_user_id += random.choice(chars)
    return(rand_user_id)

print(random_user_id()) 

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_chars = int(input("Num chars\n"))
    num_ids = int(input("Num IDs\n"))
    chars = string.ascii_letters + string.digits
    rand_user_ids = []
    rand_user_id = ""

    for _ in range(num_ids):
        for _ in range(num_chars):
            rand_user_id += random.choice(chars)
        rand_user_ids.append(rand_user_id)
        rand_user_id=""
    
    return rand_user_ids

print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    return(f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})" )

print(rgb_color_gen())

## LEVEL 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.)
def list_of_hexa_colors(number):
    symbols = string.digits + "abcdef"
    colors = []
    color = "#"

    for _ in range(number):
        for _ in range(6):
            color += random.choice(symbols)
        colors.append(color)
        color = "#"

    return colors

print(list_of_hexa_colors(3))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(number):
    colors = []
    for _ in range(number):
        colors.append(rgb_color_gen())
    
    return colors

print(list_of_rgb_colors(3))

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type, number):
    colors = []
    if type == "hexa":
        colors = list_of_hexa_colors(number)
    elif type == "rgb":
        colors = list_of_rgb_colors(number)
    else:
        return None
    
    return colors

print("RGB and Hexa generators")
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

