# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
from math import *
from GMatrix import Matrix
class Function:
	def __init__(self,dx=0.001,func=lambda *x: 0):
		self.__dx=dx
		self.__f=func
	def setDx(self,dx):self.__dx=dx
	def getDx(self):return self.__dx
	def setF(self,f):self.__f=f
	def calcDy(self,list_dx,x):
		x1=[j+self.__dx if i==list_dx[0] else j for i,j in enumerate(x)]
		x2=[j-self.__dx if i==list_dx[0] else j for i,j in enumerate(x)]
		if len(list_dx)==1:
			return (self.__f(*x1)-self.__f(*x2))/(self.__dx*2)
		else:
			return (self.calcDy(list_dx[1:],x1)-self.calcDy(list_dx[1:],x2))/(self.__dx*2)
	def getHesse(self,x):
		return Matrix([[self.calcDy((i,j),x) for j in range(len(x))] for i in range(len(x))])
	def calcF(self,x):return self.__f(*x)


def _newton(x,func,e=(0.2,0.15)):
	xm=Matrix(vrow=x)
	_h=~func.getHesse(x)
	#print(_h)
	f3=lambda *x: (func.calcDy((0,),x),func.calcDy((1,),x))
	x1=round(xm-Matrix(vrow=f3(*x))*_h,5)
	#print(x1)
	if (x1-xm).getRadius()<e[0] or abs(func.calcF(x1.getList())-func.calcF(x))<e[1]:
		return x1.getList()
	else:
		return _newton(x1.getList(),func,e)
def Newton(x,func,e=(0.2,0.15)):
	return _newton(x,Function(func=func),e)



def main():
	#~ f=Function(func=lambda *x: x[0]**2)
	#~ print(f.calcDy((0,),(50,)))
	#~ f=lambda x1,x2: 2*x1**2+x1*x2+x2**2
	f=lambda x,y: sin(0.5*x**2-0.25*y**2+3)*cos(2*x+1-exp(y))
	print(Newton((0,0.5),f,e=(0.001,0.001)))

if __name__=='__main__':
	main()
