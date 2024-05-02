# Write a Python program to print all unique values in a dictionary.

def unique_values(dictionary):
    unique_set=set()

    for value in dictionary.values():
        unique_set.add(value)

    return unique_set

my_dict={'a':100,'b':200,'c':100,'d':300,'e':200}

unique_vals=unique_values(my_dict)

print("Uniques values in the dictionary:")
for value in unique_vals:
    print(value)


