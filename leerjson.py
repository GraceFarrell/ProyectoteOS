import json
import time
import datetime
import random
from threading import Thread
from tkinter import *
import os

class Orden:
    def __init__(self,part_id,typee,meat,quantity,ingredients):
        self.part_id = part_id
        self.typee = typee
        self.meat=meat
        self.quantity = quantity
        self.ingredients = ingredients
    def __str__(self):
        return "part_id:{0}\n typee:{1}\n meat:{2}\n quantity:{3}\n ingredients:{4}\n".format(self.part_id,self.typee,self.meat,self.quantity,self.ingredients)
    def __iter__(self):
        return self
    def __next__(self):
        return self

#Variable para la ruta al directorio
path = "/Users/miguelfrias/Documents/CetysU/QuintoS/OperatingS/JsonP"
 
#Lista vacia para incluir los ficheros
lstFiles = []
 
#Lista con todos los ficheros del directorio:
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
 
 
#Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
 
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".txt"):
            lstFiles.append(nombreFichero+extension)
            #print (nombreFichero+extension)
             
print(lstFiles)            
arc_json=[]
x = ['projectJson.txt','projectJson.txt','projectJson.txt','json.txt']
for i in lstFiles:
    with open(i, 'r') as f:
        data = json.load(f)
    arc_json.append(data)

for data in arc_json:
    date = data["datetime"]
    request_id = data["request_id"]
    ordenes = data["orden"]
##    orden = data["orden"][0]["type"]
##    orden2 = data ["orden"][1]

    ordeness = []
    for i in range (len(ordenes)):
        x = data["orden"][i]["part_id"]
        typee = data["orden"][i]["type"]
        meat = data["orden"][i]["meat"]
        quantity = data["orden"][i]["quantity"]
        ingredients = data["orden"][i]["ingredients"]
        no = Orden(x,typee,meat,quantity,ingredients)
        ordeness.append(no)

    for i in ordeness:
        print(i)
    
