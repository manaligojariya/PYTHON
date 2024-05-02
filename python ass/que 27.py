# Write a Python program to replace last value of tuples in a list 

def replace_last_value_in_tuples(input_list,new_value):
    result=[]

    for tuple in input_list:
        
        if len(tuple)>0:
            new_tuple=tuple[:-1] + (new_value,)

            result.append(new_tuple)
        else:
            result.append(tuple)
    return result

tuple_list=[(1,2,3),(4,5,6),(7,8,9)]
new_value=99

new_tuples_list=replace_last_value_in_tuples(tuple_list,new_value)
print(new_tuples_list)

