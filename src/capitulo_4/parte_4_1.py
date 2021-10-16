desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy importar binomial como nC
desde sympy importar pi
desde sympy importar FiniteSet como Con
desde sympy.functions importar exp
desde fractions importar Fraction como Frac
desde estadistica.esperanza importar E_disc
desde estadistica.esperanza.esp_cont importar EspCont
desde estadistica.distribuciones.dist_cont importar DistCont
desde redondeo.redondeo importar redondear
desde sympy importar simplify

t = Simbolo("t", real=Verdadero)
x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)

esp_cont = EspCont()

escribir("4.3")
dist = {20:Frac(1,5),
        25:Frac(3,5),
        30:Frac(1,5)}
f = E_disc.dist_a_dp(dist, t)
E_disc.establecer_dp(f)
E_T = E_disc.E(t)
escribir("E(T) = ", E_T, "centavos")

escribir("")
escribir("4.5")
dist = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = redondear(E_disc.E(x), 2)
escribir("E(X) = ", E_X, "imperfecciones")

escribir("")
escribir("4.7")
dist = {4000:0.3, -1000:0.7}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = redondear(E_disc.E(x), 0)
escribir("E(X) = $", E_X)

escribir("")
escribir("4.9")
dist = {3:Frac(8,52),
        5:Frac(8,52),
        0:Frac(36,52)}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = redondear(E_disc.E(x).evalf(), 2)
escribir("E(X) = $", E_X)

escribir("")
escribir("4.11")
dist = {200000:0.002,
        100000:0.01,
         50000:0.1}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_X = redondear(E_disc.E(x), 0) + 500
escribir("E(X) = $", E_X)

escribir("")
escribir("4.13")
f = Trozos((4/(pi*(1+x**2)), (0<x) & (x<1)),
           (0, otro_caso))
esp_cont.establecer_fdp(f)
E_X = esp_cont.esperanza(x)
escribir("E(X) =", E_X)

escribir("")
escribir("4.15")
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0, otro_caso))
esp_cont.establecer_fdp(f)
E_X = esp_cont.esperanza(x)*100
escribir("E(X) =", E_X, "horas")

escribir("")
escribir("4.17")
dist = {-3:Frac(1,6),
         6:Frac(1,2),
         9:Frac(1,3)}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_g_X = redondear(E_disc.E((2*x+1)**2).evalf(), 0)
escribir("g(X) = (2X+1)^2, E(g(X)) =", E_g_X)

escribir("")
escribir("4.19")
dist = {0:Frac(1,10),
        1:Frac(3,10),
        2:Frac(2,5),
        3:Frac(1,5)}
f = E_disc.dist_a_dp(dist, x)
E_disc.establecer_dp(f)
E_g_X = redondear(E_disc.E(1200*x-50*x**2).evalf(), 0)
escribir("g(X) = 1200X - 50X^2, E(g(X)) = $", E_g_X)

escribir("")
escribir("4.21")
f = Trozos((2*(1-x), (0<x) & (x<1)),
           (0, otro_caso))
esp_cont.establecer_fdp(f)
E_g_X = redondear(esp_cont.esperanza(x**2).evalf()*5000, 2)
escribir("g(X) = X^2, E(g(X)) = $", E_g_X)

escribir("")
escribir("4.23")
dist = {(2, 1): 0.10, (4, 1): 0.15, 
        (2, 3): 0.20, (4, 3): 0.30, 
        (2, 5): 0.10, (4, 5): 0.15}
f = E_disc.dist_a_dp(dist, [x, y])
E_disc.establecer_dp(f)
E_g_XY = redondear(E_disc.E(x*y**2).evalf(), 1)
escribir("a) g(X,Y) = XY^2, E(g(X,Y)) =", E_g_XY)
E_X = redondear(E_disc.E(x).evalf(), 2)
escribir("b) E(X) =", E_X)
E_Y = redondear(E_disc.E(y).evalf(), 2)
escribir("c) E(Y) =", E_Y)

escribir("")
escribir("4.25")
f = Trozos(( (nC(4,x)*nC(4,y)*nC(4,3-x-y))/nC(12,3), Con(0,1,2,3).pert(x) &
                                                     Con(0,1,2,3).pert(y)))
E_disc.establecer_dp(f)
E_g_XY = E_disc.E(x+y)
escribir("g(X,Y) = X+Y, E(g(X,Y)) =", E_g_XY, "para jacks y reyes")

escribir("")
escribir("4.27")
f = Trozos((Frac(1,2000)*exp(-x/2000), (x>=0)), 
           (0, otro_caso))
esp_cont.establecer_fdp(f)
E_X = esp_cont.esperanza(x)
escribir("E(X) =", E_X, "horas")

escribir("")
escribir("4.29")
f = Trozos((3*x**(-4), (x>1)), 
             (0, otro_caso))
esp_cont.establecer_fdp(f)
E_X = esp_cont.esperanza(x)
escribir("E(X) =", E_X)

escribir("")
escribir("4.31")
f = Trozos((5*(1-y)**4, (0<=y) & (y<=1)), 
             (0, otro_caso))
esp_cont.establecer_fdp(f)
E_Y = esp_cont.esperanza(y)
escribir("a) E(Y) =", E_Y)
dist_cont = DistCont()
dist_cont.est_func_dist(f)
prob = simplify(dist_cont.prob(y>E_Y))
escribir("a) P(Y > E) =", prob, "= (5/6)^5")