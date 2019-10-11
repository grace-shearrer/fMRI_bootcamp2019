#script to check level 3 analysis
import os
import glob
import shutil

basedir='/projects/niblab/data/eric_data/W1/milkshake'
os.chdir(basedir)
with open('level3_grace_edit/randomize/Cluster_check.txt', 'w') as output:
  for file in glob.glob('level3_grace_edit/randomize/cope*_risk_randomized_tfce_corrp_tstat*.txt'):
    print(file)
    filename=file.split('/')
    label=str(filename[2])
    print(label)
    with open(file, 'r+') as openfile:#open cluster file write new first line
      content=openfile.read()
      openfile.seek(0,0)
      openfile.write(label.rstrip('\r\n')+'\n'+content)
    with open(file,'r+') as infile:#
      for line in infile:
        output.write(line)
output.close()
