# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
from tkinter import *
		
__all__=['GraphToplevel','GraphTk']

class CanvasDescriptor:
	
	def __get__(self,ins,own):
		return ins._Graph__canv

class Graph:
	
	canv=CanvasDescriptor()
	
	def __init__(self,x=(-25,25),y=(0,100),x_grid_len=500,y_grid_len=500):
		self.__x=x
		self.__y=y
		self.__x_grid_len=x_grid_len
		self.__y_grid_len=y_grid_len
		self.__x_indent=100
		self.__y_indent=10
		self.__y_down_indent=50
		self.__plotter_list=[]
		self.__canv=Canvas(self,width=self.__x_grid_len+self.__x_indent,height=self.__y_grid_len+self.__y_indent+self.__y_down_indent)
		self.__x_grid()
		self.__y_grid()
		self.__canv.pack()
						
	def addPlotter(self,plotter):
		self.__plotter_list.append(plotter)
		
	def delPointList(self,plotter):
		for i in self.__plotter_list:
			if plotter is i[0]:
				self.__plotter_list.remove(i)
				break
				
	def setX(self,x):self.__x=x
		
	def setY(self,y):self.__y=y
				
	def getX(self):return self.__x
		
	def getY(self):return self.__y
		
	def setAuto(self,axis=(0,1)):
		mi=self.__plotter_list[0].min()
		ma=self.__plotter_list[0].max()
		for i in self.__plotter_list:
			mi=mi.min(i.min())
			ma=ma.max(i.max())
		xl=ma[axis[0]]-mi[axis[0]]
		yl=ma[axis[1]]-mi[axis[1]]
		xl*=0.05
		yl*=0.05
		x=mi[axis[0]]-xl,ma[axis[0]]+xl
		y=mi[axis[1]]-yl,ma[axis[1]]+yl
		self.setX(x)
		self.setY(y)
		
	def _x_func(self,i):
		return (self.__x[1]-self.__x[0])/self.__x_grid_len*i+self.__x[0]
		
	def _y_func(self,i):
		return (self.__y[1]-self.__y[0])/self.__y_grid_len*(self.__y_grid_len-i)+self.__y[0]
		
	def _x_to_grid(self,x):
		return int((x-self.__x[0])/(self.__x[1]-self.__x[0])*self.__x_grid_len)+self.__x_indent
		
	def _y_to_grid(self,y):
		return int(self.__y_grid_len-(y-self.__y[0])/(self.__y[1]-self.__y[0])*self.__y_grid_len)+self.__y_indent
		
	def __x_grid(self,marks=10,grid=False,mark_list=None):
		self.__canv.delete('xgrid')
		self.__canv.create_line(
			self.__x_indent,
			self.__y_grid_len+self.__y_indent,
			self.__x_grid_len+self.__x_indent,
			self.__y_grid_len+self.__y_indent,
			width=2,
			fill='black',
			tags='xgrid'
		)
		self.__canv.create_line(
			self.__x_indent,
			self.__y_indent,
			self.__x_grid_len+self.__x_indent,
			self.__y_indent,
			width=2,
			fill='black',
			tags='xgrid'
		)
		for i in range(marks):
			xg=i*self.__x_grid_len//marks
			if not xg:continue
			if grid:
				self.__canv.create_line(
					xg+self.__x_indent,
					self.__y_grid_len+self.__y_indent,
					xg+self.__x_indent,
					self.__y_indent,
					width=0.2,
					fill='gray',
					tags='xgrid'
				)
			self.__canv.create_text(
				xg+self.__x_indent,
				self.__y_grid_len+10+self.__y_indent,
				text='{0:4.2f}'.format(self._x_func(xg)),
				fill='black',
				tags='xgrid',
				anchor=N
			)
		if mark_list:
			for i in mark_list:
				x=self._x_to_grid(i)
				if not self._xInGraph(x):continue
				if grid:
					self.__canv.create_line(
						x,
						self.__y_grid_len+self.__y_indent,
						x,
						self.__y_indent,
						width=0.2,
						fill='gray',
						tags='xgrid'
					)
				self.__canv.create_text(
					x,
					self.__y_grid_len+10+self.__y_indent,
					text='{0:4.2f}'.format(i),
					fill='black',
					tags='xgrid',
					anchor=N
				)
		self.__canv.update()
		
	def __y_grid(self,marks=10,grid=False,mark_list=None):
		self.__canv.delete('ygrid')
		self.__canv.create_line(
			self.__x_indent,
			self.__y_indent,
			self.__x_indent,
			self.__y_grid_len+self.__y_indent,
			width=2,
			fill='black',
			tags='ygrid'
		)
		self.__canv.create_line(
			self.__x_indent+self.__x_grid_len,
			self.__y_indent,
			self.__x_indent+self.__x_grid_len,
			self.__y_grid_len+self.__y_indent,
			width=2,
			fill='black',
			tags='ygrid'
		)
		for i in range(marks):
			yg=i*self.__y_grid_len//marks
			if not yg:continue
			if grid:
				self.__canv.create_line(
					self.__x_indent,
					yg+self.__y_indent,
					self.__x_grid_len+self.__x_indent,
					yg+self.__y_indent,
					width=0.2,
					fill='gray',
					tags='ygrid'
				)
			self.__canv.create_text(
				self.__x_indent-10,
				yg+self.__y_indent,
				text='{0:4.2f}'.format(self._y_func(yg)),
				fill='black',
				tags='ygrid',
				anchor=E
			)
		if mark_list:
			for i in mark_list:
				y=self._y_to_grid(i)
				if not self._yInGraph(y):continue
				if grid:
					self.__canv.create_line(
						self.__x_indent,
						y,
						self.__x_grid_len+self.__x_indent,
						y,
						width=0.2,
						fill='gray',
						tags='ygrid'
					)
				self.__canv.create_text(
					self.__x_indent-10,
					y,
					text='{0:4.2f}'.format(i),
					fill='black',
					tags='ygrid',
					anchor=E
				)
		self.__canv.update()
		
	def addXLine(self,x,clr='black'):
		self.__canv.create_line(
			self._x_to_grid(x),
			self.__y_grid_len+self.__y_indent,
			self._x_to_grid(x),
			self.__y_indent,
			width=0.2,
			fill=clr,
			tags='xline',
			dash=(20,10)
		)
		self.__canv.update()
		
	def addYLine(self,y,clr='black'):
		self.__canv.create_line(
			self.__x_indent,
			self._y_to_grid(y),
			self.__x_grid_len+self.__x_indent,
			self._y_to_grid(y),
			width=0.2,
			fill=clr,
			tags='yline',
			dash=(20,10)
		)
		self.__canv.update()
		
	def _xInGraph(self,x):
		if self.__x_indent<x<self.__x_indent+self.__x_grid_len:
			return True
		return False
		
	def _yInGraph(self,y):
		if self.__y_indent<y<self.__y_indent+self.__y_grid_len:
			return True
		return False
		
	def clearXLine(self):
		self.__canv.delete('xline')
		self.__canv.update()
				
	def clearYLine(self):
		self.__canv.delete('yline')
		self.__canv.update()
		
	def reGrid(self,axis=(0,1),autoset=True,grid=False,legend=True,xmarks=10,ymarks=10,x_mark_list=None,y_mark_list=None):
		self.__canv.delete('noname')
		if legend:
			self.__canv.config(height=self.__y_grid_len+self.__y_indent+self.__y_down_indent+20*len(self.__plotter_list))
			self.config(height=self.__y_grid_len+self.__y_indent+self.__y_down_indent+20*len(self.__plotter_list))
			self.update()
		if autoset:self.setAuto(axis)
		self.__x_grid(marks=xmarks,grid=grid,mark_list=x_mark_list)
		self.__y_grid(marks=ymarks,grid=grid,mark_list=y_mark_list)
		for i,plotter in enumerate(self.__plotter_list):
			plotter.plot(axis)
			if legend:
				plotter.plotLegend(self.__x_indent,self.__y_grid_len+self.__y_indent+self.__y_down_indent+20*i)
		self.__canv.update()
		
class GraphToplevel(Toplevel,Graph):
	
	def __init__(self,parrent=None,x=(-25,25),y=(0,100),x_grid_len=500,y_grid_len=500,name='graph'):
		Toplevel.__init__(self,parrent)
		Graph.__init__(self,x=x,y=y,x_grid_len=x_grid_len,y_grid_len=y_grid_len)
		self.title(name)
		
class GraphTk(Tk,Graph):
	
	def __init__(self,parrent=None,x=(-25,25),y=(0,100),x_grid_len=500,y_grid_len=500,name='graph'):
		Tk.__init__(self)
		Graph.__init__(self,x=x,y=y,x_grid_len=x_grid_len,y_grid_len=y_grid_len)
		self.title(name)

