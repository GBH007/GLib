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
			
	def addText(self,text,tag='text'):
		print('<div class="{tag}">{0}</div>'.format(text,tag=tag),file=self.report)
		
	def addTable(self,table,tag='table',selected_row=[],selected_col=[],selected_rc=[]):
		stable=[[str(i) for i in s] for s in table]
		print('<table class="{tag}">'.format(tag=tag),file=self.report)
		tmpl='<td class="{tag}">{0}</td>'
		for i,ei in enumerate(stable):
			print('<tr class="{tag}">'.format(tag=('selected' if i in selected_row else ('r1' if i%2 else 'r0'))),file=self.report)
			for j,ej in enumerate(ei):
				print(tmpl.format(ej,tag=('selected' if ((i,j) in selected_rc) or (j in selected_col) else 'None')),end='',file=self.report)
			print('</tr>',file=self.report)
		print('</table>',file=self.report)
		
	def commitAndExit(self):
		print(end_template,file=self.report)
		ReportGenerator.commitAndExit(self)
		

