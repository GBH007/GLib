# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

class ReportGenerator:
	'''базовый класс отчета'''
	
	def __init__(self,name='report'):
		'''конструктор принимает имя файла для отчета
		открывает этот файл для записи'''
		self.report=open(name,'w')
		
	def addText(self,text):
		'''добавляет текст в файл отчета'''
		pass
		
	def addTable(self,table):
		'''добавляет таблицу в файл отчета'''
		pass
		
	def commitAndExit(self):
		'''закрывает файл отчета'''
		self.report.close()
