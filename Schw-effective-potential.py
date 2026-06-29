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



def plot_Veff(r_min, r_max, **values):
    V = V_eff(**values)
    r_vals = np.linspace(r_min, r_max)
    plt.plot(r_vals, V(r_vals))
    plt.xlabel(r"$r$")
    plt.ylabel(r"$V_eff$")
    plt.show()