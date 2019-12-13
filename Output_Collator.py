import os
import re
import glob

def Output_Collator(filePath):
    boundruntimestring = ''
    count = 0
    finalOutput = open("Collated_Output.txt",'a')
    with open(filePath) as f:
        data = f.read()
        #print(data)
        match = re.findall('brk>\s+(\d+)\s+brk>\s+(\d+)', data)
        #print(match)
    for i in range(len(match)):
        finalOutput.write(str(match[i])+'\n')
for name in glob.glob(os.getcwd()+'/clusterun*'):
    Output_Collator(name)
