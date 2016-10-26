# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

import sys
sys.path.append('/home/gbh007/Dropbox/python/lib')
from GLib import *
#~ from reportgenerator import *

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
	b.addTable(table,col_names=['col {0}'.format(i) for i in range(10)],row_names=['row {0}'.format(i) for i in range(10)],table_name='tttt')
	#~ a.commitAndExit()
	b.commitAndExit()

if __name__=='__main__':
	main()
