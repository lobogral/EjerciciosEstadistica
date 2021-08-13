desde sympy importar C, Trozos
desde sympy.abc importar x, y, z
desde fracciones importar Fracción
desde redondeo importar redondear
desde distribuciones importar conjuntaContinua como conjCont

escribir("3.41")
f = Trozos((24*x*y, (0<=x) & (x<=1) &
                    (0<=y) & (y<=1) &
                    (x + y <= 1)),             
            (0, otroCaso))

intervalo = x + y < Fracción(1,2)
prob = conjCont.Prob(f, intervalo)
escribir("a) P(X + Y < 1/2) =", prob)
escribir("b) g(x) =", conjCont.ProbMarginal(f,x))
intervaloDep = y < Fracción(1,8)
valIndep = Fracción(3,4)
prob = conjCont.ProbCondicional(f, intervaloDep, x, valIndep)
escribir("c) P( Y < 1/8 | X = 3/4 ) =", prob)


escribir("")
escribir("3.43")
f = Trozos((4*x*y, (0<x) & (x<1) & (0<y) & (y<1)),        
           (0, otroCaso))
intervalo = (0<=x) & (x<=Fracción(1,2)) 
intervalo = intervalo & (Fracción(1,4)<=y) & (y<=Fracción(1,2))
prob = conjCont.Prob(f, intervalo)
escribir("a) P(0 <= X <= 1/2, 1/4 < Y < 1/2) =", prob)
intervalo = (x<y)
prob = conjCont.Prob(f, intervalo)
escribir("b) P(X < Y) =", prob)

escribir("")
escribir("3.45")
f = Trozos((1/y, (0<x) & (x<y) & (y<1)),        
           (0, otroCaso))
intervalo = x + y > 1/2
prob = conjCont.Prob(f, intervalo)
escribir("P(X + Y > 1/2) =", redondear(prob, 4))

escribir("")
escribir("3.47")
f = Trozos((2, (0<x) & (x<y) & (y<1)),            
           (0, otroCaso))
intervaloDep = (Fracción(1,4) < x) & (x < Fracción(1,2))
valIndep = Fracción(3,4)
prob = conjCont.ProbCondicional(f, intervaloDep, y, valIndep)
escribir("b) P( 1/4 < X < 1/2 | Y = 3/4 ) =", prob)

escribir("")
escribir("3.55")
f = Trozos(((6-x-y)/8, (0<x) & (x<2) & 
                       (2<y) & (y<4)),            
           (0, otroCaso))
intervaloDep = (1 < y) & (y < 3)
valIndep = 1
prob = conjCont.ProbCondicional(f, intervaloDep, x, valIndep)
escribir("P( 1 < Y < 3 | X = 1 ) =", prob)

escribir("")
escribir("3.59")
f = Trozos((x*(y**2)*z, (0<x) & (x<1) &
                        (0<y) & (y<1) & 
                        (0<z) & (z<2)),            
           (0, otroCaso))
k = 1/conjCont.ProbTotal(f)
escribir("a) k =", k)
intervalo = (x<Fracción(1,4)) & (y > Fracción(1,2)) & (1<z) & (z<2)
prob = conjCont.Prob(k*f, intervalo)
escribir("b) P(X < 1/4, Y > 1/2, 1 < Z < 2) =", prob)