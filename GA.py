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
	C_mute=[]
	if x<pm:
		for D in C :
			Doublet=[]
			for y in D:
				Doublet+=[y+generator.gauss(0,sigma)]
		C_mute+=[Doublet]
	return C_mute

def mutation_all(C_list,pm,sigma):
	C_list_mut=[]
	for i in range(len(C_list)):
		C_mute=mutation(C_list[i],pm,sigma)
		C_list_mut+=[C_mute]
	return C_list_mut


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

def crossover1_all(C_list,P,pc):
	C_list_cross=[]
	for i in range(len(C_list)):
		C_cross=crossover1(C_list,P,pc)
		C_list_cross+=[C_cross]
	return C_list_cross



def mutation2(C,pm,sigma):                #au cas où on essaie de prendre en compte les tables de couleurs la liste C a pour avant dernier élement les paramètres RGB et comme dernier élements les paramètres de lumière
	x=generator.uniform(0,1)
	if x<pm:
		l=len(C)
		for i in range(l-2):                  #on mute les doublets [cx,cy]
			D=C[i]
			for y in D:
				y+=generator.gauss(0,sigma)
				
		for y in C[l-2]:                     #on mute la couleur (RGB)
			y+=generator.uniform(0,10)
			if y>255:
				y=255
			else:
				if y<0:
					y=0

		for y in C[l-1]:
			y+=generator.gauss(0,sigma^2)
			if y>1:
				y=1
			else:
				if y<0:
					y=0