from podio import podiotxt
from podio import mostrarPodio
from podio import ordenarMejordisp
from podio import ultimoLugar
from conteo import cantidadParticipantes
from conteo import cantidadHombres
from conteo import edadMujeres
from conteo import ordenadoEdad
from conteo import mostrarOrdenado
from conteo import sumarDisparos
from conteo import mejorPromedio

participantes = []

participantes.append({"nro":'1',
                    "nombre": 'Nicolas',
                    "apellido":'Fernandez',
                    "edad": 22,
                    "sexo": 'M',
                    "disp1": 10,
                    "disp2": 10,
                    "disp3": 10,
                    "mejordisp": 10,
                    "promdisp": 10,
                    })

participantes.append({"nro":'4',
                    "nombre": 'Dobby',
                    "apellido":'Makemenke',
                    "edad": 3,
                    "sexo": 'M',
                    "disp1": 2,
                    "disp2": 2,
                    "disp3": 2,
                    "mejordisp": 2,
                    "promdisp": 2,
                    })

participantes.append({"nro":'2',
                    "nombre": 'Gertrudis',
                    "apellido":'Morel',
                    "edad": 50,
                    "sexo": 'F',
                    "disp1": 15,
                    "disp2": 15,
                    "disp3": 15,
                    "mejordisp": 15,
                    "promdisp": 15,
                    })

participantes.append({"nro":'3',
                    "nombre": 'Agustin',
                    "apellido":'Fernandez',
                    "edad": 48,
                    "sexo": 'M',
                    "disp1": 12,
                    "disp2": 12,
                    "disp3": 12,
                    "mejordisp": 12,
                    "promdisp": 12,
                    })

#participantes = ordenarMejordisp(participantes)
#mostrarPodio(participantes)
#podiotxt(participantes)
#ultimoLugar(participantes)
#print("La cantidad total de participantes fue de " + cantidadParticipantes(participantes))
#print("La cantidad de hombres que participaron fue de " + cantidadHombres(participantes) )
#print(edadMujeres(participantes))
#mostrarOrdenado(ordenadoEdad(participantes))
#print(sumarDisparos(participantes))
#print(mejorPromedio(participantes,sumarDisparos(participantes)))