def quadratic(L):

	n = len(L)
	if n<1:
		return L

	maxSoFar_index = 0
	max =[]
	subsequence = []

	for i in range(n):          
		max.append(L[i])

	for i in range(n):          
		subsequence.append(-1) 

	for i in range(1,n):    
		for j in range(i):                            
			if max[j] + L[i] >= max[i]:                                
				subsequence[i] =j                                
				max[i] = max[j] + L[i]                                  
		if max[i] >=max[maxSoFar_index]:                     
			maxSoFar_index = i
			 
	#print maxSoFar_index
	k = maxSoFar_index
	max_subsequence=[]

	while k != -1 : 
		#print k           
		max_subsequence.append(L[k])            
		k = subsequence[k]

	max_subsequence.reverse()                             
	return max_subsequence

def linear(L):

	sizeL = len(L)
	if sizeL < 1:
		return L
	
	subsequence = []
	for i in range(n):          
		subsequence.append(-1) 

	incl = L[0]
	excl = 0
	for i in range(1, sizeL): 
		if incl< excl:
			exclNew = excl
		else:
			exclNew = incl
			subsequence[i] = i-1
   		  
    	incl = excl + L[i]  
    	excl = exclNew 

    if(excl) 
   
	return max(incl, excl)   


if __name__ == '__main__':
	print linear([1,2,3,4,5])