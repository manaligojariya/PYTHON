# Write a Python program to find the second smallest number in a list.

def second_smallest(nums):
    if len(nums)<2:
        return None
    
    smallest=second_smallest=float('inf')

    for num in nums:
        if num<smallest:
            second_smallest=smallest
            smallest=num
        elif num<second_smallest and num!=smallest:
            second_smallest=num

    if second_smallest==float('inf'):
        return None
    
    return second_smallest

numbers=[10,9,5,4,1]
result=second_smallest(numbers)

if result is None:
    print("The second smallest number in a list:")
else:
    print("The second element is:",result)
    
    
        

