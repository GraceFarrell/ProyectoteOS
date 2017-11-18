import json
import time
import datetime
import boto3
from threading import Thread
from time import time as tiempo
from queue import Queue
from OrdenesAWS import Take_Orders
from OrdenesAWS import Recieve_Orders
from ClasesTaqueria import Orden
from ClasesTaqueria import Taqueria
from ClasesTaqueria import Cliente

ordenes_taqueria = Queue()
lista_taquero_asada = Queue()
lista_taquero_adobada = Queue()
lista_taquero_cabeza_lengua = Queue()
lista_taquero_otros = Queue()

ordenes = []

def Atender(cliente):
    for orden in cliente.getOrdenes():
        orden.ready=True
<<<<<<< HEAD
        
def AgregandoClientes(lista,taqueria,clientes):
	for i in range(len(lista)):
		customer = Cliente(lista[i]["datetime"],lista[i]["request_id"],lista[i]["orden"])
		clientes.append(customer)
		for orden in customer.getOrdenes():
			ordenes.append(orden)
			ordenes_taqueria.put(orden)
		taqueria.addCliente()  
def getData():
	inbound_Order = str({"datetime": "2017-01-01 23:23:23", "request_id": "123-$
                   "orden": [ { "part_id": "123-111",  "type": "taco", "meat": $
                              { "part_id": "123-222", "type": "mulita", "meat":$
                              { "part_id": "123-333", "type": "quesadilla", "me$
=======

def AgregandoClientes(lista,taqueria,clientes):
    for i in range(len(lista)):
        customer = Cliente(lista[i]["datetime"],lista[i]["request_id"],lista[i]["orden"])
        clientes.append(customer)
	for orden in customer.getOrdenes():
            ordenes.append(orden)
            ordenes_taqueria.put(orden)
        taqueria.addCliente()
def getData():
    try:
        sqs = boto3.client('sqs')
        data = Recieve_Orders(sqs)
    except:
        data = Take_Orders(inbound_Order)
        ordenes_aws.append(data)
>>>>>>> 45b64ba7d059edbbf256b77c94d0c713725e187a

	try:
		sqs = boto3.client("sqs")
		data = Recieve_Orders(sqs)
		ordenes_aws.append(data)
	except:
		data = Take_Orders(inbound_Order)
		ordenes_aws.append(data)
def main():
    start = tiempo()


#    inbound_Order = str({"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123",
#                  "orden": [ { "part_id": "123-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
#                              { "part_id": "123-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
#                              { "part_id": "123-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]})

    ordenes_aws=[]
    clientes = []
    Franc = Taqueria()
<<<<<<< HEAD
    
    getData()
=======
>>>>>>> 45b64ba7d059edbbf256b77c94d0c713725e187a

    getData()
    AgregandoClientes(ordenes_aws,Franc,clientes)


<<<<<<< HEAD
    for orden in ordenes:
	if orden.getMeat() == "asada":
		
=======
    print ()
    print(ordenes_taqueria)
>>>>>>> 45b64ba7d059edbbf256b77c94d0c713725e187a

    end = tiempo()
    print(end-start)

main()
