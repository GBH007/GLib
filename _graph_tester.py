# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
import sys
sys.path.append('/home/gbh007/Dropbox/python/lib')
from GLib.graph import *
from GLib.point import *
		
def main():
	g=GraphTk()
	p=Points()
	p1=Points()
	f=lambda x: x**2
	f1=lambda x: x**3
	for i in range(-20,20):
		p.add((i/10,f(i/10)))
		p1.add((i/10,f1(i/10)))
	g.addPlotter(LinePlotter(g,p,'blue','p',2))
	g.addPlotter(PointPlotter(g,p1,'red','p1',2))
	g.setX((-2,2))
	g.setY((-2,2))
	g.addXLine(1)
	g.addYLine(1)
	g.reGrid(grid=True,autoset=False)
	g.mainloop()
def main1():
	g=GraphTk()
	p=Points()
	p.add((1,),1)
	p.add((2,),2)
	p.add((3,),3)
	p.add((4,),2)
	p.add((5,),1)
	p.add((6,),0)
	g.addPlotter(GistPlotter(g,p,'blue'))
	g.setX((0,6))
	g.setY((0,5))
	g.reGrid(autoset=1)
	g.mainloop()
if __name__=='__main__':
	main1()
