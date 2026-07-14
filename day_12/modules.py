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