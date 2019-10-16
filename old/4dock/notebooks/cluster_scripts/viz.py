import os
import sys
import glob
import fnmatch
import subprocess 
#fslview cope16_risk+.gfeat/bg_image.nii.gz randomised/cope16_risk_randomized_tfce_corrp_tstat1.nii.gz -b 0.95,1 &
def viz(basedir):
	TYPE=sys.argv[1]
	COPE=sys.argv[2]
	STAT=sys.argv[3]
	if fnmatch.fnmatch(TYPE,"risk")==True:
		prePut="cope"+COPE+"_risk+.gfeat"
		INPUT1=os.path.join(basedir,"level3_grace_edit",prePut,"bg_image.nii.gz")
		print INPUT1
		image="cope"+COPE+"_risk_randomized_tfce_corrp_tstat"+STAT+".nii.gz"
		INPUT2=os.path.join(basedir,"level3_grace_edit","double_check",image)
		print INPUT2
	if fnmatch.fnmatch(TYPE,"slope")==True:
		prePut="cope"+COPE+"_slope_thr.gfeat"
		INPUT1=os.path.join(basedir,"level3_grace_edit",prePut,"bg_image.nii.gz")
		image="cope"+COPE+"_slope_randomized_tfce_corrp_tstat"+STAT+".nii.gz"
		INPUT2=os.path.join(basedir,"level3_grace_edit","double_check",image)
	if fnmatch.fnmatch(TYPE,"main_eff")==True:
		prePut="cope"+COPE+"_thr.gfeat"
		INPUT1=os.path.join(basedir,"level3_grace_edit",prePut,"bg_image.nii.gz")
		image="cope"+COPE+"_main_eff_randomized_tfce_corrp_tstat"+STAT+".nii.gz"
		INPUT2=os.path.join(basedir,"level3_grace_edit","double_check",image)
	else:
		prePut="cope"+COPE+"_"+TYPE+".gfeat"
		INPUT1=os.path.join(basedir,"level3_grace_edit",prePut,"bg_image.nii.gz")
		image="cope"+COPE+"_"+TYPE+"_randomized_tfce_corrp_tstat"+STAT+".nii.gz"
		INPUT2=os.path.join(basedir,"level3_grace_edit","randomize",image)

	subprocess.call(["fslview",INPUT1,INPUT2,"-b","0.95,1"])
def main():
	basedir='/projects/niblab/data/eric_data/W1/milkshake'
	viz(basedir)
main()
