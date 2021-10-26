from fractions import Fraction as Frac
from sympy import binomial as nC
from sympy import Piecewise as Trozos
from sympy import Symbol as Simbolo
from sympy import Eq as Ec
from sympy import FiniteSet as Con
from redondeo.redondeo import redondear
from estadistica.distribuciones.dist_conj_cont import DistConjCont
from estadistica.distribuciones.dist_conj_disc import DistConjDisc
from estadistica.distribuciones.transf_conj import dp_a_dist
from estadistica.distribuciones.transf_conj import dist_a_dp

dist_conj_cont = DistConjCont()
dist_conj_disc = DistConjDisc()

x = Simbolo("x", real=True)
y = Simbolo("y", real=True)
z = Simbolo("z", real=True)

print("3.37")
f = Trozos((x*y,
           Con(1, 2, 3).as_relational(x)
           & ((y >= 1) & (y <= 2)) | Ec(y, 3)))
c = dist_conj_disc.prob_total(f)
print("a) c =", 1/c)
f = Trozos((abs(x - y),
           Con(-2, 0, 2).as_relational(x)
           & Con(-2, 3).as_relational(y)))
c = dist_conj_disc.prob_total(f)
print("b) c =", 1/c)

print("")
print("3.39")
f = Trozos(((nC(3, x)*nC(2, y)*nC(3, 4-x-y))/nC(8, 4),
            Con(0, 1, 2, 3).as_relational(x)
            & Con(0, 1, 2).as_relational(y)))
dist_conj_disc.est_func_dist(f)
print("a) ", dp_a_dist(f, x, y))
prob = dist_conj_disc.prob(x + y <= 2)
print("b) P(X + Y <= 2) =", prob)

print("")
print("3.41")
f = Trozos((24*x*y, (x >= 0) & (x <= 1) &
                    (y >= 0) & (y <= 1) &
                    (x + y <= 1)),
           (0, True))
dist_conj_cont.est_func_dist(f)
intervalo = x + y < Frac(1, 2)
prob = dist_conj_cont.prob(intervalo)
print("a) P(X + Y < 1/2) =", prob)
print("b) g(x) =", dist_conj_cont.prob_marginal(x))
intervalo_dep = y < Frac(1, 8)
eq_dep = Ec(x, Frac(3, 4))
prob = dist_conj_cont.prob_condicional(intervalo_dep, eq_dep)
print("c) P( Y < 1/8 | X = 3/4 ) =", prob)

print("")
print("3.43")
f = Trozos((4*x*y, (x > 0) & (x < 1) &
                   (y > 0) & (y < 1)),
           (0, True))
dist_conj_cont.est_func_dist(f)
intervalo = (x >= 0) & (x <= Frac(1, 2))
intervalo = intervalo & (Frac(1, 4) <= y) & (y <= Frac(1, 2))
prob = dist_conj_cont.prob(intervalo)
print("a) P(0 <= X <= 1/2, 1/4 < Y < 1/2) =", prob)
intervalo = (x < y)
prob = dist_conj_cont.prob(intervalo)
print("b) P(X < Y) =", prob)

print("")
print("3.45")
f = Trozos((1/y, (x > 0) & (x < y) & (y < 1)),
           (0, True))
dist_conj_cont.est_func_dist(f)
intervalo = x + y > 1/2
prob = redondear(dist_conj_cont.prob(intervalo), 4)
print("P(X + Y > 1/2) =", prob)

print("")
print("3.47")
f = Trozos((2, (x > 0) & (x < y) & (y < 1)),
           (0, True))
dist_conj_cont.est_func_dist(f)
print("a)")
print("g(x) =", dist_conj_cont.prob_marginal(x))
print("h(y) =", dist_conj_cont.prob_marginal(y))
print("g(x)h(y) != f(x,y), Dependientes")
intervalo_dep = (Frac(1, 4) < x) & (x < Frac(1, 2))
eq_dep = Ec(y, Frac(3, 4))
prob = dist_conj_cont.prob_condicional(intervalo_dep, eq_dep)
print("b) P( 1/4 < X < 1/2 | Y = 3/4 ) =", prob)

print("")
print("3.49")
dist = {(1, 1): 0.05, (2, 1): 0.05, (3, 1): 0.10,
        (1, 2): 0.05, (2, 2): 0.10, (3, 2): 0.35,
        (1, 3): 0.00, (2, 3): 0.20, (3, 3): 0.10}
f = dist_a_dp(dist, [x, y])
dist_conj_disc.est_func_dist(f)
dist_marginal_X = dist_conj_disc.prob_marginal(x)
print("a) g(x) =", dist_marginal_X)
dist_marginal_Y = dist_conj_disc.prob_marginal(y)
print("b) h(y) =", dist_marginal_Y)
prob = redondear(dist_conj_disc.prob_condicional(Ec(y, 3), Ec(x, 2)), 4)
print("c) P(Y = 3 | X = 2) =", prob)

print("")
print("3.53")
f = Trozos(((nC(4, x)*nC(4, y)*nC(4, 3-x-y))/nC(12, 3),
            Con(0, 1, 2, 3).as_relational(x)
            & Con(0, 1, 2, 3).as_relational(y)))
dist_conj_disc.est_func_dist(f)
print("a)", dp_a_dist(f, x, y))
prob = dist_conj_disc.prob(x + y >= 2)
print("b) P(X + Y <= 2) =", prob)

print("")
print("3.55")
f = Trozos(((6-x-y)/8, (x > 0) & (x < 2) &
                       (y > 2) & (y < 4)),
           (0, True))
dist_conj_cont.est_func_dist(f)
intervalo_dep = (y > 1) & (y < 3)
eq_dep = Ec(x, 1)
prob = dist_conj_cont.prob_condicional(intervalo_dep, eq_dep)
print("P( 1 < Y < 3 | X = 1 ) =", prob)

print("")
print("3.59")
f = Trozos((x*(y**2)*z, (x > 0) & (x < 1) &
                        (y > 0) & (y < 1) &
                        (z > 0) & (z < 2)),
           (0, True))
k = 1/dist_conj_cont.prob_total(f)
print("a) k =", k)
dist_conj_cont.est_func_dist(k*f)
intervalo = (x < Frac(1, 4)) & (y > Frac(1, 2)) & (z > 1) & (z < 2)
prob = dist_conj_cont.prob(intervalo)
print("b) P(X < 1/4, Y > 1/2, 1 < Z < 2) =", prob)
