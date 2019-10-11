#!/usr/bin/env python

import os
import glob
import argparse
#import pdb

def create_fsf2(basedir,repl_dict, indir,arglist):
    if arglist['TASK']==False:
        print("please say which task to run on")
    else:
        print('start')
        for dir in glob.glob(os.path.join(indir,'sub-*','grace_edit')):
            feats=glob.glob(os.path.join(dir,'%s*.feat'%arglist['TASK']))
            repl_dict.update({'SECOND':feats[1]})
            repl_dict.update({'FUNCRUN':feats[0]})
            sub=dir.split('/')[7]
            repl_dict.update({'SUB':sub})
            output=os.path.join(dir,'%s.gfeat'%arglist['TASK'])
            repl_dict.update({'OUTPUT':output})
            print(repl_dict)
            with open(os.path.join(basedir,'design2.fsf'),'r') as infile:
                tempfsf=infile.read()
                for key in repl_dict:
                    tempfsf = tempfsf.replace(key, repl_dict[key])
                    with open(os.path.join(dir,'%s_second.fsf'%(arglist['TASK'])),'w') as outfile:
                        outfile.write(tempfsf)
                    outfile.close()
            infile.close()      

def main():
    repl_dict={}
    basedir='/Users/gracer/Desktop/data'
    indir=os.path.join(basedir,'derivatives','task')
    repl_dict={}

    parser=argparse.ArgumentParser(description='making fsf files')
    parser.add_argument('-task',dest='TASK',
                        default=False, help='which task are we using?')

    args = parser.parse_args()
    arglist={}

    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)

    create_fsf2(basedir,repl_dict, indir,arglist)

main()
os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts/feat_scripts')