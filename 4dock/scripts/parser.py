#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:31:42 2019

@author: gracer
"""

import glob
import os
import pandas as pd
import numpy as np
import pdb
basedir='/Users/gracer/Downloads/ds001966-1.0.1'

sub_dict={}
for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*_task-doubleauction_events.tsv')):
    sub=item.split('/')[5]
    sub_dict[sub]=item
    
for key, item in sub_dict.items():
    df=pd.read_csv(item,'\t')
    df['onset'] = df['onset'].round(3)
    df['duration'] = df['duration'].round(3)
    pics=df.loc[df['Event Type'] == 'Picture']
    pics['Event Type'].loc[pics['Event Type'] == 'Picture']= 1
    resp=df.loc[df['Event Type'] == 'Response']
    resp['Event Type'].loc[resp['Event Type'] == 'Response']= 1
    savedir=os.path.join(basedir,key,'func')
    resp.to_csv(os.path.join(savedir,'%s_resp.txt'%key), sep=' ',columns=['onset','duration','Event Type'] ,index=False, header=False)
    pics.to_csv(os.path.join(savedir,'%s_pics.txt'%key), sep=' ',columns=['onset','duration','Event Type'], index=False, header=False)

x=sub_dict['sub-04']
x
df=pd.read_csv(x,'\t')
df['onset'] = df['onset'].round(3)
df['duration'] = df['duration'].round(3)
pics=df.loc[df['Event Type'] == 'Picture']
pics['Event Type'].loc[pics['Event Type'] == 'Picture']= 1
resp=df.loc[df['Event Type'] == 'Response']
resp['Event Type'].loc[resp['Event Type'] == 'Response']= 1
savedir=os.path.join(basedir,'sub-04','func')
resp.to_csv(os.path.join(savedir,'%s_resp.txt'%'sub-04'), sep=' ',columns=['onset','duration','Event Type'] ,index=False, header=True)
pics.to_csv(os.path.join(savedir,'%s_pics.txt'%'sub-04'), sep=' ',columns=['onset','duration','Event Type'], index=False, header=True)