def pallindrome(a):
	#print(a)
	#print(a[::-1])
	#-- Check if the string is same as the reverse of the string using ::-1
	if a == a[::-1]:
	    print(a + ' is pallindrome')
	else:
	    print(a + ' is not pallindrome')
	
pallindrome('malayalam')
pallindrome('malayalee')
