from random import Random

generator=Random()

def maximum(L):
	maxi=L[0]
	rang_max=0
	for i in range(len(L)):
		if L[i]>maxi:
			rang_max=i
	return 

def mutation(C,pm,sigma):
	x=generator.uniform(0,1)
	if x<pm:
		for D in C :
			for y in D:
				y+=generator.gauss(0,sigma)
	return C


