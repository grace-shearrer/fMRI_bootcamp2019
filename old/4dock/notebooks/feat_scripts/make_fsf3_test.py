#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:57:01 2017

@author: gracer
"""
import os
import glob
import argparse
import pdb

def create_fsf2(basedir,repl_dict, indir,arglist):
    for item in arglist['COPE']:
        print item
        feats=glob.glob(os.path.join(basedir,'derivatives','task','sub-*','grace_edit','%s.gfeat'%arglist['TASK'],'cope%s.feat'%item))
        inputdir=len(feats)
        repl_dict.update({'INPUTDIR':str(inputdir)})
#        cope='cope'+str(item)
        output=os.path.join(basedir,'derivatives','task','%s_%s.gfeat'%(arglist['TASK'],item))
        repl_dict.update({'OUTPUT':output})
        i=0



        pdb.set_trace()
          
        with open(os.path.join(basedir,'level3_test.fsf'),'r') as infile:
            tempfsf=infile.read()
            pdb.set_trace()
            for key in repl_dict:
                pdb.set_trace()
                tempfsf = tempfsf.replace(key, repl_dict[key])
                pdb.set_trace()
                with open(os.path.join(basedir,'%s_second.fsf'%(arglist['TASK'])),'w') as outfile:
                    pdb.set_trace()
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
    parser.add_argument('-cope',dest='COPE',
                    default=False, help='which copes are we using?')


    args = parser.parse_args()
    arglist={}

    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)

    create_fsf2(basedir,repl_dict, indir,arglist)

main()
os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts/feat_scripts')