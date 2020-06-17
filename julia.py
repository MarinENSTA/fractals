"""
===================================
Shaded & power normalized rendering
===================================

The Mandelbrot set rendering can be improved by using a normalized recount
associated with a power normalized colormap (gamma=0.3). Rendering can be
further enhanced thanks to shading.

The `maxiter` gives the precision of the computation. `maxiter=200` should
take a few seconds on most modern laptops.
"""
import numpy as np

'''
julia_set(xmin, xmax, ymin, ymax, xn, yn, cx, cy, maxiter, horizon=2.0):

reprend les caractères donnés initialement mais prend une liste C au lieu de cx et cy
renvoie l'ensemble de julia avec l'ensemble C

'''
def julia_set(xmin, xmax, ymin, ymax, xn, yn, C_list, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    Z = X + Y[:, None] * 1j
    N = np.zeros_like(Z, dtype=int)
    
    for n in range(maxiter):
        I = np.less(abs(Z), horizon)
        N[I] = n
        C = complex(C_list[n][0], C_list[n][1])
        Z[I] = Z[I]**2 + C
    N[N == maxiter-1] = 0

    return Z, N