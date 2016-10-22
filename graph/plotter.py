# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

__all__=['LinePlotter','PointPlotter','GistPlotter']

class Plotter:
	
	def __init__(self,graph,point_list,color='black',name='noname'):
		self.gr=graph
		self.pl=point_list
		self.clr=color
		self.name=name
	
	def getName(self):return self.name
	
	def min(self):return self.pl.min()
	
	def max(self):return self.pl.max()
		
	def plot(self,axis):raise AttributeError
	
class LinePlotter(Plotter):
	
	def __init__(self,graph,point_list,color='black',name='noname',width=1):
		Plotter.__init__(self,graph,point_list,color,name)
		self.width=width
	
	def plot(self,axis):
		points=self.pl.toPlot(axis)
		point=None
		for i in points:
			x=self.gr._x_to_grid(i[0])
			y=self.gr._y_to_grid(i[1])
			if not self.gr.xInGraph(x):continue
			if not self.gr.yInGraph(y):continue
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
	
class PointPlotter(Plotter):
	
	def __init__(self,graph,point_list,color='black',name='noname',radius=1):
		Plotter.__init__(self,graph,point_list,color,name)
		self.radius=radius
	
	def plot(self,axis):
		points=self.pl.toPlot(axis)
		point=None
		for i in points:
			x=self.gr._x_to_grid(i[0])
			y=self.gr._y_to_grid(i[1])
			if not self.gr.xInGraph(x):continue
			if not self.gr.yInGraph(y):continue
			self.gr.canv.create_oval(
				x-self.radius,
				y-self.radius,
				x+self.radius,
				y+self.radius,
				fill=self.clr,
				width=0,
				tags=self.name
			)
		
class GistPlotter(Plotter):
	
	def __init__(self,graph,point_list,color='black',name='noname',dx=1):
		Plotter.__init__(self,graph,point_list,color,name)
		self.dx=dx
		
	def max(self):return self.pl.maxN()
	
	def min(self):return self.pl.minN()
	
	def plot(self,axis):
		points=self.pl.toGist(axis[0])
		for i in points:
			self.gr.canv.create_rectangle(
				self.gr._x_to_grid(i[0]-self.dx/2),
				self.gr._y_to_grid(i[1]),
				self.gr._x_to_grid(i[0]+self.dx/2),
				self.gr._y_to_grid(0),
				fill=self.clr,
				tags=self.name
			)
