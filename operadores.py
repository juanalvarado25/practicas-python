# #operadores aritmeticos (+,-,/,*) # para selecionar todo en comentario ctrl+k+c
# print (2 + 2)                   # para quitar comentarios ctrl+k+u
# print (4 - 2)
# print (3 * 2)
# print (15 / 2)
# print (11 % 4)#operador modulo signo de porcentaje (modulo)
# print (11 // 4)#operador division de piso el resultado es primero el residuo de la operacion
# print (2 ** 3)#operador potencia

# #operadores en cadenas (sting)
# print ("hola" + "mundo")#concatenacion es la suma de cadenas 
# print ("hola" * 3)#repeticon es la multiplicacion de cadenas
# print ("hola" + "mundo" * 3)

# #operadores de comparacion (permiten verificar si un operador es igual a otro)
# print ("Hola" == "hola" )#igual que
# print ("Hola" != "hola")#distinto que
# print (3 > 11) #mayor que
# print (11 >= 10)#mayor igual que
# print (10 <= 10)#menor igual que

#operadores de existencia (verifica si un elemento existe dentro de otro elemento)
# print ("ola" in "hola")# de exitencia
# print ("ola" not in "hola")# deinexitencia

# operadores booleanos (verifican si se cumple una u otra condicion)
# print (True or False) #or verifica que se cumpla solo una de las condiciones
# print (True and False)# and verifica que se cumplan las dos condiciones

#operadores de asignacion (le asigna un nuevo valor a una variable que ya ha sido definida)
# x=1 #operador de asignacion estandar
# x+=2 #operador de asignacion suma
# x*=3#operador de asignacion multiplicacion
# x%=4#operador de asignacion modulo
# print (x)

# jerarquia de operaciones 1. parentesis 2. exponentes 3. multiplicacion 4. division 5.modulo 6. divison de piso 7. suma 8. resta operadores del mismo nivel se resuelven de izquierda a derecha
x= 6 * 5 +8 /2 ** 4
print(x)