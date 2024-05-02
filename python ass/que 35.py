# Write a Python script to check if a given key already exists in a dictionary.

mydict={'apple':3,'banana':1, 'cherry':2, 'date':5, "fig":4}

key_to_check='apple'

if key_to_check in mydict:
    print(f"'{key_to_check}' exists in the dictionary:")
else:
    print(f"'{key_to_check}' does not exists in the dictionary:")