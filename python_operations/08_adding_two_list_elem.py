# Adding Two List Elements Together


def add_two_list_elem_together(lst1,lst2):
    res=[]
    for i in range(0,len(lst1)):
        res.append(lst1[i]+lst2[i])
        
    return res

lst1=[1,2,3]
lst2=[3,4,5]
print(add_two_list_elem_together(lst1,lst2))