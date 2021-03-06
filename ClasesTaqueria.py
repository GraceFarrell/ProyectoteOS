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
		self.ingredientes = {"Cebolla":500,"Salsa":500,"Cilantro":500,"Frijoles":500,"Guacamole":500,"Tortillas":500}
		self.carnes = {}

	def check_meat(self,orden,meat,how_many):
		if self.carnes[meat] < 50:
			self.carnes[meat] += 5
			time.sleep(1)

			orden.step_end_time = str(datetime.datetime.now())
			orden.add_step("On standby", "Preparing meat")
			orden.step_start_time = str(datetime.datetime.now())

		self.carnes[meat] -= how_many

class Orden:
	def __init__(self,part_id,typee,meat,quantity,ingredients):
		self.part_id = part_id
		self.typee = typee.lower()
		self.meat = meat.lower()
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
			return .1
		elif self.typee == "quesadilla":
			return .3
		elif self.typee == "mulita":
			return .3
		elif self.typee == "tostada":
			return .2
		elif self.typee == "vampiro":
			return .3
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
 
class Cliente:
	def __init__(self,date,idd,ordenes):
		self.date=date
		self.idd=idd
		self.numero_ordenes = 0 
		self.ordenes = self.addOrden(ordenes)
		self.orden = {}
		self.answer = {"start_time":"","end_time":"","steps":""}
		self.receipt = ""

	def addOrden(self,orden):
		ordenes = []
		for i in range (len(orden)):
			no = Orden(orden[i]["part_id"],orden[i]["type"],orden[i]["meat"],orden[i]["quantity"],orden[i]["ingredients"])
			self.numero_ordenes += 1
			ordenes.append(no)
		return ordenes

	def getAnswer(self):
		start_times = []
		end_times = []
		for orden in self.ordenes:
			for step in orden.steps:
				start_times.append(step["start_time"])
				end_times.append(step["end_time"])		
		self.answer["start_time"] = min(start_times)
		self.answer["end_time"] = max(end_times)
		self.answer["steps"] = self.getSteps()
		self.orden["answer"] = self.answer
		return self.orden

	def getOrdenesSize(self):
		return self.numero_ordenes

	def getOrdenes(self):
		return self.ordenes

	def getSteps(self):
		total_steps = []
		for orden in self.ordenes:
			total_steps.extend(orden.steps)
		return total_steps
				
	def getStartTime(self):
		start_times = []
		end_times = []
		for orden in self.ordenes:
			for step in orden.steps:
				start_times.append(step["start_time"])
				end_times.append(step["end_time"])		
		start_time = min(start_times)
		end_time = max(end_times)
		return start_time, end_time

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
