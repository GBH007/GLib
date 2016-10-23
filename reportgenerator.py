# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

__all__=['HTMLReportGenerator']

class ReportGenerator:
	
	def __init__(self,name='report'):
		self.report=open(name,'w')
		
	def addText(self,text,end='\n'):
		pass
		
	def addTable(self,table,end='\n'):
		pass
		
	def commitAndExit(self):
		self.report.close()
		
class TXTReportGenerator(ReportGenerator):
	
	def addText(self,text,end='\n'):
		print(text,end=end,file=self.report)
		
	def addTable(self,table,end='\n'):
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

class HTMLReportGenerator(ReportGenerator):
	
	def __init__(self,name):
		ReportGenerator.__init__(self,name)
		tmpl='''<html><head>
		<style type="text/css">
		.table{
			border: 2px solid black;
			text-align: center;
		}
		tr:hover{
			background-color: yellow;
		}
		.selected{
			border: 2px solid red;
			background-color: red;
		}
		.r0{
			background-color: #BFBFBF;
		}
		.r1{
			background-color: white;
		}
		.None{
		}
		.text{
		}
		</style>
		<title>Report</title>
		</head><body>'''
		print(tmpl,file=self.report)
		
		
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
		print('</body></html>',file=self.report)
		ReportGenerator.commitAndExit(self)
		
def main():
	#~ a=TXTReportGenerator('/home/gbh007/report.txt')
	b=HTMLReportGenerator('/home/gbh007/report.html')
	txt='hello world!'
	table=[['-'*(i+j+1) for j in range(4)] for i in range(5)]
	#~ a.addText(txt)
	b.addText(txt)
	#~ a.addTable(table)
	b.addTable(table,selected_row=[1,4],selected_rc=[(0,1)],selected_col=[0])
	b.addTable(table)
	#~ a.commitAndExit()
	b.commitAndExit()

if __name__=='__main__':
	main()
