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
	x=[i/10 for i in range(-20,20)]
	y=[f(i) for i in x]
	y1=[f1(i) for i in x]
	names=['x='+str(i) for i in x]
	p=LinePlotter(g,x,y,'blue','p',2,names)
	#~ g.addPlotter(LinePlotter(g,p,'blue','p',2))
	#~ g.addPlotter(LinePlotter(g,p1,'green','p11',0.5))
	#~ g.addPlotter(PointPlotter(g,p1,'red','p1',2))
	p1=LinePlotter(g,x,y1,'green','p11',0.5,names)
	p2=PointPlotter(g,x,y1,'red','p1',2,names)
	g.addPlotters(p,p1)
	g.addPlotter(p2)
	g.reGrid(grid=True,autoset=1,point_info=1,legend=0)
	g.mainloop()
def main1():
	g=GraphTk()
	x=[i for i in range(-10,10)]
	y=[abs(i) for i in x]
	p=GistPlotter(g,x,y,'blue','111')
	g.addPlotter(p)
	#~ g.setX((0,6))
	#~ g.setY((0,5))
	#~ g.reGrid(autoset=1,ymarks=0,xmarks=0,x_mark_list=[0,1,2,3,4,5,6],y_mark_list=[0,1,2,3,4,5,6],grid=1)
	g.reGrid(autoset=1,ymarks=0,xmarks=0,x_mark_list=range(-10,10,3),y_mark_list=range(0,12),grid=1,point_info=1)
	g.mainloop()
if __name__=='__main__':
	main()
