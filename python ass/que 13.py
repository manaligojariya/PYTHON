# Write a Python program to convert a list of characters into a string

def list_of_string(char_list):
    result_string=''.join(char_list)
    return result_string

char_list=['H','e','l','l','o', ' ','A','h','m','e','d','a','b','a','d','!']
result=list_of_string(char_list)
print("List of characters into a string:",result)