#this script will make sure there are 28 cope directories, else it will move it to a fail folder
import os
import glob
import fnmatch
import shutil

basedir='/projects/niblab/data/eric_data/W1/milkshake/level3_grace_edit'
os.chdir(basedir)
for dir in glob.glob('*risk_int.gfeat/cope1.feat/stats/'):
	print(dir)
	os.chdir(os.path.join(basedir,dir))
	if len(glob.glob('cope*.nii.gz'))==7:
    		print(dir+' has 7 cope files')
	else:
		print(dir+' is missing copes, need to rerun')
    		file=os.path.join(basedir, dir)
    		fail=os.path.join(basedir,'fail',dir)
    		shutil.move(file,fail)
