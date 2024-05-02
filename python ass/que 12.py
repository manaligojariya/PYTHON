'''Write a Python function that takes a list and returns a new list with unique 
elements of the first list'''

def unique_elements(input_list):
    unique_list=[]
    seen_elements=set()

    for item in input_list:
        if item not in seen_elements:
            unique_list.append(item)
            seen_elements.add(item)

    return unique_list

input_list=[1, 2, 2, 3, 4, 4, 5, 6, 6]
result=unique_elements(input_list)
print(result)