# Write a Python program to get unique values from a list

def get_unique_values(input_list):
    unique_values=[]
    for item in input_list:
        if item not in unique_values:
            unique_values.append(item)

    return unique_values

input_list=[1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_values=get_unique_values(input_list)
print(unique_values)