# Write a Python script to concatenate following dictionaries to create a 
# new one

dict1={'a':1, 'b':2}
dict2={'c':3, 'd':4}
dict3={'e':5, 'f':6}

concatenate_dict={key:value for d in [dict1,dict2,dict3] for key,value in d.items()}

print(concatenate_dict)