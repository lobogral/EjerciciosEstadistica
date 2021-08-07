desde sympy importar integrar, Trozos, simplificar, oo, Symbol
desde sympy.abc importar x, t, y
desde sympy.functions importar exp
desde fracciones importar Fracción
desde redondeo importar redondear

escribir("3.9")
f = Trozos((Fracción(2,5)*(x+2), (0<x) & (x<1)), 
           (0,otroCaso))
escribir("a) Área bajo curva =", integrar(f, (x,-oo,oo)))
a = Fracción(1,4)
b = Fracción(1,2)
escribir("b) P(1/4 < X < 1/2) =", integrar(f, (x,a,b)))

escribir("")
escribir("3.17")
f = Trozos((Fracción(1,2), (1<x) & (x<3)), 
           (0,otroCaso))
escribir("a) Área bajo curva =", integrar(f, (x,-oo,oo)))
a = 2
b = Fracción('2.5')
escribir("b) P(2 < X < 2.5) =", integrar(f, (x,a,b)))
a = -oo
b = Fracción('1.6')
escribir("c) P(X <= 1.6) =", float(integrar(f, (x,a,b))))

escribir("")
escribir("3.19")
f = Trozos((Fracción(1,2), (1<x) & (x<3)), 
           (0,otroCaso))
F = simplificar(integrar(f.subs(x,t), (t, -oo, x)).reescribir(Trozos))
escribir("F(x) =", F)
Fb = F.subs(x, Fracción('2.5'))
Fa = F.subs(x, 2)
escribir("P(2 < X < 2.5) =", Fb-Fa)

escribir("")
escribir("3.21")
f = Trozos((x**Fracción(1,2), (0<x) & (x<1)), 
           (0,otroCaso))
k = 1/integrar(f, (x,-oo,oo))
escribir("a) k =", k)
escribir("b)")
F = simplificar(integrar(k*f.subs(x,t), (t, -oo, x)).reescribir(Trozos))
escribir("F(x) =", F)
Fb = F.subs(x, 0.6)
Fa = F.subs(x, 0.3)
escribir("P(0.3 < X < 0.6) =", redondear(Fb-Fa, 4))

escribir("")
escribir("3.27")
f = Trozos((Fracción(1,2000)*exp(-x/2000), (x>=0)), 
           (0,otroCaso))
F = simplificar(integrar(f.subs(x,t), (t, -oo, x)).reescribir(Trozos))
escribir("a) F(x) =", F)
P = redondear(1 - F.subs(x,1000).evalf(), 4)
escribir("b) P(X > 1000) =", P)
P = redondear(F.subs(x,2000).evalf(), 4)
escribir("c) P(X <= 2000) =", P)

escribir("")
escribir("3.29")
f = Trozos((3*x**(-4), (x>1)), 
           (0,otroCaso))
escribir("a) Área bajo curva =", integrar(f, (x,-oo,oo)))
F = simplificar(integrar(f.subs(x,t), (t, -oo, x)).reescribir(Trozos))
escribir("b) F(x) =", F)
P = redondear(1 - F.subs(x,4).evalf(), 4)
escribir("c) P(X > 4) =", P)

escribir("")
escribir("3.31")
f = Trozos((Fracción(1,4)*exp(-y/4), (x>=0)), 
           (0,otroCaso))
f = Fracción(1,4)*exp(-y/4)
a = 6
b = oo
P = redondear(integrar(f, (y,a,b)).evalf(),4)
escribir("a) P(Y > 6) =", P)
a = 0
b = 1
P = redondear(integrar(f, (y,a,b)).evalf(),4)
escribir("b) P(0 < Y < 1) =", P)

escribir("")
escribir("3.33")
f = Trozos(((y**4)*(1-y)**3, (0<=y) & (y<=1)), 
           (0,otroCaso))
k = 1/integrar(f, (y,-oo,oo))
escribir("a) k =", k)
a = 0
b = 0.5
P = redondear(integrar(k*f, (y,a,b)).evalf(),4)
escribir("b) P(0 < Y < 0.5) =", P)
a = 0.8
b = 1
P = redondear(integrar(k*f, (y,a,b)).evalf(),4)
escribir("c) P(0.8 < Y < 1) =", P)