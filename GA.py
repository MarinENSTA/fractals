from random import Random

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


def crossover1(C_list,P,maxiter):
	l=len(C_list[0])
	C_cross=[]

	p_adj=0                                       #on crée une liste P_final correspondant aux nombres d'éléments que l'on veut dans le C_cross 
	for i in range(len(P)):
		p_adj+=P[i]
	P_final=[(maxiter/p_adj)*i for i in P]

	P_tot=0
	for i in range(len(P_final)):
		P_final[i]=int(P_final[i])
		P_tot+=P_final[i]
	erreur=maxiter-P_tot

	rang_ajout=maximum(P_final)                    #si cela donne un nombre de termes < maxiter (longueur de la liste), on corrige sur l'élément le plus voulu 
	P_final[rang_ajout]+=erreur
	
	if erreur != 0:
		P_adj[0]+=erreur

	for i in range(len(P_final)):                  # croisement
		rang_choisi=maximum(P_final)
		C=C_list[rang_choisi]
		rang_max=P_final[rang_choisi]
		for k in range(rang_max):
			C_cross+=[C[k]]
		P_final[rang_choisi]=-1

	return C_cross