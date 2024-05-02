# Write a Python program to remove duplicates from a list.

def remove_duplicates(input_list):
    
    unique_elements=set(input_list)

    result_list=list(unique_elements)

    return result_list

input_list=[1, 2, 3, 2, 4, 5, 1, 6, 7, 6]
result=remove_duplicates(input_list)
print(result)    



