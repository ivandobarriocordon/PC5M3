
# DOCUMENTACIÓN TÉCNICA MODÚLO 3 CHECKPOINT 5


## ¿Qué es un condicional?

Es un **tipo de estructura de control** que nos permite tomar decisiones en nuestro código en base a ciertas condiciones. Es decir, nos permite determinar qué acciones realizar **en función de si una condicion es verdadera o falsa.**

Una forma de entender esto es con un ejemplo cotidiano de la vida real. Imagina que estas en un bar que sirven tanto comida como refrescos/bebidas. Si tienes hambre, puedes pedir una comida, sino tienes hambre, puedes pedir una bebida. En este caso, la condición sería que si tienes hambre o no, si la condicion es verdadera, se ejecutaría la acción de pedir una comida, en cambio, si la condición es falsa, se ejecutaría la acción de pedir una bebida.

Eso es un ejemplo cotidiano, ahora vamos con un ejemplo que podriamos programar. Imaginemos, que queremos calcular el área de un circulo si el radio es mayor que cero, y mostrar un mensaje de error si el radio es igual a cero o menor que cero. Aqui, la condición sería que si el radio es mayor que cero o no, si es verdadera, se ejecutaría el código para calcular el área, si es falsa, se ejecutaría el código para mostrar el mensaje de error.

A continuación pondre como sería el ejemplo del código:

**(Aclaración esto es como se haría en el lenguaje de Python, entre un lenguaje o otro puede haber diferencias a la hora de declarar las variables y las funciones)**

`radio = 5`

`if radio > 0:`
    `area = 3.14 * (radio ** 2)`
    `print("El área del círculo es:", area)`
`else:`
    `print("Error: El radio debe ser mayor que cero.")`
    

Tanto en Python como en otros lenguajes de programación, **las condicionales se utilizan para evaluar si una condición es verdadera o falsa y ejecutar diferentes bloques de código en función de cada resultado.**

Hay diferentes **tipos de condicionales** en Python y son las siguientes:

 -`if-else statement`:

 **(Se utiliza para evaluar una condición y ejecutar diferentes bloques de código en función de si la condición es verdadera o falsa.)**

    numero = 10

    if numero > 0:
        print("El número es positivo")
    else:
        print("El número es negativo o cero")

-`if-elif-else statement`:

**(Se utiliza para evaluar varias condiciones y ejecutar diferentes bloques de código en función de la primera condición que sea verdadera.)**

`dia_semana = "viernes"`

`if dia_semana == "lunes":
    print("Hoy es lunes")
elif dia_semana == "viernes":
    print("Hoy es viernes")
else:
    print("Hoy no es lunes ni viernes")`

-`while loop`:

**(Se utiliza para repetir un bloque de código mientras una condición sea verdadera.)**

`contador = 1`

`while contador <= 5:`
    `print("El valor de contador es:", contador)
    contador += 1`



## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Son 3:

-`While loop`

**Se utiliza para repetir un bloque de código mientras una condición sea verdadera.**

   Sintaxis básica:
    `while condicion:`
    # código a ejecutar mientras la condición sea verdadera
    
  Ejemplo:

    contador = 1

    while contador <= 5:
        print("El valor de contador es:", contador)
        contador += 1
 
 **Es útil cuando no sabemos cuántas veces queremos repetir un bloque de código.** Por ejemplo, si queremos imprimir los números del 1 al 5, podemos usar un while loop para controlar el contador.

 -`For loop`:
 **Se utiliza para iterar sobre una secuencia de elementos, como una lista, una cadena de texto o un rango numérico.**
  Sintáxis básica:
    `for elemento in secuencia:`
    # código a ejecutar para cada elemento de la secuencia
  Ejemplo:
    `frutas = ["manzana", "pera", "platano"]`

    for fruta in frutas:
        print("La fruta es:", fruta)

**Es útil cuando queremos realizar la misma acción en cada elemento de una secuencia.** Por ejemplo, si queremos sumar los números del 1 al 10, **podemos usar un for loop para iterar sobre el rango numérico.**

-Range():
**Se utiliza para generar una secuencia de números enteros. Esto es útil cuando queremos iterar sobre una serie de números en un bucle for.**

  Sintáxis básica:
    `range(start, stop, step)`

  Aclaraciones sobre los argumentos entre parentesis:

    `start: el número inicial de la secuencia (opcional, por defecto es 0).`
    `stop: el número final de la secuencia (no se incluye en la secuencia).`
    `step: el incremento entre cada número de la secuencia (opcional, por defecto es 1).`

  Ejemplo:
    `for numero in range(1, 11):`
    `print(numero)`
    
  En este ejemplo, la función range(1, 11) genera una secuencia de números del 1 al 10 (sin incluir el 11). Luego, en el bucle for, se itera sobre cada número de la secuencia y se imprime por pantalla.

  La utilidad del bucle de tipo range() radica en que permite generar secuencias de números de manera fácil y concisa, lo que resulta útil en múltiples situaciones, como en el ejemplo anterior de sumar los números del 1 al 10.

  Además, el bucle de tipo range() es especialmente útil cuando se trabaja con listas o cadenas de texto, ya que permite iterar sobre sus elementos sin tener que conocer de antemano su longitud.

