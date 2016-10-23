# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from tkinter import *

__all__=['LinePlotter','PointPlotter','GistPlotter']

class Plotter:
	'''базовый класс для рисование графика и гистограммы'''
	
	def __init__(self,graph,point_list,color='black',name='noname'):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name'''
		self.gr=graph
		self.pl=point_list
		self.clr=color
		self.name=name
	
	def getName(self):
		'''возвращает имя графика'''
		return self.name
	
	def min(self):
		'''возвращает точку с набором минимальных координат из набора точек'''		
		return self.pl.min()
	
	def max(self):
		'''возвращает точку с набором максимальных координат из набора точек'''
		return self.pl.max()
		
	def plot(self,axis):
		'''прорисовывает график по осям axis'''
		raise AttributeError
	
	def plotLegend(self,x,y):
		'''рисует легенду к графику в точке холста x,y'''
		raise AttributeError
	
class LinePlotter(Plotter):
	'''класс для рисования графика прямыми линиями'''
	
	def __init__(self,graph,point_list,color='black',name='noname',width=1):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name толщину линии width'''
		Plotter.__init__(self,graph,point_list,color,name)
		self.width=width
	
	def plot(self,axis):
		points=self.pl.toPlot(axis)
		point=None
		for i in points:
			x=self.gr._x_to_grid(i[0])
			y=self.gr._y_to_grid(i[1])
			if not self.gr._xInGraph(x):continue
			if not self.gr._yInGraph(y):continue
			if point==None:point=i
			else:
				self.gr.canv.create_line(
					self.gr._x_to_grid(point[0]),
					self.gr._y_to_grid(point[1]),
					x,
					y,
					width=self.width,
					fill=self.clr,
					tags=self.name
				)
				point=i
				
	def plotLegend(self,x,y):
		self.gr.canv.create_text(
			x+10,
			y,
			text=self.name,
			anchor=W,
		)
		self.gr.canv.create_line(
			x-10,
			y,
			x-60,
			y,
			fill=self.clr
		)
	
class PointPlotter(Plotter):
	'''класс для рисования графика точками'''
	
	def __init__(self,graph,point_list,color='black',name='noname',radius=1):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name радиус точки radius'''
		Plotter.__init__(self,graph,point_list,color,name)
		self.radius=radius
	
	def plot(self,axis):
		points=self.pl.toPlot(axis)
		point=None
		for i in points:
			x=self.gr._x_to_grid(i[0])
			y=self.gr._y_to_grid(i[1])
			if not self.gr._xInGraph(x):continue
			if not self.gr._yInGraph(y):continue
			self.gr.canv.create_oval(
				x-self.radius,
				y-self.radius,
				x+self.radius,
				y+self.radius,
				fill=self.clr,
				width=0,
				tags=self.name
			)
				
	def plotLegend(self,x,y):
		self.gr.canv.create_text(
			x+10,
			y,
			text=self.name,
			anchor=W,
		)
		for i in range(3):
			self.gr.canv.create_oval(
				x-20-i*15,
				y-5,
				x-10-i*15,
				y+5,
				fill=self.clr
			)
		
class GistPlotter(Plotter):
	'''класс для рисования гистограммы'''
	
	def __init__(self,graph,point_list,color='black',name='noname',dx=None):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name ширину столбца dx'''
		Plotter.__init__(self,graph,point_list,color,name)
		self.dx=dx
		
	def max(self):return self.pl.maxN()
	
	def min(self):return self.pl.minN()
	
	def plot(self,axis):
		points=self.pl.toGist(axis[0])
		if not self.dx:
			self.dx=self.pl.getMinDc(axis[0])
		for i in points:
			self.gr.canv.create_rectangle(
				self.gr._x_to_grid(i[0]-self.dx/2),
				self.gr._y_to_grid(i[1]),
				self.gr._x_to_grid(i[0]+self.dx/2),
				self.gr._y_to_grid(self.gr.getY()[0]),
				fill=self.clr,
				tags=self.name
			)

	def plotLegend(self,x,y):
		self.gr.canv.create_text(
			x+10,
			y,
			text=self.name,
			anchor=W,
		)
		for i in range(3):
			self.gr.canv.create_rectangle(
				x-20-i*10,
				y-5*i,
				x-10-i*10,
				y+5,
				fill=self.clr
			)
