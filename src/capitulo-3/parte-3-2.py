desde sympy importar binomial como C
desde sympy importar Piecewise como Trozos
desde sympy importar Symbol como Simbolo
desde sympy importar Eq como Ec
desde sympy importar Contains como Pert
desde fractions importar Fraction como Fracción
desde decimal importar Decimal
desde redondeo importar redondear
desde distribuciones importar conjuntaContinua como conjCont
desde distribuciones importar conjuntaDiscreta como conjDisc

x = Simbolo("x", real=Verdadero)
y = Simbolo("y", real=Verdadero)
z = Simbolo("z", real=Verdadero)

escribir("3.37")
f = Trozos((x*y, Pert(x,{1,2,3}) & 
                 Pert(y,{1,2,3})))
c = conjDisc.ProbTotal(f)
escribir("a) c =", 1/c)
f = Trozos((abs(x - y), Pert(x,{-2,0,2}) & 
                        Pert(y,{-2,3})))
c = conjDisc.ProbTotal(f)
escribir("b) c =", 1/c)

escribir("")
escribir("3.39")
f = Trozos(((C(3,x)*C(2,y)*C(3,4-x-y))/C(8,4), Pert(x,{0,1,2,3}) & 
                                               Pert(y,{0,1,2})))
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
intervalo = x + y < Fracción(1,2)
prob = conjCont.Prob(intervalo)
escribir("a) P(X + Y < 1/2) =", prob)
escribir("b) g(x) =", conjCont.ProbMarginal(x))
intervaloDep = y < Fracción(1,8)
eqDep = Ec(x, Fracción(3,4))
prob = conjCont.ProbCondicional(intervaloDep, eqDep)
escribir("c) P( Y < 1/8 | X = 3/4 ) =", prob)

escribir("")
escribir("3.43")
f = Trozos((4*x*y, (0<x) & (x<1) & (0<y) & (y<1)),        
           (0, otroCaso))
conjCont.establecerFdp(f)
intervalo = (0<=x) & (x<=Fracción(1,2)) 
intervalo = intervalo & (Fracción(1,4)<=y) & (y<=Fracción(1,2))
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
intervaloDep = (Fracción(1,4) < x) & (x < Fracción(1,2))
eqDep = Ec(y, Fracción(3,4))
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
f = Trozos(( (C(4,x)*C(4,y)*C(4,3-x-y))/C(12,3), Pert(x, {0,1,2,3}) &
                                                 Pert(y, {0,1,2,3})))
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
intervalo = (x<Fracción(1,4)) & (y > Fracción(1,2)) & (1<z) & (z<2)
prob = conjCont.Prob(intervalo)
escribir("b) P(X < 1/4, Y > 1/2, 1 < Z < 2) =", prob)