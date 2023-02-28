texto_variado ="palabra 123 +-* #%&"
print (type(texto_variado))

#podemos utilizar comillas triples para que el teexto se muestre como la cadena que hemos escrito
print ("""
funcionamiento de \n
programas: (opciones)
-1 para acceder a opciones
-2 para salir
 """)

#subscripting e indexado
##############################################################################################
texto="Python"
print (texto[0])
print (texto[5])
print (texto[-1])
print (texto[-6])

print (texto[6])# marcaran error ya que exede el limite de la cadena no podemos acceder a una posicion que no existe
print (texto[-7])# error no podemos acceder a una pocision que no existe


letra= texto [0]
print(letra)

texto [0] = "p" # error no podemos modificar una cadena (string)

letra= "p"
print(letra)

texto_compuesto=letra + texto [1] #concanetacion
print(texto_compuesto)


######################################################################################

#slicing o substringning
texto ="Python"
print(texto [0:3])
print(texto [0:-3])
print(texto [0:-2])
print(texto [2:])
print(texto [:3])

print(texto [-3::-1])

print(texto [::-1])
print(texto [1:50])
print(texto [2:2])

###############################################################################################

#cadenas y formatos

texto= "Hola mundo! Buenastardes"
print(texto.lower ())# los metodos se utilizan por medio de un "." 
print(texto.upper())
print(texto.capitalize())#la primera letra en mayuscula y las demas en minusculas
print(texto.title())#nos ayuda a hacer que la inical de cada palabra sea mayuscula
print(texto.swapcase())#intercambia mayusculas por minusculas
texto=(texto.upper)

print(texto)

print("{} + {} = {}".format(2,3,2+3))
print("{} + {} = {}".format("hola","mundo","hola mundo"))
print("{:.3f} + {:.4f} = {}".format(2,3,2+3))
print("{1} + {0} = {2}".format(2,3,2+3))
print("{1} + {0} = {2}".format("hola","mundo","hola mundo"))
print("{:d} = {:b} = {:o}= {:x}".format(15,15,15,15))

#en terminal escrbir Python seguido enter 
# funcion dir (str) nos mostrara una lista de los metodos que tenemos disponibles para aplicar a variables













