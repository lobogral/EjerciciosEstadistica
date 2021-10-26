from fractions import Fraction as Frac
from typing import Union
from sympy import Piecewise as Trozos
from sympy import Symbol as Simbolo
from sympy import binomial as nC
from sympy import FiniteSet as Con
from sympy import simplify
from sympy import pi
from sympy.functions import exp
from estadistica.esperanza.esp_disc import EspDisc
from estadistica.esperanza.esp_cont import EspCont
from estadistica.distribuciones.dist_cont import DistCont
from estadistica.distribuciones import transf
from estadistica.distribuciones import transf_conj
from redondeo.redondeo import redondear

t = Simbolo("t", real=True)
x = Simbolo("x", real=True)
y = Simbolo("y", real=True)

esp_disc = EspDisc()
esp_cont = EspCont()

dist: dict[Union[int, tuple], Union[float, Frac]]

print("4.3")
dist = {20: Frac(1, 5),
        25: Frac(3, 5),
        30: Frac(1, 5)}
f = transf.dist_a_dp(dist, t)
esp_disc.est_func_dist(f)
E_T = esp_disc.esperanza(t)
print("E(T) = ", E_T, "centavos")

print("")
print("4.5")
dist = {0: 0.41,
        1: 0.37,
        2: 0.16,
        3: 0.05,
        4: 0.01}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
E_X = redondear(esp_disc.esperanza(x), 2)
print("E(X) = ", E_X, "imperfecciones")

print("")
print("4.7")
dist = {4000: 0.3, -1000: 0.7}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
E_X = redondear(esp_disc.esperanza(x), 0)
print("E(X) = $", E_X)

print("")
print("4.9")
dist = {3: Frac(8, 52),
        5: Frac(8, 52),
        0: Frac(36, 52)}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
E_X = redondear(esp_disc.esperanza(x).evalf(), 2)
print("E(X) = $", E_X)

print("")
print("4.11")
dist = {200000: 0.002, 100000: 0.01, 50000: 0.1}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
E_X = redondear(esp_disc.esperanza(x), 0) + 500
print("E(X) = $", E_X)

print("")
print("4.13")
f = Trozos((4/(pi*(1+x**2)), (x > 0) & (x < 1)),
           (0, True))
esp_cont.est_func_dist(f)
E_X = esp_cont.esperanza(x)
print("E(X) =", E_X)

print("")
print("4.15")
f = Trozos((x, (x > 0) & (x < 1)),
           (2-x, (x >= 1) & (x < 2)),
           (0, True))
esp_cont.est_func_dist(f)
E_X = esp_cont.esperanza(x)*100
print("E(X) =", E_X, "horas")

print("")
print("4.17")
dist = {-3: Frac(1, 6),
        6: Frac(1, 2),
        9: Frac(1, 3)}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
E_g_X = redondear(esp_disc.esperanza((2*x+1)**2).evalf(), 0)
print("g(X) = (2X+1)^2, E(g(X)) =", E_g_X)

print("")
print("4.19")
dist = {0: Frac(1, 10),
        1: Frac(3, 10),
        2: Frac(2, 5),
        3: Frac(1, 5)}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
E_g_X = redondear(esp_disc.esperanza(1200*x-50*x**2).evalf(), 0)
print("g(X) = 1200X - 50X^2, E(g(X)) = $", E_g_X)

print("")
print("4.21")
f = Trozos((2*(1-x), (x > 0) & (x < 1)),
           (0, True))
esp_cont.est_func_dist(f)
E_g_X = redondear(esp_cont.esperanza(x**2).evalf()*5000, 2)
print("g(X) = X^2, E(g(X)) = $", E_g_X)

print("")
print("4.23")
dist = {(2, 1): 0.10, (4, 1): 0.15,
        (2, 3): 0.20, (4, 3): 0.30,
        (2, 5): 0.10, (4, 5): 0.15}
f = transf_conj.dist_a_dp(dist, [x, y])
esp_disc.est_func_dist(f)
E_g_XY = redondear(esp_disc.esperanza(x*y**2).evalf(), 1)
print("a) g(X,Y) = XY^2, E(g(X,Y)) =", E_g_XY)
E_X = redondear(esp_disc.esperanza(x).evalf(), 2)
print("b) E(X) =", E_X)
E_Y = redondear(esp_disc.esperanza(y).evalf(), 2)
print("c) E(Y) =", E_Y)

print("")
print("4.25")
f = Trozos(((nC(4, x)*nC(4, y)*nC(4, 3-x-y))/nC(12, 3),
           Con(0, 1, 2, 3).as_relational(x)
           & Con(0, 1, 2, 3).as_relational(y)))
esp_disc.est_func_dist(f)
E_g_XY = esp_disc.esperanza(x+y)
print("g(X,Y) = X+Y, E(g(X,Y)) =", E_g_XY, "para jacks y reyes")

print("")
print("4.27")
f = Trozos((Frac(1, 2000)*exp(-x/2000), (x >= 0)),
           (0, True))
esp_cont.est_func_dist(f)
E_X = esp_cont.esperanza(x)
print("E(X) =", E_X, "horas")

print("")
print("4.29")
f = Trozos((3*x**(-4), (x > 1)),
           (0, True))
esp_cont.est_func_dist(f)
E_X = esp_cont.esperanza(x)
print("E(X) =", E_X)

print("")
print("4.31")
f = Trozos((5*(1-y)**4, (y >= 0) & (y <= 1)),
           (0, True))
esp_cont.est_func_dist(f)
E_Y = esp_cont.esperanza(y)
print("a) E(Y) =", E_Y)
dist_cont = DistCont()
dist_cont.est_func_dist(f)
prob = simplify(dist_cont.prob(y > E_Y))
print("a) P(Y > E) =", prob, "= (5/6)^5")
