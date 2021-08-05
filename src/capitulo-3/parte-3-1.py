desde sympy importar integrar, lambdify
desde sympy.abc importar x, t
desde sympy.functions importar exp
desde fracciones importar Fracción
desde decimal importar Decimal
desde redondeo importar redondear

escribir("3.9")
f = Fracción(2,5)*(x+2)
a = 0
b = 1
escribir("a) P(0 < X < 1) =", integrar(f, (x,a,b)))
a = Fracción(1,4)
b = Fracción(1,2)
escribir("b) P(1/4 < X < 1/2) =", integrar(f, (x,a,b)))

escribir("3.17")
f = Fracción(1,2)
a = 1
b = 3
escribir("a) P(1 < X < 3) =", integrar(f, (x,a,b)))
a = 2
b = Fracción('2.5')
escribir("b) P(2 < X < 2.5) =", integrar(f, (x,a,b)))
a = 1
b = Fracción('1.6')
escribir("c) P(X <= 1.6) =", float(integrar(f, (x,a,b))))

escribir("3.19")
f = Fracción(1,2)
I = integrar(f, (t,1,x))
escribir("F(x) =", I, ", 0 <= x < 3")
F = lambdify(x, I)
b = 2.5
a = 2
escribir("P(2 < X < 2.5) =", Fracción(F(b)-F(a)))

escribir("3.21")
f = x**Fracción(1,2)
escribir("a) k =", 1/integrar(f, (x,0,1)))
escribir("b)")
I = integrar(f, (t,0,x))
escribir("F(x) =", I, ", 0 <= x < 1")
F = lambdify(x, I)
escribir("P(0.3 < X < 0.6) =", redondear(F(0.6)-F(0.3), 4))

escribir("3.27")
f = Fracción(1,2000)*exp(-t/2000)
I = integrar(f, (t,0,x))
escribir("a) F(x) =")
escribir("|", 0, "               , x < 0")
escribir("|", I, ", x >= 0")
F = lambdify(x, I)
escribir("b) P(1000 < X) =", redondear(1-F(1000), 4))
escribir("b) P(X >= 2000) =", redondear(F(2000), 4))