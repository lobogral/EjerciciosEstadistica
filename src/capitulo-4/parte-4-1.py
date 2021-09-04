desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy importar binomial como C
desde sympy importar pi
desde sympy importar FiniteSet como Con
desde sympy.functions importar exp
desde fractions importar Fraction como Fracción
desde esperanza importar distE, contE
desde distribuciones importar continua como cont
desde redondeo importar redondear
desde sympy importar simplify

t = Simbolo("t", real=Verdadero)
x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)

escribir("4.3")
dist = {20:Fracción(1,5),
        25:Fracción(3,5),
        30:Fracción(1,5)}
f = distE.dist2Dp(dist, t)
distE.establecerDp(f)
E = distE.E(t)
escribir("E(T) = ", E, "centavos")

escribir("")
escribir("4.5")
dist = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
E = redondear(distE.E(x), 2)
escribir("E(X) = ", E, "imperfecciones")

escribir("")
escribir("4.7")
dist = {4000:0.3, -1000:0.7}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
E = redondear(distE.E(x), 0)
escribir("E(X) = $", E)

escribir("")
escribir("4.9")
dist = {3:Fracción(8,52),
        5:Fracción(8,52),
        0:Fracción(36,52)}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
E = redondear(distE.E(x).evalf(), 2)
escribir("E(X) = $", E)

escribir("")
escribir("4.11")
dist = {200000:0.002,
        100000:0.01,
         50000:0.1}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
E = redondear(distE.E(x), 0) + 500
escribir("E(X) = $", E)

escribir("")
escribir("4.13")
f = Trozos((4/(pi*(1+x**2)), (0<x) & (x<1)),
           (0, otroCaso))
contE.establecerFdp(f)
E = contE.E(x)
escribir("E(X) =", E)

escribir("")
escribir("4.15")
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0, otroCaso))
contE.establecerFdp(f)
E = contE.E(x)*100
escribir("E(X) =", E, "horas")

escribir("")
escribir("4.17")
dist = {-3:Fracción(1,6),
         6:Fracción(1,2),
         9:Fracción(1,3)}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
E = redondear(distE.E((2*x+1)**2).evalf(), 0)
escribir("g(X) = (2X+1)^2, E(g(X)) =", E)

escribir("")
escribir("4.19")
dist = {0:Fracción(1,10),
        1:Fracción(3,10),
        2:Fracción(2,5),
        3:Fracción(1,5)}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
E = redondear(distE.E(1200*x-50*x**2).evalf(), 0)
escribir("g(X) = 1200X - 50X^2, E(g(X)) = $", E)

escribir("")
escribir("4.21")
f = Trozos((2*(1-x), (0<x) & (x<1)),
           (0, otroCaso))
contE.establecerFdp(f)
E = redondear(contE.E(x**2).evalf()*5000, 2)
escribir("g(X) = X^2, E(g(X)) = $", E)

escribir("")
escribir("4.23")
dist = {(2, 1): 0.10, (4, 1): 0.15, 
        (2, 3): 0.20, (4, 3): 0.30, 
        (2, 5): 0.10, (4, 5): 0.15}
f = distE.dist2Dp(dist, [x, y])
distE.establecerDp(f)
E = redondear(distE.E(x*y**2).evalf(), 1)
escribir("a) g(X,Y) = XY^2, E(g(X,Y)) =", E)
E = redondear(distE.E(x).evalf(), 2)
escribir("b) E(X) =", E)
E = redondear(distE.E(y).evalf(), 2)
escribir("c) E(Y) =", E)

escribir("")
escribir("4.25")
f = Trozos(( (C(4,x)*C(4,y)*C(4,3-x-y))/C(12,3), Con(0,1,2,3).pert(x) &
                                                 Con(0,1,2,3).pert(y)))
distE.establecerDp(f)
E = distE.E(x+y)
escribir("g(X,Y) = X+Y, E(g(X,Y)) =", E, "para jacks y reyes")

escribir("")
escribir("4.27")
f = Trozos((Fracción(1,2000)*exp(-x/2000), (x>=0)), 
           (0, otroCaso))
contE.establecerFdp(f)
E = contE.E(x)
escribir("E(X) =", E, "horas")

escribir("")
escribir("4.29")
f = Trozos((3*x**(-4), (x>1)), 
             (0, otroCaso))
contE.establecerFdp(f)
E = contE.E(x)
escribir("E(X) =", E)

escribir("")
escribir("4.31")
f = Trozos((5*(1-y)**4, (0<=y) & (y<=1)), 
             (0, otroCaso))
contE.establecerFdp(f)
E = contE.E(y)
escribir("a) E(Y) =", E)
cont.establecerFdp(f)
prob = simplify(cont.Prob(y>E))
escribir("a) P(Y > E) =", prob, "= (5/6)^5")