# Write a Python program to read a random line from a file.

import random

def read_random_line(filename):
    try:
        with open(filename,'r') as file:
            total_lines=sum(1 for line in file)
            
            random_line_number=random.randint(1,total_lines)

            file.seek(0)

            for current_line_number,line in enumerate(file,1):
                
                if current_line_number == random_line_number:
                    return line.strip()
                
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
filename='sample.txt'
random_line=read_random_line(filename)
print(f"Random line from the file: {random_line}")