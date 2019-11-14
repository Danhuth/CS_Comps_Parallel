import os
import re

def Output_Collator(filePath):
    boundruntimestring = ''
    count = 0
    finalOutput = open("Collated_Output.txt",'w+')
    with open(filePath) as f:
        for line in f:
            match = re.search('(?<=gap> ).*(\d+)', line)
            print(match.group(1), type(match.group(1)))
            if match:
                if(count%2 == 0):
                    boundruntimestring.join(str(match.group(0)))
                if(count%2 != 0):
                    boundruntimestring.join(','+str(match.group(0))+'\n')
                count+=1
    finalOutput.write(boundruntimestring)
