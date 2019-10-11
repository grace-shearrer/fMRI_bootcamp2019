import os
import glob
import sys
import fnmatch
import sys
import subprocess
# fslmaths filtered_func_data -mul scale_factor -div mean_func -mul mask_image output image 
# the inputs must be numbers only  
#def average_PE(basedir,mean_pe):
#basedir='/projects/niblab/data/eric_data/W1/milkshake/level3_grace_edit/'
#os.chdir(basedir)
#g=open('order.txt','w')

def PE_stats(basedir,g):
	#PARADIGM=sys.argv[1]
	#TYPE=sys.argv[2]
	#COPE=sys.argv[3]
	for mask in glob.glob(os.path.join(basedir,'randomize','cluster_breaker','thr_0.0001','*_mask.nii.gz')):
		for i in range(3):
			MASK=mask
			y=mask.split('/')
			print y
			y1=y[11]
			x=y1.split('_')
			cope='cope'+x[1]
			print 'this is the cope '+cope
			stat=str(i)
			print 'this is the stat '+stat
			cluster=x[3]
			INPUT=os.path.join(basedir,cope+'_risk+.gfeat','cope1.feat','stats','pe'+stat+'.nii.gz')
			OUTPUT=os.path.join(basedir,'randomize','cluster_breaker','thr_0.0001','risk_'+cope+'_mean_PE'+'_'+stat+'_cluster_'+cluster)
			call='/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/fslstats '+INPUT+' -k '+MASK+' -m'
			print call 
			g.write('%s %s %s \n' % (cope,cluster,stat))	
			cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/fslstats",INPUT,"-k",MASK,"-s"],stdout=subprocess.PIPE)
			output=cluster.stdout.read()
			g.write(output+'\n')
	g.close()
def main():
	basedir='/projects/niblab/data/eric_data/W1/milkshake/level3_grace_edit/'
	#mean_pe=[]
	#average_PE(basedir,mean_pe)
	g=open('std_out.txt','w')
	PE_stats(basedir,g)
main()
