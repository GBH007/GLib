# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

import os
import sys
import shutil
import glob
from urllib.request import urlretrieve
import zipfile
from urllib.request import urlopen
import json
import urllib.error

_DEFAULT_LOAD_DIR=os.getcwd()
_DEFAULT_TMP_FILE='tmp.zip'
_DEFAULT_REPO_LOAD_TEMPLATE='https://github.com/{owner}/{repo}/archive/{branch}.zip'
_DEFAULT_REPO_INFO_TEMPLATE='https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}'
_DEFAULT_LIBAPPENDER_NAME='glib_appender.py'
_DEFAULT_LIBAPPENDER_TEMPLATE="""
link={link}
import sys
sys.path.append(link)
"""

class Loader:
	
	def __init__(
			self,
			repo_owner,
			repo_name,
			branch_name,
			repo_info_template=_DEFAULT_REPO_INFO_TEMPLATE,
			repo_load_template=_DEFAULT_REPO_LOAD_TEMPLATE,
			load_dir=_DEFAULT_LOAD_DIR,
			default_tmp_file=_DEFAULT_TMP_FILE,
		):
		self.repo_load_template=repo_load_template
		self.load_dir=load_dir
		self.repo_owner=repo_owner
		self.default_tmp_file=default_tmp_file
		self.repo_name=repo_name
		self.branch_name=branch_name
		self.repo_info_template=repo_info_template
		try:
			self.last_commit=json.load(open('.last_commit_info'))
		except (FileNotFoundError,json.decoder.JSONDecodeError):
			self.last_commit=None
			
	def run(self,force=False,libapp=False):
		last_com=self.getLastCommit()
		if force or not self.last_commit or last_com[0]>self.last_commit[0]:
			print('Производится загрузка новой версии')
			self.load()
			print('Производится распаковка новой версии')
			self.decompress()
			print('Производится очистка ресурсов')
			self.clear()
			print('Производится обновление информации')
			self.last_commit=last_com
			json.dump(last_com,open('.last_commit_info','w'))
			print('Обновление завершено')
		else:
			print('Используется последняя версия')
		if libapp:
			self.createLibAppender()
			
	def _fullTmpPath(self):
		return os.path.join(self.load_dir,self.default_tmp_file)
		
	def load(self):
		try:
			urlretrieve(
				self.repo_load_template.format(
					repo=self.repo_name,
					branch=self.branch_name,
					owner=self.repo_owner
				),
				self._fullTmpPath()
			)
		except urllib.error.HTTPError:
			print('Ошибка загрузки с Github')
			sys.exit(1)
			
	def remove(self,name):
		fl=[name,]
		while fl:
			f=fl[-1]
			if os.path.isdir(f):
				l=glob.glob(os.path.join(f,'*'))
				for i in l:
					if os.path.isdir(i):
						fl.append(i)
					else:
						try:
							os.remove(i)
						except FileNotFoundError:
							pass
				if not l:
					os.rmdir(f)
					fl.pop()
			else:
				try:
					os.remove(f)
				except FileNotFoundError:
					pass
				fl.pop()
				
	def decompress(self):
		zf=zipfile.ZipFile(self._fullTmpPath(),'r')
		zf.extractall(path=self.load_dir)
		dn=os.path.join(self.load_dir,zf.namelist()[0][:-1],'src')
		for i in glob.glob(os.path.join(dn,'*')):
			fn=os.path.relpath(i,dn)
			self.remove(os.path.join(self.load_dir,fn))
			shutil.move(i,self.load_dir)
		self.remove(os.path.join(self.load_dir,zf.namelist()[0][:-1]))
		zf.close()
		
	def getLastCommit(self):
		try:
			data=urlopen(
				self.repo_info_template.format(
					repo=self.repo_name,
					owner=self.repo_owner,
					branch=self.branch_name
				)
			).read()
		except urllib.error.HTTPError:
			print('Ошибка соединения с Github')
			sys.exit(1)
		data_hesh=json.loads(data.decode())
		commits=[(
			i['commit']['committer']['date'],
			i['sha'],
			i['commit']['message']
		) for i in data_hesh]
		commits.sort()
		return commits[-1]
		
	def createLibAppender(self):
		link=os.getcwd()
		f=open(_DEFAULT_LIBAPPENDER_NAME,'w')
		f.write(_DEFAULT_LIBAPPENDER_TEMPLATE.format(link=link))
		f.close()
		
	def clear(self):
		os.remove(self._fullTmpPath())

	
def main():
	l=Loader('GBH007','GLib','master')
	l.run(force=False,libapp=False)

if __name__=='__main__':
	main()
