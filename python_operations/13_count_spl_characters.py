# by importing regular expression package:

import re

def count_spl_chars(string):
    count = re.sub('[\w]+', '', string)
    
    return len(count)

print(count_spl_chars("!@#$%^&*()"))