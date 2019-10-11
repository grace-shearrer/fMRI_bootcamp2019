#randomise

import glob
import os

basedir='/projects/niblab/data/eric_data/W1/milkshake/level3_grace_edit'
f=open('randomise.sh','w')
os.chdir(basedir)

for dir in glob.glob('cope*.gfeat/'):
	print(dir)
	INPUT=os.path.join(basedir,dir,'cope1.feat','filtered_func_data.nii.gz')
	MAT=os.path.join(basedir,dir,'design.mat')
	CON=os.path.join(basedir,dir,'design.con')
#  for region in glob.glob('ROIs/binary_ROI/*.nii.gz'):
#    roi=region.split('/')
#    print(roi)
#    roi2=roi[2].strip('.nii.gz')
#    print(roi2)
#    ROI=os.path.join(basedir, region)
#    name=dir.split('.')
	name=dir.strip('.gfeat/')
#    print(name2)
	out=str(name)+str('_randomized')
	OUTPUT=os.path.join(basedir, out)
	MASK=os.path.join(basedir, dir, 'mask.nii.gz')
	call='/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/randomise -i '+INPUT+' -o '+OUTPUT+' -d '+MAT+' -t '+CON+' -n 5000 -T -m '+MASK
	f.write('%s\n' % (call,))

f.close()


#randomise -i INPUT -o OUTPUT -d MAT -t CON -n 5000 --T -m MASK (whole brain)

