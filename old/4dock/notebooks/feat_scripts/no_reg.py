#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:57:25 2017

@author: gracer
"""
import os
import glob
import shutil

def reg_check(basedir,IDmat):
    for sub in glob.glob(os.path.join(basedir,'sub-*','grace_edit','*.feat')):
        
        if os.path.exists(os.path.join(sub,'reg_standard')):
            shutil.rmtree(os.path.join(sub,'reg_standard'))
            print('%s has the reg standard'%sub)
        
        for files in glob.glob(os.path.join(sub,'reg','*.mat')):
            print(files)
            os.remove(files)
        
        shutil.copy2(IDmat,os.path.join(sub,'reg'))
        meanFUNC=os.path.join(sub,'mean_func.nii.gz')
        regDIR=os.path.join(sub,'reg','standard.nii.gz')
        shutil.copy2(meanFUNC,regDIR)
        
                    
        
            
def main(BASEDIR):
    basedir=BASEDIR
    IDmat='/usr/local/fsl/etc/flirtsch/ident.mat'
    reg_check(basedir,IDmat)

if __name__ == "__main__":
    BASEDIR='/Users/gracer/Desktop/data/derivatives/task'
    main(BASEDIR)

#check that reg_standard exists in the first level
#if it exists delete:
#delete all .mat files
#copy the mean_func.nii.gz to reg/standard.nii.gz
#check the voxel intensities in the stats/cope.nii.gz and reg_standard/stats/cope.nii.gz 
#need to be the same (level 1)
#data dimension and pixel size should be the same