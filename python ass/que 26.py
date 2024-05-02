# Write a Python program to reverse a tuple

def reverse_tuple(input_tuple):
    reverse_tuple=tuple(reversed(input_tuple))
    return reverse_tuple

mytuple=(10,20,30,40,50)

reverse_tuple=reverse_tuple(mytuple)

print("Reverse a Tuple:",reverse_tuple)
