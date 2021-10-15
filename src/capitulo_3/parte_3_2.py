desde sympy importar binomial como nC
desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy importar Eq como Ec
desde sympy importar FiniteSet como Con
desde fractions importar Fraction como Frac
desde redondeo.redondeo importar redondear
desde estadistica.distribuciones.dist_conj_cont importar DistConjCont
desde estadistica.distribuciones importar dist_conj_disc

dist_conj_cont = DistConjCont()

x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)
z = Simbolo("z", real=Verdadero)

escribir("3.37")
f = Trozos((x*y, Con(1,2,3).pert(x) & 
                 ((y>=1) & (y<=2)) | Ec(y,3)))
c = dist_conj_disc.prob_total(f)
escribir("a) c =", 1/c)
f = Trozos((abs(x - y), Con(-2,0,2).pert(x) & 
                        Con(-2,3).pert(y)))
c = dist_conj_disc.prob_total(f)
escribir("b) c =", 1/c)

escribir("")
escribir("3.39")
f = Trozos(((nC(3,x)*nC(2,y)*nC(3,4-x-y))/nC(8,4), Con(0,1,2,3).pert(x) & 
                                                   Con(0,1,2).pert(y)))
dist_conj_disc.establecer_dp(f)
escribir("a) ", dist_conj_disc.dp_a_dist(x,y))
prob = dist_conj_disc.prob(x + y <= 2)
escribir("b) P(X + Y <= 2) =", prob)

escribir("")
escribir("3.41")
f = Trozos((24*x*y, (0<=x) & (x<=1) &
                    (0<=y) & (y<=1) &
                    (x + y <= 1)),             
            (0, otro_caso))
dist_conj_cont.est_func_dist(f)
intervalo = x + y < Frac(1,2)
prob = dist_conj_cont.prob(intervalo)
escribir("a) P(X + Y < 1/2) =", prob)
escribir("b) g(x) =", dist_conj_cont.prob_marginal(x))
intervalo_dep = y < Frac(1,8)
eq_dep = Ec(x, Frac(3,4))
prob = dist_conj_cont.prob_condicional(intervalo_dep, eq_dep)
escribir("c) P( Y < 1/8 | X = 3/4 ) =", prob)

escribir("")
escribir("3.43")
f = Trozos((4*x*y, (0<x) & (x<1) & (0<y) & (y<1)),        
           (0, otro_caso))
dist_conj_cont.est_func_dist(f)
intervalo = (0<=x) & (x<=Frac(1,2)) 
intervalo = intervalo & (Frac(1,4)<=y) & (y<=Frac(1,2))
prob = dist_conj_cont.prob(intervalo)
escribir("a) P(0 <= X <= 1/2, 1/4 < Y < 1/2) =", prob)
intervalo = (x<y)
prob = dist_conj_cont.prob(intervalo)
escribir("b) P(X < Y) =", prob)

escribir("")
escribir("3.45")
f = Trozos((1/y, (0<x) & (x<y) & (y<1)),        
           (0, otro_caso))
dist_conj_cont.est_func_dist(f)
intervalo = x + y > 1/2
prob = redondear(dist_conj_cont.prob(intervalo), 4)
escribir("P(X + Y > 1/2) =", prob)

escribir("")
escribir("3.47")
f = Trozos((2, (0<x) & (x<y) & (y<1)),            
           (0, otro_caso))
dist_conj_cont.est_func_dist(f)
escribir("a)")
escribir("g(x) =", dist_conj_cont.prob_marginal(x))
escribir("h(y) =", dist_conj_cont.prob_marginal(y))
escribir("g(x)h(y) != f(x,y), Dependientes")
intervalo_dep = (Frac(1,4) < x) & (x < Frac(1,2))
eq_dep = Ec(y, Frac(3,4))
prob = dist_conj_cont.prob_condicional(intervalo_dep, eq_dep)
escribir("b) P( 1/4 < X < 1/2 | Y = 3/4 ) =", prob)

escribir("")
escribir("3.49")
dist = {(1, 1): 0.05, (2, 1): 0.05, (3, 1): 0.10, 
        (1, 2): 0.05, (2, 2): 0.10, (3, 2): 0.35, 
        (1, 3): 0.00, (2, 3): 0.20, (3, 3): 0.10}
f = dist_conj_disc.dist_a_dp(dist, [x, y])
dist_conj_disc.establecer_dp(f)
dist_marginal_X = dist_conj_disc.prob_marginal(x)
escribir("a) g(x) =", dist_marginal_X)
dist_marginal_Y = dist_conj_disc.prob_marginal(y)
escribir("b) h(y) =", dist_marginal_Y)
prob = redondear(dist_conj_disc.prob_condicional(Ec(y, 3), Ec(x, 2)), 4)
escribir("c) P(Y = 3 | X = 2) =", prob)

escribir("")
escribir("3.53")
f = Trozos(( (nC(4,x)*nC(4,y)*nC(4,3-x-y))/nC(12,3), Con(0,1,2,3).pert(x) &
                                                     Con(0,1,2,3).pert(y)))
dist_conj_disc.establecer_dp(f)
escribir("a)", dist_conj_disc.dp_a_dist(x,y))
prob = dist_conj_disc.prob(x + y >=2)
escribir("b) P(X + Y <= 2) =", prob)

escribir("")
escribir("3.55")
f = Trozos(((6-x-y)/8, (0<x) & (x<2) & 
                       (2<y) & (y<4)),            
           (0, otro_caso))
dist_conj_cont.est_func_dist(f)
intervalo_dep = (1 < y) & (y < 3)
eq_dep = Ec(x,1)
prob = dist_conj_cont.prob_condicional(intervalo_dep, eq_dep)
escribir("P( 1 < Y < 3 | X = 1 ) =", prob)

escribir("")
escribir("3.59")
f = Trozos((x*(y**2)*z, (0<x) & (x<1) &
                        (0<y) & (y<1) & 
                        (0<z) & (z<2)),            
           (0, otro_caso))
k = 1/dist_conj_cont.prob_total(f)
escribir("a) k =", k)
dist_conj_cont.est_func_dist(k*f)
intervalo = (x<Frac(1,4)) & (y > Frac(1,2)) & (1<z) & (z<2)
prob = dist_conj_cont.prob(intervalo)
escribir("b) P(X < 1/4, Y > 1/2, 1 < Z < 2) =", prob)