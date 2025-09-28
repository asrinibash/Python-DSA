# Remove Duplicates from a List

def remove_duplicates(lst):
    return list(set(lst))

lst=[1,1,3,4,1,2,4,51,1,3,4,5]

print(remove_duplicates(lst))