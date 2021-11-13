from fractions import Fraction as Frac
from typing import Union
from sympy import Piecewise as Trozos
from sympy import Symbol as Simbolo
from sympy.functions import exp
from estadistica.esperanza.esp_disc import EspDisc
from estadistica.esperanza.esp_cont import EspCont
from estadistica.transf import transf
from estadistica.transf import transf_conj
from redondeo.redondeo import redondear

esp_disc = EspDisc()
esp_cont = EspCont()

t = Simbolo("t", real=True)
x = Simbolo("x", real=True)
y = Simbolo("y", real=True)

dist: dict[Union[int, tuple], Union[float, Frac]]

print("")
print("4.33")
dist = {4000: 0.3, -1000: 0.7}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_X = redondear(esp_disc.varianza(x), 0)
print("Var(X) = $", Var_X)

print("")
print("4.35")
dist = {2: 0.01,
        3: 0.25,
        4: 0.4,
        5: 0.3,
        6: 0.04}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_X = redondear(esp_disc.varianza_alter(x), 2)
print("Var(X) = ", Var_X, "errores")

print("")
print("4.37")
f = Trozos((2*(1-x), (x > 0) & (x < 1)),
           (0, True))
esp_cont.est_func_dist(f)
Var_X = esp_cont.varianza(x)
print("Var(X) = $", Var_X, "* 5000")

print("")
print("4.39")
f = Trozos((x, (x > 0) & (x < 1)),
           (2-x, (x >= 1) & (x < 2)),
           (0, True))
esp_cont.est_func_dist(f)
Var_X = esp_cont.varianza(x)
print("Var(X) = ", Var_X, "* 100 horas")

print("")
print("4.41")
dist = {-3: Frac(1, 6),
        6: Frac(1, 2),
        9: Frac(1, 3)}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_g_X = redondear(esp_disc.desviacion((2*x+1)**2), 1)
print("g(X) = (2X+1)^2, desv(g(X)) = ", Var_g_X)

print("")
print("4.43")
f = Trozos((Frac(1, 4)*exp(-x/4), x > 0),
           (0, True))
esp_cont.est_func_dist(f)
E_g_X = esp_cont.esperanza(3*x-2)
Var_g_X = esp_cont.varianza(3*x-2)
print("Y = g(X) = 3X-2")
print("E(Y) = ", E_g_X)
print("Var(Y) = ", Var_g_X)

print("")
print("4.45")
dist = {(1, 1): 0.05, (2, 1): 0.05, (3, 1): 0.10,
        (1, 2): 0.05, (2, 2): 0.10, (3, 2): 0.35,
        (1, 3): 0.00, (2, 3): 0.20, (3, 3): 0.10}
f = transf_conj.dist_a_dp(dist, [x, y])
esp_disc.est_func_dist(f)
Cov = redondear(esp_disc.covarianza(), 3)
print("Cov(X,Y) =", Cov)

print("")
print("4.47")
f = Trozos((Frac(2, 3)*(x+2*y), (x >= 0) & (x <= 1) &
                                (y >= 0) & (y <= 1)),
           (0, True))
esp_cont.est_func_dist(f)
Cov = redondear(esp_cont.covarianza().evalf(), 4)
print("Cov(X,Y) =", Cov)

print("")
print("4.49")
dist = {0: 0.41,
        1: 0.37,
        2: 0.16,
        3: 0.05,
        4: 0.01}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_X = redondear(esp_disc.varianza(x), 4)
desv_X = redondear(esp_disc.desviacion(x), 4)
print("Var(X) =", Var_X)
print("desv(X) =", desv_X)
