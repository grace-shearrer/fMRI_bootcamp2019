#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:47:27 2018

@author: gracer
"""

num_scrub = #some number that is ~25% of TRS

for dir in glob.glob(os.path.join(<PATH TO THE FUNC DATA>)): #path to the functional, skull stripped data
    print(dir)#not needed but i get crazy 
    if not os.path.exists(os.path.join(dir,'motion_assessment')): #looking for a motion assessment dir to put out put in, I like to put it in my functional directory where my skull stripped brain is
        os.makedirs(os.path.join(dir,'motion_assessment')) #making dir if it doesn't exist
    for input in glob.glob(os.path.join(dir,'*brain.nii.gz')):
        output=input.split('.')[0]
        print(output)
        ###this is generating the fd confounds txt, it is using the fd metric, making a plot and putting it in the motion assessment directory we made above
        os.system("fsl_motion_outliers -i %s -o motion_assessment/%s_confound.txt --nomoco  --fd --thresh=%s -p motion_assessment/fd_plot -v > motion_assessment/%s_outlier_output.txt"%(output,output,arglist['MOCO'],output))
        ####this is writing the motion assessment fd metric to the html file
        os.system("cat motion_assessment/%s_outlier_output.txt >> %s"%(output,outhtml))
        ###getting the full path to the plot
        plotz=os.path.join(basedir,dir,'motion_assessment','fd_plot.png')
        #### putting the full plot in the html file
        os.system("echo '<p>=============<p>FD plot %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(output,plotz,'100%', outhtml))
        ####sometimes you have a great subject who didn't move, in this case we want to make a blank file
        if os.path.isfile("motion_assessment/%s_confound.txt"%(output))==False:
            os.system("touch motion_assessment/%s_confound.txt"%(output))
            
        check = subprocess.check_output("grep -o 1 motion_assessment/%s_confound.txt | wc -l"%(output), shell=True) #how many columns are there = how many 'bad' points
        
            
        if check>num_scrub: #if the number in check is greater than num_scrub then we don't want it
            with open(out_bad_bold_list, "a") as myfile: #making a file that lists all the bad ones
                myfile.write("%s\n"%(output))
            myfile.close()
            
 