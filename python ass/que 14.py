# Write a Python program to select an item randomly from a list
import random

def random_item(input_list):
    if len(input_list)==0:
        return None
    else:
        return random.choice(input_list)
    
items=["Apple","Banana","DryFruit","Orange","Grape"]
random_item=random_item(items)
print("Randomly items in selected:",random_item)