# Write a Python function to check whether a number is in a given range

def is_in_range(number,start,end):
    if start<=number<=end:
        return True
    else:
        return False
    
number=42
startrange=20
endrange=50

if is_in_range(number,startrange,endrange):
    print(f"{number} is in the range [{startrange},{endrange}]")
else:
    print(f"{number} is not in the range[{startrange},{endrange}]")