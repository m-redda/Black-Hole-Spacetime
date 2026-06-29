import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


r, r_s, L, E0 = sp.symbols('r r_s L E0')

f = lambda r_s: 1 - r_s/r

def V_eff(**values):
    d = -1        # massive particles
    # d = 0       # massless particles

    V = f(r_s) * (L**2/r**2 - d) - E0**2
    return sp.simplify(V.subs(values))



def plot_Veff(r_min, r_max, n = 500, **values):
    
    
    V = V_eff(**values)
    
    V_num = sp.lambdify(r, V, "numpy")
    
    r_vals = np.linspace(r_min, r_max, n)
    
    
    
    plt.plot(r_vals, V_num(r_vals))
    plt.xlabel(r"$r$")
    plt.ylabel(r"$V_eff$")
    plt.show()