from estadistica.conteo_pm import perms
from estadistica.conteo_pm import perms_clase
from estadistica.conteo_pm import factorial
from estadistica.conteo_pm import combs

print("2.21")
print("Manera de acomodar a una persona:", 6*3)

print("")
print("2.23")
print("Puntos del espacio muestral:", 6*26)

print("")
print("2.25")
print("Pares de zapatos a mostrar:", 5*4)

print("")
print("2.27")
print("Planes diferentes para el comprador:", 4*3*2*2)

print("")
print("2.29")
print("Número de pruebas:", 3*5*7*2)

print("")
print("2.31")
print("a) Formas de que un estudiante elija una respuesta:", 4**5)
print("b) Formas de elegir incorrectas todas las preguntas:", 3**5)

print("")
print("2.33")
print("Máximo de matrículas a verificar:", perms(9, 2))

print("")
print("2.35")
print("Formas de colocar casas:", perms(9, 3)*perms(6, 6))

print("")
print("2.37")
print("Maneras de sentar niños y niñas:", factorial(4)*factorial(5))

print("")
print("2.39")
print("Número de ordenamientos")
print("a) 8 finalistas:", factorial(8))
print("b) primeras 3 posiciones:", perms(8, 3))

print("")
print("2.41")
print("Manera de asignar cursos:", perms(6, 4))

print("")
print("2.43")
print("Formas de plantar 5 árboles diferentes en círculo:", factorial(5-1))

print("")
print("2.45")
print("Permutaciones con las letras de infinito:", perms_clase(8, [3, 2]))

print("")
print("2.47")
print("Formas de terminar la temporada:", perms_clase(12, [7, 3, 2]))

print("")
print("2.49")
print("Formas de seleccionar candidatos:", combs(8, 3))
