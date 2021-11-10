from estadistica.distribuciones.discretas.hipergeom import Hipergeom
from estadistica.distribuciones.discretas.binomial import Binomial
from estadistica.esperanza.esp import Esp
from redondeo.redondeo import redondear
from sympy import Symbol
from sympy import Eq

x = Symbol("x", real=True)

print("5.29")
hipergeom = Hipergeom(x, 52, 7, 12)
print("a) P(X = 2) =", redondear(hipergeom.prob(Eq(x, 2)).evalf(), 4))
hipergeom = Hipergeom(x, 52, 7, 4)
print("b) P(X >= 1) =", redondear(hipergeom.prob(x >= 1).evalf(), 4))

print("")
print("5.31")
hipergeom = Hipergeom(x, 9, 6, 4)
print("P(X = 2) =", hipergeom.prob(Eq(x, 2)))

print("")
print("5.33")
hipergeom = Hipergeom(x, 6, 3, 4)
print("a) f =", hipergeom.ret_dist().func_dist)
print("b) P(2 <= X <= 3) =", hipergeom.prob((x >= 2) & (x <= 3)))

print("")
print("5.35")
hipergeom = Hipergeom(x, 50, 5, 10)
print("P(X <= 2) =", redondear(hipergeom.prob(x <= 2).evalf(), 4))

print("")
print("5.39")
hipergeom = Hipergeom(x, 52, 13, 13)
esp = Esp(hipergeom.ret_dist())
print("E(X) =", redondear(esp.esperanza(x).evalf(), 2))

print("")
print("5.41")
hipergeom = Binomial(x, 0.5, 10)
print("P(X <= 3) =", redondear(hipergeom.prob(x >= 3).evalf(), 4))

print("")
print("5.43")
hipergeom = Binomial(x, 0.7, 18)
prob = redondear(hipergeom.prob((x > 9) & (x < 14)).evalf(), 4)
print("P(9 < X < 14) =", prob)

print("")
print("5.47")
hipergeom = Hipergeom(x, 25, 15, 10)
print("P(X <= 5) =", redondear(hipergeom.prob(Eq(x, 5)).evalf(), 4))

print("")
print("5.49")
hipergeom = Hipergeom(x, 20, 5, 3)
print("a) P(X = 0) =", redondear(hipergeom.prob(Eq(x, 0)).evalf(), 4))
print("b) P(X = 2) =", redondear(hipergeom.prob(Eq(x, 2)).evalf(), 4))
