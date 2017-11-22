from queue import Queue

class Taquero:
	def __init__(self):
		self.max_priority = Queue()
		self.med_priority = Queue()
		self.low_priority = Queue()
		self.min_priority = Queue()
		self.waiting = Queue()
		self.ingredientes = {"cebolla":500,"salsa":500,"cilantro":500,"frijoles":500,"aguacate":500}

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
		self.meat=meat
		self.quantity = quantity
		self.ingredients = ingredients
		self.ready = False
		self.time_by_type = 0
		self.toPrepare = self.quantity
		self.current_total_time = self.time_by_type * self.toPrepare
	def getType(self):
		return self.type	
	def getMeat(self):
		return self.meat
	def setTimeByType(self):
		if self.getType == "taco":
			self.time_by_type = 1
		elif self.getType == "quesadilla":
			self.time_by_type = 3
		elif self.getType == "mulita":
			self.time_by_type = 3
		elif self.getType == "tostada":
			self.time_by_type = 2
		elif self.getType == "vampiro":
			self.time_by_type = 3
		elif self.getType == "orden":
			self.time_by_type = self.toPrepare-1
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
        	return ordenes
    	def getOrdenesSize(self):
        	return self.numero_ordenes
    	def getOrdenes(self):
        	return self.ordenes
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
