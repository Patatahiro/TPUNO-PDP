def cantidadParticipantes(participantes):
    cantidad = len(participantes)
    
    return print("La cantidad de participantes fue de: " + str(cantidad))

def cantidadHombres(participantes):
    contador = 0
    for i in range(len(participantes)):
        if participantes[i]['sexo'] == "M":
            contador = contador + 1
            
    return print("La cantidad de hombres que participaron fue de: " + str(contador))

def edadMujeres(participantes):
    acum = 0
    cont = 0
    for i in range(len(participantes)):
        if participantes[i]['sexo'] == 'F':
            acum = acum + participantes[i]['edad']
            cont = cont + 1
            
    promedio = acum / cont
            
    return print("La edad promedio de las mujeres que participaron fue de: " + str(promedio))

def ordenadoEdad(participantes):
    cambio = True
    while cambio:   
        cambio = False
        for i in range(len(participantes) - 1):
            if participantes[i]['edad'] > participantes[i+1]['edad']:
                # Intercambio de posicion
                participantes[i], participantes[i+1] = participantes[i+1], participantes[i]
                # El cambio es real por lo que reiniciamos el flag
                cambio = True
    return participantes

def mostrarOrdenadoEdad(participantes):
    for i in range(len(participantes)):
        print("Nombre: " + participantes[i]['nombre'])
        print("Edad: " + str(participantes[i]['edad']))
        print('')
        
def sumarDisparos(participantes):
    acum = 0
    cont = 0
    for i in range(len(participantes)):
        acum = acum + participantes[i]['disp1'] + participantes[i]['disp2'] + participantes[i]['disp3']
        cont = cont + 1
        
    total = acum / cont
    return total

def mejorPromedio(participantes, total):
    mejorPromParticipantes = []
    for i in range(len(participantes)):
        if participantes[i]['promdisp'] > total:
            mejorPromParticipantes.append(participantes[i])
            
    return mejorPromParticipantes
            
def mostrarMejorPromedio(mejorPromParticipantes):
    for i in range(len(mejorPromParticipantes)):
        print("Nombre: " + mejorPromParticipantes[i]['nombre'])
        print("Promedio de disparo: " + str(mejorPromParticipantes[i]['promdisp']))