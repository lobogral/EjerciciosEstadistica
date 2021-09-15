desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy.functions importar exp
desde fractions importar Fraction como Frac
desde esperanza importar distE, contE
desde redondeo importar redondear

x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)

escribir("4.51")
dist = {2:0.01, 3:0.25, 4:0.4, 5:0.3, 6:0.04}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
EX = redondear(distE.E(x), 2)
VarX = redondear(distE.Var(x), 2)
escribir("Z = 3X-2")
escribir("E(Z) = ", 3*EX - 2, "errores")
escribir("Var(Z) = ", 3**2*VarX, "errores")

escribir("")
escribir("4.53")
dist = {0:Frac(1,15),
        1:Frac(2,15),
        2:Frac(2,15),
        3:Frac(3,15),
        4:Frac(4,15),
        5:Frac(3,15)}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
EX = distE.E(x)
escribir("Z = 1.65X-(1.20)*5+(0.75)(1.20)(5-X)")
escribir("Z = 0.75X - 1.5")
EZ = redondear(0.75*EX - 1.5, 2)
escribir("E(Z) = ", EZ, "dolares")

escribir("")
escribir("4.55")
dist = {-3:Frac(1,6),
         6:Frac(1,2),
         9:Frac(1,3)}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
EX = distE.E(x)
EX2 = distE.E(x**2)
escribir("Z = (2X + 1)^2 = 4X^2 + 4X + 1")
EZ = 4*EX2 + 4*EX + 1
escribir("E(Z) = ", EZ)

escribir("")
escribir("4.59")
dist = {(0, 0):Frac(3,28), (1, 0):Frac(9,28), (2, 0):Frac(3,28), 
        (0, 1):Frac(3,14), (1, 1):Frac(3,14), (2, 1):0, 
        (0, 2):Frac(1,28), (1, 2):0,          (2, 2):0}
f = distE.dist2Dp(dist, [x, y])
distE.establecerDp(f)
E2XY2 = distE.E(2*x*y**2)
EX2Y = distE.E(x**2*y)
escribir("Z = XY^2 - X^2Y")
escribir("E(Z) = ", E2XY2 - EX2Y)

escribir("")
escribir("4.65")
escribir("Z = -2X + 4Y - 3")
escribir("Var(Z) =", (-2)**2*5 + (4)**2*3 + 2*(-2)*(4)*(1))

escribir("")
escribir("4.69")
dist = {1:Frac(1,6),
        2:Frac(1,6),
        3:Frac(1,6),
        4:Frac(1,6),
        5:Frac(1,6),
        6:Frac(1,6)}
f = distE.dist2Dp(dist, x)
distE.establecerDp(f)
EX = distE.E(x)
escribir("E(X + Y) =", EX + EX)
escribir("E(X - Y) =", EX - EX)
EXY = redondear((EX**2).evalf(), 2)
escribir("E(XY) =", EXY)

escribir("")
escribir("4.71")
f = Trozos((Frac(2,7)*(x+2*y), (0<=x) & (x<=1) &
                               (1<=y) & (y<=2)),
           (0, otroCaso))
contE.establecerFdp(f)
EXY3 = contE.E(x/(y**3))
EX2Y = contE.E(x**2*y)
escribir("E(X/(Y^3) + (X^2)Y) =", EXY3 + EX2Y)

escribir("")
escribir("4.73")
f = Trozos((Frac(1,5), (0<=x) & (x<=5)),
           (0, otroCaso))
contE.establecerFdp(f)
EX = redondear(contE.E(x).evalf(), 1)
EX2 = redondear(contE.E(x**2).evalf(), 2)
escribir("E(X) =", EX)
escribir("Var(X) =", EX2 - EX**2)

escribir("")
escribir("4.75")
f = Trozos((Frac(9,16)*1/(4**(x+y)), (x>=0) & (y>=0)))
distE.establecerDp(f)
EX = distE.E(x)
VarX = distE.Var(x)
escribir("a)") 
escribir("E(X) =", EX, ", E(Y) =", EX) 
escribir("Var(X) =", VarX, ", Var(Y) =", VarX)
escribir("b)") 
escribir("E(X+Y) =", EX + EX)
escribir("Var(X+Y) =", 1**2*VarX + 1**2*VarX)

escribir("")
escribir("4.77")
f = Trozos((Frac(1,4)*exp(-y/4), (y>=0)), 
           (0, otroCaso))
contE.establecerFdp(f)
EY = contE.E(y)
EY2 = contE.E(y**2)
escribir("a)")
escribir("E(Y) =", EY)
escribir("b)")
escribir("E(Y^2) =", EY2, "Var(Y) =", EY2- EY**2)

escribir("")
escribir("4.79")
f = Trozos((1, (7<=y) & (y<=8) ), 
           (0, otroCaso))
contE.establecerFdp(f)
EY = contE.E(y)
VarY = contE.Var(y)
EeY = redondear(contE.E(exp(y)).evalf(), 2)
escribir("De forma exacta, E(e^y) =", EeY)
EeY = redondear((exp(EY)*(1 + VarY/2)).evalf(), 2)
escribir("Por series de Taylor, E(e^y) =", EeY) 
escribir("Es una buena aproximacion")