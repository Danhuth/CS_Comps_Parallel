import os
from ParallelGapCall import GapCaller
from clusterun import sequencerun
import os
import re

def Output_Collator(filePath):
    boundruntimestring = ''
    count = 0
    finalOutput = open("Collated_Output.txt",'w+')
    with open(filePath) as f:
        data = f.read()
        match = re.findall('gap>\s+(\d+)\s+gap>\s+(\d+)', data)
    for i in range(len(match)):
        finalOutput.write(str(match[i])+'\n')
sequencerun(GapCaller(pathTuple),pathTuple)
