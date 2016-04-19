# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
from tkinter import *
from GPG import Point,Points
#~ class Graph(Toplevel):
class Graph(Tk):
	def __init__(self,parrent=None,x=(-25,25),y=(0,100),x_grid_len=500,y_grid_len=500,name='graph'):
		#~ Toplevel.__init__(self,parrent)
		Tk.__init__(self)
		self.title(name)
		self.__x=x
		self.__y=y
		self.__x_grid_len=x_grid_len
		self.__y_grid_len=y_grid_len
		self.__point_lists=[]
		self.__canv=Canvas(self,width=self.__x_grid_len,height=self.__y_grid_len)
		self.__x_grid()
		self.__y_grid()
		self.__canv.pack()
	def addPointList(self,point_list,sign='green'):
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
		mi=self.__point_lists[0][0].min()
		ma=self.__point_lists[0][0].max()
		for i,sign in self.__point_lists:
			mi=mi.min(i.min())
			ma=ma.max(i.max())
		x=mi[axis[0]],ma[axis[0]]
		y=mi[axis[1]],ma[axis[1]]
		self.setX(x)
		self.setY(y)
	def _x_func(self,i):
		return (self.__x[1]-self.__x[0])/self.__x_grid_len*i+self.__x[0]
	def _y_func(self,i):
		return (self.__y[1]-self.__y[0])/self.__y_grid_len*(self.__y_grid_len-i)+self.__y[0]
	def _x_to_grid(self,x):
		return int((x-self.__x[0])/(self.__x[1]-self.__x[0])*self.__x_grid_len)
	def _y_to_grid(self,y):
		return int(self.__y_grid_len-(y-self.__y[0])/(self.__y[1]-self.__y[0])*self.__y_grid_len)
	def __x_grid(self,marks=10,grid=False):
		self.__canv.delete('xgrid')
		for i in range(marks):
			xg=i*self.__x_grid_len//marks
			if not xg:continue
			if grid:self.__canv.create_line(xg,self.__y_grid_len,xg,0,width=0.2,fill='gray',tags='xgrid')
			self.__canv.create_line(xg,self.__y_grid_len,xg,self.__y_grid_len-6,width=0.5,fill='black',tags='xgrid')
			#~ self.__canv.create_text(xg,self.__y_grid_len-20,text=str(self._x_func(xg)),fill='red',tags='xgrid')
			self.__canv.create_text(xg,self.__y_grid_len-20,text='{0:4.2}'.format(self._x_func(xg)),fill='black',tags='xgrid')
		self.__canv.update()
	def __y_grid(self,marks=10,grid=False):
		self.__canv.delete('ygrid')
		for i in range(marks):
			yg=i*self.__y_grid_len//marks
			if not yg:continue
			if grid:self.__canv.create_line(0,yg,self.__x_grid_len,yg,width=0.2,fill='gray',tags='ygrid')
			self.__canv.create_line(0,yg,6,yg,width=0.5,fill='black',tags='ygrid')
			#~ self.__canv.create_text(20,yg,text=str(self._y_func(yg)),fill='red',tags='ygrid')
			self.__canv.create_text(20,yg,text='{0:4.2}'.format(self._y_func(yg)),fill='black',tags='ygrid')
		self.__canv.update()
	def addXLine(self,x,clr='black'):
		self.__canv.create_line(self._x_to_grid(x),self.__y_grid_len,self._x_to_grid(x),0,width=0.2,fill=clr,tags='xline',dash=(20,10))
		self.__canv.update()
	def addYLine(self,y,clr='black'):
		self.__canv.create_line(0,self._y_to_grid(y),self.__x_grid_len,self._y_to_grid(y),width=0.2,fill=clr,tags='yline',dash=(20,10))
		self.__canv.update()
	def clearXLine(self):
		self.__canv.delete('xline')
		self.__canv.update()
	def clearYLine(self):
		self.__canv.delete('yline')
		self.__canv.update()
	def reGrid(self,axis=(0,1),autoset=True,grid=False):
		self.__canv.delete('func')
		if autoset:self.setAuto(axis)
		self.__x_grid(grid=grid)
		self.__y_grid(grid=grid)
		for i,sign in self.__point_lists:
			points=i.toPlot(axis)
			point=None
			for i in points:
				if point==None:point=i
				else:
					self.__canv.create_line(self._x_to_grid(point[0]),self._y_to_grid(point[1]),self._x_to_grid(i[0]),self._y_to_grid(i[1]),width=1,fill=sign,tags='func')
					point=i
		self.__canv.update()
def main():
	g=Graph()
	p=Points()
	p1=Points()
	f=lambda x: x**2
	f1=lambda x: x**3
	for i in range(-20,20):
		p.add((i/10,f(i/10)))
		p1.add((i/10,f1(i/10)))
	#~ g=Graph()
	g.addPointList(p,'blue')
	g.addPointList(p1,'red')
	#~ print(p1)
	#~ g.reGrid(gist=True,axis=0)
	g.setX((-2,2))
	g.setY((-2,2))
	g.addXLine(1)
	g.addYLine(1)
	g.reGrid(grid=True,autoset=False)
	mainloop()
if __name__=='__main__':
	main()
