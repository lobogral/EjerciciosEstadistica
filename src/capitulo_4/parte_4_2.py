desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy.functions importar exp
desde fractions importar Fraction como Frac
desde estadistica.esperanza importar dist_E, cont_E
desde redondeo.redondeo importar redondear

t = Simbolo("t", real=Verdadero)
x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)

escribir("")
escribir("4.33")
dist = {4000:0.3, -1000:0.7}
f = dist_E.dist_a_dp(dist, x)
dist_E.establecer_dp(f)
var = redondear(dist_E.Var(x), 0)
escribir("Var(X) = $", var)

escribir("")
escribir("4.35")
dist = {2:0.01, 3:0.25, 4:0.4, 5:0.3, 6:0.04}
f = dist_E.dist_a_dp(dist, x)
dist_E.establecer_dp(f)
var = redondear(dist_E.Var_Alter(x), 2)
escribir("Var(X) = ", var, "errores")

escribir("")
escribir("4.37")
f = Trozos((2*(1-x), (0<x) & (x<1)),
           (0, otroCaso))
cont_E.establecer_fdp(f)
var = cont_E.Var(x)
escribir("Var(X) = $", var, "* 5000")

escribir("")
escribir("4.39")
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0, otroCaso))
cont_E.establecer_fdp(f)
var = cont_E.Var(x)
escribir("Var(X) = ", var, "* 100 horas")

escribir("")
escribir("4.41")
dist = {-3:Frac(1,6),
         6:Frac(1,2),
         9:Frac(1,3)}
f = dist_E.dist_a_dp(dist, x)
dist_E.establecer_dp(f)
var = redondear(dist_E.desv((2*x+1)**2), 1)
escribir("g(X) = (2X+1)^2, desv(g(X)) = ", var)

escribir("")
escribir("4.43")
f = Trozos((Frac(1,4)*exp(-x/4), x>0),
           (0, otroCaso))
cont_E.establecer_fdp(f)
E = cont_E.E(3*x-2)
var = cont_E.Var(3*x-2)
escribir("Y = g(X) = 3X-2")
escribir("E(Y) = ", E)
escribir("Var(Y) = ", var)

escribir("")
escribir("4.45")
dist = {(1, 1): 0.05, (2, 1): 0.05, (3, 1): 0.10, 
        (1, 2): 0.05, (2, 2): 0.10, (3, 2): 0.35, 
        (1, 3): 0.00, (2, 3): 0.20, (3, 3): 0.10}
f = dist_E.dist_a_dp(dist, [x, y])
dist_E.establecer_dp(f)
cov = redondear(dist_E.Cov(),3)
escribir("Cov(X,Y) =", cov)

escribir("")
escribir("4.47")
f = Trozos((Frac(2,3)*(x+2*y), (0<=x) & (x<=1) &
                               (0<=y) & (y<=1)),
           (0, otroCaso))
cont_E.establecer_fdp(f)
cov = redondear(cont_E.Cov().evalf(), 4)
escribir("Cov(X,Y) =", cov)

escribir("")
escribir("4.49")
dist = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
f = dist_E.dist_a_dp(dist, x)
dist_E.establecer_dp(f)
var = redondear(dist_E.Var(x), 4)
desv = redondear(dist_E.desv(x), 4)
escribir("Var(X) =", var)
escribir("desv(X) =", desv)