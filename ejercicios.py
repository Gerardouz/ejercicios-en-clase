#invertir lista: https://repl.it/X3G/4160
#eliminar la mitad de la lista: https://repl.it/X3G/4161
#verificar si hay numeros repetidos en la lista: https://repl.it/X3G/4162
#saber si dos listas son iguales: https://repl.it/X3G/4163
#sumar los elementos de una lista multitipo: https://repl.it/X3G/4164
#saber si los elementos de una lista son consecutivos o no: https://repl.it/X3G/4471
#eliminar numeros repetidos: https://repl.it/X3G/4276


# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
	
	# Metodo para vaciar la lista 
	def vacia_lista(self):
		
		num = self.__n
		for i in range(num):
			self.elimina_primero()

	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		
		nodo = self.__primero
		for i in range (self.__n):
			if (i == self.__pos):
				print "(",nodo.info,")", 
			else: 
				print nodo.info, 
			nodo=nodo.sig	
	
	# Metodo para eliminar el primer elemento de la lista
	def eliminar_prim(self):
		
		if (self.__primero == None):
			return
		h = self.__primero
		self.__primero = h.sig
		if (self.__actual == h):

		
			self.__actual = h.sig

			
		if (self.__ultimo == h):
			
			self.__ultimo = h.sig
		del h
		self.__n = self.__n - 1
		self.__pos = self.__pos - 1


	# Metodo para invertir la lista

	def invertir_lista(self):
		l = []
		nodo = self.__primero
		while(nodo != None):
			l.append(nodo.info)
			nodo = nodo.sig
			self.eliminar_prim()
		for i in l:
			self.insertar_inicio(i)

	# Metodo para eliminar la mitad de una lista

	def eliminar_mitad(self):

		if (self.__primero == None):
			return
		h = self.__n / 2

		for i in range(h):
			self.eliminar_prim()

	# Metodo para verificar si hay numeros repetidos en la lista

	def numeros_repetidos(self):

		nodo = self.__primero

		cont = 0

		while (nodo != None):

			valor = nodo.sig
			while (valor != None):

				if (nodo.info == valor.info):

					cont = cont + 1

				valor = valor.sig

			nodo = nodo.sig

		if (cont > 0):

			return True

		if (cont == 0):

			return False

	# Metodo para consultar la cantidad de elementos de una lista

	def consultar_n(self):

		return self.__n

	# Metodo para saber si dos listas son iguales

	def listas_iguales(self,lista):


		if (self.__n != lista.consultar_n() ):

			return False

		nodo1 = self.__primero
		nodo2 = lista.__primero
		cont = 0

		while (nodo1 != None and nodo2 != None):

			if (nodo1.info != nodo2.info):
				return False

			nodo1 = nodo1.sig
			nodo2 = nodo2.sig

		return True

	# Metodo para sumar los elementos de una lista multitipo

	def sumar_lista(self):

		suma = 0

		nodo = self.__primero

		while (nodo != None):

			if (type(nodo.info) == int):

				suma = suma + nodo.info

			nodo = nodo.sig

		return suma
		
	def elem_consecutivos(self):

		nodo = self.__primero
		cont = self.__primero.sig

		while (nodo != None):

			for i in range(self.__n-1):

				if (nodo > cont):

					return False

				nodo = nodo.sig

		return True
		
	def eliminar_numerosR(self):

		nodo = self.__primero

		while (nodo != None):

			valor = nodo.sig

			while (valor != None):

				if(nodo.info == valor.info):

					self.eliminar_numeroR2(nodo.info)

				valor = valor.sig

			nodo = nodo.sig


	def eliminar_numeroR2(self,valor):


		while (self.__primero != None and self.__primero.info == valor):

			temp = self.__primero

			self.__primero = temp.sig

			if(self.__primero == self.__actual):

				self.__actual = self.__primero

			self.__n = self.__n - 1
			self.__pos = self.__pos - 1
			del temp

			if (self.__primero == self.__ultimo):

				self.__primero = None
				self.__ultimo = None
				self.__actual = None

		nodo = self.__primero

		while (nodo != None):

			while (nodo.sig != None and nodo.sig.info == valor):

				temp = nodo.sig

				if (nodo.sig == self.__ultimo):
					self.__ultimo = nodo

				nodo.sig = temp.sig

				if (nodo.sig == self.__actual):

					self.__actual = temp.sig

				self.__n = self.__n - 1
				self.__pos = self.__pos - 1

				del temp

			nodo = nodo.sig

