desde sympy importar binomial como nC
desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy importar Eq como Ec
desde sympy importar FiniteSet como Con
desde fractions importar Fraction como Frac
desde redondeo importar redondear
desde distribuciones importar conjuntaContinua como conjCont
desde distribuciones importar conjuntaDiscreta como conjDisc

x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)
z = Simbolo("z", real=Verdadero)

escribir("3.37")
f = Trozos((x*y, Con(1,2,3).pert(x) & 
                 ((y>=1) & (y<=2)) | Ec(y,3)))
c = conjDisc.ProbTotal(f)
escribir("a) c =", 1/c)
f = Trozos((abs(x - y), Con(-2,0,2).pert(x) & 
                        Con(-2,3).pert(y)))
c = conjDisc.ProbTotal(f)
escribir("b) c =", 1/c)

escribir("")
escribir("3.39")
f = Trozos(((nC(3,x)*nC(2,y)*nC(3,4-x-y))/nC(8,4), Con(0,1,2,3).pert(x) & 
                                                   Con(0,1,2).pert(y)))
conjDisc.establecerDp(f)
escribir("a) ", conjDisc.dp2Dist(x,y))
prob = conjDisc.Prob(x + y <= 2)
escribir("b) P(X + Y <= 2) =", prob)

escribir("")
escribir("3.41")
f = Trozos((24*x*y, (0<=x) & (x<=1) &
                    (0<=y) & (y<=1) &
                    (x + y <= 1)),             
            (0, otroCaso))
conjCont.establecerFdp(f)
intervalo = x + y < Frac(1,2)
prob = conjCont.Prob(intervalo)
escribir("a) P(X + Y < 1/2) =", prob)
escribir("b) g(x) =", conjCont.ProbMarginal(x))
intervaloDep = y < Frac(1,8)
eqDep = Ec(x, Frac(3,4))
prob = conjCont.ProbCondicional(intervaloDep, eqDep)
escribir("c) P( Y < 1/8 | X = 3/4 ) =", prob)

escribir("")
escribir("3.43")
f = Trozos((4*x*y, (0<x) & (x<1) & (0<y) & (y<1)),        
           (0, otroCaso))
conjCont.establecerFdp(f)
intervalo = (0<=x) & (x<=Frac(1,2)) 
intervalo = intervalo & (Frac(1,4)<=y) & (y<=Frac(1,2))
prob = conjCont.Prob(intervalo)
escribir("a) P(0 <= X <= 1/2, 1/4 < Y < 1/2) =", prob)
intervalo = (x<y)
prob = conjCont.Prob(intervalo)
escribir("b) P(X < Y) =", prob)

escribir("")
escribir("3.45")
f = Trozos((1/y, (0<x) & (x<y) & (y<1)),        
           (0, otroCaso))
conjCont.establecerFdp(f)
intervalo = x + y > 1/2
prob = redondear(conjCont.Prob(intervalo), 4)
escribir("P(X + Y > 1/2) =", prob)

escribir("")
escribir("3.47")
f = Trozos((2, (0<x) & (x<y) & (y<1)),            
           (0, otroCaso))
conjCont.establecerFdp(f)
escribir("a)")
escribir("g(x) =", conjCont.ProbMarginal(x))
escribir("h(y) =", conjCont.ProbMarginal(y))
escribir("g(x)h(y) != f(x,y), Dependientes")
intervaloDep = (Frac(1,4) < x) & (x < Frac(1,2))
eqDep = Ec(y, Frac(3,4))
prob = conjCont.ProbCondicional(intervaloDep, eqDep)
escribir("b) P( 1/4 < X < 1/2 | Y = 3/4 ) =", prob)

escribir("")
escribir("3.49")
dist = {(1, 1): 0.05, (2, 1): 0.05, (3, 1): 0.10, 
        (1, 2): 0.05, (2, 2): 0.10, (3, 2): 0.35, 
        (1, 3): 0.00, (2, 3): 0.20, (3, 3): 0.10}
f = conjDisc.dist2Dp(dist, [x, y])
conjDisc.establecerDp(f)
distMarginalX = conjDisc.ProbMarginal(x)
escribir("a) g(x) =", distMarginalX)
distMarginalY = conjDisc.ProbMarginal(y)
escribir("b) h(y) =", distMarginalY)
prob = redondear(conjDisc.ProbCondicional(Ec(y, 3), Ec(x, 2)), 4)
escribir("c) P(Y = 3 | X = 2) =", prob)

escribir("")
escribir("3.53")
f = Trozos(( (nC(4,x)*nC(4,y)*nC(4,3-x-y))/nC(12,3), Con(0,1,2,3).pert(x) &
                                                     Con(0,1,2,3).pert(y)))
conjDisc.establecerDp(f)
escribir("a)", conjDisc.dp2Dist(x,y))
prob = conjDisc.Prob(x + y >=2)
escribir("b) P(X + Y <= 2) =", prob)

escribir("")
escribir("3.55")
f = Trozos(((6-x-y)/8, (0<x) & (x<2) & 
                       (2<y) & (y<4)),            
           (0, otroCaso))
conjCont.establecerFdp(f)
intervaloDep = (1 < y) & (y < 3)
eqDep = Ec(x,1)
prob = conjCont.ProbCondicional(intervaloDep, eqDep)
escribir("P( 1 < Y < 3 | X = 1 ) =", prob)

escribir("")
escribir("3.59")
f = Trozos((x*(y**2)*z, (0<x) & (x<1) &
                        (0<y) & (y<1) & 
                        (0<z) & (z<2)),            
           (0, otroCaso))
k = 1/conjCont.ProbTotal(f)
escribir("a) k =", k)
conjCont.establecerFdp(k*f)
intervalo = (x<Frac(1,4)) & (y > Frac(1,2)) & (1<z) & (z<2)
prob = conjCont.Prob(intervalo)
escribir("b) P(X < 1/4, Y > 1/2, 1 < Z < 2) =", prob)