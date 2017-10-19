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

LARGE_FONT=("Verdana", 12)

class Orden:
    def __init__(self,date,idd,part_id,typee,meat,quantity,ingredients):
        self.date = date
        self.idd = idd
        self.part_id = part_id
        self.typee = typee
        self.meat=meat
        self.quantity = quantity
        self.ingredients = ingredients
    def __str__(self):
        return "datetime:{0}\n request_id:{1}\n part_id:{2}\n typee:{3}\n meat:{4}\n quantity:{5}\n ingredients:{6}\n".format(self.date,self.idd,self.part_id,self.typee,self.meat,self.quantity,self.ingredients)
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
		message.append
		print(message['Body'])
		message_string = message['Body']

	for r in recibos:
		response = sqs.delete_message(QueueURL='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team2',ReceiptHandle=r)

	return Take_Orders(message_string)

#inbound_Order = str({"datetime": "2017-01-01 23:23:23", "request_id": "123-123-123",
#               "orden": [ { "part_id": "123-111",  "type": "taco", "meat": "asada", "quantity": 3, "ingredients": [ "cebolla", "salsa"] },
#                          { "part_id": "123-222", "type": "mulita", "meat": "asada", "quantity": 1, "ingredients": []  },
#                          { "part_id": "123-333", "type": "quesadilla", "meat": "adobada", "quantity": 2, "ingredients": ["cebolla", "aguacate", "salsa"]} ]})

#data = Take_Orders(inbound_Order)
#print(data)

sqs = boto3.client('sqs')
data = Recieve_Orders(sqs)

ordeness=[]
threads=[]
ordenes_aws=[data]
       
def MakeOrder(date,idd,ordenes):
    for i in range (len(ordenes)):
        x = ordenes[i]["part_id"]
        typee = ordenes[i]["type"]
        meat = ordenes[i]["meat"]
        quantity = ordenes[i]["quantity"]
        ingredients = ordenes[i]["ingredients"]
        no = Orden(date,idd,x,typee,meat,quantity,ingredients)
        ordeness.append(no)
        
def MakeThreads(ordenes_aws):
    for data in ordenes_aws:
        date = data["datetime"]
        request_id = data["request_id"]
        ordenes = data["orden"]
        thread = Thread(target=MakeOrder,args=(date,request_id,ordenes))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()
        
MakeThreads(ordenes_aws)

for i in ordeness:
    print (i)

