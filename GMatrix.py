# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
class MatrixError(Exception):pass
class Matrix:
	def __init__(self,m=None,vcol=None,vrow=None):
		self.__m=m if m else [[i,] for i in vcol] if vcol else [[i for i in vrow],] if vrow else []
	def set(self,m):
		self.__m=m
	def get(self):
		return self.__m
	def getList(self):
		return [j for i in self.__m for j in i]
	def getRadius(self):
		return sum(map(lambda x:x**2,self.getList()))**0.5
	def len(self):
		return (len(self.__m),len(self.__m[0]))
	def __abs__(self):return self.det()
	def det(self,m=None):
		m=m if m else self.get()
		n=len(m)
		return sum([(-1)**l*m[0][l]*self.det([[m[i][j] for j in range(n) if j!=l] for i in range(1,n)]) if n>1 else (-1)**l*m[0][0] for l in range(n)])
	def trans(self):
		return Matrix(list(zip(*self.get())))
	def ematrix(self,n=None):
		n=n if n else self.len()[0]
		return Matrix([[1 if i==j else 0 for j in range(n)] for i in range(n)])
	def _con(self):
		m=self.get()
		n=self.len()[0]
		c=[[(-1)**(i+j)*self.det([[m[i1][j1] for j1 in range(n) if j!=j1] for i1 in range(n) if i!=i1]) for j in range(n)] for i in range(n)] if n>1 else [[m[0][0]]]
		return Matrix(c)
	def __str__(self):
		return '\n'.join([' '.join([str(j) for j in i]) for i in self.get()])
	def __round__(self,k):
		return Matrix([[round(j,k) for j in i] for i in self.get()])
	def __lshift__(self,k):
		return Matrix([[j*k for j in i] for i in self.get()])
	def __rshift__(self,k):
		return Matrix([[j/k for j in i] for i in self.get()])
	def __mul__(self,other):
		m=self.get()
		b=other.get()
		n=self.len()
		n1=other.len()
		if n1[0]!=n[1]:raise MatrixError
		return Matrix([[sum([m[i][l]*b[l][j] for l in range(n1[0])]) for j in range(n1[1])] for i in range(n[0])])
	def __invert__(self):
		return self._con().trans()>>self.det()
	def __truediv__(self,other):
		return self*~other
	def format(self,n1=None,n2=None):
		m=self.get()
		n=self.len()
		n1,n2=n1 if n1 else n[0],n2 if n2 else n[1]
		return Matrix([[m[i][j] if i<n[0] and j<n[1] else 0 for j in range(n2)] for i in range(n1)])
	def __add__(self,other):return self.__sum(other)
	def __sub__(self,other):return self.__sum(other,-1)
	def __sum(self,other,sign=1):
		n=tuple(map(max,self.len(),other.len()))
		m=self.format(*n).get()
		m1=other.format(*n).get()
		return Matrix([[m[i][j]+m1[i][j]*sign for j in range(n[1])] for i in range(n[0])])
		
def main():
	m=Matrix()
	print((m.ematrix(6).format(10,1)+m.ematrix(5).format(10,1)).getRadius())
if __name__=='__main__':
	main()
		
