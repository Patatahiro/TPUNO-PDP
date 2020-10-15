from obtenerdatos import cargaDatos

list1 = [1, 3, 2, 4]
list2 = ["uno", "tres", "dos", "cuatro"]
list3 = ["one", "three", "two", "four"]

print(list1, list2, list3)

list1, list2, list3 = zip(*sorted(zip(list1,list2,list3)))

list1 = list(list1)
list2 = list(list2)
list3 = list(list3)

print(list1, list2, list3)

#Funcion que recibe un diccionario y lo ordena segun se le indique
def ordenarDatos(datos):
    print()