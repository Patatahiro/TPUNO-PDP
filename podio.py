#Funcion que ordena la lista de participantes tomando como referencia el mejor disparo
def ordenarMejordisp(participantes):
    cambio = True
    while cambio:   
        cambio = False
        for i in range(len(participantes) - 1):
            if participantes[i]['mejordisp'] > participantes[i+1]['mejordisp']:
                # Intercambio de posicion
                participantes[i], participantes[i+1] = participantes[i+1], participantes[i]
                # El cambio es real por lo que reiniciamos el flag
                cambio = True
    return participantes 

#Funcion que muestra el podio de participantes
def mostrarPodio(participantes):
    for x in range(3):
        print("Puesto "+ str(x+1))
        print("Participante nro: " + participantes[x]["nro"])
        print("Nombre: " + participantes[x]["nombre"])
        print("Apellido: " + participantes[x]["apellido"])
        print("Mejor disparo: " + str(participantes[x]["mejordisp"]))
        print('')
    
def podiotxt(participantes):
    f = open("podio.txt", "w+")
    
    for x in range(3):
        f.write("Puesto "+ str(x+1) + "\n")
        f.write("Participante nro: " + participantes[x]["nro"] + "\n")
        f.write("Nombre: " + participantes[x]["nombre"] + "\n")
        f.write("Apellido: " + participantes[x]["apellido"] + "\n")
        f.write("Mejor disparo: " + (str(participantes[x]["mejordisp"]) + "\n"))
        f.write("\n")
        
def ultimoLugar(participantes):
    x = len(participantes) - 1
    print("El ultimo lugar es del participante numero " + participantes[x]['nro'])
    print("Nombre: " + participantes[x]["nombre"])
    print("Apellido: " + participantes[x]["apellido"])
    print("Mejor disparo: " + (str(participantes[x]["mejordisp"])))