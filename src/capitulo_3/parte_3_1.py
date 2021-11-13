from fractions import Fraction as Frac
from typing import Union
from sympy import Piecewise as Trozos
from sympy import binomial as nC
from sympy import Eq as Ec
from sympy import FiniteSet as Con
from sympy import Symbol
from sympy.functions import exp
from sympy.functions import factorial
from redondeo.redondeo import redondear
from estadistica.distribuciones.dist_cont import DistCont
from estadistica.distribuciones.dist_disc import DistDisc
from estadistica.transf.transf import dp_a_dist
from estadistica.transf.transf import dist_a_dp

x = Symbol("x", real=True)
y = Symbol("y", real=True)
w = Symbol("w", real=True)

dist_cont = DistCont()
dist_disc = DistDisc()

dist: dict[int, Union[float, Frac]]

print("3.5")
f = Trozos((x**2 + 4, (x >= 0) & (x <= 3)))
c = 1/dist_disc.prob_total(f)
print("a) c =", c)
f = Trozos((nC(2, x)*nC(3, 3-x), Con(0, 1, 2).as_relational(x)))
c = 1/dist_disc.prob_total(f)
print("b) c =", c)

print("")
print("3.7")
f = Trozos((x, (x > 0) & (x < 1)),
           (2-x, (x >= 1) & (x < 2)),
           (0, True))
dist_cont.est_func_dist(f)
prob = redondear(dist_cont.prob(x <= 1.2), 2)
print("a) P(X < 1.2) =", prob)
prob = redondear(dist_cont.prob((x > 0.5) & (x < 1)), 3)
print("b) P(0.5 < X < 1) =", prob)

print("")
print("3.9")
f = Trozos((Frac(2, 5)*(x+2), (x > 0) & (x < 1)),
           (0, True))
dist_cont.est_func_dist(f)
prob = dist_cont.prob_total(f)
print("a) Área bajo curva =", prob)
a = Frac(1, 4)
b = Frac(1, 2)
prob = dist_cont.prob((a < x) & (x < b))
print("b) P(1/4 < X < 1/2) =", prob)

print("")
print("3.11")
f = Trozos(((nC(2, x)*nC(5, 3-x))/nC(7, 3), (x >= 0) & (x <= 2)))
dist_disc.est_func_dist(f)
print("Distribucion:", dp_a_dist(f))

print("")
print("3.13")
dist = {0: 0.41,
        1: 0.37,
        2: 0.16,
        3: 0.05,
        4: 0.01}
f = dist_a_dp(dist, x)
dist_disc.est_func_dist(f)
print("F(x)=", dist_disc.prob_acum())

print("")
print("3.15")
f = Trozos(((nC(2, x)*nC(5, 3-x))/nC(7, 3), (x >= 0) & (x <= 2)))
dist_disc.est_func_dist(f)
F = dist_disc.prob_acum()
print("F(x)=", F)
print("-- P(X = 1) = f(1)")
print("-- F(1) = f(1) + f(0)")
print("-- F(0) = f(0)")
Fb = F.subs(x, 1)
Fa = F.subs(x, 0)
print("a) P(X = 1) =", Fb-Fa)
print("-- P(0 < X <= 2) = f(2) + f(1)")
print("-- F(2) = f(2) + f(1) + f(0)")
print("-- F(0) = f(0)")
Fb = F.subs(x, 2)
Fa = F.subs(x, 0)
print("b) P(0 < X <= 2) =", Fb-Fa)

print("")
print("3.17")
f = Trozos((Frac(1, 2), (x > 1) & (x < 3)),
           (0, True))
dist_cont.est_func_dist(f)
prob = dist_cont.prob_total(f)
print("a) Área bajo curva =", prob)
a = Frac('2')
b = Frac('2.5')
prob = dist_cont.prob((a < x) & (x < b))
print("b) P(2 < X < 2.5) =", prob)
prob = redondear(dist_cont.prob(x <= 1.6), 1)
print("c) P(X <= 1.6) =", prob)

