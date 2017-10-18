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

def Take_Orders(orders):
    orders = orders.replace("'", "\"")    
    data = json.loads(orders)  
    return data

def Recieve_Orders(sqs):
	response = sqs.receive_message(QueueUrl = 'https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team2')

	recibos = []
	message_string = ""

	for message in response["Messages"]:
	#	message.append
	#	print(message['Body'])
		message_string = message['Body']

	#for r in recibos:
	#	response = sqs.delete_message(QueueURL='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team2',ReceiptHandle=r)

	return Take_Orders(message_string)
  
#with open('projectJson.txt', 'r') as f:
#     data = json.load(f)

#inbound_Order = str({"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123",
#               "orden": [ { "part_id": "123-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
#                          { "part_id": "123-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
#                          { "part_id": "123-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]})

#data = Take_Orders(inbound_Order)

sqs = boto3.client('sqs')
data = Recieve_Orders(sqs)
     
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
