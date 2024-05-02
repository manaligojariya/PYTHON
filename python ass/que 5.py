'''
Write a Python function to get the largest number, smallest num and sum 
of all from a list.
'''

def get_largest_smallest_sum(numbers):

    largest = smallest =  numbers[0]
    total_sum = 0

    for num in numbers:
        if num > largest:
            largest=num
        if num < smallest:
            smallest=num
        total_sum+=num

    return largest,smallest,total_sum

numbers_list=[23, 45,12,67,5,89,34]
largest_num,smallest_num,sum_of_all = get_largest_smallest_sum(numbers_list)
print("largest numbers:",largest_num)
print("smallest numbers:",smallest_num)
print("sum of all:",sum_of_all)

