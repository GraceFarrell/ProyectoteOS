import json
import time
import datetime
import boto3
from threading import Thread
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk as Ttk
import matplotlib.pyplot as plt
from time import time as tiempo

clientes = [] 

class Taqueria:
    def __init__(self):
        self.clientes = []
	self.numero_clientes = 0
    def addCliente(self):
        self.numero_clientes += 1 
    def getClientes(self):
        return self.numero_clientes
         
class Orden:
    def __init__(self,part_id,typee,meat,quantity,ingredients,ready=False):
        self.part_id = part_id
        self.typee = typee
        self.meat=meat
        self.quantity = quantity
        self.ingredients = ingredients
        self.meatG = []
    def getType(self):
        return self.typee
    def getMeat(self):
        return self.meat
    def getQuantity(self):
        return self.quantity
    def String(self):
        return "part_id:{0}\n typee:{1}\n meat:{2}\n quantity:{3}\n ingredients:{4}\n".format(self.part_id,self.typee,self.meat,self.quantity,self.ingredients)
    def __str__(self):
        return "part_id:{0}\n typee:{1}\n meat:{2}\n quantity:{3}\n ingredients:{4}\n".format(self.part_id,self.typee,self.meat,self.quantity,self.ingredients)
    def __iter__(self):
        return self
    
class Cliente:
    def __init__(self,date,idd,ordenes):
        self.date=date
        self.idd=idd
        self.numero_ordenes = 0
        self.ordenes = self.addOrden(ordenes)
    def addOrden(self,orden):
	ordenes = []
        for i in range (len(orden)):
            no = Orden(orden[i]["part_id"],orden[i]["type"],orden[i]["meat"],orden[i]["quantity"],orden[i]["ingredients"],False)
            self.numero_ordenes += 1
	    ordenes.append(no)
    def getOrdenesSize(self):
        return self.numero_ordenes
    def getOrdenes(self):
        return self.ordenes
    def getCompletado(self):
        temp = 0
        for orden in ordenes:
            if orden.ready:
                temp += 1
        if temp == self.numero_ordenes:
            return True
        return False
    def __str__(self):
        temp = ""
        for orden in self.ordenes:
            temp += orden.String()
        return "Cliente: {0} \n{1}\n{2}".format(self.idd,self.date,temp)

def Atender(cliente):
    for orden in cliente.getOrdenes():
	orden.ready = True

def CustomerService2(lista,taqueria): 
    for i in range(len(lista)):
        customer = Cliente(lista[i]["datetime"],lista[i]["request_id"],lista[i]["orden"])
        clientes.append(customer)
        taqueria.addCliente()
    
def Take_Orders(orders):
    orders = orders.replace("'", "\"")    
    data = json.loads(orders)  
    return data

def Recieve_Orders(sqs):
	response = sqs.receive_message(QueueUrl = 'https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team2')

	recibos = []
	message_string = ""

	for message in response["Messages"]:
		message.append
		print(message['Body'])
		message_string = message['Body']

	for r in recibos:
		response = sqs.delete_message(QueueURL='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team2',ReceiptHandle=r)

	return Take_Orders(message_string)


def Graficar(clientes):
    carnes = {"asada":0,"adobada":0,"cabeza":0, "lengua":0, "suadero":0, "veggie":0,"Tripa":0}
    x_labels = ["asada","adobada","cabeza","lengua","suadero","veggie","tripa"]

##    for cliente in clientes:    
    
def main():
    start = tiempo()
    inbound_Order = str({"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123",
                   "orden": [ { "part_id": "123-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "123-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "123-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]})

    ordenes_aws=[]
    Franc = Taqueria()
    
    try:
        sqs = boto3.client('sqs')
        data = Recieve_Orders(sqs)
    except:
        data = Take_Orders(inbound_Order)
        ordenes_aws.append(data)

    CustomerService(ordenes_aws,Franc)
    Atender(clientes[0])

    for c in Franc.getClientes():
	if c.getCompletado():
	   print("Esta completada la orden del cliente")
        print (c)

    end = tiempo()
    print(end-start)

main()

