desde sympy importar Trozos, C, Rational
desde sympy.abc importar x, y
desde sympy.functions importar exp
desde fracciones importar Fracción
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
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0,otroCaso))
b = 1.2
escribir("a) P(X < 1.2) =", redondear(cont.ProbAcum(f,x,b),2))
a = 0.5
b = 1
escribir("b) P(0.5 < X < 1) =", redondear(cont.Prob(f,x,a,b),3))

escribir("")
escribir("3.9")
f = Trozos((Fracción(2,5)*(x+2), (0<x) & (x<1)), 
           (0,otroCaso))
escribir("a) Área bajo curva =", cont.ProbTotal(f,x))
a = Fracción(1,4)
b = Fracción(1,2)
escribir("b) P(1/4 < X < 1/2) =", cont.Prob(f,x,a,b))

escribir("")
escribir("3.11")
f = (C(2,x)*C(5,3-x))/C(7,3)
print("Distribución:", disc.Func2Dist(f, x, [0,1,2]))

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
f = Trozos((Fracción(1,2), (1<x) & (x<3)), 
           (0,otroCaso))
escribir("a) Área bajo curva =", cont.ProbTotal(f,x))
a = 2
b = Fracción('2.5')
escribir("b) P(2 < X < 2.5) =", cont.Prob(f,x,a,b))
b = Fracción('1.6')
escribir("c) P(X <= 1.6) =", float(cont.ProbAcum(f,x,b)))

escribir("")
escribir("3.19")
f = Trozos((Fracción(1,2), (1<x) & (x<3)), 
           (0,otroCaso))
F = cont.ProbAcum(f,x)
escribir("F(x) =", F)
Fb = F.subs(x, Fracción('2.5'))
Fa = F.subs(x, 2)
escribir("P(2 < X < 2.5) =", Fb-Fa)

escribir("")
escribir("3.21")
f = Trozos((x**Fracción(1,2), (0<x) & (x<1)), 
           (0,otroCaso))
k = 1/cont.ProbTotal(f,x)
escribir("a) k =", k)
escribir("b)")
F = cont.ProbAcum(k*f,x)
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
f = Trozos((Fracción(1,2000)*exp(-x/2000), (x>=0)), 
           (0,otroCaso))
F = cont.ProbAcum(f,x)
escribir("a) F(x) =", F)
P = redondear(1 - F.subs(x,1000).evalf(), 4)
escribir("b) P(X > 1000) =", P)
P = redondear(F.subs(x,2000).evalf(), 4)
escribir("c) P(X <= 2000) =", P)

escribir("")
escribir("3.29")
f = Trozos((3*x**(-4), (x>1)), 
           (0,otroCaso))
escribir("a) Área bajo curva =", cont.ProbTotal(f,x))
F = cont.ProbAcum(f,x)
escribir("b) F(x) =", F)
P = redondear(1 - F.subs(x,4).evalf(), 4)
escribir("c) P(X > 4) =", P)

escribir("")
escribir("3.31")
f = Trozos((Fracción(1,4)*exp(-y/4), (y>=0)), 
           (0,otroCaso))
b = 6
P = redondear(1 - cont.ProbAcum(f,y,b).evalf(), 4)
escribir("a) P(Y > 6) =", P)
a = 0
b = 1
P = redondear(cont.Prob(f,y,a,b).evalf(),4)
escribir("b) P(0 < Y < 1) =", P)

escribir("")
escribir("3.33")
f = Trozos(((y**4)*(1-y)**3, (0<=y) & (y<=1)), 
           (0,otroCaso))
k = 1/cont.ProbTotal(f,y)
escribir("a) k =", k)
a = 0
b = 0.5
P = redondear(cont.Prob(k*f,y,a,b).evalf(),4)
escribir("b) P(0 < Y < 0.5) =", P)
a = 0.8
b = 1
P = redondear(cont.Prob(k*f,y,a,b).evalf(),4)
escribir("c) P(0.8 < Y < 1) =", P)