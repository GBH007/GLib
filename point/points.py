# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
class Point:
	'''класс точка'''
	
	def __init__(self,cord=None,sign=('x','y','z')):
		'''конструктор принимает
		кортеж координат cord 
		текстовые наименование осей координат sign'''
		self.__cord=tuple(cord) if cord else tuple()
		self.__sign=sign
		
	def getCord(self):
		'''возвращает кортеж координат'''
		return self.__cord
	
	def setLinkedCord(self,cord):
		'''устанавливает новые координаты через ссылку'''
		self.__cord=cord
	
	def setCord(self,cord):
		'''устанавливает новые координаты через копирование'''
		self.__cord=tuple(cord)
	
	def getSign(self):
		'''возвращат наименования осей координат'''
		return self.__sign if self.__sign else ['' for i in self.__cord]
	
	def setSign(self,sign):
		'''устанавливает наименования осей координат через ссылку'''
		self.__sign=sign
	
	def radius(self,other):
		'''возврашает расстояние между точками self,other'''
		return sum(map(lambda *x: (x[0]-x[1])**2,self.getCord(),other.getCord()))**0.5
		
	def __eq__(self,other):
		'''возвращает истину если координаты точек равны лож иначе'''
		return not sum(map(lambda *x: x[0]!=x[1],self.getCord(),other.getCord()))	#rewrite
		
	def __add__(self,other):
		'''возвращает точку результат суммы координат точек self,other'''
		cord1,cord2=self.stab(other)
		cord=tuple(map(lambda *x: x[0]+x[1],cord1,cord2))
		return Point(cord=cord)
		
	def max(self,other):
		'''возвращает точку с набором максимальных координат из self,other'''
		cord1,cord2=self.stab(other)
		cord=tuple(map(max,cord1,cord2))
		return Point(cord=cord)
		
	def min(self,other):
		'''возвращает точку с набором минимальных координат из self,other'''
		cord1,cord2=self.stab(other)
		cord=tuple(map(min,cord1,cord2)) #rewrite
		return Point(cord=cord)
		
	def stab(self,other):	#rewrite
		'''возвращает кортеж из координат self,other дозаполненых нулями'''
		cord1=self.getCord()
		cord2=other.getCord()
		l1=len(cord1)
		l2=len(cord2)
		n=max(l1,l2)
		cord1+=tuple([0 for i in range(n-l1)])
		cord2+=tuple([0 for i in range(n-l2)])
		return cord1,cord2
		
	def __sub__(self,other):
		'''возвращает точку результат разности координат точек self,other'''
		cord1,cord2=self.stab(other)
		cord=tuple(map(lambda *x: x[0]-x[1],cord1,cord2)) #rewrite
		return Point(cord=cord)
		
	def __mul__(self,other):
		'''возвращает точку результат произведения координат точек self,other'''
		cord1,cord2=self.stab(other)
		return sum(map(lambda *x: x[0]*x[1],cord1,cord2)) #rewrite
		
	def __pow__(self,k):
		'''возвращает точку результат возведения в степень k текущих координат'''
		return Point(cord=tuple(map(lambda x: x**k,self.getCord())))
		
	def __lshift__(self,k):
		'''возвращает точку результат умножения на k текущих координат'''
		return Point(cord=tuple(map(lambda x: x*k,self.getCord())))
		
	def __rshift__(self,k):
		'''возвращает точку результат деления на k текущих координат'''
		return Point(cord=tuple(map(lambda x: x/k,self.getCord())))
		
	def __repr__(self):
		'''возврашает строку грубого отображения точки'''
		return 'Point {0}{1}'.format(self.getCord(),self.getSign())
		
	def __getitem__(self,key):
		'''возврашает значение координаты по индексу'''
		try:
			return self.__cord[key]
		except IndexError:
			return 0
			
	def __str__(self):
		'''возврашает строку отображения точки'''
		return ' , '.join(map(lambda x,s:'{1}={0}'.format(x,s),self.getCord(),self.getSign()))
		
	def __len__(self):
		'''возврашает число координат'''
		return len(self.__cord)
		
