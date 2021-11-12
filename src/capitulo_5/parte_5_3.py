from estadistica.distribuciones.discretas.bin_neg import BinNeg
from estadistica.distribuciones.discretas.poisson import Poisson
from estadistica.distribuciones.discretas.geometrica import Geometrica
from redondeo.redondeo import redondear
from sympy import Symbol
from sympy import Eq

x = Symbol("x", real=True)

print("5.51")
bin_neg = BinNeg(x, 0.3, 5)
print("P(X = 10) =", redondear(bin_neg.prob(Eq(x, 10)).evalf(), 4))

print("")
print("5.53")
poisson = Poisson(x, 5)
print("a) P(X > 5) =", redondear(poisson.prob(x > 5).evalf(), 4))
print("b) P(X = 0) =", redondear(poisson.prob(Eq(x, 0)).evalf(), 4))

print("")
print("5.57")
geometrica = Geometrica(x, 0.7)
print("a) P(X = 3) =", redondear(geometrica.prob(Eq(x, 3)).evalf(), 4))
print("b) P(X < 4) =", redondear(geometrica.prob(x < 4).evalf(), 4))
