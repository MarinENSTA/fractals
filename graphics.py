#constantes
#WINDOWW
#WINDOWH

def alive():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
        elif event.type == KEYDOWN:
            pygame.quit()

def menu(prop):   
    
    WHITE = (255, 255, 255)
    ROUGE = (255,0,0)
    VERT = (50,205,50)
    BLEU = (0,0,255)
    BLACK = (0,0,0)
    fitness = [0]*4
    
    ## ECRITURE DES -1
    ml_surf = FONT.render("-1", True, WHITE)
    ml_rect = ml_surf.get_rect(topleft=(0,int(170*prop)))
    screen.blit(ml_surf, ml_rect)
    
    mr_surf = FONT.render("-1", True, WHITE)
    mr_rect = mr_surf.get_rect(topleft=((180+50)*prop, int(170*prop)))
    screen.blit(mr_surf, mr_rect)
    
    mlm_surf = FONT.render("-1", True, WHITE)
    mlm_rect = mlm_surf.get_rect(topleft=((180+50)*2*prop, int(170*prop)))
    screen.blit(mlm_surf, mlm_rect)
    
    mrm_surf = FONT.render("-1", True, WHITE)
    mrm_rect = mrm_surf.get_rect(topleft=((180+50)*3*prop, int(170*prop)))
    screen.blit(mrm_surf, mrm_rect)

    ## ECRITURE DES +1
    pl_surf = FONT.render("+1", True, WHITE)
    pl_rect = pl_surf.get_rect(topleft=(int(150*prop),int(170*prop)))
    screen.blit(pl_surf, pl_rect)
    
    pr_surf = FONT.render("+1", True, WHITE)
    pr_rect = pr_surf.get_rect(topleft=(int((150+50+180)*prop), int(170*prop)))
    screen.blit(pr_surf, pr_rect)
    
    plm_surf = FONT.render("+1", True, WHITE)
    plm_rect = plm_surf.get_rect(topleft=(int((180+50)*prop*2+150*prop), int(170*prop)))
    screen.blit(plm_surf, plm_rect)
    
    prm_surf = FONT.render("+1", True, WHITE)
    prm_rect = prm_surf.get_rect(topleft=(int((180+50)*prop*3+150*prop), int(170*prop)))
    screen.blit(prm_surf, prm_rect)
    score(prop,fitness)
    
    next_surf = FONT.render("SUIVANTE", True, WHITE)
    next_rect = next_surf.get_rect(center=(int(870*prop/2), int(310*prop)))
    pygame.draw.rect(screen,VERT,next_rect, 0)
    screen.blit(next_surf, next_rect)
    
    previous_surf = FONT.render("PRECEDENTE", True, WHITE)
    previous_rect = previous_surf.get_rect(center=(int(870*prop/4), int(310*prop)))
    pygame.draw.rect(screen, BLEU,previous_rect, 0)
    screen.blit(previous_surf, previous_rect)
    
    leave_surf = FONT.render("QUITTER", True, WHITE)
    leave_rect = leave_surf.get_rect(center=(int(3*870*prop/4), int(310*prop)))
    pygame.draw.rect(screen, ROUGE,leave_rect, 0)
    screen.blit(leave_surf, leave_rect)
    
    
    
    pygame.display.flip()
    
    done=False
    
    while not done:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if pl_rect.collidepoint(event.pos):
                        if fitness[0]<9:
                            fitness[0]+=1
                    if ml_rect.collidepoint(event.pos):
                        if fitness[0]>0:
                            fitness[0]-=1
                    if mr_rect.collidepoint(event.pos):
                        if fitness[3]>0:
                            fitness[3]-=1
                    if pr_rect.collidepoint(event.pos):
                        if fitness[3]<9:
                            fitness[3]+=1
                    if mrm_rect.collidepoint(event.pos):
                        if fitness[2]>0:
                            fitness[2]-=1
                    if prm_rect.collidepoint(event.pos):
                        if fitness[2]<9:
                            fitness[2]+=1
                    if plm_rect.collidepoint(event.pos):
                        if fitness[1]<9:
                            fitness[1]+=1
                    if mlm_rect.collidepoint(event.pos):
                        if fitness[1]>0:
                            fitness[1]-=1
                    if leave_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    if next_rect.collidepoint(event.pos):
                        done = True
                    if previous_rect.collidepoint(event.pos):
                        return False
        score(prop,fitness)
        pygame.display.flip()
    
    return fitness
                    
    
