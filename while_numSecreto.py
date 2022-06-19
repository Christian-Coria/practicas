numeroSecreto = 777
print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

while numeroSecreto != 77:
    print("aun no has adivinado", numeroSecreto)
    numeroSecreto -=1
print("me descubriste!!!", numeroSecreto)