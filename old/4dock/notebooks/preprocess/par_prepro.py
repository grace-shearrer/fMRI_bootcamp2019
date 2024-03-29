#!/usr/bin/env python
import glob
import os
#import pdb
import datetime
import argparse
import shutil
import subprocess
from multiprocessing import Pool

def prepro(basedir, args, arglist, outhtml, out_bad_bold_list,DATA):
#def better(args,arglist,basedir):
    #bet
    if args.STRIP==True:
        print("starting bet")

        for sub in DATA:
            for nifti in glob.glob(os.path.join(sub,'func','sub-*_task-%s_bold.nii.gz')%(arglist['TASK'])):
                input=nifti
                output=nifti.strip('.nii.gz')
                if os.path.exists(output+'_brain.nii.gz'):
                    print(output+' exists, skipping')
                else:
                    BET_OUTPUT=output+'_brain'
                    x=("/usr/local/fsl/bin/bet %s %s -F"%(input, BET_OUTPUT))
                    os.system(x)
                    

#bet rage
    if args.RAGE==True:
        print("starting bet rage")
        for sub in DATA:
            for input in glob.glob(os.path.join(sub,'anat','*T1w.nii.gz')):
                output=input.strip('.nii.gz')
                print(output)
                if os.path.exists(output+'_brain.nii.gz'):
                    print(output+' exists, skipping')
                else:
                    BET_OUTPUT=output+'_defaced'
                    x=("/usr/local/fsl/bin/bet %s %s -R"%(input, BET_OUTPUT))
                    print(x)
                    os.system(x)
                    

       
#motion correction
    if args.MOCO==False:
        print("No moco ")
    else:
        print("starting motion correction")
        for sub in DATA:
            for dir in glob.glob(os.path.join(sub,'func')):
                print(dir)
                if not os.path.exists(os.path.join(dir,'motion_assessment')):
                    os.makedirs(os.path.join(dir,'motion_assessment'))
                for input in glob.glob(os.path.join(dir,'*bart*brain.nii.gz')):
                    output=input.split('.')[0]
                    print(output)
                    if os.path.exists(os.path.join(dir,output+'_mcf.nii.gz')):
                        print(output+'_mcf.nii.gz exists, skipping')
                    else:
                        os.system("mcflirt -in %s -plots"%(output))
                        os.system("fsl_motion_outliers -i %s -o motion_assessment/%s_confound.txt --fd --thresh=%s -p motion_assessment/fd_plot -v > motion_assessment/%s_outlier_output.txt"%(output,output,arglist['MOCO'],output))
                        os.system("cat motion_assessment/%s_outlier_output.txt >> %s"%(output,outhtml))
                        plotz=os.path.join(basedir,dir,'motion_assessment','fd_plot.png')
                        os.system("echo '<p>=============<p>FD plot %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(output,plotz,'100%', outhtml))
                    
                        if os.path.isfile("motion_assessment/%s_confound.txt"%(output))==False:
                            os.system("touch motion_assessment/%s_confound.txt"%(output))
                        
                        check = subprocess.check_output("grep -o 1 motion_assessment/%s_confound.txt | wc -l"%(output), shell=True)
                        num_scrub = [int(s) for s in check.split() if s.isdigit()]
                        
                        if num_scrub[0]>45:
                            with open(out_bad_bold_list, "a") as myfile:
                                myfile.write("%s\n"%(output))
                            myfile.close()
                            
#                        if os.path.exists("%s_mcf.par"%(output)):
#                            if os.path.exists(os.path.join(basedir,dir,'motion_assessment',"%s_mcf.par"%(output))):
#                                os.remove(os.path.join(basedir,dir,'motion_assessment',"%s_mcf.par"%(output)))
#
#                            shutil.move("%s_mcf.par"%(output),os.path.join(basedir,dir,'motion_assessment'))
#                            rawfile = open(os.path.join(os.path.join(basedir,dir,'motion_assessment','%s_mcf.par'%(output))), 'r')
#                            table = [line.rstrip().split() for line in rawfile.readlines()]
#                            for i in range(6):
#                                newtable = ([[line[i]] for line in table])
#                                f=open(os.path.join(basedir,dir,'motion_assessment','%s_motcor%i.txt'%(output,i)),'w')
#                                for item in newtable:
#                                    neat=item[0]
#                                    f.write(str(neat)+'\n')
#                                f.close()
                
 




def split_list(a_list):
        half = len(a_list)/2
        return a_list[:half], a_list[half:]


def main(DATA):
    basedir='/Users/gracer/Desktop/data'
    writedir='/Users/gracer/Desktop/data'
    
    datestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
    outhtml = os.path.join(writedir,'bold_motion_QA_%s.html'%(datestamp))
    out_bad_bold_list = os.path.join(writedir,'lose_gt_45_vol_scrub_%s.txt'%(datestamp))

    parser=argparse.ArgumentParser(description='preprocessing')
    parser.add_argument('-task',dest='TASK',
                        default=False, help='which task are we running on?')
    parser.add_argument('-bet',dest='STRIP',action='store_true',
                        default=False, help='bet via fsl using defaults for functional images')
    parser.add_argument('-betrage',dest='RAGE',action='store_true',
                        default=False, help='bet via fsl using robust estimation for anatomical images')
    parser.add_argument('-moco',dest='MOCO',
                        default=False, help='this is using fsl_motion_outliers to preform motion correction and generate a confounds.txt as well as DVARS')
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    prepro(basedir, args, arglist, outhtml, out_bad_bold_list,DATA)

all_data=glob.glob('/Users/gracer/Desktop/data/sub*')
B, C = split_list(all_data)

if __name__ == "__main__": 
    pool = Pool(processes=2)
    pool.map(main, [B,C]) 
           

os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts')