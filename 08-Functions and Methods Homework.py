def vol(rad):
    return(4/3 * 3.17 * rad **3)

print(vol(2))

-----------------
def ran_check(num,low,high):
    
    if num >= low and num <= high:
        print(str(num) + ' is in the range between ' + str(low) + ' and ' + str(high))
    else:
        print(str(num) + ' is NOT in the range between ' + str(low) + ' and ' + str(high))
        
ran_check(5,2,7)

-----------------
def ran_bool(num,low,high):
    return(num >= low and num <= high)

print(ran_bool(3,1,10))

-----------------
def up_lows(s):
    up = 0
    lo = 0
    for i in s:
        if i.isupper(): up = up + 1
        if i.islower(): lo = lo + 1

    print('Original String : ' + s)
    print('No. of Upper case characters : ' + str(up))
    print('No. of Lower case characters : ' + str(lo))
up_lows('Hello Mr. Rogers, how are you this fine Tuesday?')

-----------------
def unique_list(lst):
    ulst = []
    for i in lst:
        if i not in ulst: ulst.append(i)
    
    print(ulst)
        
unique_list([1,1,2,2,3,3,4,5])
-----------------
def multiply(numbers):
    num = 1
    for i in numbers:num = i * num
    print(num)

multiply([1,2,3,-4])

-----------------
def palindrome(s): return s.upper() == s[::-1].upper()
    
print(palindrome('Appa'))
-----------------

import string
    
alphabet = string.ascii_lowercase
#print(alphabet)

def unique_list(lst):
    a = []
    ulst = []
    word = ''
    for i in lst:
        a.append(i)
        if i not in ulst: ulst.append(i)
    
    for j in ulst:
        word = word + j
    
    word = word.split(" ")
    word = "".join(word)

    if 'a' in word.lower() and 'm' in word.lower(): 
        print(True) 
    else: 
        print(False)
    

   # print(a)
    print(ulst)
    print(word)
    
    s = []
    for k in word:
        s.append(k)
    
    print(s)
unique_list('Hello My name is someone')
