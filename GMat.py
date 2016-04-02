# -*- coding: utf-8 -*-
#
import random
class GPoint():
	def __init__(self,x_name='x',y_name='y'):
		self._point=[]
		self._x_name=x_name
		self._y_name=y_name
	def _xy(self,x,y,p='.'):
		self._point.append((x,y,p))
	def _x_find(self,x):
		s=-1
		for i in range(len(self._point)):
			if x==self._point[i][0]:
				s=i
				break
		return s
	def _y_find(self,y):
		s=-1
		for i in range(len(self._point)):
			if y==self._point[i][1]:
				s=i
				break
		return s
	def _xn(self,x,n=1,p='.'):
		i=self._x_find(x)
		if i==-1:
			self._xy(x,n,p)
		else:
			self._point[i]=(x,self._point[i][1]+n,p)
	def _sum_y(self):
		s=0
		for i in self._point:
			s+=i[1]
		return s
	def _compress(self):
		for i in range(len(self._point)-1,-1,-1):
			j=self._x_find(self._point[i][0])
			if i!=j:
				self._xn(self._point[i][0],self._point[i][1],self._point[i][2])
				self._point.pop(i)
	def __str__(self):
		s='     '+self._x_name+'|'+self._y_name+'\n'
		for i in self._point:
			s+='{0:>6.2}|{1:<6.2}\n'.format(float(i[0]),float(i[1]))
		s+='mat={0}\ndis={1}'.format(self._mat(),self._dis())
		return s
	def toWA(self):
		#~ s='     '+self._x_name+'|'+self._y_name+'\n'
		s='polynom fit '
		for i in self._point:
			s+='{'+'{0:>6.2},{1:<6.2}'.format(float(i[0]),float(i[1]))+'},'
		#~ s+='mat={0}\ndis={1}'.format(self._mat(),self._dis())
		return s
	def _point_set(self,point):
		self._point=point
	def _point_get(self):
		return self._point
	def _to_list(self):
		l=[]
		for i in range(len(self._point)):
			try:
				for j in range(self._point[i][1]):
					l.append(self._point[i][0])
			except:
				l.append(self._point[i][0])
		return l
	def _mat(self):
		l=self._to_list()
		return sum(l)/len(l)
	def _dis(self):
		l=self._to_list()
		m=self._mat()
		return sum([(i-m)**2 for i in l])/(len(l)-1)
class GGraph():
	def __init__(self,x_0=-25,x_1=25,y_0=0,y_1=100,x_grid_len=50,y_grid_len=20):
		self._x_0=x_0
		self._x_1=x_1
		self._y_0=y_0
		self._y_1=y_1
		self._x_grid_len=x_grid_len
		self._y_grid_len=y_grid_len
		self._point=[]
		self._grid=[]
	def _func(self,x):
		return x**2
	def _point_set(self,point):
		self._point=point
	def _point_get(self):
		return self._point
	def _x_set(self,x_0,x_1):
		self._x_0=x_0
		self._x_1=x_1
	def _y_set(self,y_0,y_1):
		self._y_0=y_0
		self._y_1=y_1
	def _auto_set(self):
		x_0=self._point[0][0]
		x_1=self._point[0][0]
		y_0=self._point[0][1]
		y_1=self._point[0][1]
		for i in self._point:
			x_0=min(x_0,i[0])
			x_1=max(x_1,i[0])
			y_0=min(y_0,i[1])
			y_1=max(y_1,i[1])
		self._x_set(x_0,x_1)
		self._y_set(y_0,y_1)
	def _gist(self):
		self._auto_set()
		g=GPoint()
		g._point_set(self._point_get())
		import copy
		m=copy.deepcopy(self._point)
		m.sort()
		self._point.clear()
		step=(self._x_1-self._x_0)/self._x_grid_len
		for i in range(self._x_grid_len):
			for j in m:
				if self._x_0+i*step<=j[0]<self._x_0+(i+1)*step:
					g._xn(self._x_0+i*step,1,j[2])
	def _free_calc(self,_range):
		self._point=[(i,self._func(i)) for i in _range]
	def _calc_func(self):
		self._point=[(self._x_func(i),self._func(self._x_func(i)),'.') for i in range(self._x_grid_len)]
	def _re_grid(self,gist=False):
		self._grid=[]
		for i in range(self._x_grid_len):
			self._grid.append([])
			for j in range(self._y_grid_len):
				self._grid[i].append(' ')
		for i in self._point:
			if gist:
				for j in range(self._y_to_grid(i[1])):
					try:
						self._grid[self._x_to_grid(i[0])][j]=i[2]
					except:
						pass
			else:
				try:
					self._grid[self._x_to_grid(i[0])][self._y_to_grid(i[1])]=i[2]
				except:
					pass
	def _x_func(self,i):
		return (self._x_1-self._x_0)/self._x_grid_len*i+self._x_0
	def _y_func(self,i):
		return (self._y_1-self._y_0)/self._y_grid_len*i+self._y_0
	def _x_to_grid(self,x):
		return int((x-self._x_0)/(self._x_1-self._x_0)*self._x_grid_len)
	def _y_to_grid(self,y):
		return int((y-self._y_0)/(self._y_1-self._y_0)*self._y_grid_len)
	def _y_grid(self):
		l=[]
		for i in range(self._y_grid_len-1,-1,-1):
			if (i==(self._y_grid_len-1))or(i==0)or(i==int((self._y_grid_len-1)/2)):
				l.append('{0:7.2}-'.format(self._y_func(i)))
			else:
				l.append('{0:7}|'.format(' '))
		return l
	def _x_grid(self):
		_3=int(self._x_grid_len/2)
		s1='{0:>9}'.format('+|')
		s1+=('-'*(_3-1)+'|')*2
		s1+='\n'
		s2='{0:>10.2}'+'{1:>'+str(_3)+'.2}'+'{2:>'+str(_3)+'.2}\n'
		s2=s2.format(self._x_func(0),self._x_func(_3),self._x_func(self._x_grid_len-1))
		return [s1,s2]
	def __str__(self):
		s=''
		l=self._y_grid()
		l1=self._x_grid()
		for j in range(self._y_grid_len):
			s+=l[j]
			for i in range(self._x_grid_len):
				s+=self._grid[i][self._y_grid_len-j-1]
			s+='\n'
		s+=l1[0]
		s+=l1[1]
		return s
		
def main():
	g=GGraph()
	import math
	#~ g._func=lambda x: (x**0.5+3)
	#~ g._func=lambda x: 2.7**x
	g._func=lambda x: x**2
	g._x_set(-5,5)
	g._calc_func()
	#~ g._free_calc([(i+0.0)/1000 for i in range(0,100)])
	g._auto_set()
	g._re_grid()
	print(g)
def main2():
	g=GPoint()
	for i in range(1000):
		#~ g._xn(round(random.random(),2))
		g._xy(round(random.normalvariate(0,10),2),random.normalvariate(0,10))
	gr=GGraph()
	gr._point_set(g._point_get())
	#~ gr._auto_set()
	#~ gr._re_grid()
	gr._gist()
	gr._re_grid(True)
	print(gr)
	#~ g._compress()
	#~ print(g)
	
if __name__=='__main__':
	main2()
