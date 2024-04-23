# 1-Cree un bucle For de Python.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2-Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(a, b, c):
  return a + b + c
resultado= suma(2, 4, 6)
print(resultado)

# 3-Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma_lambda = lambda a, b, c: a + b + c
resultado_lambda = suma_lambda(3, 7, 9)
print(resultado_lambda)


# 4-Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in. nombre = 'Enrique' lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

 # Forma 1:

nombre = 'Enrique'
lista_nombres = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombres:
    print("El nombre está en la lista.")
else:
    print("El nombre no está en la lista.")

# Forma 2:

nombre = 'Enrique'
lista_nombres = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for n in lista_nombres:
    if n == nombre:
        print("El nombre está en la lista.")
        break
else:
    print("El nombre no está en la lista.")