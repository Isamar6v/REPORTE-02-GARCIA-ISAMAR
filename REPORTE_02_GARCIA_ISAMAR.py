# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:13:37 2020

@author: isamar
"""


import csv

'''
transport = ["Sea", "Rail", "Air", "Road"]
contador = 0
totales = []

with open("synergy_logistics_database.csv", "r") as archivo:
    lector = csv.reader(archivo)
    
    
    for transporte in transport:
        archivo.seek(0)
        for linea in lector:
            if linea[7] == transporte:
                contador += 1
                
        totales.append([transporte, contador])
        contador = 0
        
        
        
print(totales)
'''

  
    

lista_datos = [] ##lista vacía para obtener una lista de listas

with open("synergy_logistics_database.csv", "r") as archivo:
    lector = csv.reader(archivo)

    for linea in lector: ##el objeto almacena la información del archivo línea por línea
        lista_datos.append(linea) ##nueva lista con toda mi información
        
'''##todo se puede agregar en la funcion de import y export 
lista_datos.pop(0)
valores = []    
for ruta in lista_datos:
    valores.append(int(ruta)[9])
    
print(sum(valores))##de importaciones a exportaciones'''

 
      
        #####



##GENERAR RUTAS DE EXPORTACION
   
def exportaciones_total (direccion, lista_datos):
    direccion = "Exports"
    contador = 0
    contador2 = 0
    rutas_contadas = []
    conteo_rutas = []

    for export in lista_datos:
        if export[1] == direccion: ##verifica que la dirección sea exports
            ruta_actual = [export[2], export[3]] ##origen y destino
        
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2], movimiento[3]]:
                        if movimiento[1] == direccion: ##vuelvo a comprobar la dirección
                            contador2 += int(movimiento[9]) ##se va agregando cuánto revenue genera cada ruta
                            contador += 1 ##va contando las rutas que ya existen
                        
                rutas_contadas.append(ruta_actual)
                    
                    
                conteo_rutas.append([export[2], export[3], contador, contador2])
                contador = 0
                contador2 = 0
                    
    conteo_rutas.sort(reverse = True, key = lambda x:x[3]) ##ordeno por el contador2 que es la cantidad mayor de ganancia
    return conteo_rutas

#print(exportaciones_total("Exports", lista_datos)[:10])

 
      
        #####


##GENERAR RUTAS DE IMPORTACION
       
def importaciones_total (direccion, lista_datos):
    direccion = "Imports"
    contador = 0
    contador2 = 0
    rutas_contadas = []
    conteo_rutas = []

    for imports in lista_datos:
        if imports[1] == direccion: ##verifica que la dirección sea imports
            ruta_actual = [imports[2], imports[3]] ##origen y destino
        
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2], movimiento[3]]:
                        if movimiento[1] == direccion: ##vuelvo a comprobar la dirección
                            contador2 += int(movimiento[9]) ##se va agregando cuánto revenue genera cada ruta
                            contador += 1 ##va contando las rutas que ya existen
                        
                rutas_contadas.append(ruta_actual)
                    
                    
                conteo_rutas.append([imports[2], imports[3], contador, contador2])
                contador = 0
                contador2 = 0
                    
    conteo_rutas.sort(reverse = True, key = lambda x:x[3])
    return conteo_rutas

#print(importaciones_total("Imports", lista_datos)[:10])

 
      
        #####


##GENERAR RUTAS POR MEDIO DE TRANSPORTE

def transporte(medio, lista_datos): 
    medio = "transport_mode" ##ya sea aire, mar, tren o carretera
    contador = 0
    contador2 = 0
    rutas_contadas = []
    conteo_rutas = []

    for ruta in lista_datos:
        if ruta[7] != medio:
            ruta_actual = [ruta[7]]
        
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[7]]:
                        contador2 += int(movimiento[9]) ##se va agregando cuánto revenue genera cada medio de transporte
                        contador += 1 ##va contando los medios de transporte que ya existen
                        
                rutas_contadas.append(ruta_actual)
                    
                    
                conteo_rutas.append([ruta[7], contador, contador2])
                contador = 0
                contador2 = 0
                    
    conteo_rutas.sort(reverse = True, key = lambda x:x[1]) ##ordeno por el contador2 que es la cantidad mayor de ganancia
    return conteo_rutas

#print(transporte("transport_mode", lista_datos))

 
      
        #####


##GENERAR EL 80% DEL VALOR DE IMPORT
    
def importaciones_80 (direccion, lista_datos):
    direccion = "Imports"
    contador2 = 0
    rutas_contadas = []
    conteo_rutas = []

    for imports in lista_datos:
        if imports[1] == direccion:   
            ruta_actual = [imports[3]] ##destino
        
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[3]]:
                        if movimiento[1] == direccion:
                            contador2 += int(movimiento[9])
                        
                rutas_contadas.append(ruta_actual)
                    
                    
                conteo_rutas.append([imports[3], contador2])
                contador2 = 0
                    
    conteo_rutas.sort(reverse = True, key = lambda x:x[1]) ##ordeno por el contador2 que es la cantidad mayor de ganancia
    return conteo_rutas

#print(importaciones_80("Imports", lista_datos)[:6])

 
      
        #####


##GENERAR EL 80% DEL VALOR DE EXPORT
    
def exportaciones_80 (direccion, lista_datos):
    direccion = "Exports"
    contador2 = 0
    rutas_contadas = []
    conteo_rutas = []

    for imports in lista_datos:
        if imports[1] == direccion:   
            ruta_actual = [imports[2]] ##origen
        
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2]]:
                        if movimiento[1] == direccion:
                            contador2 += int(movimiento[9])
                        
                rutas_contadas.append(ruta_actual)
                    
                    
                conteo_rutas.append([imports[2], contador2])
                contador2 = 0
                    
    conteo_rutas.sort(reverse = True, key = lambda x:x[1]) ##ordeno por el contador2 que es la cantidad mayor de ganancia
    return conteo_rutas

#print(exportaciones_80("Exports", lista_datos)[:8])
    

      
        #####


               
print("#####BIENVENID@#####")
opc = int(input("Elige una opción\n 1.- 10 rutas más demandadas acorde a los flujos de exportación\n 2.- 10 rutas más demandadas acorde a los flujos de importación\n 3.- Medios de transporte utilizados considerando el valor de las importaciones y exportaciones\n 4.- Países que le generan el 80% del valor de las exportaciones\n 5.- Países que le generan el 80% del valor de las importaciones\n Opc -->"))
if opc == 1:
    print(exportaciones_total("Exports", lista_datos)[:10])
if opc == 2:
    print(importaciones_total("Imports", lista_datos)[:10])
if opc == 3:
    print(transporte("transport_mode", lista_datos))
if opc == 4:
    print(exportaciones_80("Exports", lista_datos)[:8])
if opc == 5:
    print(importaciones_80("Imports", lista_datos)[:6])
else:
    print("Te equivocaste :(")
    
