if __name__ == '__main__':
	import time
	import matplotlib
	from matplotlib import colors
	import matplotlib.pyplot as plt

	from julia import *
	from GA import *

	xmin, xmax, xn = -1.25, +1.25, 3000/2
	ymin, ymax, yn = -1.25, +1.25, 2500/2

	maxiter = 100
	horizon = 2.0 ** 40
	log_horizon = np.log(np.log(horizon))/np.log(2)

	dpi = 72
	width = 10
	height = 10*yn/xn

	C0 = [[-0.4,0.6]]*100
	C1 = [[0.285, 0.01]]*100
	C2 = [[0.3,0.5]]*100
	C3 = [[0,-1]]*100
	C = [C0, C1, C2, C3]
	quit = False
	while not quit:
		
		fig = plt.figure(figsize=(width, height), dpi=dpi)
		ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

		# Shaded rendering
		light = colors.LightSource(azdeg=315, altdeg=10)
		
		for i in range(4):
			Z, N = julia_set(xmin, xmax, ymin, ymax, xn, yn, C[i], maxiter, horizon)

			#  This line will generate warnings for null values but it is faster to
			# process them afterwards using the nan_to_num
			with np.errstate(invalid='ignore'):
				M = np.nan_to_num(N + 1 -
								  np.log(np.log(abs(Z)))/np.log(2) +
								  log_horizon)

			M = light.shade(M, cmap=plt.get_cmap("PiYG"))
			# see https://matplotlib.org/examples/color/colormaps_reference.html
			fig.add_subplot(2, 2, i+1)
			plt.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
			ax.set_xticks([])
			ax.set_yticks([])

		plt.ion()
		plt.show()

		fitness = [0,0,0,0]

		print("Continuer ? (n ou 'no' pour arrêter)")
		q = input()
		if q == 'no' or q == 'n':
			quit = True

		else:
			print("Garder l'ancienne génération ou la nouvelle ? (ancienne = 0, nouvelle = entrée)")
			i = input()

			if i != '0':
				for j in range(4):
					print("Préférences de l'image", j, "(entre 1 et 10) :")
					fitness[j] = int(input())

				print()
				C = crossover_all(C, fitness, 0.9)
				C = mutation_all(C, 0.1, 0.1)

	# Normalized recount as explained in:
	# https://linas.org/art-gallery/escape/smooth.html
	# https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift

	