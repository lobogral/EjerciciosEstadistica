from decimal import Decimal
from fractions import Fraction as Frac
from typing import Union
from estadistica.conteo_pm import combs
from estadistica.conteo_pm import perms
from redondeo.redondeo import redondear

prob: Union[Decimal, Frac]

print("2.55")
print("S -> Ubicado en Shanghai")
print("B -> Ubicado en Beijing")
prob = Decimal('0.4') + Decimal('0.7') - Decimal('0.8')
print("a) P(S ∩ B) =", prob)
prob = 1 - Decimal('0.8')
print("b) P(S' ∩ B') =", prob)

print("")
print("2.57")
prob = Frac(5, 26)
print("a) Vocal excepto y:", prob)
prob = Frac(9, 26)
print("b) Listada antes de la j:", prob)
prob = Frac(19, 26)
print("c) Listada despues de la g:", prob)

print("")
print("2.59")
prob = Frac(5*perms(25, 2)*(9**3)*4, perms(26, 3)*(9**4))
print("Seleccionar artículo:", prob)

print("")
print("2.61")
prob = Frac(combs(20, 2), combs(52, 2))
print("Escoger cartas correctas:", prob)

print("")
print("2.63")
prob = Frac(combs(4, 3)*combs(48, 2), combs(52, 5))
print("a) Tener 3 ases:", prob)
prob = Frac(combs(13, 4)*combs(13, 1), combs(52, 5))
print("b) Tener 4 corazones y 1 tréboles:", prob)

print("")
print("2.65")
print("M -> Estudio matemáticas")
print("H -> Estudio historia")
prob = Frac(54+69-35, 100)
print("a) P(M ∪ H) =", prob)
prob = 1 - prob
print("b) P(M' ∩ H') =", prob)
prob = Frac(69-35, 100)
print("c) P(M ∩ H') = ", prob)

print("")
print("2.67")
print("A -> PC en dormitorio de adultos")
print("N -> PC en dormitorio de niños")
print("O -> PC en otro dormitorio")
print("F -> Oficina o estudio")
print("H -> Otra habitación")
prob = Decimal('0.03') + Decimal('0.15') + Decimal('0.14')
print("a) P(A ∪ N ∪ O) =", prob)
prob = 1 - prob
print("b) P(F ∪ H) =", prob)

print("")
print("2.69")
print("A -> Componente falle")
print("B -> Componente falle pero no se deforme")
prob = 1 - Decimal('0.2')
print("a) P(A') =", prob)
prob = prob - Decimal('0.35')
print("b) P(A' ∩ B') =", prob)
prob = 1 - prob
print("c) P(A ∩ B) =", prob)

print("")
print("2.71")
prob = Decimal('0.12') + Decimal('0.19')
print("a) No mas de 4 autos reciba servicio:", prob)
prob = 1 - Decimal('0.07')
print("b) Menos de 8 autos reciben servicio:", prob)
prob = Decimal('0.12') + Decimal('0.19')
print("c) 3 o 4 autos reciben servicio:", prob)

print("")
print("2.73")
print("A -> Cumple con llenado")
print("B -> Llena por debajo")
print("C -> Llena por arriba")
prob = 1 - Decimal('0.990') - Decimal('0.001')
print("a) P(C) =", prob)
prob = 1 - Decimal('0.001')
print("b) P(B') =", prob)
prob = 1 - Decimal('0.99')
print("c) P(A') =", prob)

print("")
print("2.75")
prob = 1 - Decimal('0.95') - Decimal('0.002')
print("a) Paquete muy pesado:", prob)
UTILIDADES = (25 - 20) * 10000
print("b) Utilidades 10000 paquetes ideal: $", UTILIDADES)
UTILIDADES = redondear(UTILIDADES - ((25*0.95 - 20)*10000), 0)
print("c) Reducción utilidad defectuosos: $", UTILIDADES)
