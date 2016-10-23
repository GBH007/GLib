# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

class ReportGenerator:
	
	def __init__(self,name='report'):
		self.report=open(name,'w')
		
	def addText(self,text,end='\n'):
		pass
		
	def addTable(self,table,end='\n'):
		pass
		
	def commitAndExit(self):
		self.report.close()
