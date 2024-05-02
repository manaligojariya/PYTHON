# Write a Python program to unzip a list of tuples into individual lists

def unzip_list_of_tuples(list_of_tuples):
    unzipped_lists=list(map(list,zip(*list_of_tuples)))

    return unzipped_lists

list_of_tuples=[(1,'a'),(2,'b'),(3,'c')]

unzipped_lists=unzip_list_of_tuples(list_of_tuples)

print("Unzip a list Of Tuples Into Individual Lists:",unzipped_lists)
