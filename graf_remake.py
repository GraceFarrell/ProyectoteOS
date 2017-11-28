import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk as Ttk
import matplotlib.pyplot as plt

class Taqueria:
	def __init__(self):
        	self.cliente = []
		self.numero_clientes = 0

	def addCliente(self,cliente):
		self.clientes.append(cliente)
		self.numero_clientes += 1

    	def getClientes(self):
        	return self.numero_clientes

    	def getMeats(self, orden):
        	dict_meat = {"asada":0,"adobada":0,"cabeza":0, "lengua":0, "suadero":0, "veggie":0,"tripa":0}
		for meats in dict_meat.keys():
			if meats == orden.meat:
				dict_meat[meats] += orden.quantity
	
       		total_meat = sum(dict_meat.values())
		return dict_meat, total_meat

	def getTipos(self, orden):
		dict_tipo = {"taco":0,"quesadilla":0,"mulita":0,"tostada":0,"vampiro":0,"taco":0,"orden":0}
		for tipos in dict_tipo.keys():
			if tipos == orden.typee:
				dict_tipo[tipos] += orden.quantity
	
       		total_tipos = sum(dict_tipo.values())
		return dict_tipo, total_tipos










