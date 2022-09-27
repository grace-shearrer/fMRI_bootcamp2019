import sys
import glob
import os
from subprocess import check_output
#cs154_mkC.feat
#cs154_mkC
def create_fsf(basedir,subdir,repl_dict):
	os.chdir(subdir)
	for dir in glob.glob('cs*/BOLD/mk*_brain.nii.gz'):
		sub0=dir.split('/')
		sub1=sub0[0]
    		repl_dict.update({'NAME':sub1})
		run=sub0[2].strip('_brain.nii.gz')
		sub=sub1+'_'+run
    		repl_dict.update({'SUB':sub})
      		funcrun=os.path.join(subdir,dir)
      		repl_dict.update({'FUNCRUN':funcrun})
      		print repl_dict
      		ntmpts=check_output(['fslnvols',funcrun])
      		repl_dict.update({'NTIMEPOINTS':ntmpts})
		sub_file=sub+'.fsf'
     		with open(os.path.join(basedir, 'scripts','milkshake','feat_scripts','new_level1.fsf'),'r') as infile:
        		tempfsf=infile.read()
        		for key in repl_dict:
         			tempfsf = tempfsf.replace(key, repl_dict[key])
          			with open(os.path.join(basedir, 'data','eric_data','design_files','milkshake','grace_edit',sub_file),'w') as outfile:
            				outfile.write(tempfsf)
            				os.chdir(os.path.join(basedir,'scripts','milkshake'))

def main ():
  basedir='/projects/niblab/'
  subdir='/projects/niblab/data/eric_data/W1/subjects'
  repl_dict={}
  create_fsf(basedir,subdir,repl_dict)
main()
