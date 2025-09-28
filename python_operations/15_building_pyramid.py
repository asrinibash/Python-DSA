
def buildPyramid(floor):
    h=2*floor-1
    
    for i in range(1,h,2):
        print('{:^{}}'.format('*'*i,h))
        

buildPyramid(5)

# output:
#         *    
#        ***   
#       *****
#      *******