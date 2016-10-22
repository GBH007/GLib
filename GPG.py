# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
class Point:
	
	def __init__(self,cord=None,sign=('x','y','z')):
		self.__cord=tuple(cord) if cord else tuple()
		self.__sign=sign
		
	def getCord(self):return self.__cord
	
	def setLinkedCord(self,cord):self.__cord=cord
	
	def setCord(self,cord):self.__cord=tuple(cord)
	
	def getSign(self):return self.__sign if self.__sign else ['' for i in self.__cord]
	
	def setSign(self,sign):self.__sign=sign
	
	def radius(self,other):
		return sum(map(lambda *x: (x[0]-x[1])**2,self.getCord(),other.getCord()))**0.5
		
	def __eq__(self,other):
		return not sum(map(lambda *x: x[0]!=x[1],self.getCord(),other.getCord()))
		
	def __add__(self,other):
		cord1,cord2=self.stab(other)
		cord=tuple(map(lambda *x: x[0]+x[1],cord1,cord2))
		return Point(cord=cord)
		
	def max(self,other):
		cord1,cord2=self.stab(other)
		cord=tuple(map(max,cord1,cord2))
		return Point(cord=cord)
		
	def min(self,other):
		cord1,cord2=self.stab(other)
		cord=tuple(map(min,cord1,cord2))
		return Point(cord=cord)
		
	def stab(self,other):
		cord1=self.getCord()
		cord2=other.getCord()
		l1=len(cord1)
		l2=len(cord2)
		n=max(l1,l2)
		cord1+=tuple([0 for i in range(n-l1)])
		cord2+=tuple([0 for i in range(n-l2)])
		return cord1,cord2
		
	def __sub__(self,other):
		cord1,cord2=self.stab(other)
		cord=tuple(map(lambda *x: x[0]-x[1],cord1,cord2))
		return Point(cord=cord)
		
	def __mul__(self,other):
		cord1,cord2=self.stab(other)
		return sum(map(lambda *x: x[0]*x[1],cord1,cord2))
		
	def __pow__(self,k):
		return Point(cord=tuple(map(lambda x: x**k,self.getCord())))
		
	def __lshift__(self,k):
		return Point(cord=tuple(map(lambda x: x*k,self.getCord())))
		
	def __rshift__(self,k):
		return Point(cord=tuple(map(lambda x: x/k,self.getCord())))
		
	def __repr__(self):
		return 'Point {0}{1}'.format(self.getCord(),self.getSign())
		
	def __getitem__(self,key):
		try:
			return self.__cord[key]
		except IndexError:
			return 0
			
	def __str__(self):
		return ' , '.join(map(lambda x,s:'{1}={0}'.format(x,s),self.getCord(),self.getSign()))
		
	def __len__(self):
		return len(self.__cord)
		
class Points:
	
	def __init__(self,sign=('x','y','z')):
		self.__points=[]		#i[0] - Point obj i[1] - n i[0]
		self.__sign=sign
		
	def getSign(self):return self.__sign
	
	def setSign(self,sign):self.__sign=sign
	
	def __contains__(self,point):
		for i,n in self.__points:
			if i==point:return True
		return False
		
	def __getitem__(self,point):
		for i in self.__points:
			if i[0]==point:return i
		return None
		
	def __setitem__(self,point,n):
		for i in self.__points:
			if i[0]==point:
				i[1]=n
				
	def __delitem__(self,point):
		for i in self.__points:
			if i[0]==point:
				i[1]-=1
				if i[1]==0:self.__points.remove(i)
				
	def add(self,cord,num=1):
		p=Point(cord=cord,sign=self.__sign)
		if p in self:
			self[p]=self[p][1]+num
		else:
			self.__points.append([p,num])
		return p
		
	def remove(self,point):
		del self[point]
		
	def initialMoment(self,k=1):
		m=Point()
		n=0
		for i in self.__points:
			m+=(i[0]**k)<<i[1]
			n+=i[1]
		if n:
			m>>=n
		return m
		
	def min(self):
		m=self.__points[0][0]
		for i in self.__points:
			m=m.min(i[0])
		return m
		
	def minN(self):
		m=self.__points[0][1]
		for i in self.__points:
			m=min(i[1],m)
		return m
		
	def max(self):
		m=self.__points[0][0]
		for i in self.__points:
			m=m.max(i[0])
		return m
		
	def maxN(self):
		m=self.__points[0][1]
		for i in self.__points:
			m=max(i[1],m)
		return m
		
	def centralMoment(self,k=2):
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
		s=[]
		for i in self.__points:
			s.append([i[0][j] for j in axis])
		return s
		
	def toGist(self,axis):
		s=[]
		for i in self.__points:
			s.append([i[0][axis],i[1]])
		return s
		
	def __iter__(self):
		return iter(self.__points)
		
	def __str__(self):
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
