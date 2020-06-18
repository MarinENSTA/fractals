from random import Random
from random import choices

generator=Random()

def maximum(L):
	maxi=L[0]
	rang_max=0
	for i in range(len(L)):
		if L[i]>maxi:
			rang_max=i
	return rang_max

def mutation(C,pm,sigma):
	x=generator.uniform(0,1)
	if x<pm:
		for D in C :
			for y in D:
				y+=generator.gauss(0,sigma)
	return C


def crossover1(C_list,P,pc):
	x=generator.uniform(0,1)
	if x<pc:
		l=len(C_list[0])
		C_cross=[]

		p_adj=0                                       #on crée une liste P_final correspondant aux probabilités d'avoir un élément d'une liste C dans C_cross
		for i in range(len(P)):
			p_adj+=P[i]
		P_final=[(1/p_adj)*i for i in P]


		for j in range(l):                           #on choisi aléatoirement le coefficient dans une des listes C selon la préférence de l'utilisateur
			C_choisi=choices(C_list,P_final)
			C_cross+=[C_choisi[0][j]]

	return C_cross
