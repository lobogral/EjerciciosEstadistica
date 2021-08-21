desde sympy importar Piecewise como Trozos
desde sympy importar binomial como C
desde sympy.abc importar x, y
desde sympy.functions importar exp
desde sympy.stats importar ContinuousRV
desde fractions importar Fraction como Fracción
desde redondeo importar redondear
desde distribuciones importar continua como cont
desde distribuciones importar discreta como disc

escribir("3.5")
f = x**2 + 4
distribución = disc.Func2Dist(f, x, [0,1,2,3])
escribir("a) c =", 1/disc.ProbTotal(distribución))
f = C(2,x)*C(3,3-x)
distribución = disc.Func2Dist(f, x, [0,1,2])
escribir("b) c =", 1/disc.ProbTotal(distribución))

escribir("")
escribir("3.7")
fdp = Trozos((x, (0<x) & (x<1)),
             (2-x, (1<=x) & (x<2)), 
             (0, otroCaso))
X = ContinuousRV(x, fdp)
prob = redondear(cont.Prob(X <= 1.2), 2)
escribir("a) P(X < 1.2) =", prob)
prob = redondear(cont.Prob( (0.5 < X) & (X < 1) ), 3)
escribir("b) P(0.5 < X < 1) =", prob)

escribir("")
escribir("3.9")
fdp = Trozos((Fracción(2,5)*(x+2), (0<x) & (x<1)), 
             (0, otroCaso))
X = ContinuousRV(x, fdp)
prob = cont.ProbTotal(fdp)
escribir("a) Área bajo curva =", prob)
a = Fracción(1,4)
b = Fracción(1,2)
prob = cont.Prob( (a < X) & (X < b) )
escribir("b) P(1/4 < X < 1/2) =", prob)

escribir("")
escribir("3.11")
f = (C(2,x)*C(5,3-x))/C(7,3)
escribir("Distribución:", disc.Func2Dist(f, x, [0,1,2]))

escribir("")
escribir("3.13")
distribución = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
escribir("F(x)=", disc.ProbAcum(distribución))

escribir("")
escribir("3.15")
f = (C(2,x)*C(5,3-x))/C(7,3)
distribución = disc.Func2Dist(f, x, [0,1,2])
F = disc.ProbAcum(distribución)
escribir("F(x)=", F)
Fb = F.subs(x,1.9)
Fa = F.subs(x,0.9)
escribir("a) P(X = 1) =", Fb-Fa)
Fb = F.subs(x,2)
Fa = F.subs(x,0.1)
escribir("b) P(0 < X <= 2) =", Fb-Fa)


escribir("")
escribir("3.17")
fdp = Trozos((Fracción(1,2), (1<x) & (x<3)), 
             (0, otroCaso))
X = ContinuousRV(x, fdp)
prob = cont.ProbTotal(fdp)
escribir("a) Área bajo curva =", prob)
a = 2
b = Fracción('2.5')
prob = cont.Prob( (a < X) & (X < b) )
escribir("b) P(2 < X < 2.5) =", prob)
prob = redondear(cont.Prob(X <= 1.6), 1)
escribir("c) P(X <= 1.6) =", prob)

escribir("")
escribir("3.19")
fdp = Trozos((Fracción(1,2), (1<x) & (x<3)), 
             (0, otroCaso))
X = ContinuousRV(x, fdp)
F = cont.ProbAcum(X)
escribir("F(x) =", F)
Fb = F.subs(x, Fracción('2.5'))
Fa = F.subs(x, 2)
escribir("P(2 < X < 2.5) =", Fb-Fa)

escribir("")
escribir("3.21")
fdp = Trozos((x**Fracción(1,2), (0<x) & (x<1)), 
             (0, otroCaso))
k = 1/cont.ProbTotal(fdp)
escribir("a) k =", k)
escribir("b)")
X = ContinuousRV(x, k*fdp)
F = cont.ProbAcum(X)
escribir("F(x) =", F)
Fb = F.subs(x, 0.6)
Fa = F.subs(x, 0.3)
escribir("P(0.3 < X < 0.6) =", redondear(Fb-Fa, 4))

escribir("")
escribir("3.23")
distribución = {-3:Fracción(1,27), 
                -1:Fracción(6,27), 
                 1:Fracción(12,27), 
                 3:Fracción(8,27)}
F = disc.ProbAcum(distribución)
escribir("F(x)=", F)
escribir("a) P(X > 0) =", 1-F.subs(x,0))
Fb = F.subs(x,2.9)
Fa = F.subs(x,-1)
escribir("b) P(-1 <= X < 3) =", Fb-Fa)

escribir("")
escribir("3.27")
fdp = Trozos((Fracción(1,2000)*exp(-x/2000), (x>=0)), 
             (0, otroCaso))
X = ContinuousRV(x, fdp)
F = cont.ProbAcum(X)
escribir("a) F(x) =", F)
prob = redondear(1 - F.subs(x,1000).evalf(), 4)
escribir("b) P(X > 1000) =", prob)
prob = redondear(F.subs(x,2000).evalf(), 4)
escribir("c) P(X <= 2000) =", prob)

escribir("")
escribir("3.29")
fdp = Trozos((3*x**(-4), (x>1)), 
             (0, otroCaso))
prob = cont.ProbTotal(fdp)
escribir("a) Área bajo curva =", prob)
X = ContinuousRV(x, fdp)
F = cont.ProbAcum(X)
escribir("b) F(x) =", F)
P = redondear(1 - F.subs(x,4).evalf(), 4)
escribir("c) P(X > 4) =", P)

escribir("")
escribir("3.31")
fdp = Trozos((0.25*exp(-y/4), (y>=0)), 
             (0, otroCaso))
Y = ContinuousRV(y, fdp)
prob = redondear(cont.Prob(Y > 6).evalf(),4)
escribir("a) P(Y > 6) =", prob)
prob = redondear(cont.Prob((0 < Y) & (Y < 1)).evalf(),4)
escribir("b) P(0 < Y < 1) =", prob)

escribir("")
escribir("3.33")
fdp = Trozos(((y**4)*(1-y)**3, (0<=y) & (y<=1)), 
             (0, otroCaso))
k = 1/cont.ProbTotal(fdp)
escribir("a) k =", k)
Y = ContinuousRV(y, k*fdp)
prob = redondear(cont.Prob((0 < Y) & (Y < 0.5)),4)
escribir("b) P(0 < Y < 0.5) =", prob)
prob = redondear(cont.Prob((0.8 < Y) & (Y < 1)),4)
escribir("c) P(0.8 < Y < 1) =", prob)