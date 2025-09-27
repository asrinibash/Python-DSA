# find the maximum number in a list:


def find_max_num(lis):
    max=-1e109
    
    for i in range(len(lis)):
        if lis[i]> max:
            max=lis[i]
        
    return max

print(find_max_num([1,2,3,4,5,63,7,8,9,10,11]))


# find minimum number in list:

def find_min_num(lis):
    min=1e109
    
    for i in lis:
        if min > i:
            min=i
            
    return min

print(find_min_num([1,2,3,4,5,63,7,8,9,10,11]))


#find middle element
lis=[1,2,3,4,5,63,7,8,9,10,11]
midElement = int((len(lis))/2) 
print(lis[midElement])