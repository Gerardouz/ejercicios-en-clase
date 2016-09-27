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
	# Metodo para intercambiar los valores de un nodo y el nodo de una posición dada por parametro
	def intercambiar(self,nodo,pos):

		if (nodo == None):
			return
		if (pos >= self.__n):
			self.intercambiar(nodo,self.__n - 1)
			return
		n = self.__primero
		cont = 0
		while (n != None):

			if (cont == pos):

				h = nodo.info
				nodo.info = n.info
				n.info = h
				del h
				return

			cont = cont + 1
			n = n.sig
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
	#Metodo que retorna el mayor elemento de una lista
	def encontrar_mayor(self):


		nodo = self.__primero
		mayor = self.__primero.info
		while (nodo != None):

			if (nodo.sig != None and mayor < nodo.sig.info):


				mayor = nodo.sig.info

			nodo = nodo.sig
		return mayor
	# Metodo para consultar la cantidad de elementos de una lista

	def consulta_n(self):

		return self.__n

	# Metodo para saber si dos listas son iguales

	def listas_iguales(self,lista):


		if (self.__n != lista.consulta_n() ):

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
	# Metodo para saber si una lista tiene sus elementos consecutivos (ascendiente)
	def consecutivos_asc(self):

		nodo = self.__primero

		while (nodo != None):
			siguiente = nodo.sig

			if (siguiente == None):

				return True
			if (nodo.info > siguiente.info):

				return False
			nodo = nodo.sig

		return True
	#Metodo para saber si una lista tiene sus elementos consecutivos (descendiente)
	def consecutivos_desc(self):

		nodo = self.__primero

		while (nodo != None):

			siguiente = nodo.sig

			if (siguiente == None):

				return True

			if (nodo.info < siguiente.info):

				return False

			nodo = nodo.sig
	#Metodo para eliminar los numeros repetidos
		
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
			
	# Metodo para mezclar dos listas ordenadas 
	def mezclar(self,l):

		l1 = self.__n
		l2 = l.consulta_n()

		i = 0
		j = 0
		c = Lista()

		while (i < l1 and j < l2):

			if (self.return_elem(i) < l.return_elem(j) ):

				c.insertar_ultimo(self.return_elem(i))
				i = i + 1

			else:

				c.insertar_ultimo(l.return_elem(j))
				j = j + 1

		while (i < l1):

			c.insertar_ultimo(self.return_elem(i))
			i = i + 1
		while (j < l2):

			c.insertar_ultimo(l.return_elem(j))
			j = j + 1

		return c.mostrar()
	
	#Metodo que retorna el elemento que esté en la posición dada por parametro
	def return_elem(self,pos):

		nodo = self.__primero
		cont = 0
		while (nodo != None):

			if (cont == pos):

				return nodo.info

			nodo = nodo.sig
			cont = cont + 1
			
			
	#Metodo para ordenar la lista a traves del metodo burbuja
	def ordenar(self):

		nodo = self.__primero
		ordenado = False
		cont = 0
		while (ordenado == False):
			


			if (nodo.sig == None):
				nodo = self.__primero
				cont = 0

			
			if (nodo.info > nodo.sig.info):

				self.intercambiar(nodo,cont + 1)
				

			if (self.consecutivos_asc() == True):
				ordenado = True
				return

			

			nodo = nodo.sig
			cont = cont + 1
	

