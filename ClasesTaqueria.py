import time
import datetime
from queue import Queue

class Taquero:
	def __init__(self):
		self.max_priority = Queue()
		self.med_priority = Queue()
		self.low_priority = Queue()
		self.min_priority = Queue()
		self.waiting = Queue()
		self.ingredientes = {"cebolla":500,"salsa":500,"cilantro":500,"frijoles":500,"guacamole":500,"tortillas":500}
		self.carnes = {}

	def check_meat(self,orden,meat,how_many):
		if self.carnes[meat] < 50:
			self.carnes[meat] += 5
			time.sleep(1)

			orden.step_end_time = str(datetime.datetime.now())
			orden.add_step("On standby", "Preparing meat")
			orden.step_start_time = str(datetime.datetime.now())

		self.carnes[meat] -= how_many

class Taqueria:
    	def __init__(self):
        	self.clientes = []
        	self.numero_clientes= 0 

    	def addCliente(self):
        	self.numero_clientes += 1

    	def getClientes(self):
        	return self.numero_clientes

class Orden:
	def __init__(self,part_id,typee,meat,quantity,ingredients):
		self.part_id = part_id
		self.typee = typee
		self.meat = meat
		self.quantity = quantity
		self.ingredients = ingredients
		self.ready = False
		self.toPrepare = self.quantity
		self.time_by_type = self.setTimeByType()
		self.current_total_time = self.time_by_type * self.toPrepare
		self.step_start_time = 0
		self.step_end_time = 0
		self.current_step = 1
		self.steps = [] #Lista de pasos de la suborden

	def add_step(self,state,action):
		step = {}
		step["step"] = self.current_step
		self.current_step += 1
		step["state"] = state
		step["action"] = action
		step["part_id"] = self.part_id
		step["start_time"] = self.step_start_time
		step["end_time"] = self.step_end_time
		self.steps.append(step)

	def getType(self):
		return self.typee
	
	def getMeat(self):
		return self.meat

	def setTimeByType(self):
		if self.typee == "taco":
			return 1
		elif self.typee == "quesadilla":
			return 3
		elif self.typee == "mulita":
			return 3
		elif self.typee == "tostada":
			return 2
		elif self.typee == "vampiro":
			return 3
		elif self.typee == "orden":
			return self.toPrepare

	def getQuantity(self):
		return self.quantity

	def String(self):
		return "part_id:{0}\n typee:{1}\n meat:{2}\n quantity:{3}\n ingredients:{4}\n".format(self.part_id,self.typee,self.meat,self.quantity,self.ingredients)

	def __str__(self):
		return "part_id:{0}\n typee:{1}\n meat:{2}\n quantity:{3}\n ingredients:{4}\n".format(self.part_id,self.typee,self.meat,self.quantity,self.ingredients)

	def __iter__(self):
		return self

	def getSteps(self):
		for step in self.steps:
			print(step)
 
class Cliente:
	def __init__(self,date,idd,ordenes):
		self.date=date
		self.idd=idd
		self.numero_ordenes = 0
		self.ordenes = self.addOrden(ordenes)
		self.answer = {"start_time":"","end_time":""}

	def addOrden(self,orden):
		ordenes = []
		for i in range (len(orden)):
			no = Orden(orden[i]["part_id"],orden[i]["type"],orden[i]["meat"],orden[i]["quantity"],orden[i]["ingredients"])
			self.numero_ordenes += 1
			ordenes.append(no)
		return ordenes

	def getOrdenesSize(self):
		return self.numero_ordenes

	def getOrdenes(self):
		return self.ordenes

	def getSteps(self):
		for orden in self.ordenes:
			for step in orden.steps:
				print(step)

	def getCompletado(self):
		temp = 0
		for orden in self.ordenes:
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
