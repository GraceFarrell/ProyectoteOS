import json
import time
import datetime
##import boto3
from threading import Thread
from time import time as tiempo
from queue import Queue
from OrdenesAWS import Take_Orders
##from OrdenesAWS import Recieve_Orders
from ClasesTaqueria import Orden
from ClasesTaqueria import Taqueria
from ClasesTaqueria import Cliente
from ClasesTaqueria import Taquero
import threading

ordenes_taqueria = Queue()
clientes = []
ordenes = []
Franc = Taqueria()

def CustomerReady():
	while True:
		for cliente in clientes:
			if cliente.getCompletado():
				cliente.getSteps()
				clientes.remove(cliente)
				print("termine cliente")

def AgregandoClientes(cliente,taqueria,clientes):
	customer = Cliente(cliente["datetime"],cliente["request_id"],cliente["orden"])
	clientes.append(customer)
	for orden in customer.getOrdenes():
		ordenes.append(orden)
		ordenes_taqueria.put(orden)
	taqueria.addCliente()

def setMeats(taquero_uno, taquero_dos, taquero_tres):
	for i in range(ordenes_taqueria.qsize()):
		meat = ordenes_taqueria.get()
		if meat.getMeat() == "asada":
			taquero_uno.max_priority.put(meat)
		elif meat.getMeat() == "adobada":
			taquero_dos.max_priority.put(meat)
		elif meat.getMeat() == "lengua":
			taquero_tres.max_priority.put(meat)
		elif meat.getMeat() == "veggie":
			taquero_uno.max_priority.put(meat)
		elif meat.getMeat() == "tripa":
			taquero_dos.max_priority.put(meat)
		elif meat.getMeat() == "cabeza":
			taquero_tres.max_priority.put(meat)
		elif meat.getMeat() == "suadero":
			taquero_tres.max_priority.put(meat)
		#print ("ya asigne")

