# Write a Python program to check whether a list contains a sub list  

def sublist(sublist,mainlist):
    if len(sublist)==0:

        return True
    
    if len(sublist) > len(mainlist):
        return False
    
    for i in range(len(mainlist)-len(sublist)+1):
        if mainlist[i:i+len(sublist)]==sublist:
            return True
    return False

main_list=[1,2,3,4,5,6,7,8]
sub_list=[3,4,5]

if sublist(sub_list,main_list):
    print("Sublist Found The Mainlist:")
else:
    print("Sublist Not Found The Mainlist: ")
