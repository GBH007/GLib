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
		print('<div class="{tag}">{0}</div>'.format(text,tag=tag),file=self.report)
		if newline:self.addNewLine()
		
	def addNewLine(self):
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
		