def getData(taquero_uno, taquero_dos, taquero_tres):
	inbound_Order = str({"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123",
                   "orden": [ { "part_id": "123-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "123-222", "type": "mulita", "meat": "lengua", "quantity": 1, "ingredients": []  },
                              { "part_id": "123-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]})

	try_Order = [str({"datetime": "2017-01-01 23:23:23", "request_id": "223-223-223",
                   "orden": [ { "part_id": "223-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "223-222", "type": "mulita", "meat": "lengua", "quantity": 1, "ingredients": []  },
                              { "part_id": "223-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "323-323-323",
                   "orden": [ { "part_id": "323-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "323-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "323-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "423-423-423",
                   "orden": [ { "part_id": "423-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "423-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "423-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "523-523-523",
                   "orden": [ { "part_id": "523-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "523-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "523-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "623-623-623",
                   "orden": [ { "part_id": "623-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "623-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "623-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "723-723-723",
                   "orden": [ { "part_id": "723-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "723-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "723-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "823-823-823",
                   "orden": [ { "part_id": "823-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "823-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "823-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "923-923-923",
                   "orden": [ { "part_id": "923-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "923-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "923-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]}), str({"datetime": "2017-01-01 23:23:23", "request_id": "023-023-023",
                   "orden": [ { "part_id": "023-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "023-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
                              { "part_id": "023-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]})]

	counter = 0

	while len(try_Order) != counter:
##        try:
##            sqs = boto3.client('sqs')
##            data = Recieve_Orders(sqs)
##        except:
##        data = Take_Orders(inbound_Order)
		data = Take_Orders(try_Order[counter])
		AgregandoClientes(data,Franc,clientes)
		setMeats(taquero_uno, taquero_dos, taquero_tres)
		counter += 1

def manejo_ingredientes(lock, orden, num, who, taquero, ingredient):
	lock.acquire()
	if who==1:
		for ingredient in orden.ingredients:
			taquero.ingredientes[ingredient]-=num
		taquero.ingredientes["tortillas"]-=num
	else:
		taquero.ingredientes[ingredient]+=num 
	time.sleep(1)
	lock.release()
            
def Tortillera(lock, taquero):
	while True:
		for ingredient in taquero.ingredientes:
			if taquero.ingredientes[ingredient] <= 200:
				manejo_ingredientes(lock, False, 200, 0, taquero, ingredient)

def Queue_algorithm(lock, taquero):
	while True:
		if taquero.max_priority.empty() == False:
			cocinar(lock,taquero,1,taquero.max_priority,taquero.med_priority)
                
		if taquero.med_priority.empty() == False:
			cocinar(lock,taquero,2,taquero.med_priority,taquero.low_priority)

		if taquero.low_priority.empty() == False:
			cocinar(lock,taquero,4,taquero.low_priority,taquero.min_priority)

		if taquero.waiting.empty() == False or taquero.min_priority.empty() == False:
			if taquero.waiting.empty() == False:
				time_slice = orden.current_total_time
				orden.ready = True 
				time.sleep(time_slice)

			elif taquero.min_priority.empty() == False:
				cocinar(lock,taquero,32,taquero.min_priority,taquero.waiting)

def cocinar(lock,taquero,time_slice,start_priority,next_priority):
	orden = start_priority.get()
	orden.setTimeByType()
	toPrepare = orden.toPrepare
	how_many = time_slice//orden.time_by_type #cuantos de ese tipo puede hacer en ese time slice

	#for ingredient in orden.ingredients:
	#	while taquero.ingredientes[ingredient] < how_many*50 or taquero.ingredientes["tortillas"] < how_many*50:
	#		orden.steps.append("Waiting for " + ingredient)

	orden.steps.append("Running")

	if how_many < toPrepare:
		manejo_ingredientes(lock, orden, 50, 1, taquero, False)
		taquero.ingredientes[orden.getMeat()]-=how_many
		orden.toPrepare -= how_many
		next_priority.put(orden)
		orden.steps.append("Paused") 
		time.sleep(time_slice)
 
	else:
		manejo_ingredientes(lock, orden, 50, 1, taquero, False)
		taquero.ingredientes[orden.getMeat()]-=toPrepare
		orden.ready = True
		time.sleep(orden.current_total_time)

def main():
	threads = []
##    start = tiempo()
    
	taquero_uno = Taquero() #Asada, veggie
	taquero_uno.ingredientes["asada"]=500
	taquero_uno.ingredientes["veggie"]=500
	taquero_dos = Taquero() #Adobada, tripa
	taquero_dos.ingredientes["adobada"]=500
	taquero_dos.ingredientes["tripa"]=500
	taquero_tres = Taquero() #Lengua, cabeza, suadero
	taquero_tres.ingredientes["lengua"]=500
	taquero_tres.ingredientes["cabeza"]=500
	taquero_tres.ingredientes["suadero"]=500
	
	lock1 = threading.Lock()
	lock2 = threading.Lock()
	lock3 = threading.Lock()
    
	thread_getData = Thread(target=getData,args= (taquero_uno, taquero_dos, taquero_tres))
	thread_getData.setDaemon(True)
	thread_getData.start()
	threads.append(thread_getData)

	thread_uno = Thread(target=Queue_algorithm,args= (lock1,taquero_uno,))
	thread_uno.setDaemon(True)
	thread_uno.start()
	threads.append(thread_uno)

	tortillera_uno = Thread(target=Tortillera,args= (lock1,taquero_uno,))
	tortillera_uno.setDaemon(True)
	tortillera_uno.start()
	threads.append(tortillera_uno)

	thread_dos = Thread(target=Queue_algorithm,args= (lock2,taquero_dos,))
	thread_dos.setDaemon(True)
	thread_dos.start()
	threads.append(thread_dos)

	tortillera_dos = Thread(target=Tortillera,args= (lock2,taquero_dos,))
	tortillera_dos.setDaemon(True)
	tortillera_dos.start()
	threads.append(tortillera_dos)

	thread_tres = Thread(target=Queue_algorithm,args= (lock3,taquero_tres,))
	thread_tres.setDaemon(True)
	thread_tres.start()
	threads.append(thread_tres)

	tortillera_tres = Thread(target=Tortillera,args= (lock3,taquero_tres,))
	tortillera_tres.setDaemon(True)
	tortillera_tres.start()
	threads.append(tortillera_tres)

	thread_customer_ready = Thread(target=CustomerReady)
	thread_customer_ready.setDaemon(True)
	thread_customer_ready.start()
	threads.append(thread_customer_ready)
    
main()
