# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
import sys
sys.path.append('../src/')
#~ from GLib.graph import *
#~ from GLib.point import *
from GLib.easygraph import *
		
def main():
	g=GraphTk()
	f=lambda x: x**2
	f1=lambda x: x**3
	f2=lambda x: x
	x=[i/10 for i in range(-20,20)]
	y=[f(i) for i in x]
	y1=[f1(i) for i in x]
	y2=[f2(i) for i in x]
	names=['x='+str(i) for i in x]
	p=LinePlotter(g,x,y,'blue','p',2,names)
	p1=LinePlotter(g,x,y1,'green','p11',0.5,names)
	p2=PointPlotter(g,x,y1,'red','p1',2,names)
	p3=RectanglePlotter(g,x,y,'yellow','p12',2,names)
	p4=CrossPlotter(g,x,y2,'magenta','p13',2,names)
	g.addPlotters(p,p1,p3,p4)
	g.addPlotter(p2)
	g.setX((-2,2))
	g.setY((-2,2))
	g.reGrid(grid=True,autoset=0,point_info=1,legend=1)
	g.mainloop()
def main1():
	g=GraphTk()
	x=[i for i in range(-10,10)]
	y=[abs(i) for i in x]
	p=GistPlotter(g,x,y,'blue','111')
	g.addPlotter(p)
	g.reGrid(autoset=1,ymarks=0,xmarks=0,x_mark_list=range(-10,10,3),y_mark_list=range(0,12),grid=1,point_info=1)
	g.mainloop()
if __name__=='__main__':
	main()
