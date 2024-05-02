# Write a Python function that checks whether a passed string is palindrome 
# or not

def is_palindrome(input_string):

    cleaned_string=''.join(input_string.split()).lower()

    return cleaned_string==cleaned_string[::-1]

input_str="racecar"
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not palindrome.")

    