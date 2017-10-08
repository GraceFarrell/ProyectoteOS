import json
import time
import datetime
from threading import Thread

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
    
with open('projectJson.txt', 'r') as f:
     data = json.load(f)
       
date = data["datetime"]
request_id = data["request_id"]
ordenes = data["orden"]
orden = data["orden"][0]["type"]
orden2 = data ["orden"][1]

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
##def procesarOrden(orden):
##    print(orden.meat)
##    
##ordenes_threads = []
##for i in ordeness:
##    thread = Thread(target = procesarOrden,args= i)
##    thread.setDaemon(True)
##    thread.start()
##    ordenes_threads.append(thread)
##
##for j in ordenes_threads:
##    j.join()
