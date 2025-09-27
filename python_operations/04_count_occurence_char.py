# Counting the number of Occurrences  of character in a String

def count_occur_char(string,character):
    count=0
    for i in string:
        if i == character:
            count+=1
    return count

print(count_occur_char("srinibash",'s'))