def printReverse(n):
	if n>0 : 
		print(n)
		printReverse(n-1)
printReverse(10)


def factoriel(n):
	if(n<0):
	    print("Impossible!")
	if(n==0 OR n==1):
		return 1
	return n*factoriel(n-1)

print(factoriel(5))


                
        
