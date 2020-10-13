#Pasos a seguir para el desarrollo del programa
#1 - Ingreso de datos del participante
#2 - Almacenar los datos en una estructura
#   Numero unico del participante
#   Edad del participante
#   Sexo del participante
#   Ubicacion de los disparos en pares X e Y (tomando como referencia la distancia del origen)
#   Disparo 1
#   Disparo 2
#   Disparo 3
#3 - Comparar los 3 disparos para:
#4 - Almacenar el MejorDisp
#5 - Almacenar el promedio de disparos
#NOTA - Si el numero de participante es el 999, se termina la carga.
#############################################################################
#1 - Mostrar el podio de los tres ganadores, en funcion del mejor disparo de cada uno
#   Nombre, Apellido, Mejor disparo
# Esto se debe informar tambien en un archivo de texto
#2 - Informar el ultimo participante
#3 - Informar cuantos participantes formaron parte del concurso
#4 - Informar cuantos hombres formaron parte del concurso
#5 - Informar edad promedio de las mujeres
#6 - Mostrar el listado de todos los participantes ordenados por edad
#7 - Informar el promedio de todos los disparos
#8 - Mostrar los participantes cuyo promedio de disparo sea mayor al promedio general
#EXTRA - Si en el punto 1 se da el caso de que dos participantes tengan el mismo MEJOR DISPARO, ordenar tambien por promedio

# Funcion para calculo del disparo. Recibe las coordenadas y retorna la distancia al centro
def calculoDisparo(corX, corY):
    print("")

#Funcion para el calculo del mejor disparo. Recibe las 3 distancias y retorna la mejor    
def mejorDisparo(distUno, distDos, distTres):
    print("")
    
#Funcion para el calculo del promedio de los disparos. Recibe las 3 distancias y retorna el promedio    
def promedioDisparos(distUno, distDos, distTres):
    print("")
