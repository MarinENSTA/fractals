from random import Random

generator=Random()

def mutation(C,pm,sigma):
	x=generator.uniform(0,1)
	if x<pm:
		for D in C :
			D[0]+=generator.gauss(0,sigma)
			D[1]+=generator.gauss(0,sigma)
	return C
