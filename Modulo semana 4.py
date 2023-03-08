#Error de sintaxis es un error que e¿impide la ejecucion del programa y que necesita ser resuelto antes de que este se pueda probar.

# Errores en tiempo de ejecucion comunmente suele deberse a la falta de validacion de un dato por parte del programador, a la existencia de un dato (que este sea nulo)

numHuevos= 12 
print("tengo" + numHuevos + "huevos.") # error

#Solucion 1.-
print("tengo"+ str(numHuevos)+ "huevos.")

#Solucion 2 
print ("tengo %s huevos." %(numHuevos))

#Error de logica los dos errores anteriores impediran la ejecucion del programa pero un error en la logica de programacion no. Este simplemente mostraria un resultado no deseado.

#calcular el area o superficie de un cuadrado 

lado= int(input ("ingrse la medida del lado del cuadrado: ")) #error 
superficie= lado*lado*lado
print(" la superficie del cuadrado es: " str())

|#solucion

lado= int(input ("ingrse la medida del lado del cuadrado: "))
superficie= lado*lado
print(" la superficie del cuadrado es: " str())