print("")
print("3.19")
f = Trozos((Frac(1, 2), (x > 1) & (x < 3)),
           (0, True))
dist_cont.est_func_dist(f)
F = dist_cont.prob_acum()
print("F(x) =", F)
Fb = F.subs(x, Frac('2.5'))
Fa = F.subs(x, 2)
print("P(2 < X < 2.5) =", Fb-Fa)

print("")
print("3.21")
f = Trozos((x**Frac(1, 2), (x > 0) & (x < 1)),
           (0, True))
k = 1/dist_cont.prob_total(f)
print("a) k =", k)
print("b)")
dist_cont.est_func_dist(k*f)
F = dist_cont.prob_acum()
print("F(x) =", F)
Fb = F.subs(x, 0.6)
Fa = F.subs(x, 0.3)
print("P(0.3 < X < 0.6) =", redondear(Fb-Fa, 4))

print("")
print("3.23")
dist = {-3: Frac(1, 27),
        -1: Frac(6, 27),
        1: Frac(12, 27),
        3: Frac(8, 27)}
f = dist_a_dp(dist, w)
dist_disc.est_func_dist(f)
F = dist_disc.prob_acum()
print("F(w)=", F)
print("a) P(W > 0) =", 1-F.subs(w, 0))
print("-- P(-1 <= W < 3) = f(-1) + f(1)")
print("-- F(1) = f(1) + f(-1) + f(-3)")
print("-- F(-3) = f(-3)")
Fb = F.subs(w, 1)
Fa = F.subs(w, -3)
print("b) P(-1 <= W < 3) =", Fb-Fa)

print("")
print("3.27")
f = Trozos((Frac(1, 2000)*exp(-x/2000), (x >= 0)),
           (0, True))
dist_cont.est_func_dist(f)
F = dist_cont.prob_acum()
print("a) F(x) =", F)
prob = redondear(1 - F.subs(x, 1000).evalf(), 4)
print("b) P(X > 1000) =", prob)
prob = redondear(F.subs(x, 2000).evalf(), 4)
print("c) P(X <= 2000) =", prob)

print("")
print("3.29")
f = Trozos((3*x**(-4), (x > 1)),
           (0, True))
prob = dist_cont.prob_total(f)
print("a) Área bajo curva =", prob)
dist_cont.est_func_dist(f)
F = dist_cont.prob_acum()
print("b) F(x) =", F)
P = redondear(1 - F.subs(x, 4).evalf(), 4)
print("c) P(X > 4) =", P)

print("")
print("3.31")
f = Trozos((0.25*exp(-y/4), (y >= 0)),
           (0, True))
dist_cont.est_func_dist(f)
prob = redondear(dist_cont.prob(y > 6).evalf(), 4)
print("a) P(Y > 6) =", prob)
prob = redondear(dist_cont.prob((y > 0) & (y < 1)).evalf(), 4)
print("b) P(0 < Y < 1) =", prob)

print("")
print("3.33")
f = Trozos(((y**4)*(1-y)**3, (y >= 0) & (y <= 1)),
           (0, True))
k = 1/dist_cont.prob_total(f)
print("a) k =", k)
dist_cont.est_func_dist(k*f)
prob = redondear(dist_cont.prob((y > 0) & (y < 0.5)), 4)
print("b) P(0 < Y < 0.5) =", prob)
prob = redondear(dist_cont.prob((y > 0.8) & (y < 1)), 4)
print("c) P(0.8 < Y < 1) =", prob)

print("")
print("3.35")
f = Trozos((exp(-6)*(6**x)/factorial(x), x >= 0))
dist_disc.est_func_dist(f)
prob = redondear(1 - dist_disc.prob(x <= 8).evalf(), 4)
print("a) P(X > 8) =", prob)
prob = redondear(dist_disc.prob(Ec(x, 2)).evalf(), 4)
print("b) P(X = 2) =", prob)
