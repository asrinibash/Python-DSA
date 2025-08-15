## PYTHON FROM SCRATCH

# print("hello World")

print("india","python","Usa",5.5,"2",2,False)
# india python Usa 5.5 2 2 False
# in the output where is the space came from ? --> its due to 'sep' parameter - if we use ',' then it automatically take sep param

print("india","python","Usa",5.5,"2",2,False,sep='/')
# india/python/Usa/5.5/2/2/False --we can change the sep param value

# end - this makes an new line. we can change explicitly its value
print("hello",end=' ')
print("world") #now it print in single line- no new line



# NOTES:
# Prints the values to a stream, or to sys.stdout by default.

# Consists 4 parameter:
# sep
#   string inserted between values, default a space.
# end
#   string appended after the last value, default a newline.
# file
#   a file-like object (stream); defaults to the current sys.stdout.
# flush
#   whether to forcibly flush the stream.