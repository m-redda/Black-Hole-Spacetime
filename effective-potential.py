
import sympy as sp
import matplotlib.pyplot as plt


r, r_s = sp.symbols('r r_s', positive=True)
L, E0 = sp.symbols('L E0', real=True)
d = sp.symbols('d')

def V_eff(**values):
    
    """masless particles"""
    #d = 0 
    """massive particles"""
    d = -1 

    V = (1 - r_s/r) * (L**2/r**2 - d) - E0**2
    

    return sp.simplify(V.subs(values))


