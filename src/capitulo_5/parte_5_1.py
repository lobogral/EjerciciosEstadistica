from estadistica.distribuciones.discretas.uniforme import Uniforme
from estadistica.distribuciones.discretas.binomial import Binomial
from estadistica.esperanza.esp import Esp
from redondeo.redondeo import redondear
from sympy import Symbol
from sympy import Eq

x = Symbol("x", real=True)

print("5.1")
uniforme = Uniforme(10, (x >= 1) & (x <= 10))
print("P(X < 4) =", uniforme.prob(x < 4))

print("")
print("5.3")
esp = Esp(uniforme.ret_dist())
print("E(X) =", redondear(esp.esperanza(x).evalf(), 1))
print("Var(X) =", redondear(esp.varianza(x).evalf(), 2))

print("")
print("5.5")
binomial = Binomial(x, 0.3, 20)
print("a) P(X >= 10) =", redondear(binomial.prob(x >= 10), 4))
print("b) P(X <= 4) =", redondear(binomial.prob(x <= 4), 4))
print("c) P(X = 5 | p = 0.3) =", redondear(binomial.prob(Eq(x, 5)), 4))
print("p = 0.3 es razonable, la probabilidad es baja")

print("")
print("5.7")
binomial = Binomial(x, 0.7, 10)
print("a) P(X < 5) =", redondear(binomial.prob(x < 5), 4))
binomial = Binomial(x, 0.7, 20)
print("b) P(X < 10) =", redondear(binomial.prob(x < 10), 4))

print("")
print("5.9")
binomial = Binomial(x, 0.25, 15)
print("a) P(3 <= X <= 6) =", redondear(binomial.prob((x >= 3) & (x <= 6)), 4))
print("b) P(X < 4) =", redondear(binomial.prob(x < 4), 4))
print("c) P(X > 5) =", redondear(binomial.prob(x > 5), 4))

print("")
print("5.11")
binomial = Binomial(x, 0.9, 7)
print("P(X = 5) =", redondear(binomial.prob(Eq(x, 5)), 4))

print("")
print("5.13")
binomial = Binomial(x, 0.7, 5)
print("P(X >= 3) =", redondear(binomial.prob(x >= 3), 4))

print("")
print("5.15")
binomial = Binomial(x, 0.4, 5)
print("a) P(X = 0) =", redondear(binomial.prob(Eq(x, 0)), 4))
print("b) P(X < 2) =", redondear(binomial.prob(x < 2), 4))
print("c) P(X > 3) =", redondear(binomial.prob(x > 3), 4))

print("")
print("5.25")
binomial = Binomial(x, 0.1, 20)
print("P(X <= 3) =", redondear(binomial.prob(x <= 3), 4))

print("")
print("5.27")
binomial = Binomial(x, 0.9, 20)
print("a) P(X = 18) =", redondear(binomial.prob(Eq(x, 18)), 4))
print("b) P(X >= 15) =", redondear(binomial.prob(x >= 15), 4))
binomial = Binomial(x, 0.1, 20)
print("c) P(X >= 2) =", redondear(binomial.prob(x >= 2), 4))
