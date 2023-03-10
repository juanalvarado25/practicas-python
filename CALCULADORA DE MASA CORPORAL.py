nombre= input("¿como te llamas?: ")
apellido1= input("¿cual es tu apellido paterno?: ")
apellido2= input("¿cual es tu apellido materno?: ")

print("hola",nombre, apellido1, apellido2)    

edad= int (input ("¿cuantos años tienes?: "))

altura = float(input ("¿cuanto mides? :"))

masa = float (input("¿cual es tu peso? :"))

IMC = masa / altura**2

print("",nombre, apellido1,apellido2, "tiene", edad,"años")

print("mide", altura,"cm", "y tiene un peso de", masa,"kg")

print("Su IMC es : " + str(IMC) )

if IMC >= 0 and IMC <= 15.99 :   
        print ("tiene","Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print ("tiene","Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print ("tiene","Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print ("es","Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("tiene","Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("tiene","obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print ("tiene","obesidad media")
elif IMC >= 40.00:
        print ("tiene","obesidad morbida")




