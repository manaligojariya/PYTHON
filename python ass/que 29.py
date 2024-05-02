# Write a Python program to remove an empty tuple(s) from a list of tuples

def remove_empty_tuples(list):
    return [tuple for tuple in list if tuple]

list_of_tuple=[(1,2),(),(3,4),(),(5,6),(),()]

filtered_list=remove_empty_tuples(list_of_tuple)

print("Remove an Empty Tuple From a List Of Tuple:",filtered_list)

