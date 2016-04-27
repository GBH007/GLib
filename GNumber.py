# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
def prost(n):
	s=[2,]
	for i in range(2,n):
		for j in s:
			if i%j==0:break
		else:s.append(i)
	return s
def eiler(n):
	p=prost(int(n**0.5)+1)
	s=1
	for i in p:
		if n%i==0:
			n//=i
			s*=i-1
	return s*n
def main():
	print(eiler(3000000))

if __name__=='__main__':
	main()
