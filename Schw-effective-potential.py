import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


#Define variables as syymbols ( r -> radius, r_s -> Schwarzschild radius, L -> angular momentum, E0 -> energy)
r, r_s, L, E0 = sp.symbols('r r_s L E0')

#Schwarzschild metric function 
f = lambda r_s: 1 - r_s/r


#Effective potential function: values -> values to substitute for the symbolic variables
def V_eff(**values):
    
    #Define the normalization constant, δ  as d 
    d = -1        # massive particles
    # d = 0       # massless particles

    #Effective potential equation
    V = f(r_s) * (L**2/r**2 - d) - E0**2
    
    return sp.simplify(V.subs(values))


#V_eff plot function: r_min/r_max -> lower/upper bound of the radial coordinate, n -> number of points used in the plot (default is 500)
# plot_Veff(0.8, 10, r_s=1, L=10, E0=1) 
def plot_Veff(r_min, r_max, n = 500, **values):
    
    #Obtains previous V_eff
    V = V_eff(**values)
    
    #Converts V_eff into a numericalfunction
    V_num = sp.lambdify(r, V, "numpy")
    
    #Generate equally spaced r values
    r_vals = np.linspace(r_min, r_max, n)
    
    
    #Plot the effective potential
    plt.plot(r_vals, V_num(r_vals))
    plt.xlabel(r"$r$")
    plt.ylabel(r"$V_eff$")
    plt.title("Schwarschild Effective Potential")
    # Parameter box-ChatGPT
    params = "\n".join(
        rf"${symbol} = {value}$"
        for symbol, value in values.items()
    )

    plt.text(
        0.98, 0.98, params,
        transform=plt.gca().transAxes,
        ha="right",
        va="top",
        bbox=dict(facecolor="white", edgecolor="black", alpha=0.8)
    )

    plt.show()