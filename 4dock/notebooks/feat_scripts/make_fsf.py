#!/usr/bin/env python

import glob
import os
from subprocess import check_output
#import pdb
import argparse


def create_fsf(basedir,repl_dict,outdir, arglist):
    os.chdir(basedir)
    for sub in glob.glob('sub-*'):
        repl_dict.update({'SUB':sub})

        scan=(os.path.join(sub,'func','%s_task-%s_bold_brain_mcf.nii.gz')%(sub,arglist['TASK']))

        funcrun=os.path.join(basedir,scan)
        repl_dict.update({'FUNCRUN':funcrun})

        ntmpts=check_output(['fslnvols',funcrun])
        repl_dict.update({'NTIMEPOINTS':ntmpts})

        trs=check_output(['fslval','%s'%(funcrun),'pixdim4',scan])
        print(trs)
        repl_dict.update({'TRS':trs})


        output=os.path.join(outdir,sub,'grace_edit',arglist['TASK'])
        repl_dict.update({'OUTPUT':output})            
        anat=os.path.join(basedir,sub,'anat','%s_T1w_brain.nii.gz'%(sub))
        repl_dict.update({'ANAT':anat})

        confounds=os.path.join(basedir,sub,'func','motion_assessment','%s_task-%s_bold_brain_confound.txt'%(sub,arglist['TASK']))
        repl_dict.update({'CONFOUNDS':confounds})
        ctr=0
        for item in arglist['EV']:
            print(item)
            ctr=ctr+1
            repl_dict.update({'EV%iTITLE'%ctr:item})
            ev=os.path.join(basedir,sub,'func','onsets','%s_%s_%s_output.txt'%(sub,arglist['TASK'],item))
            repl_dict.update({'EV%i'%ctr:ev}) 
        for i in range(6):
            motcor=os.path.join(basedir,sub,'func','motion_assessment','%s_task-%s_bold_brain_motcor%i.txt' %(sub,arglist['TASK'],i))
            repl_dict.update({'MOTCOR%i'%i:motcor})

        print(repl_dict)
        if arglist['NOREG']==False:
            with open(os.path.join(basedir,'design.fsf'),'r') as infile:
                tempfsf=infile.read()
                for key in repl_dict:
                    tempfsf = tempfsf.replace(key, repl_dict[key])
                    with open(os.path.join(outdir,sub,'%s_%s.fsf'%(sub,arglist['TASK'])),'w') as outfile:
                        outfile.write(tempfsf)
                    outfile.close()
                infile.close()

        else:
            print("skipping registration")
            with open(os.path.join(basedir,'no_reg_design.fsf'),'r') as infile:
                tempfsf=infile.read()
                for key in repl_dict:
                    tempfsf = tempfsf.replace(key, repl_dict[key])
                    with open(os.path.join(outdir,sub,'%s_%s_no_reg.fsf'%(sub,arglist['TASK'])),'w') as outfile:
                        outfile.write(tempfsf)
                    outfile.close()
                infile.close()
    os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts/feat_scripts')
                       

def main ():
  basedir='/Users/gracer/Desktop/data'
  outdir=os.path.join(basedir,'derivatives','task')
  parser=argparse.ArgumentParser(description='making fsf files')
  parser.add_argument('-noreg',dest='NOREG', action='store_true',
                        default=False, help='Did you already register your data (using ANTZ maybe)?')
  parser.add_argument('-task',dest='TASK',
                        default=False, help='which task are we using?')
  parser.add_argument('-evs',dest='EV',nargs='+',
                        default=False, help='which evs are we using?')

  repl_dict={}
  args = parser.parse_args()
  arglist={}
  for a in args._get_kwargs():
      arglist[a[0]]=a[1]
      print(arglist)
  create_fsf(basedir,repl_dict, outdir, arglist)
main()
os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts/feat_scripts')