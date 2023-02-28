# ejemplos de la funcion print

print("hola mundo")
print("hola mundo", "otra vez")
print("son las",9, "mañana")
print("el resultado de 3 * 4 es :",3*4)

#ejemplo de cadenas formateadas (cadena formateada durante la impresion podemos pedir que se muestren determinados valores en determinados sistemas que eligamos)
print("el numero 15 en sistema decimal es %d, en sistema octal es %o, en el sistema hexadecimal es%x" %(15,15,15))

pi= 3.141592
r=5
print(f"el radio de un circulo es{r} y el area de un circulo es {pi * r **2: .2f}")

#impresion de caracteres especiales
print ("la letra beta es:\n\t \u03b2") #\n nos sirve para realizar saltos de linea continua la impresion en la siguiente linea # \t es para tabulacion por defecto son 4 \u03b2 sistema aski

# caracteres de escape (es el ultimo por defecto en la segunda impresion)
print("hola mundo", end= " ")
print ("otra vez", end= "\t")
print("y otra vez")

