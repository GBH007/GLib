# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from tkinter import *

__all__=['LinePlotter','PointPlotter','GistPlotter']

class Plotter:
	'''базовый класс для рисование графика и гистограммы'''
	
	def __init__(self,graph,x_list,y_list,color='black',name='noname',name_list=None):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name описания точек name_list'''
		self.gr=graph
		self.x_list=x_list
		self.y_list=y_list
		self.name_list=name_list
		self.clr=color
		self.name=name
	
	def getName(self):
		'''возвращает имя графика'''
		return self.name
	
	def min(self):
		'''возвращает точку с набором минимальных координат из набора точек'''		
		return (min(self.x_list),min(self.y_list))
	
	def max(self):
		'''возвращает точку с набором максимальных координат из набора точек'''
		return (max(self.x_list),max(self.y_list))
		
	def plot(self):
		'''прорисовывает график'''
		raise AttributeError
	
	def plotLegend(self,x,y):
		'''рисует легенду к графику в точке холста x,y'''
		raise AttributeError
	
class LinePlotter(Plotter):
	'''класс для рисования графика прямыми линиями'''
	
	def __init__(self,graph,x_list,y_list,color='black',name='noname',width=1,name_list=None):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name толщину линии width'''
		Plotter.__init__(self,graph,x_list,y_list,color,name,name_list)
		self.width=width
	
	def plot(self):
		self.gr.canv.delete(self.name)
		points=zip(self.x_list,self.y_list)
		point=None
		for ind,i in enumerate(points):
			x=self.gr._x_to_grid(i[0])
			y=self.gr._y_to_grid(i[1])
			if not self.gr._xInGraph(x):continue
			if not self.gr._yInGraph(y):continue
			if point==None:point=i
			else:
				try:
					tags=(self.name,'plotter',self.name_list[ind])
				except (IndexError,TypeError):
					tags=(self.name,'plotter')
				self.gr.canv.create_line(
					self.gr._x_to_grid(point[0]),
					self.gr._y_to_grid(point[1]),
					x,
					y,
					width=self.width,
					fill=self.clr,
					tags=tags
				)
				point=i
				
	def plotLegend(self,x,y):
		self.gr.canv.create_text(
			x+10,
			y,
			text=self.name,
			anchor=W,
			tags=self.name
		)
		self.gr.canv.create_line(
			x-10,
			y,
			x-60,
			y,
			fill=self.clr,
			tags=self.name
		)
	
class PointPlotter(Plotter):
	'''класс для рисования графика точками'''
	
	def __init__(self,graph,x_list,y_list,color='black',name='noname',radius=1,name_list=None):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name радиус точки radius'''
		Plotter.__init__(self,graph,x_list,y_list,color,name,name_list)
		self.radius=radius
	
	def plot(self):
		self.gr.canv.delete(self.name)
		points=zip(self.x_list,self.y_list)
		for ind,i in enumerate(points):
			x=self.gr._x_to_grid(i[0])
			y=self.gr._y_to_grid(i[1])
			if not self.gr._xInGraph(x):continue
			if not self.gr._yInGraph(y):continue
			try:
				tags=(self.name,'plotter',self.name_list[ind])
			except (IndexError,TypeError):
				tags=(self.name,'plotter')
			self.gr.canv.create_oval(
				x-self.radius,
				y-self.radius,
				x+self.radius,
				y+self.radius,
				fill=self.clr,
				width=0,
				tags=tags
			)
				
	def plotLegend(self,x,y):
		self.gr.canv.create_text(
			x+10,
			y,
			text=self.name,
			anchor=W,
			tags=self.name
		)
		for i in range(3):
			self.gr.canv.create_oval(
				x-20-i*15,
				y-5,
				x-10-i*15,
				y+5,
				fill=self.clr,
				tags=self.name
			)
		
class GistPlotter(Plotter):
	'''класс для рисования гистограммы'''
	
	def __init__(self,graph,x_list,y_list,color='black',name='noname',dx=None,name_list=None):
		'''конструктор принимает объект графа (Graph) graph
		список точек (Points) point_list цвет графика color
		имя графика name ширину столбца dx'''
		Plotter.__init__(self,graph,x_list,y_list,color,name,name_list)
		self.dx=dx
	
	def plot(self):
		self.gr.canv.delete(self.name)
		points=zip(self.x_list,self.y_list)
		if not self.dx:
			m=sorted(self.x_list)
			self.dx=min([abs(m[i]-m[i-1]) for i in range(len(m)-1,0,-1)])
		for ind,i in enumerate(points):
			try:
				tags=(self.name,'plotter',self.name_list[ind])
			except (IndexError,TypeError):
				tags=(self.name,'plotter')
			self.gr.canv.create_rectangle(
				self.gr._x_to_grid(i[0]-self.dx/2),
				self.gr._y_to_grid(i[1]),
				self.gr._x_to_grid(i[0]+self.dx/2),
				self.gr._y_to_grid(self.gr.getY()[0]),
				fill=self.clr,
				tags=tags
			)

	def plotLegend(self,x,y):
		self.gr.canv.create_text(
			x+10,
			y,
			text=self.name,
			anchor=W,
			tags=self.name
		)
		for i in range(3):
			self.gr.canv.create_rectangle(
				x-20-i*10,
				y-5*i,
				x-10-i*10,
				y+5,
				fill=self.clr,
				tags=self.name
			)
