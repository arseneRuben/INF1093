def printReverse(n):
	if n>0 : 
		print(n)
		printReverse(n-1)
printReverse(10)