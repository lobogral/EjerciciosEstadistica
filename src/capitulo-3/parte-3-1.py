desde sympy importar Piecewise como Trozos
desde sympy importar binomial como C
desde sympy importar Eq
desde sympy.abc importar x, y, w
desde sympy.functions importar exp, factorial
desde sympy.stats importar ContinuousRV
desde fractions importar Fraction como Fracción
desde redondeo importar redondear
desde distribuciones importar continua como cont
desde distribuciones importar discreta como disc

escribir("3.5")
f = x**2 + 4
c = 1/disc.ProbTotal(f, {x: (0,3)})
escribir("a) c =", c)
f = C(2,x)*C(3,3-x)
c = 1/disc.ProbTotal(f, {x: [0,1,2]})
escribir("b) c =", c)

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
dom = {x: [0,1,2]}
disc.establecerDpDom(f, dom)
escribir("f(x) =", disc.Func2Troz())

escribir("")
escribir("3.13")
f = Trozos((0.41, Eq(x, 0)), 
           (0.37, Eq(x, 1)), 
           (0.16, Eq(x, 2)), 
           (0.05, Eq(x, 3)), 
           (0.01, Eq(x, 4)))
dom = {x: (0,4)}
disc.establecerDpDom(f, dom)
escribir("F(x)=", disc.ProbAcum())

escribir("")
escribir("3.15")
f = (C(2,x)*C(5,3-x))/C(7,3)
dom = {x: [0,1,2]}
disc.establecerDpDom(f, dom)
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
f = Trozos((Fracción(1,27), Eq(w,-3)),
           (Fracción(6,27), Eq(w,-1)),
           (Fracción(12,27), Eq(w,1)),
           (Fracción(8,27), Eq(w,3)))
dom = {w: [-3,-1,1,3]}
disc.establecerDpDom(f, dom)
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

escribir("")
escribir("3.35")
f = exp(-6)*(6**x)/factorial(x)
disc.establecerDpDom(f)
subDom = {x: (0,8)}
prob = redondear(1 - disc.Prob(subDom).evalf(), 4)
escribir("a) P(X > 8) =", prob)
subDom = {x: [2]}
prob = redondear(disc.Prob(subDom).evalf(), 4)
escribir("b) P(X = 2) =", prob)