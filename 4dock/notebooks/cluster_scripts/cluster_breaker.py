import os
import fnmatch
import glob
import subprocess
import sys
import fnmatch
#will create a summary of significant clusters from the randomized output
#need to define which type of file you want
##masking this with the significant voxels from corrp
##fslmaths grot_tfce_corrp_tstat1 -thr 0.95 -bin -mul grot_tstat1 grot_thresh_tstat1
#cluster to extract the clusters and local maxima in several different outputs
#cluster --in=grot_thresh_tstat1 --thresh=0.0001 --oindex=grot_cluster_index --olmax=grot_lmax.txt --osize=grot_cluster_size
#cope9_risk_randomized_tfce_corrp_tstat1.nii.gz
def cluster_breaker(basedir):
	PARADIGM=sys.argv[1]
	TYPE=sys.argv[2]
	COPE=sys.argv[3]
	STAT=sys.argv[4]
	THRESH=sys.argv[5]
	os.chdir(os.path.join(basedir,PARADIGM,'level3_grace_edit'))
	if fnmatch.fnmatch(COPE, 'all')==True and fnmatch.fnmatch(STAT, 'all')==True:
		print ('clustering all'+TYPE)
		g=open('all_output.txt','a')
		for file in glob.glob('randomize/cope*_'+TYPE+'_randomized_tfce_corrp_*.nii.gz'):
                	print(file)
                	name=file.split('/')
                	name2=name[1].strip('.nii.gz')
                	print(name2)
			getcope=name2.split('_')
			COPE2=getcope[0]
			STAT2=getcope[5]
			print STAT2
			RAWINPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit',COPE2+'_'+TYPE+'.gfeat','cope1.feat','stats',STAT2+'.nii.gz')
                	INPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','randomize',COPE2+'_'+TYPE+'_randomized_tfce_corrp_'+STAT2+'.nii.gz')
                	OUTPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_'+COPE2+'_'+STAT2)
               		sigvox=subprocess.call(['/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/fslmaths',INPUT,'-thr','0.95','-bin','-mul',RAWINPUT,OUTPUT])
                	OUTPUT2=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE2+'_'+STAT2+'_cluster_index')
                	OUTPUT3=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE2+'_'+STAT2+'_lmax.txt')
                	x=open(OUTPUT3,'w+')
                	OUTPUT4=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE2+'_'+STAT2+'_cluster_size')
                	INPUT2=OUTPUT+'.nii.gz'
                	print INPUT2
                	cmd='/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster -i '+OUTPUT+' -t '+THRESH+' -o '+OUTPUT+' --olmax='+OUTPUT3+' --osize='+OUTPUT4+' --mm'
                	print cmd
                	cluster=subprocess.call([cmd.split()],stdout=subprocess.PIPE)
			output=cluster.stdout.read()
                        g.write(output+'\n')
                	x.close()               
		g.close() 
	else:	
		if fnmatch.fnmatch(TYPE,'risk')==True:
			RAWINPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','cope'+COPE+'_risk+.gfeat','cope1.feat','stats','tstat'+STAT+'.nii.gz')
			INPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','randomize','cope'+COPE+'_risk_randomized_tfce_corrp_tstat'+STAT+'.nii.gz')
			OUTPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_'+COPE+'_'+STAT)
			sigvox=subprocess.call(['/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/fslmaths',INPUT,'-thr','0.95','-bin','-mul',RAWINPUT,OUTPUT])
			OUTPUT2=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE+'_'+STAT+'_cluster_index')
			OUTPUT3=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE+'_'+STAT+'_lmax.txt')
			x=open(OUTPUT3,'w+')
			OUTPUT4=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE+'_'+STAT+'_cluster_size')
			INPUT2=OUTPUT+'.nii.gz'
			print INPUT2
			cmd='/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster -i '+OUTPUT+' -t '+THRESH+' -o '+OUTPUT+' --olmax='+OUTPUT3+' --osize='+OUTPUT4+' --mm'
			print cmd
                	cluster=subprocess.call(cmd.split())
			x.close()
		else:
			RAWINPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','cope'+COPE+'_'+TYPE+'.gfeat','cope1.feat','stats','tstat'+STAT+'.nii.gz')
			INPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','randomize','cope'+COPE+'_risk_randomized_tfce_corrp_tstat'+STAT+'.nii.gz')
			OUTPUT=os.path.join(basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker','cope'+COPE+'_'+STAT)
			sigvox=subprocess.Popen(['/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/fslmaths','-i',INPUT,'-thr','0.95','-bin','-mul',RAWINPUT,OUTPUT])
			OUTPUT2=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE+'_'+STAT+'_cluster_index')
			OUTPUT3=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE+'_'+STAT+'_lmax.txt')
			x=open(OUTPUT3,'w+')
			OUTPUT4=os.path.join( basedir,PARADIGM,'level3_grace_edit','randomize','cluster_breaker',TYPE+'_cope'+COPE+'_'+STAT+'_cluster_size')
			INPUT2=OUTPUT+'.nii.gz'
			print INPUT2
			cmd='/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster -i '+OUTPUT+' -t '+THRESH+' -o '+OUTPUT+' --olmax='+OUTPUT3+' --osize='+OUTPUT4+' --mm'
			print cmd
                	cluster=subprocess.call(cmd.split())
			x.close()

def main():
	if len(sys.argv)<4:
		print('please give the the paradigm, type of analysis, cope, stat')
		sys.exit()
	basedir='/projects/niblab/data/eric_data/W1'
	cluster_breaker(basedir)
main()
