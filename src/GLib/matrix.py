# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

class MatrixError(Exception):pass

class Matrix:
	'''класс для работы с матрицами'''
	
	def __init__(self,m=None,vcol=None,vrow=None):
		'''конструктор принимает либо двухмерную матрицу m
		либо матрицу столбец vcol
		либо матрицу строку vrow
		либо создает пустую матрицу нулевой размерности'''
		self.__m=m if m else [[i,] for i in vcol] if vcol else [[i for i in vrow],] if vrow else []
		
	def set(self,m):
		'''устанавливает двумерную матрицу'''
		self.__m=m
		
	def get(self):
		'''возвращает матрицу'''
		return self.__m
		
	def getList(self):
		'''возвращает список элементов 
		где первее элемент с меньшей строкой
		иначе с меньшим столбцом'''
		return [j for i in self.__m for j in i]
		
	def getRadius(self):
		'''возвращает корень из суммы квадратов элементов
		т.е. для матриц столбцов,строк возвращает длину вектора'''
		return sum(map(lambda x:x**2,self.getList()))**0.5
		
	def len(self):
		'''возвращает кортеж (количество строк,количество столбцов)'''
		return (len(self.__m),len(self.__m[0]))
		
	def __abs__(self):
		'''возвращает детерминант матрицы'''
		return self.det()
	
	def det(self,m=None):
		'''возвращает детерминант матрицы
		если не указан m то для текущей'''
		m=m if m else self.get()
		n=len(m)
		return sum([(-1)**l*m[0][l]*self.det([[m[i][j] for j in range(n) if j!=l] for i in range(1,n)]) if n>1 else (-1)**l*m[0][0] for l in range(n)])
		
	def trans(self):
		'''возвращает новую матрицу после транспонирования текущей матрицы'''
		return Matrix(list(zip(*self.get())))
		
	def ematrix(self,n=None):
		'''возвращает новую единичную матрицу
		если указан n то nxn иначе
		mxm где m количество строк в текущей матрице'''
		n=n if n else self.len()[0]
		return Matrix([[1 if i==j else 0 for j in range(n)] for i in range(n)])
		
	def _con(self):
		'''возвращает новую присоединненую матрицу'''
		m=self.get()
		n=self.len()[0]
		c=[[(-1)**(i+j)*self.det([[m[i1][j1] for j1 in range(n) if j!=j1] for i1 in range(n) if i!=i1]) for j in range(n)] for i in range(n)] if n>1 else [[m[0][0]]]
		return Matrix(c)
		
	def __str__(self):
		'''возвращает строковое представление данной матрицы'''
		return '\n'.join([' '.join([str(j) for j in i]) for i in self.get()])
		
	def __round__(self,k):
		'''возвращает матрицу с округлеными до k элементами текущей матрицы'''
		return Matrix([[round(j,k) for j in i] for i in self.get()])
		
	def __lshift__(self,k):
		'''возвращает матрицу с элементами текущей домноженными на число k'''
		return Matrix([[j*k for j in i] for i in self.get()])
		
	def __rshift__(self,k):
		'''возвращает матрицу с элементами текущей поделенными на число k'''
		return Matrix([[j/k for j in i] for i in self.get()])
		
	def __mul__(self,other):
		'''возвращает матрицу произведения матриц self и other
		возбуждает исключение MatrixError если матрицы нельзя перемножить'''
		m=self.get()
		b=other.get()
		n=self.len()
		n1=other.len()
		if n1[0]!=n[1]:raise MatrixError
		return Matrix([[sum([m[i][l]*b[l][j] for l in range(n1[0])]) for j in range(n1[1])] for i in range(n[0])])
		
	def __invert__(self):
		'''возвращает матрицу обратную текущей'''
		return self._con().trans()>>self.det()
		
	def __truediv__(self,other):
		'''возвращает матрицу деления матрицы self на other'''
		return self*~other
		
	def format(self,n1=None,n2=None,empty_element=0):
		'''возвращет отформатированую матрицу размера n1xn2
		где недостающие элементы заполняются empty_element'''
		m=self.get()
		n=self.len()
		n1,n2=n1 if n1 else n[0],n2 if n2 else n[1]
		return Matrix([[m[i][j] if i<n[0] and j<n[1] else empty_element for j in range(n2)] for i in range(n1)])
		
	def __add__(self,other):
		'''возврашает сумму матриц self,other'''
		return self.__sum(other)
	
	def __sub__(self,other):
		'''возврашает разность матриц self,other'''
		return self.__sum(other,-1)
	
	def __sum(self,other,sign=1):
		'''возврашает сумму со знаком sign матриц self,other'''
		n=tuple(map(max,self.len(),other.len()))
		m=self.format(*n).get()
		m1=other.format(*n).get()
		return Matrix([[m[i][j]+m1[i][j]*sign for j in range(n[1])] for i in range(n[0])])
		
		
