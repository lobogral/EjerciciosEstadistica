desde sympy importar C, Trozos, oo
desde sympy.abc importar x, y
desde fracciones importar Fracción
desde distribuciones importar conjuntaContinua como conjCont

escribir("3.41")
f = Trozos((24*x*y, (0<=x) & (x<=1) &
                    (0<=y) & (y<=1) &
                    (x + y <= 1)),             
            (0, otroCaso))

escribir("b) g(x) =", conjCont.ProbMarginal(f,x))
valDep1 = -oo
valDep2 = Fracción(1,8)
valIndep = Fracción(3,4)
prob = conjCont.ProbCondicional(f, valDep1, valDep2, x, valIndep)
escribir("c) P( Y < 1/8 | X = 3/4 ) =", prob)

escribir("")
escribir("3.47")
f = Trozos((2, (0<x) & (x<y) & (y<1)),            
           (0, otroCaso))
valDep1 = Fracción(1,4)
valDep2 = Fracción(1,2)
valIndep = Fracción(3,4)
prob = conjCont.ProbCondicional(f, valDep1, valDep2, y, valIndep)
escribir("b) P( 1/4 < X < 1/2 | Y = 3/4 ) =", prob)

escribir("")
escribir("3.55")
f = Trozos(((6-x-y)/8, (0<x) & (x<2) & 
                       (2<y) & (y<4)),            
           (0, otroCaso))
valDep1 = 1
valDep2 = 3
valIndep = 1
prob = conjCont.ProbCondicional(f, valDep1, valDep2, x, valIndep)
escribir("P( 1 < Y < 3 | X = 1 ) =", prob)