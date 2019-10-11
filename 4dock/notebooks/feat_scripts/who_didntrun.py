import os
import glob
import fnmatch
import shutil

basedir='/projects/niblab/data/eric_data/'
os.chdir(basedir)
for dir in glob.glob('W1/milkshake/level1_grace_edit/fail/*.feat/'):
	dir2=dir.split('/')
	name=dir2[4]
	newfile=os.path.join(basedir,'W1','milkshake','level1_grace_edit',name)
	if os.path.exists(newfile):
		print (' ')
	else:
		print(newfile+' DOES NOT EXIST')
