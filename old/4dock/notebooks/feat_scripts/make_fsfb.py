import sys
import glob
import os
from subprocess import check_output
#cs154_mkC.feat
#cs154_mkC
def create_fsf(basedir,subdir,repl_dict):
	os.chdir(subdir)
	for dir in glob.glob('*/milkshake/*.nii.gz'):
		sub0=dir.split('/')
		sub=sub0[0]
#    		repl_dict.update({'DIR':dir})
    		repl_dict.update({'SUB':sub})
		cond=sub0[2]
    		repl_dict.update({'COND':cond})
#    		os.chdir(os.path.join(subdir,dir))
#    		for name in glob.glob('BOLD/wtp_run*'):
#      		funcrun='filtered_func_data_clean.nii.gz'
#      		funcrun=funcrun.strip('BOLD/')
#      		repl_dict.update({'FUNCRUN':funcrun})
#      		runnum2=funcrun.split("_")[1]
      			#print runnum2
#      		runnum=runnum2.strip('run0')
      			#print runnum
#      		repl_dict.update({'RUNNUM':runnum})
      		print repl_dict
#      		os.chdir(os.path.join(basedir,dir,name))
#      		ntmpts=check_output(['fslnvols',cond])
#      		repl_dict.update({'NTIMEPOINTS':ntmpts})
		cond2=cond.split('.')
		cond1=cond2[0]
    		repl_dict.update({'COND1':cond1})
		sub_file=sub+'_'+cond1+'.fsf'
     		with open(os.path.join(basedir, 'scripts','milkshake','designb.fsf'),'r') as infile:
        		tempfsf=infile.read()
        		for key in repl_dict:
         			tempfsf = tempfsf.replace(key, repl_dict[key])
#          			with open(basedir + dir + '/wtp_model/' + 'run0'+runnum + '.fsf','w') as outfile:
          			with open(os.path.join(basedir, 'data','eric_data','design_files','milkshake','grace_edit',sub_file),'w') as outfile:
            				outfile.write(tempfsf)
            				os.chdir(os.path.join(basedir,'scripts','milkshake'))

def main ():
  basedir='/projects/niblab/'
  subdir='/projects/niblab/data/eric_data/W1/subjects/'
  repl_dict={}
  create_fsf(basedir,subdir,repl_dict)
main()
