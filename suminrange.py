
def suminrange(a,b):
    j = 0
    for i in range(a,b+1):
        #print(i)
        j = j + i
    
    print(j)
    print('Sum of numbers between ' + str(a) + ' and ' + str(b) + ' is ' + str(j))
suminrange(1,2)
suminrange(1,3)    
suminrange(1,4)
suminrange(1,5)
