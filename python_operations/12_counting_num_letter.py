# By importing Regular Expression Library, we can able to do this
import re

name="Programming a number 1 choice"

digitsCount=re.sub("[^0-9]", "",name)
letterCount=re.sub("[^a-zA-Z]", "",name)
spaceCount=re.findall("[ \n]",name)

print("digits: ",len(digitsCount))
print("letter: ",len(letterCount))
print("space: ",len(spaceCount))