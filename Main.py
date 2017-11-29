import json
import time
import datetime
import boto3
import threading
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from time import time as tiempo
from queue import Queue
from OrdenesAWS import Take_Orders
from OrdenesAWS import Recieve_Orders
from ClasesTaqueria import Orden
from ClasesTaqueria import Taqueria
from ClasesTaqueria import Cliente
from ClasesTaqueria import Taquero

ordenes_taqueria = Queue()
clientes = []
Franc = Taqueria()

def CustomerReady():
	while True:
		for cliente in clientes:
			if cliente.getCompletado():
				times = cliente.getStartTime()
				cliente.answer["start_time"] = times[0]
				cliente.answer["end_time"] = times[1]
				cliente.answer["steps"] = cliente.getSteps()
				clientes.remove(cliente)
				print("termine cliente")
				print(cliente.answer)

def AgregandoClientes(cliente,taqueria,clientes):
	customer = Cliente(cliente["datetime"],cliente["request_id"],cliente["orden"])
	clientes.append(customer)

	for orden in customer.getOrdenes():
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

def getData(taquero_uno, taquero_dos, taquero_tres):
	inbound_Order = str({"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123",
                   "orden": [ { "part_id": "123-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
                              { "part_id": "123-222", "type": "mulita", "meat": "lengua", "quantity": 1, "ingredients": []  },
                              { "part_id": "123-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "guacamole", "salsa"]} ]})

	counter = 0

	while 10 != counter:
		try:
			data = Recieve_Orders()
		except:
			h = ""

		AgregandoClientes(data,Franc,clientes)
		setMeats(taquero_uno, taquero_dos, taquero_tres)
		counter += 1

def manejo_ingredientes(lock, orden, num, who, taquero, ingredient):
	lock.acquire()
	if who==1:
		for ingredient in orden.ingredients:
			taquero.ingredientes[ingredient]-=num
		taquero.ingredientes["Tortillas"]-=1
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
		for small_orders in range(3):
			if taquero.max_priority.empty() == False:
				cocinar(lock,taquero,.1,taquero.max_priority,taquero.med_priority)

		for medium_orders in range(2):                
			if taquero.med_priority.empty() == False:
				cocinar(lock,taquero,.2,taquero.med_priority,taquero.low_priority)

		if taquero.low_priority.empty() == False:
			cocinar(lock,taquero,.4,taquero.low_priority,taquero.min_priority)

		if taquero.waiting.empty() == False or taquero.min_priority.empty() == False:
			if taquero.waiting.empty() == False:
				orden = taquero.waiting.get()

				orden.step_start_time = orden.step_end_time
				orden.step_end_time = str(datetime.datetime.now())
				orden.add_step("Paused", "Working on other orders")
				
				orden.step_start_time = str(datetime.datetime.now())           
				taquero.check_meat(orden,orden.meat,orden.toPrepare)
				manejo_ingredientes(lock,orden,50,1,taquero,False)
				time_slice = orden.current_total_time 
				time.sleep(time_slice)
				orden.ready = True

				orden.step_end_time = str(datetime.datetime.now())
				orden.add_step("Running", "Working on order")
				#print(orden.steps)

			elif taquero.min_priority.empty() == False:
				cocinar(lock,taquero,.8,taquero.min_priority,taquero.waiting)

def cocinar(lock,taquero,time_slice,start_priority,next_priority):
	orden = start_priority.get()

	if start_priority != taquero.max_priority:
		orden.step_start_time = orden.step_end_time
		orden.step_end_time = str(datetime.datetime.now())
		orden.add_step("Paused", "Working on other orders")

	orden.setTimeByType()
	toPrepare = orden.toPrepare
	how_many = time_slice//orden.time_by_type #cuantos de ese tipo puede hacer en ese time slice

	orden.step_start_time = str(datetime.datetime.now())

	if how_many < toPrepare:
		taquero.check_meat(orden,orden.meat,how_many)
		manejo_ingredientes(lock, orden, 50, 1, taquero, False)
		orden.toPrepare -= how_many

		##orden.steps.append("Paused") 
		time.sleep(time_slice)
		next_priority.put(orden)

		orden.step_end_time = str(datetime.datetime.now())
		orden.add_step("Running", "Working on order")
 
	else:
		taquero.check_meat(orden,orden.meat,toPrepare)
		manejo_ingredientes(lock, orden, 50, 1, taquero, False)

		time.sleep(orden.current_total_time)
		orden.ready = True

		orden.step_end_time = str(datetime.datetime.now())
		orden.add_step("Running", "Working on order")
		##print(orden.steps)

def main():
	threads = []
##    start = tiempo()
    
	taquero_uno = Taquero() #Asada, veggie
	taquero_uno.carnes["asada"]=50
	taquero_uno.carnes["veggie"]=50
	taquero_dos = Taquero() #Adobada, tripa
	taquero_dos.carnes["adobada"]=50
	taquero_dos.carnes["tripa"]=50
	taquero_tres = Taquero() #Lengua, cabeza, suadero
	taquero_tres.carnes["lengua"]=50
	taquero_tres.carnes["cabeza"]=50
	taquero_tres.carnes["suadero"]=50
	
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
		
	ingredientes = (1,2,3,4,5,6)
	
	def demo():
		plt.sca(axes[0, 0])
		ingredientes = ("cebolla","salsa","cilantro","frijoles","aguacate","tortillas")
		valores = [taquero_uno.ingredientes["Cebolla"],taquero_uno.ingredientes["Salsa"],taquero_uno.ingredientes["Cilantro"],taquero_uno.ingredientes["Frijoles"],taquero_uno.ingredientes["Guacamole"],taquero_uno.ingredientes["Tortillas"]]
		plt.bar(range(6),valores,align = "center",alpha = 0.5)
		plt.xticks(range(6), ingredientes,fontsize = 8)
		plt.yticks([100,200,300,400,500])
		plt.title("Ingredientes Taquero 1")

		plt.sca(axes[1,0])
		eje = ("Queue 1","Queue 2","Queue 3","Queue 4","Queue 5")
		valores_2 = [taquero_uno.max_priority.qsize(),taquero_uno.med_priority.qsize(),taquero_uno.low_priority.qsize(),taquero_uno.min_priority.qsize(),taquero_uno.waiting.qsize()]    
		plt.bar(range(5),valores_2,align = "center",alpha = 0.5)
		plt.xticks(range(6), eje,fontsize = 8)
		plt.yticks([5,10,15,20,25])
		plt.title("Queues Taquero 1")


		plt.sca(axes[0,1])
		valores_3 = [taquero_dos.ingredientes["Cebolla"],taquero_dos.ingredientes["Salsa"],taquero_dos.ingredientes["Cilantro"],taquero_dos.ingredientes["Frijoles"],taquero_dos.ingredientes["Guacamole"],taquero_dos.ingredientes["Tortillas"]]
		ingredientes_2 = ("cebolla","salsa","cilantro","frijoles","aguacate","tortillas")
		plt.bar(range(6),valores_3,align = "center",alpha = 0.5)
		plt.xticks(range(6), ingredientes_2,fontsize = 8)
		plt.yticks([100,200,300,400,500])
		plt.title("Ingredientes Taquero 2")

		plt.sca(axes[1,1])
		queues_2 = ("Queue 1","Queue 2","Queue 3","Queue 4","Queue 5")
		valores_4 = [taquero_dos.max_priority.qsize(),taquero_dos.med_priority.qsize(),taquero_dos.low_priority.qsize(),taquero_dos.min_priority.qsize(),taquero_dos.waiting.qsize()]
		plt.bar(range(5),valores_4,align = "center",alpha = 0.5)
		plt.xticks(range(6), queues_2,fontsize = 8)
		plt.yticks([5,10,15,20,25])
		plt.title("Queues Taquero 2")

		plt.sca(axes[0,2])
		valores_4 = [taquero_tres.ingredientes["Cebolla"],taquero_tres.ingredientes["Salsa"],taquero_tres.ingredientes["Cilantro"],taquero_tres.ingredientes["Frijoles"],taquero_tres.ingredientes["Guacamole"],taquero_tres.ingredientes["Tortillas"]]
		ingredientes_3 = ("cebolla","salsa","cilantro","frijoles","aguacate","tortillas")
		plt.bar(range(6),valores_4,align = "center",alpha = 0.5)
		plt.xticks(range(6), ingredientes_3,fontsize = 8)
		plt.yticks([100,200,300,400,500])
		plt.title("Ingredientes Taquero 3")

		plt.sca(axes[1,2])
		queues_3 = ("Queue 1","Queue 2","Queue 3","Queue 4","Queue 5")
		valores_5 = [taquero_tres.max_priority.qsize(),taquero_tres.med_priority.qsize(),taquero_tres.low_priority.qsize(),taquero_tres.min_priority.qsize(),taquero_tres.waiting.qsize()]
		plt.bar(range(5),valores_5,align = "center",alpha = 0.5)
		plt.xticks(range(6), queues_3,fontsize = 8)
		plt.yticks([5,10,15,20,25])
		plt.title("Queues Taquero 3")

        
	plt.ion()
	for i in range(10):
		fig, axes = plt.subplots(nrows=2, ncols=3,figsize=(12,6))
		demo()
		fig.tight_layout()
		plt.pause(1)
		plt.draw()
		if i != 9:
			plt.close()
  
main()
