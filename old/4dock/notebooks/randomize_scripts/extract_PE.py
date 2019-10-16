import os
import fnmatch
import glob
basedir='/projects/niblab/data/eric_data/W1/milkshake/level3_grace_edit'
f=open('PE_extraction.sh','w')

for dir in glob.glob('cope*_risk.gfeat/cope1.feat/'):
  print(dir)
  INPUT1=os.path.join(basedir, dir, 'filtered_func_data.nii.gz')
  INPUT2=os.path.join(basedir, dir, 'mean_func.nii.gz')
  for file in glob.glob('random_insulin/cluster_index_cope*mask.nii.gz'):
    MASK=os.path.join(basedir,file)
    name=MASK.split('/')
    name2=name[8].strip('mask.nii.gz')
    OUTPUT=os.path.join(basedir, name2)
    call='fslmaths '+INPUT1+' -div '+INPUT2+' -mul '+MASK+' '+OUTPUT+'_PE'
    f.write('%s\n' % (call,))
  for file in glob.glob('random_insulin/cluster_index_cope*mask2.nii.gz'):
    MASK=os.path.join(basedir,file)
    name=MASK.split('/')
    name2=name[8].strip('mask2.nii.gz')
    OUTPUT=os.path.join(basedir, name2)
    call='fslmaths '+INPUT1+' -div '+INPUT2+' -mul '+MASK+' '+OUTPUT+'_PE'
    f.write('%s\n' % (call,))
f.close()
