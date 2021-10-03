desde sympy importar Piecewise como Trozos
desde sympy importar binomial como nC
desde sympy importar Eq como Ec
desde sympy importar FiniteSet como Con
desde sympy.abc importar x, y, w
desde sympy.functions importar exp, factorial
desde fractions importar Fraction como Frac
desde redondeo.redondeo importar redondear
desde estadistica.distribuciones importar continua como cont
desde estadistica.distribuciones importar discreta como disc

escribir("3.5")
f = Trozos((x**2 + 4, (x>=0) & (x<=3)))
c = 1/disc.prob_total(f)
escribir("a) c =", c)
f = Trozos((nC(2,x)*nC(3,3-x), Con(0,1,2).pert(x)))
c = 1/disc.prob_total(f)
escribir("b) c =", c)

escribir("")
escribir("3.7")
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0, otroCaso))
cont.establecer_fdp(f)
prob = redondear(cont.prob(x <= 1.2), 2)
escribir("a) P(X < 1.2) =", prob)
prob = redondear(cont.prob( (0.5 < x) & (x < 1) ), 3)
escribir("b) P(0.5 < X < 1) =", prob)

escribir("")
escribir("3.9")
f = Trozos((Frac(2,5)*(x+2), (0<x) & (x<1)), 
           (0, otroCaso))
cont.establecer_fdp(f)
prob = cont.prob_total(f)
escribir("a) Área bajo curva =", prob)
a = Frac(1,4)
b = Frac(1,2)
prob = cont.prob( (a < x) & (x < b) )
escribir("b) P(1/4 < X < 1/2) =", prob)

escribir("")
escribir("3.11")
f = Trozos(((nC(2,x)*nC(5,3-x))/nC(7,3), (x>=0) & (x<=2)))
disc.establecer_dp(f)
escribir("Distribucion:", disc.dp_a_dist())

escribir("")
escribir("3.13")
dist = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
f = disc.dist_a_dp(dist, x)
disc.establecer_dp(f)
escribir("F(x)=", disc.prob_acum())

escribir("")
escribir("3.15")
f = Trozos(((nC(2,x)*nC(5,3-x))/nC(7,3), (x>=0) & (x<=2)))
disc.establecer_dp(f)
F = disc.prob_acum()
escribir("F(x)=", F)
escribir("-- P(X = 1) = f(1)")
escribir("-- F(1) = f(1) + f(0)")
escribir("-- F(0) = f(0)")
Fb = F.subs(x,1)
Fa = F.subs(x,0)
escribir("a) P(X = 1) =", Fb-Fa)
escribir("-- P(0 < X <= 2) = f(2) + f(1)")
escribir("-- F(2) = f(2) + f(1) + f(0)")
escribir("-- F(0) = f(0)")
Fb = F.subs(x,2)
Fa = F.subs(x,0)
escribir("b) P(0 < X <= 2) =", Fb-Fa)

escribir("")
escribir("3.17")
f = Trozos((Frac(1,2), (1<x) & (x<3)), 
           (0, otroCaso))
cont.establecer_fdp(f)
prob = cont.prob_total(f)
escribir("a) Área bajo curva =", prob)
a = 2
b = Frac('2.5')
prob = cont.prob( (a < x) & (x < b) )
escribir("b) P(2 < X < 2.5) =", prob)
prob = redondear(cont.prob(x <= 1.6), 1)
escribir("c) P(X <= 1.6) =", prob)

escribir("")
escribir("3.19")
f = Trozos((Frac(1,2), (1<x) & (x<3)), 
           (0, otroCaso))
cont.establecer_fdp(f)
F = cont.prob_acum()
escribir("F(x) =", F)
Fb = F.subs(x, Frac('2.5'))
Fa = F.subs(x, 2)
escribir("P(2 < X < 2.5) =", Fb-Fa)

escribir("")
escribir("3.21")
f = Trozos((x**Frac(1,2), (0<x) & (x<1)), 
           (0, otroCaso))
k = 1/cont.prob_total(f)
escribir("a) k =", k)
escribir("b)")
cont.establecer_fdp(k*f)
F = cont.prob_acum()
escribir("F(x) =", F)
Fb = F.subs(x, 0.6)
Fa = F.subs(x, 0.3)
escribir("P(0.3 < X < 0.6) =", redondear(Fb-Fa, 4))

escribir("")
escribir("3.23") 
dist = {-3:Frac(1,27),
        -1:Frac(6,27),
         1:Frac(12,27),
         3:Frac(8,27)}
f = disc.dist_a_dp(dist, w)
disc.establecer_dp(f)
F = disc.prob_acum()
escribir("F(w)=", F)
escribir("a) P(W > 0) =", 1-F.subs(w,0))
escribir("-- P(-1 <= W < 3) = f(-1) + f(1)")
escribir("-- F(1) = f(1) + f(-1) + f(-3)")
escribir("-- F(-3) = f(-3)")
Fb = F.subs(w,1)
Fa = F.subs(w,-3)
escribir("b) P(-1 <= W < 3) =", Fb-Fa)

escribir("")
escribir("3.27")
f = Trozos((Frac(1,2000)*exp(-x/2000), (x>=0)), 
           (0, otroCaso))
cont.establecer_fdp(f)
F = cont.prob_acum()
escribir("a) F(x) =", F)
prob = redondear(1 - F.subs(x,1000).evalf(), 4)
escribir("b) P(X > 1000) =", prob)
prob = redondear(F.subs(x,2000).evalf(), 4)
escribir("c) P(X <= 2000) =", prob)

escribir("")
escribir("3.29")
f = Trozos((3*x**(-4), (x>1)), 
             (0, otroCaso))
prob = cont.prob_total(f)
escribir("a) Área bajo curva =", prob)
cont.establecer_fdp(f)
F = cont.prob_acum()
escribir("b) F(x) =", F)
P = redondear(1 - F.subs(x,4).evalf(), 4)
escribir("c) P(X > 4) =", P)

escribir("")
escribir("3.31")
f = Trozos((0.25*exp(-y/4), (y>=0)), 
           (0, otroCaso))
cont.establecer_fdp(f)
prob = redondear(cont.prob(y > 6).evalf(),4)
escribir("a) P(Y > 6) =", prob)
prob = redondear(cont.prob((0 < y) & (y < 1)).evalf(),4)
escribir("b) P(0 < Y < 1) =", prob)

escribir("")
escribir("3.33")
f = Trozos(((y**4)*(1-y)**3, (0<=y) & (y<=1)), 
           (0, otroCaso))
k = 1/cont.prob_total(f)
escribir("a) k =", k)
cont.establecer_fdp(k*f)
prob = redondear(cont.prob((0 < y) & (y < 0.5)),4)
escribir("b) P(0 < Y < 0.5) =", prob)
prob = redondear(cont.prob((0.8 < y) & (y < 1)),4)
escribir("c) P(0.8 < Y < 1) =", prob)

escribir("")
escribir("3.35")
f = Trozos((exp(-6)*(6**x)/factorial(x), x>=0))
disc.establecer_dp(f)
prob = redondear(1 - disc.prob(x<=8).evalf(), 4)
escribir("a) P(X > 8) =", prob)
prob = redondear(disc.prob(Ec(x,2)).evalf(), 4)
escribir("b) P(X = 2) =", prob)