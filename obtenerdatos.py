def cargaDatos():
    #Datos de los participantes que seran utilizados posteriormente por el programa
    nro = []
    nombres = []
    apellidos = []
    edades = []
    sexos = []
    disp1 = []
    disp2 = []
    disp3 = []
    mejordisp = []
    promdisp = []
    condition = True
    
    datos = {"Nro Part": nro,
             "Nombre": nombres,
             "Apellido": apellidos,
             "Edad": edades,
             "Sexo": sexos,
             "Disp1":disp1,
             "Disp2":disp2,
             "Disp3":disp3,
             "MejorDisp":mejordisp,
             "PromDisp":promdisp
    }
    while condition == True:
        #Carga del numero de participante
        numero = input("Ingrese el numero del participante: ")
        nro.append(numero)
        #Carga del nombre del participante
        nombre = input("Ingrese el nombre del participante: ")
        nombres.append(nombre)
        #Carga del apellido del participante
        apellido = input("Ingrese el apellido del participante: ")
        apellidos.append(apellido)
        #Carga de la edad del participante
        edad = input("Ingrese la edad del participante: ")
        edades.append(edad)
        #Carga del sexo del participante
        sexo = input("Ingrese el sexo del participante: ")
        sexos.append(sexo)
        #Carga del primer disparo
        dis1 = [input("Ingrese el eje en X del disparo:"), input("Ingrese el eje en Y del disparo:")]
        disp1.append(dis1)
        #Carga del segundo disparo
        dis2 = [input("Ingrese el eje en X del disparo:"), input("Ingrese el eje en Y del disparo:")]
        disp2.append(dis2)
        #Carga del tercer disparo
        dis3 = [input("Ingrese el eje en X del disparo:"), input("Ingrese el eje en Y del disparo:")]
        disp3.append(dis3)
        #Si el numero del participante es 999 se interrumpe la carga
        if numero == '999':
            condition = False
            
        return datos