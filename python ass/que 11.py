'''Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.'''

def generate_square_list(start,end):
    square_list=[x**2 for x in range (start,end+1)]
    return square_list

def main():
    start_number=1
    end_number=30

    square_list=generate_square_list(start_number,end_number)

    print("List of squares of numbers between 1 and 30:")
    print(square_list[:5])
    print(square_list[-5:])

if __name__=="__main__":
    main()