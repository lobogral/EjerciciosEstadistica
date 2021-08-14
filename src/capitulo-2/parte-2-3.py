desde decimal importar Decimal
desde fractions importar Fraction como Fracción
desde conteoPM importar *
desde redondeo importar *

escribir("2.55")
prob = Decimal('0.4') + Decimal('0.7') - Decimal('0.8')
escribir("a) Ambas ciudades:", prob)
prob = 1 - Decimal('0.8')
escribir("b) En ninguna de las ciudades:", prob)

escribir("")
escribir("2.57")
prob = Fracción(5, 26)
escribir("a) Vocal excepto y:", prob)
prob = Fracción(9, 26)
escribir("b) Listada antes de la j:", prob)
prob = Fracción(19, 26)
escribir("c) Listada despues de la g:", prob)

escribir("")
escribir("2.59")
prob = Fracción(5*P(25,2)*(9**3)*4, P(26,3)*(9**4))
escribir("Seleccionar artículo:", prob)

escribir("")
escribir("2.61")
prob = Fracción(C(20,2),C(52,2))
escribir("Escoger cartas correctas:", prob)

escribir("")
escribir("2.63")
prob = Fracción(C(4,3)*C(48,2),C(52,5))
escribir("a) Tener 3 ases:", prob)
prob = Fracción(C(13,4)*C(13,1),C(52,5))
escribir("b) Tener 4 corazones y 1 tréboles:", prob)

escribir("")
escribir("2.65")
prob = Fracción(54+69-35,100)
escribir("a) Estudiante estudió matemáticas o historia:", prob)
prob = 1 - prob
escribir("b) Estudiante no estudió:", prob)
prob = Fracción(69-35,100)
escribir("c) Estudiante estudio mates pero no historia:", prob)

escribir("")
escribir("2.67")
prob = Decimal('0.03') + Decimal('0.15') + Decimal('0.14')
escribir("a) PC en un dormitorio:", prob)
prob = 1 - prob
escribir("b) PC no está en un dormitorio:", prob)

escribir("")
escribir("2.69")
prob = 1 - Decimal('0.2')
escribir("a) No fallo:", prob)
prob = prob - Decimal('0.35')
escribir("b) No fallo ni deformidad:", prob)
prob = 1 - prob
escribir("c) fallo o deformidad:", prob)

escribir("")
escribir("2.71")
prob = Decimal('0.12') + Decimal('0.19')
escribir("a) No mas de 4 autos reciba servicio:", prob)
prob = 1 - Decimal('0.07')
escribir("b) Menos de 8 autos reciben servicio:", prob)
prob = Decimal('0.12') + Decimal('0.19')
escribir("c) 3 o 4 autos reciben servicio:", prob)

escribir("")
escribir("2.73")
prob = 1 - Decimal('0.990') - Decimal('0.001')
escribir("a) P(C) =", prob)
prob = 1 - Decimal('0.001')
escribir("b) No de llenado insuficiente:", prob)
prob = 1 - Decimal('0.99')
escribir("c) Maquina llene de más o de menos:", prob)

escribir("")
escribir("2.75")
prob = 1 - Decimal('0.95') - Decimal('0.002')
escribir("a) Paquete muy pesado:", prob)
utilidades = (25 - 20) * 10000
escribir("b) Utilidades 10000 paquetes ideal:", utilidades)
utilidades = redondear(utilidades - ((25*0.95 - 20)*10000), 0)
escribir("c) Reducción utilidad defectuosos:", utilidades)