# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from ..report import ReportGenerator

__all__=['TXTReportGenerator']

class TXTReportGenerator(ReportGenerator):
	'''класс для отчетов в txt файле'''
	
	def addText(self,text,end='\n'):
		'''добавляет текст в файл отчета записывает в конец end'''
		print(text,end=end,file=self.report)
		
	def addTable(self,table,end='\n'):
		'''добавляет таблицу в файл отчета записывает в конец end'''
		stable=[[str(i) for i in s] for s in table]
		mlen=max(max(len(j) for j in i) for i in stable)
		ylen=len(stable)
		xlen=len(stable[0])
		sep='-'*((1+mlen)*xlen+1)
		tmpl='|{0:'+str(xlen)+'}'
		print(sep,file=self.report)
		for i,ei in enumerate(stable):
			for j,ej in enumerate(ei):
				print(tmpl.format(ej),end='',file=self.report)
			print('|',file=self.report)
			print(sep,file=self.report)
