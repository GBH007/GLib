# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

import sys
sys.path.append('../src/')
from GLib.matrix import Matrix

def main():
	a=Matrix([
		[1,2,3],
		[4,5,6],
		[7,8,9],
	])
	a1=Matrix([
		[1,2,3],
		[4,5,6],
		[7,8,9],
		[10,11,12],
	])
	b=Matrix(vcol=[1,2,3])
	b1=Matrix([
		[1,2,3],
		[4,5,6],
		[7,8,9],
	])
	print(a*b,'\n')
	print(a1*b,'\n')
	print(a*b1,'\n')
	m=Matrix()
	m=m.ematrix(4)
	print(m,'\n')
	m14=m.format(1,4)
	m42=m.format(4,2)
	m33=m.format(3,3)
	print(m14,'\n')
	print(m42,'\n')
	print(m33,'\n')
	print(a.trans(),'\n')

if __name__=='__main__':
	main()
