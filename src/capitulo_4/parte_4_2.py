desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy.functions importar exp
desde fractions importar Fraction como Frac
desde estadistica.esperanza.esp_disc importar EspDisc
desde estadistica.esperanza.esp_cont importar EspCont
desde redondeo.redondeo importar redondear
desde estadistica.distribuciones importar transf
desde estadistica.distribuciones importar transf_conj

esp_disc = EspDisc()
esp_cont = EspCont()

t = Simbolo("t", real=Verdadero)
x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)

escribir("")
escribir("4.33")
dist = {4000:0.3, -1000:0.7}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_X = redondear(esp_disc.varianza(x), 0)
escribir("Var(X) = $", Var_X)

escribir("")
escribir("4.35")
dist = {2:0.01, 3:0.25, 4:0.4, 5:0.3, 6:0.04}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_X = redondear(esp_disc.varianza_alter(x), 2)
escribir("Var(X) = ", Var_X, "errores")

escribir("")
escribir("4.37")
f = Trozos((2*(1-x), (0<x) & (x<1)),
           (0, otro_caso))
esp_cont.est_func_dist(f)
Var_X = esp_cont.varianza(x)
escribir("Var(X) = $", Var_X, "* 5000")

escribir("")
escribir("4.39")
f = Trozos((x, (0<x) & (x<1)),
           (2-x, (1<=x) & (x<2)), 
           (0, otro_caso))
esp_cont.est_func_dist(f)
Var_X = esp_cont.varianza(x)
escribir("Var(X) = ", Var_X, "* 100 horas")

escribir("")
escribir("4.41")
dist = {-3:Frac(1,6),
         6:Frac(1,2),
         9:Frac(1,3)}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_g_X = redondear(esp_disc.desviacion((2*x+1)**2), 1)
escribir("g(X) = (2X+1)^2, desv(g(X)) = ", Var_g_X)

escribir("")
escribir("4.43")
f = Trozos((Frac(1,4)*exp(-x/4), x>0),
           (0, otro_caso))
esp_cont.est_func_dist(f)
E_g_X = esp_cont.esperanza(3*x-2)
Var_g_X = esp_cont.varianza(3*x-2)
escribir("Y = g(X) = 3X-2")
escribir("E(Y) = ", E_g_X)
escribir("Var(Y) = ", Var_g_X)

escribir("")
escribir("4.45")
dist = {(1, 1): 0.05, (2, 1): 0.05, (3, 1): 0.10, 
        (1, 2): 0.05, (2, 2): 0.10, (3, 2): 0.35, 
        (1, 3): 0.00, (2, 3): 0.20, (3, 3): 0.10}
f = transf_conj.dist_a_dp(dist, [x, y])
esp_disc.est_func_dist(f)
Cov = redondear(esp_disc.covarianza(),3)
escribir("Cov(X,Y) =", Cov)

escribir("")
escribir("4.47")
f = Trozos((Frac(2,3)*(x+2*y), (0<=x) & (x<=1) &
                               (0<=y) & (y<=1)),
           (0, otro_caso))
esp_cont.est_func_dist(f)
Cov = redondear(esp_cont.covarianza().evalf(), 4)
escribir("Cov(X,Y) =", Cov)

escribir("")
escribir("4.49")
dist = {0:0.41, 1:0.37, 2:0.16, 3:0.05, 4:0.01}
f = transf.dist_a_dp(dist, x)
esp_disc.est_func_dist(f)
Var_X = redondear(esp_disc.varianza(x), 4)
desv_X = redondear(esp_disc.desviacion(x), 4)
escribir("Var(X) =", Var_X)
escribir("desv(X) =", desv_X)