class Frank(tk.Tk):	

	def __init__(self, ordeness, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.wm_title(self, "Graficas")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)

		ordeness = ordeness

		self.frames = {}
		
		frame = Inicio(container, self)
		self.frames[Inicio] = frame
		frame.grid(row=0, column=0, sticky="nsew")


		for F in (Grafica1, Grafica2, Tabla):
			frame = F(container, self, ordeness)
			self.frames[F] = frame 
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(Inicio)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class Inicio(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Inicio", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button = Ttk.Button(self, text="Grafica 1", command=lambda: controller.show_frame(Grafica1))
		button.pack()

		button3 = Ttk.Button(self, text="Grafica 2", command=lambda: controller.show_frame(Grafica2))
		button3.pack()

		button4 = Ttk.Button(self, text="Tabla", command=lambda: controller.show_frame(Tabla))
		button4.pack()

class Grafica1(tk.Frame):

	def __init__(self, parent, controller, ordeness):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Grafica 1", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = Ttk.Button(self, text="Inicio", command=lambda: controller.show_frame(Inicio))
		button1.pack()

		f = Figure(figsize=(6,6), dpi=100)
		a = f.add_subplot(111)
	
		tipos = []
		slices = []

		taco=["Taco"]
		quesadilla=["Quesadilla"]
		mulita=["Mulita"]
		tostada=["Tostada"]
		vampiro=["Vampiro"]
		orden=["Orden"]

		Tipos = [taco, quesadilla, mulita, tostada, vampiro, orden]

		for i in ordeness:
			if i.typee == "taco":
				taco.append(i.quantity)

			elif i.typee == "quesadilla":
				quesadilla.append(i.quantity)

			elif i.typee == "mulita":
				mulita.append(i.quantity)

			elif i.typee == "tostada":
				tostada.append(i.quantity)

			elif i.typee == "vampiro":
				vampiro.append(i.quantity)

			elif i.typee == "orden":
				orden.append(i.quantity)

		total = sum(taco[:0:-1]+quesadilla[:0:-1]+mulita[:0:-1]+tostada[:0:-1]+vampiro[:0:-1]+orden[:0:-1])

		for i in Tipos:
			amount = sum(i[:0:-1])
			if amount != 0:
				tipos.append(i[0])
				slices.append((amount*100)/total)


		a.pie(slices, labels=tipos, startangle=90, autopct='%1.1f%%')

		canvas = FigureCanvasTkAgg(f, self)
		canvas.show
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class Grafica2(tk.Frame):

	def __init__(self, parent, controller, ordeness):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Grafica 2", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button2 = Ttk.Button(self, text="Inicio", command=lambda: controller.show_frame(Inicio))
		button2.pack()

		f = Figure(figsize=(6,6), dpi=100)
		a = f.add_subplot(111)
		
		carne = []
		slices = []

		asada=["Asada"]
		adobada=["Adobada"]
		cabeza=["Cabeza"]
		lengua=["Lengua"]
		suadero=["Suadero"]
		veggie=["Veggie"]
		tripa=["Tripa"]

		carnes = [asada,adobada,cabeza,lengua,suadero,veggie,tripa]

		for i in ordeness:
			if i.meat == "asada":
				asada.append(i.quantity)

			elif i.meat == "adobada":
				adobada.append(i.quantity)

			elif i.meat == "cabeza":
				cabeza.append(i.quantity)

			elif i.meat == "lengua":
				lengua.append(i.quantity)

			elif i.meat == "suadero":
				suadero.append(i.quantity)

			elif i.meat == "veggie":
				veggie.append(i.quantity)

			elif i.meat == "tripa":
				tripa.append(i.quantity)

		total = sum(asada[:0:-1]+adobada[:0:-1]+cabeza[:0:-1]+lengua[:0:-1]+suadero[:0:-1]+veggie[:0:-1]+tripa[:0:-1])

		for i in carnes:
			amount = sum(i[:0:-1])
			if amount != 0:
				carne.append(i[0])
				slices.append((amount*100)/total)

		a.pie(slices, labels=carne, startangle=90, autopct='%1.1f%%')

		canvas = FigureCanvasTkAgg(f, self)
		canvas.show
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

class Tabla(tk.Frame):

	def __init__(self, parent, controller, ordeness):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Tabla", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button5 = Ttk.Button(self, text="Inicio", command=lambda: controller.show_frame(Inicio))
		button5.pack()

		f = Figure(figsize=(6,6), dpi=100)
		a = f.add_subplot(111)

		asada=["Asada"]
		adobada=["Adobada"]
		cabeza=["Cabeza"]
		lengua=["Lengua"]
		suadero=["Suadero"]
		veggie=["Veggie"]
		tripa=["Tripa"]

		carnes = [asada,adobada,cabeza,lengua,suadero,veggie,tripa]

		for i in ordeness:
			if i.meat == "asada":
				asada.append(i.quantity)

			elif i.meat == "adobada":
				adobada.append(i.quantity)

			elif i.meat == "cabeza":
				cabeza.append(i.quantity)

			elif i.meat == "lengua":
				lengua.append(i.quantity)

			elif i.meat == "suadero":
				suadero.append(i.quantity)

			elif i.meat == "veggie":
				veggie.append(i.quantity)

			elif i.meat == "tripa":
				tripa.append(i.quantity)

		columns = ['Cantidad']
		rows = ['Asada','Adobada','Cabeza','Lengua','Suadero','Veggie','Tripa']
		data_list = []
		for i in carnes:
			amount = [sum(i[:0:-1])]
			data_list.append(amount)
		
		a.table(cellText=data_list, colLabels=columns, rowLabels=rows, loc="upper center")

		a.axis("off")
		
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

app = Frank(ordeness)
app.mainloop()

