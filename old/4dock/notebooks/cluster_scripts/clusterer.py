import os
import fnmatch
import glob
import subprocess
import sys
import fnmatch
#will create a summary of significant clusters from the randomized output
#need to define which type of file you want
def clusterer(basedir, g, PARADIGM):
	TYPE=sys.argv[2]
	RAND=sys.argv[3]
	os.chdir(basedir)
	if fnmatch.fnmatch(RAND,"randomized")==True:
		if fnmatch.fnmatch(PARADIGM,"milkshake")==True:
			for file in glob.glob('level3_grace_edit/randomize/cope*_'+TYPE+'_randomized_tfce_corrp_*.nii.gz'):
				print(file)
				INPUT=os.path.join(basedir,file)
				name=INPUT.split('/')
				name2=name[9].strip('.nii.gz')
				print(name2)
				g.write(name2+'\n')
				OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
				cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","0.95","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
				output=cluster.stdout.read()
				print output
				g.write(output+'\n')
			g.close()
		else:
			for file in glob.glob('level3_grace_edit/randomised/cope*_'+TYPE+'_randomized_tfce_corrp_*.nii.gz'):
				print(file)
				INPUT=os.path.join(basedir,file)
				name=INPUT.split('/')
				name2=name[9].strip('.nii.gz')
				print(name2)
				g.write(name2+'\n')
				OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
				cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","0.95","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
				output=cluster.stdout.read()
				print output
				g.write(output+'\n')
			g.close()

	else:
		if fnmatch.fnmatch(TYPE, "risk"):
			if fnmatch.fnmatch(PARADIGM,"milkshake"):
				for file in glob.glob('level3_grace_edit/cope*_risk+.gfeat/cope1.feat/stats/zstat1.nii.gz'):
					print(file)
					INPUT=os.path.join(basedir,file)
					name=INPUT.split('/')
					name2=name[8].strip('.nii.gz')
					print(name2)
					g.write(file+'\n')
					OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
					cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","3","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
					output=cluster.stdout.read()
					print output
					g.write(output+'\n')
				g.close()
			else:
				for file in glob.glob('level3_grace_edit/cope*_risk.gfeat/cope1.feat/stats/zstat1.nii.gz'):
					print(file)
					INPUT=os.path.join(basedir,file)
					name=INPUT.split('/')
					name2=name[8].strip('.nii.gz')
					print(name2)
					g.write(file+'\n')
					OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
					cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","3","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
					output=cluster.stdout.read()
					print output
					g.write(output+'\n')
				g.close()
	
		if fnmatch.fnmatch(TYPE,"slope"):
			for file in glob.glob('level3_grace_edit/cope*_slope_thr.gfeat/cope1.feat/stats/zstat1.nii.gz'):
				print(file)
				INPUT=os.path.join(basedir,file)
				name=INPUT.split('/')
				name2=name[8].strip('.nii.gz')
				print(name2)
				g.write(file+'\n')
				OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
				cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","3","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
				output=cluster.stdout.read()
				print output
				g.write(output+'\n')
			g.close()
		if fnmatch.fnmatch(TYPE,"main_eff"):
			for file in glob.glob('level3_grace_edit/cope*_thr.gfeat/cope1.feat/stats/zstat1.nii.gz'):
				print(file)
				INPUT=os.path.join(basedir,file)
				name=INPUT.split('/')
				name2=name[8].strip('.nii.gz')
				print(name2)
				g.write(file+'\n')
				OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
				cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","3","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
				output=cluster.stdout.read()
				print output
				g.write(output+'\n')
			g.close()
		else:
			for file in glob.glob('level3_grace_edit/cope*_'+TYPE+'.gfeat/cope1.feat/stats/zstat*.nii.gz'):
				print(file)
				INPUT=os.path.join(basedir,file)
				name=INPUT.split('/')
				name2=name[8].strip('.gfeat')
				print(file)
				g.write(file+'\n')
				OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
				cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","3","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
				output=cluster.stdout.read()
				print output
				g.write(output+'\n')
			g.close()

def main():
	if len(sys.argv)<4:
		print('please give the the type and if you want the raw or randomized image')
		sys.exit()
	PARADIGM=sys.argv[1]
	basedir='/projects/niblab/data/eric_data/W1/'+PARADIGM
	g=open('output.txt','w')
	clusterer(basedir, g,PARADIGM)
main()
