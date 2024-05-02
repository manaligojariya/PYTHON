'''Write a Python program to check whether an element exists within a 
tuple.'''

mytuple=(10,20,30,40,50)

check_element=40

if check_element in mytuple:
    print(f"{check_element} exists in the tuple.")
else:
    print(f"{check_element} does not exists in the tuple.")
