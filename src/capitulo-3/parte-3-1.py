desde sympy importar Piecewise como Trozos
desde sympy importar binomial como nC
desde sympy importar Eq como Ec
desde sympy importar FiniteSet como Con
desde sympy.abc importar x, y, w
desde sympy.functions importar exp, factorial
desde fractions importar Fraction como Fracción
desde redondeo importar redondear
desde distribuciones importar continua como cont
desde distribuciones importar discreta como disc

escribir("3.5")
f = Trozos((x**2 + 4, (x>=0) & (x<=3)))
c = 1/disc.ProbTotal(f)
escribir("a) c =", c)
f = Trozos((nC(2,x)*nC(3,3-x), Con(0,1,2).pert(x)))
c = 1/disc.ProbTotal(f)
escribir("b) c =", c)

escribir("")
escribir("3.7")
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0, otroCaso))
cont.establecerFdp(f)
prob = redondear(cont.Prob(x <= 1.2), 2)
escribir("a) P(X < 1.2) =", prob)
prob = redondear(cont.Prob( (0.5 < x) & (x < 1) ), 3)
escribir("b) P(0.5 < X < 1) =", prob)

escribir("")
escribir("3.9")
f = Trozos((Fracción(2,5)*(x+2), (0<x) & (x<1)), 
           (0, otroCaso))
cont.establecerFdp(f)
prob = cont.ProbTotal(f)
escribir("a) Área bajo curva =", prob)
a = Fracción(1,4)
b = Fracción(1,2)
prob = cont.Prob( (a < x) & (x < b) )
escribir("b) P(1/4 < X < 1/2) =", prob)

escribir("")
escribir("3.11")
f = Trozos(((nC(2,x)*nC(5,3-x))/nC(7,3), (x>=0) & (x<=2)))
disc.establecerDp(f)
escribir("Distribucion:", disc.dp2Dist())

escribir("")
escribir("3.13")
dist = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
f = disc.dist2Dp(dist, x)
disc.establecerDp(f)
escribir("F(x)=", disc.ProbAcum())

escribir("")
escribir("3.15")
f = Trozos(((nC(2,x)*nC(5,3-x))/nC(7,3), (x>=0) & (x<=2)))
disc.establecerDp(f)
F = disc.ProbAcum()
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
f = Trozos((Fracción(1,2), (1<x) & (x<3)), 
           (0, otroCaso))
cont.establecerFdp(f)
prob = cont.ProbTotal(f)
escribir("a) Área bajo curva =", prob)
a = 2
b = Fracción('2.5')
prob = cont.Prob( (a < x) & (x < b) )
escribir("b) P(2 < X < 2.5) =", prob)
prob = redondear(cont.Prob(x <= 1.6), 1)
escribir("c) P(X <= 1.6) =", prob)

escribir("")
escribir("3.19")
f = Trozos((Fracción(1,2), (1<x) & (x<3)), 
           (0, otroCaso))
cont.establecerFdp(f)
F = cont.ProbAcum()
escribir("F(x) =", F)
Fb = F.subs(x, Fracción('2.5'))
Fa = F.subs(x, 2)
escribir("P(2 < X < 2.5) =", Fb-Fa)

escribir("")
escribir("3.21")
f = Trozos((x**Fracción(1,2), (0<x) & (x<1)), 
           (0, otroCaso))
k = 1/cont.ProbTotal(f)
escribir("a) k =", k)
escribir("b)")
cont.establecerFdp(k*f)
F = cont.ProbAcum()
escribir("F(x) =", F)
Fb = F.subs(x, 0.6)
Fa = F.subs(x, 0.3)
escribir("P(0.3 < X < 0.6) =", redondear(Fb-Fa, 4))

escribir("")
escribir("3.23") 
dist = {-3:Fracción(1,27),
        -1:Fracción(6,27),
         1:Fracción(12,27),
         3:Fracción(8,27)}
f = disc.dist2Dp(dist, w)
disc.establecerDp(f)
F = disc.ProbAcum()
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
f = Trozos((Fracción(1,2000)*exp(-x/2000), (x>=0)), 
           (0, otroCaso))
cont.establecerFdp(f)
F = cont.ProbAcum()
escribir("a) F(x) =", F)
prob = redondear(1 - F.subs(x,1000).evalf(), 4)
escribir("b) P(X > 1000) =", prob)
prob = redondear(F.subs(x,2000).evalf(), 4)
escribir("c) P(X <= 2000) =", prob)

escribir("")
escribir("3.29")
f = Trozos((3*x**(-4), (x>1)), 
             (0, otroCaso))
prob = cont.ProbTotal(f)
escribir("a) Área bajo curva =", prob)
cont.establecerFdp(f)
F = cont.ProbAcum()
escribir("b) F(x) =", F)
P = redondear(1 - F.subs(x,4).evalf(), 4)
escribir("c) P(X > 4) =", P)

escribir("")
escribir("3.31")
f = Trozos((0.25*exp(-y/4), (y>=0)), 
           (0, otroCaso))
cont.establecerFdp(f)
prob = redondear(cont.Prob(y > 6).evalf(),4)
escribir("a) P(Y > 6) =", prob)
prob = redondear(cont.Prob((0 < y) & (y < 1)).evalf(),4)
escribir("b) P(0 < Y < 1) =", prob)

escribir("")
escribir("3.33")
f = Trozos(((y**4)*(1-y)**3, (0<=y) & (y<=1)), 
           (0, otroCaso))
k = 1/cont.ProbTotal(f)
escribir("a) k =", k)
cont.establecerFdp(k*f)
prob = redondear(cont.Prob((0 < y) & (y < 0.5)),4)
escribir("b) P(0 < Y < 0.5) =", prob)
prob = redondear(cont.Prob((0.8 < y) & (y < 1)),4)
escribir("c) P(0.8 < Y < 1) =", prob)

escribir("")
escribir("3.35")
f = Trozos((exp(-6)*(6**x)/factorial(x), x>=0))
disc.establecerDp(f)
prob = redondear(1 - disc.Prob(x<=8).evalf(), 4)
escribir("a) P(X > 8) =", prob)
prob = redondear(disc.Prob(Ec(x,2)).evalf(), 4)
escribir("b) P(X = 2) =", prob)