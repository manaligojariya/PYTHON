# Write a Python program to convert a list of tuples into a dictionary.

def list_of_tuples_to_dict(tuple_list):
    dictionary={}

    for item in tuple_list:
        if len(item) ==2:
            key,value=item
            dictionary[key]=value
        else:
            print(f"Ignoring tuple {item} as it does not have exzactly 2 elements.")

    return dictionary

tuple_list=[('a',1),('b',2),('c',3)] 

result_dict=list_of_tuples_to_dict(tuple_list)

print(result_dict)

