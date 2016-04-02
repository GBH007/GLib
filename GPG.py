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
class Graph():
	def __init__(self,x=(-25,25),y=(0,100),x_grid_len=50,y_grid_len=20):
		self.__x=x
		self.__y=y
		self.__x_grid_len=x_grid_len
		self.__y_grid_len=y_grid_len
		self.__point_lists=[]
		self.__grid=[]
	def addPointList(self,point_list,sign='.'):
		self.__point_lists.append((point_list,sign))
	def delPointList(self,point_list):
		for i in self.__point_lists:
			if point_list is i[0]:
				self.__point_lists.remove(i)
				break
	def setX(self,x):
		self.__x=x
	def setY(self,y):
		self.__y=y
	def setAuto(self,axis=(0,1)):
		#~ mi=Point()
		mi=self.__point_lists[0][0].min()
		ma=self.__point_lists[0][0].max()
		#~ ma=Point()
		for i,sign in self.__point_lists:
			mi=mi.min(i.min())
			ma=ma.max(i.max())
		x=mi[axis[0]],ma[axis[0]]
		y=mi[axis[1]],ma[axis[1]]
		self.setX(x)
		self.setY(y)
	def setAutoX(self,axis=0):
		mi=self.__point_lists[0][0].min()
		ma=self.__point_lists[0][0].max()
		mi_n=self.__point_lists[0][0].minN()
		ma_n=self.__point_lists[0][0].maxN()
		for i,sign in self.__point_lists:
			mi=mi.min(i.min())
			ma=ma.max(i.max())
			mi_n=min(mi_n,i.minN())
			ma_n=min(ma_n,i.maxN())
		x=mi[axis],ma[axis]
		y=mi_n,ma_n
		self.setX(x)
		self.setY(y)
	def _x_func(self,i):
		return (self.__x[1]-self.__x[0])/self.__x_grid_len*i+self.__x[0]
	def _y_func(self,i):
		return (self.__y[1]-self.__y[0])/self.__y_grid_len*i+self.__y[0]
	def _x_to_grid(self,x):
		return int((x-self.__x[0])/(self.__x[1]-self.__x[0])*self.__x_grid_len)
	def _y_to_grid(self,y):
		return int((y-self.__y[0])/(self.__y[1]-self.__y[0])*self.__y_grid_len)
	def __y_grid(self):
		l=[]
		for i in range(self.__y_grid_len-1,-1,-1):
			if (i==(self.__y_grid_len-1))or(i==0)or(i==int((self.__y_grid_len-1)/2)):
				l.append('{0:7.2}-'.format(self._y_func(i)))
			else:
				l.append('{0:7}|'.format(' '))
		return l
	def __x_grid(self):
		_3=int(self.__x_grid_len/2)
		s1='{0:>9}'.format('+|')
		s1+=('-'*(_3-1)+'|')*2
		s1+='\n'
		s2='{0:>10.2}'+'{1:>'+str(_3)+'.2}'+'{2:>'+str(_3)+'.2}\n'
		s2=s2.format(self._x_func(0),self._x_func(_3),self._x_func(self.__x_grid_len-1))
		return [s1,s2]
	def __str__(self):
		s=''
		l=self.__y_grid()
		l1=self.__x_grid()
		for j in range(self.__y_grid_len):
			s+=l[j]
			for i in range(self.__x_grid_len):
				s+=self.__grid[i][self.__y_grid_len-j-1]
			s+='\n'
		s+=l1[0]
		s+=l1[1]
		return s
	def reGrid(self,axis=(0,1),gist=False,autoset=True):
		self.__grid=[]
		for i in range(self.__x_grid_len):
			self.__grid.append([])
			for j in range(self.__y_grid_len):
				self.__grid[i].append(' ')
		if not gist:
			if autoset:self.setAuto(axis)
			for i,sign in self.__point_lists:
				points=i.toPlot(axis)
				for i in points:
					try:
						self.__grid[self._x_to_grid(i[0])][self._y_to_grid(i[1])]=sign
					except IndexError:
						pass
		else:
			if autoset:self.setAutoX(axis)
			for i,sign in self.__point_lists:
				points=i.toGist(axis)
				for i in points:
					for j in range(self._y_to_grid(i[1])):
						try:
							self.__grid[self._x_to_grid(i[0])][j]=sign
						except IndexError:
							pass
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
	g=Graph()
	g.addPointList(p)
	#~ g.reGrid(gist=True,axis=0)
	g.reGrid()
	print(g)
	#~ print(p)
	#~ print(p.initialMoment())
	#~ print(p.centralMoment())
	#~ print(p.min())
	#~ print(p.max())
def main2():
	import random
	g=Graph()
	p=Points()
	for i in range(10000):
		p.add((round(random.normalvariate(0,0.1),2),))
		#~ g._xy(round(random.normalvariate(0,10),2),random.normalvariate(0,10))
	print(p.initialMoment())
	g.addPointList(p)
	g.reGrid(axis=0,gist=True)
	print(g)
	#~ g._compress()
	#~ print(g)

if __name__=='__main__':
	main2()
