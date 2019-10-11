#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:55:43 2017

@author: gracer
"""
import glob
import os
import shutil

#mcflirtdefault='-plots -sinc_final'
#'betfunc':"'bet %s/bold_mcf.nii.gz %s/bold_mcf_brain.nii.gz -F
#'bet %s %s -f 0.3 -R,

basedir='/Users/gracer/Desktop/data'

os.chdir(basedir)
trash='/Users/gracer/Desktop/trash'

for nifti in glob.glob(os.path.join(basedir,'sub-*/anat')):
    if os.path.exists(os.path.join(basedir,nifti,'motion_assessment')):
        shutil.rmtree(os.path.join(basedir,nifti,'motion_assessment'))
    os.chdir(os.path.join(basedir, nifti))
#    for input in glob.glob('*brain*'):
#        os.remove(input)
    for input in glob.glob('*defaced*'):
        os.remove(input)
    

#for dir in glob.glob("/Users/gracer/Desktop/data/derivatives/task/sub-*"):
#    model=os.path.join(dir,'grace_edit')
#    if os.path.exists(model):
#        print("already here baby")
#    else:
#        os.makedirs(model)