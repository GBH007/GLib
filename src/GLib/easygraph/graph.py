# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
from tkinter import *
		
__all__=['GraphToplevel','GraphTk']

class CanvasDescriptor:
	'''класс дескриптор холста'''
	
	def __get__(self,ins,own):
		'''возвращает холст'''
		return ins._Graph__canv

class Graph:
	'''базовый класс для рисования набора графиков или гистограмм'''
	canv=CanvasDescriptor()
	
	def __init__(self,x=(-25,25),y=(0,100),x_grid_len=500,y_grid_len=500):
		'''конструктор принимает диапозон значений по оси абцисс x, ординат y
		длину сетки по x x_grid_len по y y_grid_len'''
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
		'''добавление нового графика, принимает плоттер'''
		self.__plotter_list.append(plotter)
		
	def delPlotter(self,plotter):
		'''удаление графика, принимает плоттер'''
		for i in self.__plotter_list:
			if plotter is i[0]:
				self.__plotter_list.remove(i)
				break
				
	def setX(self,x):
		'''устанавливает диапозон значений x'''
		self.__x=x
		
	def setY(self,y):
		'''устанавливает диапозон значений y'''
		self.__y=y
				
	def getX(self):
		'''возвращает диапозон значений x'''
		return self.__x
		
	def getY(self):
		'''возвращает диапозон значений y'''
		return self.__y
		
	def setAuto(self,axis=(0,1)):
		'''автоматически устанавливает диапозон значений x,y по заданым осям axis из плоттеров'''
		mi=[i.min() for i in self.__plotter_list]
		ma=[i.max() for i in self.__plotter_list]
		x,y=zip(*mi)
		mi=min(x),min(y)
		x,y=zip(*ma)
		ma=max(x),max(y)
		#~ ma=self.__plotter_list[0].max()
		#~ for i in self.__plotter_list:
			#~ mi=mi.min(i.min())
			#~ ma=ma.max(i.max())
		xl=ma[axis[0]]-mi[axis[0]]
		yl=ma[axis[1]]-mi[axis[1]]
		xl*=0.05
		yl*=0.05
		x=mi[axis[0]]-xl,ma[axis[0]]+xl
		y=mi[axis[1]]-yl,ma[axis[1]]+yl
		self.setX(x)
		self.setY(y)
		
	def _x_func(self,i):
		'''возвращает значение x принимает сдвиг i (0.0-1.0)'''
		return (self.__x[1]-self.__x[0])/self.__x_grid_len*i+self.__x[0]
		
	def _y_func(self,i):
		'''возвращает значение y принимает сдвиг i (0.0-1.0)'''
		return (self.__y[1]-self.__y[0])/self.__y_grid_len*(self.__y_grid_len-i)+self.__y[0]
		
	def _x_to_grid(self,x):
		'''возвращает (переводит) координаты холста по x принимает x'''
		return int((x-self.__x[0])/(self.__x[1]-self.__x[0])*self.__x_grid_len)+self.__x_indent
		
	def _y_to_grid(self,y):
		'''возвращает (переводит) координаты холста по y принимает y'''
		return int(self.__y_grid_len-(y-self.__y[0])/(self.__y[1]-self.__y[0])*self.__y_grid_len)+self.__y_indent
		
	def __x_grid(self,marks=10,grid=False,mark_list=None):
		'''отрисовывает метаданные по x принимает
		количество рисок marks флаг отрисовки сетки grid
		список фиксированных меток mark_list'''
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
		'''отрисовывает метаданные по y принимает
		количество рисок marks флаг отрисовки сетки grid
		список фиксированных меток mark_list'''
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
		'''добавляет вертикальную линию в координате x цвета clr
		примечание: не использовать до autoset, setX, setY'''
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
		'''добавляет горизонтальную линию в координате y цвета clr
		примечание: не использовать до autoset, setX, setY'''
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
		'''проверяет находится ли координата холста x на поле графика'''
		if self.__x_indent<x<self.__x_indent+self.__x_grid_len:
			return True
		return False
		
	def _yInGraph(self,y):
		'''проверяет находится ли координата холста y на поле графика'''
		if self.__y_indent<y<self.__y_indent+self.__y_grid_len:
			return True
		return False
		
	def clearXLine(self):
		'''удаляет вертикальные линии'''
		self.__canv.delete('xline')
		self.__canv.update()
				
	def clearYLine(self):
		'''удаляет горизонтальные линии'''
		self.__canv.delete('yline')
		self.__canv.update()
		
	def reGrid(
			self,
			axis=(0,1),
			autoset=True,
			grid=False,
			legend=True,
			xmarks=10,
			ymarks=10,
			x_mark_list=None,
			y_mark_list=None
		):
		'''отрисовывает графики принимает оси для отрисовки axis
		опцию автоматического определения границ autoset
		опцию прорисовки сетки grid
		опцию прорисовки легенды legend
		количество отметок по x xmarks по y ymarks
		макркированые отметки по x x_mark_list по y y_mark_list'''
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
	'''класс для рисования графиков в новом дочернем окне'''
	
	def __init__(self,parrent=None,x=(-25,25),y=(0,100),x_grid_len=500,y_grid_len=500,name='graph'):
		Toplevel.__init__(self,parrent)
		Graph.__init__(self,x=x,y=y,x_grid_len=x_grid_len,y_grid_len=y_grid_len)
		self.title(name)
		
class GraphTk(Tk,Graph):
	'''класс для рисования графиков в окне верхнего уровня'''
	
	def __init__(self,parrent=None,x=(-25,25),y=(0,100),x_grid_len=500,y_grid_len=500,name='graph'):
		Tk.__init__(self)
		Graph.__init__(self,x=x,y=y,x_grid_len=x_grid_len,y_grid_len=y_grid_len)
		self.title(name)