## ¿Qué es una lista por comprensión en Python?
    Una lista por comprensión es una forma concisa de crear una nueva lista a partir de otra lista o secuencia, aplicando una transformación o filtro a cada elemento.

  Ejemplo 1: Crear una nueva lista con los números del 1 al 10, pero solo los pares:
    `lista_pares = [numero for numero in range(1, 11) if numero % 2 == 0]`
    `print(lista_pares)`

  En este ejemplo, se utiliza una lista por comprensión para crear una nueva lista llamada lista_pares, que contiene solo los números pares del 1 al 10. La condición if numero % 2 == 0 filtra los números impares.

  Ejemplo 2: Crear una nueva lista con los cuadrados de los números del 1 al 5:
    `lista_cuadrados = [numero**2 for numero in range(1, 6)]`
    `print(lista_cuadrados)`

  En este ejemplo, se utiliza una lista por comprensión para crear una nueva lista llamada lista_cuadrados, que contiene los cuadrados de los números del 1 al 5. La expresión numero**2 calcula el cuadrado de cada número.

  La utilidad de las listas por comprensión radica en que permiten crear listas nuevas de manera eficiente y concisa, aplicando transformaciones o filtros a las secuencias existentes. Esto resulta especialmente útil cuando se trabaja con 
  listas o cadenas de texto, ya que permite realizar operaciones de manipulación de datos de manera más sencilla y legible.

  La sintaxis básica de una lista por comprensión es la siguiente:
    `nueva_lista = [expresion for elemento in secuencia if condicion]`
    `expresión: la transformación que se aplica a cada elemento de la secuencia.`
    `elemento: el elemento actual que se está iterando en la secuencia.`
    `secuencia: la secuencia de elementos sobre la que se itera.`
    `condición (opcional): una condición que debe ser verdadera para que el elemento se incluya en la nueva lista.`

## ¿Qué es un argumento en Python?

Un argumento se refiere a los valores que se pasan a una función para que pueda realizar ciertas operaciones o tareas. Los argumentos permiten proporcionar información adicional al llamar a una función, lo que permite que la función realice diferentes acciones o manipule los datos de acuerdo a los valores que se le pasen.

Un ejemplo para ilustrar cómo se utiliza un argumento en una función:
        `def saludar(nombre):`
            `print("Hola, " + nombre + "!")`

        `saludar("Ana")`

**Los argumentos pueden ser de diferentes tipos, como números, cadenas de texto, listas, diccionarios, etc. También se pueden pasar múltiples argumentos a una función, separados por comas al llamar a la función.**
La sintaxis para definir una función que acepta argumentos en Python es la siguiente:
    
    `def nombre_funcion(argumento1, argumento2, ...):`
    `# código de la función`

## ¿Qué es una función Lambda en Python?

Una función lambda en Python es una función anónima o de una sola línea que se utiliza para definir una expresión de función sin nombre. Las funciones lambda son útiles cuando necesitas definir una función pequeña y rápida que se utiliza solo una vez.

**Un ejemplo para ilustrar cómo se utiliza una función lambda en Python:**

    `suma = lambda a, b: a + b`
    `print(suma(3, 4))`

**Las funciones lambda son útiles cuando necesitas definir una función rápidamente y no necesitas asignarle un nombre.** También se pueden utilizar en situaciones en las que se necesita pasar una función como argumento a otra función.

La sintaxis básica de una función lambda en Python es la siguiente:
  
  `lambda argumento1, argumento2, ...: expresion`

## ¿Qué es un paquete pip?
    
pip es el administrador de paquetes oficial de Python, utilizado para instalar, actualizar y administrar paquetes y módulos de Python. Los paquetes pip son colecciones de código Python y recursos adicionales que pueden ser utilizados en tus proyectos.

**Algunos conceptos clave sobre los paquetes pip:**

    Paquete: Un paquete pip es una colección de código Python y recursos adicionales que se distribuyen como una unidad.

    Instalación: Pip te permite instalar paquetes desde el índice de paquetes de Python, conocido como PyPI (Python Package Index). Puedes instalar un paquete utilizando el comando pip install nombre_del_paquete.

    Actualización: Pip también te permite actualizar paquetes existentes a versiones más recientes. Puedes hacerlo utilizando el comando pip install --upgrade nombre_del_paquete.

    Desinstalación: Si ya no necesitas un paquete, puedes desinstalarlo utilizando el comando pip uninstall nombre_del_paquete.

    Dependencias: Los paquetes pip pueden tener dependencias, lo que significa que pueden requerir otros paquetes para funcionar correctamente. Pip se encarga de resolver estas dependencias automáticamente durante la instalación.

  **Un ejemplo de cómo utilizar pip para instalar un paquete:**

    `pip install numpy`

    En este ejemplo, se utiliza el comando pip install para instalar el paquete numpy. Una vez instalado, puedes importar y utilizar el paquete en tus proyectos Python.

    Recuerda que pip debe estar instalado en tu sistema para poder utilizarlo. Puedes verificar si pip está instalado ejecutando el comando pip --version en tu terminal.
