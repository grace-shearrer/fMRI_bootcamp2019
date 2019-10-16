import os
import glob
import sys
import fnmatch
import sys
import subprocess
# will make binary masks, input is as follows <cope#> <stat#> <cluster#>
# the inputs must be numbers only  
def make_masks(basedir):
	TYPE=sys.argv[1]
	COPE=sys.argv[2]
	STAT=sys.argv[3]
	CLUSTER=sys.argv[4]
	INPUT=os.path.join(basedir,'randomize','cluster_breaker','thr_0.0001',TYPE+'_'+COPE+'_'+STAT+'.nii.gz')
	OUTPUT=os.path.join(basedir,'randomize','cluster_breaker','thr_0.0001',TYPE+'_'+COPE+'_'+STAT+'_'+CLUSTER+'_mask.nii.gz')
	call='/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/fslmaths -dt int '+INPUT+' -thr '+CLUSTER+' -uthr '+CLUSTER+' -bin '+OUTPUT
	print(call)
	subprocess.call(call.split())
	#subprocess.call(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/fslmaths","-dt", "int",INPUT,"-thr",CLUSTER,"-uthr",CLUSTER,"-bin",OUTPUT])
	
def main():
	basedir='/projects/niblab/data/eric_data/W1/milkshake/level3_grace_edit'
	make_masks(basedir)
main()
