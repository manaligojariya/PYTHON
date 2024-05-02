# Write a Python program to check a list is empty or not.

def list_empty(input_list):
    
    if not (input_list,list):
        print("This input is not a list")
    
    if len(input_list)==0:
        return True
    else:
        return False
    
if __name__ =="__main__":
    
    empty_list=[]
    print("The List is empty?",list_empty(empty_list))

    not_empty_list=[1,2,3]
    print("The List is empty?",list_empty(not_empty_list))





