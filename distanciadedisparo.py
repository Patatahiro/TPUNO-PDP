import math

def distanciaDisparo(x,y):
    X = (x*x)
    Y = (y*y)
    distancia = math.sqrt(X+Y)
    
    return distancia

#Prueba de funcionamiento
print(distanciaDisparo(10,20))