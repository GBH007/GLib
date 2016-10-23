# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from ..report import ReportGenerator
from .html_template import *

__all__=['HTMLReportGenerator']

class HTMLReportGenerator(ReportGenerator):
	
	def __init__(self,name):
		ReportGenerator.__init__(self,name)
		print(start_template.format(css=css_template),file=self.report)
			
	def addText(self,text,tag='text',newline=True):
		'''добавляет текст с тегом tag в файл отчета
		если newline истина переводит каретку на новую строку'''
		print('<div class="{tag}">{0}</div>'.format(text,tag=tag),file=self.report)
		if newline:self.addNewLine()
		
	def addNewLine(self):
		'''переводит каретку на новую строку'''
		print('<br>',file=self.report)
		
	def addTable(
			self,
			table,
			tag='table',
			selected_row=[],
			selected_col=[],
			selected_rc=[],
			col_names=None,
			row_names=None,
			table_name='table',
			newline=True,
		):
		'''добавляет таблицу с тегом tag в файл отчета принимает аргументы
		список выделеных строк selected_row (выделяются красным)
		список выделеных столбцов selected_col (выделяются красным)
		список выделеных ячеек selected_rc (выделяются красным)
		список названий столбцов col_names
		список названий строк row_names
		название таблицы table_name (пишеться) если есть название строк и столбцов
		если newline истина переводит каретку на новую строку'''
		stable=[[str(i) for i in s] for s in table]
		print('<table class="{tag}">'.format(tag=tag),file=self.report)
		tmpl='<td class="{tag}">{0}</td>'
		if col_names:
			print('<tr>',file=self.report)
			if row_names:
				print('<td>{0}</td>'.format(table_name),file=self.report)
			for i in range(len(stable[0])):
				try:
					print('<td>{0}</td>'.format(col_names[i]),file=self.report)
				except IndexError:
					print('<td></td>',file=self.report)
			print('</tr>',file=self.report)
		for i,ei in enumerate(stable):
			print('<tr class="{tag}">'.format(tag=('selected' if i in selected_row else ('r1' if i%2 else 'r0'))),file=self.report)
			if row_names:
				try:
					print('<td>{0}</td>'.format(row_names[i]),file=self.report)
				except IndexError:
					print('<td></td>',file=self.report)
			for j,ej in enumerate(ei):
				print(tmpl.format(ej,tag=('selected' if ((i,j) in selected_rc) or (j in selected_col) else 'None')),end='',file=self.report)
			print('</tr>',file=self.report)
		print('</table>',file=self.report)
		if newline:self.addNewLine()
		
	def commitAndExit(self):
		print(end_template,file=self.report)
		ReportGenerator.commitAndExit(self)
		

