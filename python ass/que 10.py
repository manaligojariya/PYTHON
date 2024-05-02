# Write a Python function that takes two lists and returns true if they have 
# at least one common member

def common_member(list1,list2):

    set1 = set(list1)
    set2 = set(list2)

    common_elements=set1.intersection(set2)

    if common_elements:
        return True

    else:
        return False

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

print(common_member(list1,list2))

list3=[1,2,3]
list4=[4,5,6]

print(common_member(list3,list4))





