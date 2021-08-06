desde sympy importar integrar
desde sympy.abc importar x, t
desde sympy.functions importar exp
desde fracciones importar Fracción
desde redondeo importar redondear

escribir("3.9")
f = Fracción(2,5)*(t+2)
a = 0
b = 1
escribir("a) P(0 < X < 1) =", integrar(f, (t,a,b)))
a = Fracción(1,4)
b = Fracción(1,2)
escribir("b) P(1/4 < X < 1/2) =", integrar(f, (t,a,b)))

escribir("")
escribir("3.17")
f = Fracción(1,2)
a = 1
b = 3
escribir("a) P(1 < X < 3) =", integrar(f, (t,a,b)))
a = 2
b = Fracción('2.5')
escribir("b) P(2 < X < 2.5) =", integrar(f, (t,a,b)))
a = 1
b = Fracción('1.6')
escribir("c) P(X <= 1.6) =", float(integrar(f, (t,a,b))))

escribir("")
escribir("3.19")
f = Fracción(1,2)
F = integrar(f, (t,1,x))
escribir("F(x) =", F, ", 0 <= x < 3")
Fb = F.subs(x, Fracción('2.5'))
Fa = F.subs(x, 2)
escribir("P(2 < X < 2.5) =", Fb-Fa)

escribir("")
escribir("3.21")
f = t**Fracción(1,2)
k = 1/integrar(f, (t,0,1))
escribir("a) k =", k)
escribir("b)")
F = integrar(k*f, (t,0,x))
escribir("F(x) =", F, ", 0 <= x < 1")
Fb = F.subs(x, 0.6)
Fa = F.subs(x, 0.3)
escribir("P(0.3 < X < 0.6) =", redondear(Fb-Fa, 4))

escribir("")
escribir("3.27")
f = Fracción(1,2000)*exp(-t/2000)
F = integrar(f, (t,0,x))
escribir("a) F(x) =")
escribir("|", 0, "               , x < 0")
escribir("|", F, ", x >= 0")
P = redondear(1 - F.subs(x,1000).evalf(), 4)
escribir("b) P(X > 1000) =", P)
P = redondear(F.subs(x,2000).evalf(), 4)
escribir("c) P(X <= 2000) =", P)