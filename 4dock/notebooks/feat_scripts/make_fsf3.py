import os
import glob
import sys

#set feat_files(13) "/vxfsvol/home/research/sticelab/Chocolate/W1/milkshake/level2_fix/cs014.gfeat/cope1.feat"

basedir='/projects/niblab/data/eric_data/W1/milkshake/level2_grace_edit'
os.chdir(basedir)
i=0
for dir in glob.glob('*.gfeat'):
	x=os.path.join(basedir, dir,'cope1.feat')
	i=i+1
	print('set feat_files('+str(i)+') '+'"'+x+'"')
