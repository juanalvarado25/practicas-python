#input sirve para capturar datos ingresados por el usuario desde la terminal de pyton sin la necesidad de haberlos definido previamente en el programa
nombre = input ("¿como te llamas?")
print ("hola" +  nombre)

edad= input ("¿cuantos años tienes?")
print (type (edad))
print(f"{nombre} tiene {edad} años")

#programa que pide dos numeros al usuario y los suma.
numero1 = int (input("introduce un numero por favor: "))
numero2= int (input ("introduce otro numero por favor: "))
numero3= numero1 + numero2

print(f"el resultado de la suma es: {numero3}")