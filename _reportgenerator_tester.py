# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from reportgenerator import *

def main():
	#~ a=TXTReportGenerator('/home/gbh007/report.txt')
	b=HTMLReportGenerator('/home/gbh007/report.html')
	txt='hello world1!'
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
