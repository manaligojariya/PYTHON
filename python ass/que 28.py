# Write a Python program to find the repeated items of a tuple

def find_repeated_items(input_tuple):
    item_count = {}
    repeated_items = []

    for item in input_tuple:
        if item in item_count:
            item_count[item] += 1
            if item not in repeated_items:
                repeated_items.append(item)
        else:
            item_count[item] = 1
    
    return repeated_items

my_tuple = (1, 2, 3, 4, 3, 2, 5, 6, 7, 5)
repeated_items = find_repeated_items(my_tuple)

if repeated_items:
    print("Repeated items:", repeated_items)
else:
    print("No repeated items found in the tuple.")



                
            

