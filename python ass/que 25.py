# Write a Python program to convert a list to a tuple

def list_to_tuple(input_list):
    output_tuple=tuple(input_list)
    return output_tuple

mylist=['Pizza','Frenchfries','Dabeli','Vadapav','Panipuri']
mytuple=list_to_tuple(mylist)

print("Convert a List To a Tuple:",mytuple)
