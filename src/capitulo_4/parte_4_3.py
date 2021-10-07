desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy.functions importar exp
desde fractions importar Fraction como Frac
desde estadistica.esperanza importar E_disc, E_cont
desde redondeo.redondeo importar redondear

x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)

escribir("4.51")
dist = {2:0.01, 3:0.25, 4:0.4, 5:0.3, 6:0.04}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = redondear(E_disc.E(x), 2)
Var_X = redondear(E_disc.Var(x), 2)
escribir("Z = 3X-2")
escribir("E(Z) = ", 3*E_X - 2, "errores")
escribir("Var(Z) = ", 3**2*Var_X, "errores")

escribir("")
escribir("4.53")
dist = {0:Frac(1,15),
        1:Frac(2,15),
        2:Frac(2,15),
        3:Frac(3,15),
        4:Frac(4,15),
        5:Frac(3,15)}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = E_disc.E(x)
escribir("Z = 1.65X-(1.20)*5+(0.75)(1.20)(5-X)")
escribir("Z = 0.75X - 1.5")
E_Z = redondear(0.75*E_X - 1.5, 2)
escribir("E(Z) = ", E_Z, "dolares")

escribir("")
escribir("4.55")
dist = {-3:Frac(1,6),
         6:Frac(1,2),
         9:Frac(1,3)}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = E_disc.E(x)
E_X2 = E_disc.E(x**2)
escribir("Z = (2X + 1)^2 = 4X^2 + 4X + 1")
E_Z = 4*E_X2 + 4*E_X + 1
escribir("E(Z) = ", E_Z)

escribir("")
escribir("4.59")
dist = {(0, 0):Frac(3,28), (1, 0):Frac(9,28), (2, 0):Frac(3,28), 
        (0, 1):Frac(3,14), (1, 1):Frac(3,14), (2, 1):0, 
        (0, 2):Frac(1,28), (1, 2):0,          (2, 2):0}
f = E_disc.dist_a_dp(dist, [x, y])
E_disc.establecer_dp(f)
E_2XY2 = E_disc.E(2*x*y**2)
E_X2Y = E_disc.E(x**2*y)
escribir("Z = XY^2 - X^2Y")
escribir("E(Z) = ", E_2XY2 - E_X2Y)

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
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = E_disc.E(x)
escribir("E(X + Y) =", E_X + E_X)
escribir("E(X - Y) =", E_X - E_X)
E_XY = redondear((E_X**2).evalf(), 2)
escribir("E(XY) =", E_XY)

escribir("")
escribir("4.71")
f = Trozos((Frac(2,7)*(x+2*y), (0<=x) & (x<=1) &
                               (1<=y) & (y<=2)),
           (0, otro_caso))
E_cont.establecer_fdp(f)
E_XY3 = E_cont.E(x/(y**3))
E_X2Y = E_cont.E(x**2*y)
escribir("E(X/(Y^3) + (X^2)Y) =", E_XY3 + E_X2Y)

escribir("")
escribir("4.73")
f = Trozos((Frac(1,5), (0<=x) & (x<=5)),
           (0, otro_caso))
E_cont.establecer_fdp(f)
E_X = redondear(E_cont.E(x).evalf(), 1)
E_X2 = redondear(E_cont.E(x**2).evalf(), 2)
escribir("E(X) =", E_X)
escribir("Var(X) =", E_X2 - E_X**2)

escribir("")
escribir("4.75")
f = Trozos((Frac(9,16)*1/(4**(x+y)), (x>=0) & (y>=0)))
E_disc.establecer_dp(f)
E_X = E_disc.E(x)
Var_X = E_disc.Var(x)
escribir("a)") 
escribir("E(X) =", E_X, ", E(Y) =", E_X) 
escribir("Var(X) =", Var_X, ", Var(Y) =", Var_X)
escribir("b)") 
escribir("E(X+Y) =", E_X + E_X)
escribir("Var(X+Y) =", 1**2*Var_X + 1**2*Var_X)

escribir("")
escribir("4.77")
f = Trozos((Frac(1,4)*exp(-y/4), (y>=0)), 
           (0, otro_caso))
E_cont.establecer_fdp(f)
E_Y = E_cont.E(y)
E_Y2 = E_cont.E(y**2)
escribir("a)")
escribir("E(Y) =", E_Y)
escribir("b)")
escribir("E(Y^2) =", E_Y2, "Var(Y) =", E_Y2- E_Y**2)

escribir("")
escribir("4.79")
f = Trozos((1, (7<=y) & (y<=8) ), 
           (0, otro_caso))
E_cont.establecer_fdp(f)
E_Y = E_cont.E(y)
Var_Y = E_cont.Var(y)
E_eY = redondear(E_cont.E(exp(y)).evalf(), 2)
escribir("De forma exacta, E(e^y) =", E_eY)
E_eY = redondear((exp(E_Y)*(1 + Var_Y/2)).evalf(), 2)
escribir("Por series de Taylor, E(e^y) =", E_eY) 
escribir("Es una buena aproximacion")