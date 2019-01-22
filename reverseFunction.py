def reverse(a):
    #print(a)
    j = len(a) -1
    #print(j)
    rword = ''
    for i in range(0,len(a)):
        #print(a[j])
        rword = rword + a[j]
        j = j-1
        
    print('Reverse of ' + a + ' is ' + rword)
    
reverse('usa')
reverse(input('Enter the word : '))
