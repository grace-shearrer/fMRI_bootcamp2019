import os
import glob

#fslmaths filtered_func -mul scaleF -dev mean_func -mul mask output
#fslmeants -i output -m mask
#basedir='/corral-repl/utexas/poldracklab/data/sugar_brain/group_ana/'
basedir='/projects/niblab/data/eric_data/W1/milkshake/level3_grace_edit'
os.chdir(basedir)
f=open('percent_change.sh', 'w')
for dir in glob.glob('cope*/cope*/cope1.feat/'):
  ff_data=os.path.join(basedir,dir,'filtered_func_data')
  mean_data=os.path.join(basedir,dir,'mean_func')
  mask_im=os.path.join(basedir,dir,'mask')
  output=os.path.join(basedir, dir, 'change_im')
  command= 'fslmaths '+ff_data+' -mul 1 -div '+mean_data+' -mul '+mask_im+' '+output+'%s\n echo starting '+dir
  f.write('%s\n' % (command,))
f.close()