class Points:
	'''класс набор точек'''
	
	def __init__(self,sign=('x','y','z')):
		'''конструктор принимает
		текстовые наименование осей координат sign'''
		self.__points=[]		#i[0] - Point obj i[1] - n i[0]
		self.__sign=sign
		
	def getSign(self):
		'''возвращат наименования осей координат'''
		return self.__sign
	
	def setSign(self,sign):
		'''устанавливает наименования осей координат через ссылку'''
		self.__sign=sign
	
	def __contains__(self,point):
		'''проверяет вхождение (наличие) точки в набор'''
		for i,n in self.__points:
			if i==point:return True
		return False
		
	def __getitem__(self,point):
		'''возвращает кортеж точка,количество вхождений
		принимает точку'''
		for i in self.__points:
			if i[0]==point:return i
		return None
		
	def __setitem__(self,point,n):
		'''устанавливает точке point количество вхождений n в набор'''
		for i in self.__points:
			if i[0]==point:
				i[1]=n
				break
				
	def __delitem__(self,point):
		'''уменьшает количество вхождений точки point в набор на 1
		если количество становится равным 0 то удаляет точку из набора'''
		for i in self.__points:
			if i[0]==point:
				i[1]-=1
				if i[1]<1:self.__points.remove(i)
				
	def add(self,cord,num=1):
		'''добавляет точку с координатами cord в набор увеличивая
		число вхождений на num'''
		p=Point(cord=cord,sign=self.__sign)
		if p in self:
			self[p]=self[p][1]+num
		else:
			self.__points.append([p,num])
		return p
		
	def remove(self,point):
		'''уменьшает количество вхождений точки point в набор на 1
		если количество становится равным 0 то удаляет точку из набора'''
		del self[point]
		
	def initialMoment(self,k=1):
		'''возвращает начальный момент k порядка для набора точек
		без аргументов возвращает математическое ожидание набора'''
		m=Point()
		n=0
		for i in self.__points:
			m+=(i[0]**k)<<i[1]
			n+=i[1]
		if n:
			m>>=n
		return m
		
	def min(self):
		'''возвращает точку с набором минимальных координат из набора'''
		m=self.__points[0][0]
		for i in self.__points:
			m=m.min(i[0])
		return m
		
	def minN(self):
		'''возвращает точку с набором минимальных координат из набора
		последней координатой идет минимальное количество вхождений'''
		n=self.__points[0][1]
		for i in self.__points:
			n=min(i[1],n)
		m=self.min()
		m.setCord(m.getCord()+(n,))
		return m
		
	def max(self):
		'''возвращает точку с набором максимальных координат из набора'''
		m=self.__points[0][0]
		for i in self.__points:
			m=m.max(i[0])
		return m
		
	def maxN(self):
		'''возвращает точку с набором максимальных координат из набора
		последней координатой идет максимальное количество вхождений'''
		n=self.__points[0][1]
		for i in self.__points:
			n=max(i[1],n)
		m=self.max()
		m.setCord(m.getCord()+(n,))
		return m
		
	def centralMoment(self,k=2):
		'''возвращает центральный момент k порядка для набора точек
		без аргументов возвращает дисперсию'''
		m=self.initialMoment()
		n=0
		s=Point()
		for i in self.__points:
			s+=((i[0]-m)**k)<<i[1]
			n+=i[1]
		if n:
			s>>=n
		return s
		
	def toPlot(self,axis):
		'''возвращает список с кортежами координат (точек) с номерами из axis'''
		s=[]
		for i in self.__points:
			s.append([i[0][j] for j in axis])
		return s
		
	def toGist(self,axis):
		'''возвращает список с кортежами 
		координата (точки) с номерам axis,количество вхождений (точки)'''
		s=[]
		for i in self.__points:
			s.append([i[0][axis],i[1]])
		return s
		
	def getMinDc(self,axis):
		'''возврашает минимальное расстояние по координате axis в наборе'''
		m=self.__points[1][0][axis]-self.__points[0][0][axis]
		n=len(self)
		for i in range(2,n):
			if self.__points[i][0][axis]-self.__points[i-1][0][axis]<m:
				m=self.__points[i][0][axis]-self.__points[i-1][0][axis]
		return m
		
	def sort(self,axis=0):
		'''сортирует набор по координате axis (в порядке неубывания)'''
		self.__points.sort(key=lambda e:e[axis])
		
	def __len__(self):
		'''возвращает длину набора'''
		return len(self.__points)
		
	def __iter__(self):
		'''возвращает итератор набора'''
		return iter(self.__points)
		
	def __str__(self):
		'''возвращает строковое представление набора'''
		return '\n'.join(map(str,self.__points))
		
def main():
	#~ p1=Point((0,0))
	#~ p11=Point((0,0))
	#~ p2=Point((3,4))
	#~ p3=Point()
	#~ p3+=p2
	#~ p3<<=2
	#~ print(p3[4])
	#~ print(p3>>5)
	p=Points()
	f=lambda x: x**2
	for i in range(-20,20):
		p.add((i,f(i)))
	#~ p.add((0,1),1)
	#~ p.add((0,14),3)
	#~ p.add((-2,8),7)
	#~ p1=p.add((-4,17))
	#~ print(p)
	#~ print(p.initialMoment())
	#~ print(p.centralMoment())
	#~ print(p.min())
	#~ print(p.max())
def main2():
	import random
	p=Points()
	for i in range(10000):
		p.add((round(random.normalvariate(0,0.1),2),))
	print(p.initialMoment())

if __name__=='__main__':
	main2()
