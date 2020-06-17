if __name__ == '__main__':
    import time
    import matplotlib
    from matplotlib import colors
    import matplotlib.pyplot as plt

    from julia import *
	
    xmin, xmax, xn = -1.25, +1.25, 3000/2
    ymin, ymax, yn = -1.25, +1.25, 2500/2

    maxiter = 100
    horizon = 2.0 ** 40
    log_horizon = np.log(np.log(horizon))/np.log(2)

    # C = [[0.285, 0.01]]*100

    # C = [[0.285,0.013]]*100

    # C = [[0,-1]]*100

    # C = [[0.3,0.5]]*100

    C = [[0.285, 0.01],[0.285,0.013],[0,-1],[0.3,0.5]]*25

    Z, N = julia_set(xmin, xmax, ymin, ymax, xn, yn, C, maxiter, horizon)

    # Normalized recount as explained in:
    # https://linas.org/art-gallery/escape/smooth.html
    # https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift

    #  This line will generate warnings for null values but it is faster to
    # process them afterwards using the nan_to_num
    with np.errstate(invalid='ignore'):
        M = np.nan_to_num(N + 1 -
                          np.log(np.log(abs(Z)))/np.log(2) +
                          log_horizon)

    dpi = 72
    width = 10
    height = 10*yn/xn
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

    # Shaded rendering
    light = colors.LightSource(azdeg=130, altdeg=100)
    M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5, norm=colors.PowerNorm(0.3), blend_mode='hsv')
    # M = light.shade(M, cmap=plt.cm.coolwarm) # or cmap=plt.cm.coolwarm
    # see https://matplotlib.org/examples/color/colormaps_reference.html
    plt.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
    ax.set_xticks([])
    ax.set_yticks([])
# faire tourner source azdeg et altdef
    plt.show()

