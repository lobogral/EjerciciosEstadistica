desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy.functions importar exp
desde fractions importar Fraction como Frac
desde estadistica.esperanza importar E_disc, E_cont
desde redondeo.redondeo importar redondear

t = Simbolo("t", real=Verdadero)
x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)

escribir("")
escribir("4.33")
dist = {4000:0.3, -1000:0.7}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
var = redondear(E_disc.Var(x), 0)
escribir("Var(X) = $", var)

escribir("")
escribir("4.35")
dist = {2:0.01, 3:0.25, 4:0.4, 5:0.3, 6:0.04}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
var = redondear(E_disc.Var_Alter(x), 2)
escribir("Var(X) = ", var, "errores")

escribir("")
escribir("4.37")
f = Trozos((2*(1-x), (0<x) & (x<1)),
           (0, otro_caso))
E_cont.establecer_fdp(f)
var = E_cont.Var(x)
escribir("Var(X) = $", var, "* 5000")

escribir("")
escribir("4.39")
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0, otro_caso))
E_cont.establecer_fdp(f)
var = E_cont.Var(x)
escribir("Var(X) = ", var, "* 100 horas")

escribir("")
escribir("4.41")
dist = {-3:Frac(1,6),
         6:Frac(1,2),
         9:Frac(1,3)}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
var = redondear(E_disc.desv((2*x+1)**2), 1)
escribir("g(X) = (2X+1)^2, desv(g(X)) = ", var)

escribir("")
escribir("4.43")
f = Trozos((Frac(1,4)*exp(-x/4), x>0),
           (0, otro_caso))
E_cont.establecer_fdp(f)
E = E_cont.E(3*x-2)
var = E_cont.Var(3*x-2)
escribir("Y = g(X) = 3X-2")
escribir("E(Y) = ", E)
escribir("Var(Y) = ", var)

escribir("")
escribir("4.45")
dist = {(1, 1): 0.05, (2, 1): 0.05, (3, 1): 0.10, 
        (1, 2): 0.05, (2, 2): 0.10, (3, 2): 0.35, 
        (1, 3): 0.00, (2, 3): 0.20, (3, 3): 0.10}
f = E_disc.dist_a_dp(dist, [x, y])
E_disc.establecer_dp(f)
cov = redondear(E_disc.Cov(),3)
escribir("Cov(X,Y) =", cov)

escribir("")
escribir("4.47")
f = Trozos((Frac(2,3)*(x+2*y), (0<=x) & (x<=1) &
                               (0<=y) & (y<=1)),
           (0, otro_caso))
E_cont.establecer_fdp(f)
cov = redondear(E_cont.Cov().evalf(), 4)
escribir("Cov(X,Y) =", cov)

escribir("")
escribir("4.49")
dist = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
var = redondear(E_disc.Var(x), 4)
desv = redondear(E_disc.desv(x), 4)
escribir("Var(X) =", var)
escribir("desv(X) =", desv)