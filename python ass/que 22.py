# Write a Python program to convert a tuple to a string.

def tuple_to_string(input_tuple):

    string_elements=[str(element) for element in input_tuple]

    output_string=','.join(string_elements)
    
    return output_string

mytuple=(10,20,30,40,50,60,70,80,90,100)

mystring=tuple_to_string(mytuple)

print("Convert a tuple to a string:",mystring)

