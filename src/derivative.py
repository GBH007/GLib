# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
from .matrix import Matrix

__all__=['Function']

class Function:
	'''класс для работы с численными производными'''
	
	def __init__(self,dx=0.001,func=lambda *x: 0):
		'''конструктор принимает шаг дифференцирования dx
		функцию для дифференцирования func вида f(*x)'''
		self.__dx=dx
		self.__f=func
		
	def setDx(self,dx):
		'''устанавливает шаг диффиренцирования'''
		self.__dx=dx
	
	def getDx(self):
		'''возвращает шаг диффиренцирования'''
		return self.__dx
	
	def setF(self,f):
		'''устанавливает функцию для дифференцирования'''
		self.__f=f
	
	def calcDy(self,list_dx,x):
		'''возвращает производную фунции в точке x
		где list_dx кортеж индексов диффиренцирования по переменой'''
		x1=[j+self.__dx if i==list_dx[0] else j for i,j in enumerate(x)]
		x2=[j-self.__dx if i==list_dx[0] else j for i,j in enumerate(x)]
		if len(list_dx)==1:
			return (self.__f(*x1)-self.__f(*x2))/(self.__dx*2)
		else:
			return (self.calcDy(list_dx[1:],x1)-self.calcDy(list_dx[1:],x2))/(self.__dx*2)
			
	def getHesse(self,x):
		'''возвращает матрицу Гессе для функции в точке x'''
		return Matrix([[self.calcDy((i,j),x) for j in range(len(x))] for i in range(len(x))])
		
	def calcF(self,x):
		'''возвращает значение функции в точке x'''
		return self.__f(*x)

def _newton(x,func,e=(0.2,0.15)):
	xm=Matrix(vrow=x)
	_h=~func.getHesse(x)
	f3=lambda *x: (func.calcDy((0,),x),func.calcDy((1,),x))
	x1=round(xm-Matrix(vrow=f3(*x))*_h,5)
	if (x1-xm).getRadius()<e[0] or abs(func.calcF(x1.getList())-func.calcF(x))<e[1]:
		return x1.getList()
	else:
		return _newton(x1.getList(),func,e)
		
def Newton(x,func,e=(0.2,0.15)):
	return _newton(x,Function(func=func),e)



def main():
	#~ f=Function(func=lambda *x: x[0]**2,dx=0.00001)
	#~ print(f.calcDy((0,0),(50,)))
	#~ f=lambda x1,x2: 2*x1**2+x1*x2+x2**2
	#~ f=lambda x,y: sin(0.5*x**2-0.25*y**2+3)*cos(2*x+1-exp(y))
	f=lambda x,y: 2 *x**2 + x * y + y**2
	print(Newton((0.5,1),f,e=(0.1,0.15)))

if __name__=='__main__':
	main()