def score(prop, fitness):
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    
    left_surf = FONT.render(str(fitness[0]), True, BLACK)
    left_rect = left_surf.get_rect(center=(90*prop, int((170+30)*prop)))
    pygame.draw.rect(screen, WHITE,left_rect, 0)
    screen.blit(left_surf, left_rect)
    
    right_surf = FONT.render(str(fitness[3]), True, BLACK)
    right_rect = right_surf.get_rect(center=(90*prop*3+50*prop, int((170+30)*prop)))
    pygame.draw.rect(screen, WHITE,right_rect, 0)
    screen.blit(right_surf, right_rect)
    
    mleft_surf = FONT.render(str(fitness[1]), True, BLACK)
    mleft_rect = mleft_surf.get_rect(center=(90*prop*5+50*2*prop, int((170+30)*prop)))
    pygame.draw.rect(screen, WHITE,mleft_rect, 0)
    screen.blit(mleft_surf, mleft_rect)
    
    mright_surf = FONT.render(str(fitness[2]), True, BLACK)
    mright_rect = mright_surf.get_rect(center=(90*prop*7+50*3*prop, int((170+30)*prop)))
    pygame.draw.rect(screen, WHITE,mright_rect, 0)
    screen.blit(mright_surf, mright_rect)
    
    
if __name__ == '__main__':
    import time
    import matplotlib
    from matplotlib import colors
    import matplotlib.pyplot as plt
    import pygame
    from pygame.locals import *
    from julia import *
    from GA import *
    import os
    import sys
    
    pygame.init()
    FONT = pygame.font.Font("freesansbold.ttf", 60)
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)
    prop = 2
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((int(870*prop), int(350*prop)))
    pygame.display.set_caption('JuliaSets')
    icone = pygame.image.load("fract.png")
    pygame.display.set_icon(icone)

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
    oldgen=C
    
    quit = False
    while not quit:
        #clock.tick(30)
        alive()
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)
        
        # Shaded rendering
        light = colors.LightSource(azdeg=315, altdeg=10)
        screen.fill((0,0,0))
        alive()
        for i in range(4):
            alive()
            Z, N = julia_set(xmin, xmax, ymin, ymax, xn, yn, C[i], maxiter, horizon)

            #  This line will generate warnings for null values but it is faster to
            # process them afterwards using the nan_to_num
            with np.errstate(invalid='ignore'):
                M = np.nan_to_num(N + 1 - np.log(np.log(abs(Z)))/np.log(2) + log_horizon)
            
            M = light.shade(M, cmap=plt.get_cmap("viridis"))
            plt.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
            ax.set_xticks([])
            ax.set_yticks([])
            alive()
            plt.savefig("frac"+str(i)+".png")
            fraclist[i] = pygame.image.load("frac"+str(i)+".png").convert()
            fraclist[i] = pygame.transform.scale(fraclist[i],(int(180*prop),int(150*prop)))
            reclist[i] = fraclist[i].get_rect()
            reclist[i] = reclist[i].move((int((180+50)*i*prop),int(20*prop)))
            screen.blit(fraclist[i],reclist[i])
            pygame.display.flip()
            
        
        alive()
        pygame.display.flip()
        
        fitness=menu(prop)
        if fitness == False:
            C=oldgen
        else:
            oldgen=C
            C = crossover_all(C, fitness, 0.9)
            C = mutation_all(C, 0.1, 0.1)
        
        

    for i in range(4):
        if os.path.exists("frac"+str(i)+".png"):
            os.remove("frac"+str(i)+".png")
    
    

