#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:22:38 2017

@author: gracer
"""
import shutil
import glob
import os

for folder in glob.glob('/Users/gracer/Desktop/data/derivatives/task/sub-*/grace_edit/bart*.feat'):
    folder2=folder.split('.')[0].strip('.')
    output=folder2+('2.feat')
    shutil.copytree(folder, output)
os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts')