from estadistica.distribuciones.discretas.poisson import Poisson
from redondeo.redondeo import redondear
from sympy import Symbol
from sympy import Eq

x = Symbol("x", real=True)

print("5.53")
poisson = Poisson(x, 5)
print("a) P(X > 5) =", redondear(poisson.prob(x > 5).evalf(), 4))
print("b) P(X = 0) =", redondear(poisson.prob(Eq(x, 0)).evalf(), 4))
