import os
import glob
import shutil
<<<<<<< HEAD
#import pdb
import datetime

def QA_writer(basedir,outfile,writedir):

    for file in glob.glob(os.path.join(basedir,'sub*','grace_edit','*.feat')):
        os.chdir(file)
        print(file)
        sub=file.split('/')[7]
        dict_of_files = {}
        for (dirpath, dirnames, filenames) in os.walk(file):
            for filename in filenames:
                if filename.startswith('fsl') or filename.startswith('vert'):
                    print('skipping')
                elif filename.endswith('.png'): 
                    dict_of_files[filename] = os.sep.join([dirpath, filename])

        for key in dict_of_files:
            os.system("echo '<p>=============<p> %s %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(sub,key,dict_of_files[key],'100%', outfile))
            #shutil.copy(dict_of_files[key],writedir)
        if os.path.exists(os.path.join(basedir,'fails'))==False:
            os.makedirs(os.path.join(basedir,'fails'))

        if len(glob.glob(os.path.join(file,'stats','cope*.nii.gz')))==4:
            print(file+' has 4 cope files :D')
        else:
            print(file+' is missing copes, need to rerun')
            name=file.split('/')[9].split('.')[0]
            shutil.copytree(file,os.path.join(basedir,'fail',sub,name))
=======
import no_reg
import datetime
import argparse
#import pdb

def QA_writer(basedir,outfile,writedir,arglist):
    
    if os.path.exists(os.path.join(basedir,'fails'))==False:
                os.makedirs(os.path.join(basedir,'fails'))
            
    for file in glob.glob(os.path.join(basedir,'sub*','grace_edit','*.feat')): 
        sub=file.split('/')[7]
        if len(glob.glob(os.path.join(file,'stats','cope*.nii.gz')))==2:
            print(file+' has 2 cope files :D')
        else:
            print(file+' is missing copes, need to rerun')
            name=file.split('/')[9].split('.')[0]
            shutil.copytree(file,os.path.join(basedir,'fail',sub, name))
        
    if arglist['NOREG']== False:
        for file in glob.glob(os.path.join(basedir,'sub*','grace_edit','*.feat')):
            sub=file.split('/')[7]
            dict_of_files = {}
            for (dirpath, dirnames, filenames) in os.walk(file):
                for filename in filenames:
                    if filename.startswith('fsl') or filename.startswith('vert'):
                        print('skipping')
                    elif filename.endswith('.png'): 
                        dict_of_files[filename] = os.sep.join([dirpath, filename])

            for key in dict_of_files:
                os.system("echo '<p>=============<p> %s %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(sub,key,dict_of_files[key],'100%', outfile))
                #shutil.copy(dict_of_files[key],writedir)
    else:
        print("no need to look at fake registration, but do need to clean up this reg dirctory!")
        no_reg.main(basedir)
        for file in glob.glob(os.path.join(basedir,'sub*','grace_edit','*.feat')):
            sub=file.split('/')[7]
            #pdb.set_trace()
            for design_file in glob.glob(os.path.join(file,'design*.png')):
                #pdb.set_trace()
                os.system("echo '<p>=============<p> %s <br><IMG BORDER=0 SRC=%s WIDTH=%s></BODY></HTML>' >> %s"%(sub,design_file,'100%', outfile))
    
>>>>>>> d312e10b016610fba2335ab012872035fc8ffe69

def main():
    basedir='/Users/gracer/Desktop/data/derivatives/task'
    writedir='/Users/gracer/Desktop/data/'
    datestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
<<<<<<< HEAD
    outfile = os.path.join(writedir,'lev1_QA_%s.html'%datestamp)        
    QA_writer(basedir,outfile,writedir)
=======
    outfile = os.path.join(writedir,'lev1_QA_%s.html'%datestamp)  
    parser=argparse.ArgumentParser(description='checking first level feat analysis')
    parser.add_argument('-noreg',dest='NOREG', action='store_true',
                        default=False, help='Did you already register your data (using ANTZ maybe)?')
    
    args = parser.parse_args()
    arglist={}
    for a in args._get_kwargs():
        arglist[a[0]]=a[1]
    print(arglist)
    
    QA_writer(basedir,outfile,writedir,arglist)
>>>>>>> d312e10b016610fba2335ab012872035fc8ffe69
main()

os.chdir('/Users/gracer/Google Drive/fMRI_workshop/scripts')