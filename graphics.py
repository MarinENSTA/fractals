if __name__ == '__main__':
    import time
    import matplotlib
    from matplotlib import colors
    import matplotlib.pyplot as plt
    import pygame
    from pygame.locals import *
    from julia import *
    
    prop = 1.5
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((int(870*prop), int(400*prop)))
    pygame.display.set_caption('JuliaSets')

    fraclist = [0]*4
    reclist = [0]*4

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
        #clock.tick(30)
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)
        
        # Shaded rendering
        light = colors.LightSource(azdeg=315, altdeg=10)
        screen.fill((0,0,0))
        for i in range(4):
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                elif event.type == KEYDOWN:
                    pygame.quit()
            
            Z, N = julia_set(xmin, xmax, ymin, ymax, xn, yn, C[i], maxiter, horizon)

            #  This line will generate warnings for null values but it is faster to
            # process them afterwards using the nan_to_num
            with np.errstate(invalid='ignore'):
                M = np.nan_to_num(N + 1 - np.log(np.log(abs(Z)))/np.log(2) + log_horizon)
            
            M=light.shade(M,cmap=plt.cm.hot,vert_exag=1.5,norm=colors.PowerNorm(0.3),blend_mode='hsv')
            plt.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
            ax.set_xticks([])
            ax.set_yticks([])
            
            plt.savefig("frac"+str(i)+".png")
            fraclist[i] = pygame.image.load("frac"+str(i)+".png").convert()
            fraclist[i] = pygame.transform.scale(fraclist[i],(int(180*prop),int(150*prop)))
            reclist[i] = fraclist[i].get_rect()
            reclist[i] = reclist[i].move((int((180+50)*i*prop),int(20*prop)))
            screen.blit(fraclist[i],reclist[i])
            
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
            elif event.type == KEYDOWN:
                    pygame.quit()
        pygame.display.flip()
    
        fitness = [0,0,0,0]

        print("Continuer ?")
        q = input()
        if q == 'no' or q == 'n':
            quit = True

        else:
            print("Garder l'ancienne génération ou la nouvelle ? (nouvelle = 0, ancienne passer)")
            i = int(input())
            if i == 0:
                for j in range(4):
                    print("Préférences de l'image", j, "(entre 1 et 10) :")
                    fitness[i] = int(input())
                
                print()
                
                #print(C)
                C = crossover_all(C, fitness, 0.9)
                #print(C)
                C = mutation_all(C, 0.1, 0.1)

                #print(C)

    
    

