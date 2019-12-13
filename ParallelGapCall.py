from clusterun import *
import subprocess
import os
import time
import re
from pathlib import Path
from Output_Collator import Output_Collator
#from Cleaning_Script import Cleaning_Script
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Description of dictFormat function: This function takes two arguments: A file object containing a generator set, and a file object containing the corresponding Delta_Set_As_String set.
#   dictFormat reads both of these files into a string. Then it writes these two strings to a new file, whose name is specified by the user.
#Description of gapCaller function: This function takes string representing a file Generator_Set_File_Path as an argument. It then asks the user to specify where it should store the computed generator set Delta_Set_As_String set pair.
#   After this, gapCaller opens GAP as a Python subprocess, and allocates 8g of ram. You can adjust this value by editing the -o and -k values in the Gap_Path variable.
#       We default to 8g because this program was written for computers with 8g physical ram.
#   Once gap has returned the delta set, we call the dictFormat function to format our Generator Set, Delta Set pair so that it can be easily searched.
#Description of Cleaning_Script: Using this interface will generate a lot of files in the .../PythonGapInterface/Generator_Storage_Folder/ directory. Cleaning Script simply deletes
#   all files ending with .g in the .../Generator_Storage_Folder/ directory. Cleaning script runs before any delta sets are generated, and after all computations are complete
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dictFormat(Generator_Set_File, Delta_Set_File, timerun): 
    with open(Generator_Set_File,'r+') as inputfile:
        Generator_String = inputfile.read()
    with open(Delta_Set_File, 'r+') as Out_File:
        Delta_String = Out_File.read()
    Gen_Left_Bracket_Index = Generator_String.find('[')
    Gen_Right_Bracket_Index = Generator_String.find(']')
    generator = (Generator_String[Gen_Left_Bracket_Index+1:Gen_Right_Bracket_Index])
    Del_Left_Bracket_Index = Delta_String.find('[')
    Del_Right_Bracket_Index = Delta_String.find(']')
    End_Of_String_Trash = Delta_String[Del_Right_Bracket_Index:len(Delta_String)]
    Delta_Set_As_String = '0'
    if(Del_Left_Bracket_Index != -1 & Del_Right_Bracket_Index != -1):
        Delta_Set_As_String = (Delta_String[Del_Left_Bracket_Index+1:Del_Right_Bracket_Index])
        boundvalue = int(re.search(r'\d+', End_Of_String_Trash).group())
    else:
        Delta_Set_As_String = 'There is not enough memory available to compute this delta set.'
        boundvalue = 'failed to compute delta set, no bound'
    Final_Value = ('Generator Set: ', generator,'\n Delta Set: ',Delta_Set_As_String,'\n','Periodicity Bound: ',str(boundvalue),'\n','timerun: ',str(timerun))
    Final_Value = ''.join(Final_Value)
    return Final_Value





def GapCaller(pathTuple):# Need to bump this to a tuple of two objects and then separate
    Out_File_Path = os.getcwd()+'/outputfile'
    Out_File = open(Out_File_Path, 'w+') 
    Generator_Set_File_Path = pathTuple
    Gap_Path = "/home/dhuth/gap-4.10.2/bin/gap.sh -o 9g -K 8g"
    Progress_Check_Iterator = 0
    #pathlist = Path('/home/dhuth/CS_Comps_Parallel/Generator_Storage_Folder/').glob('*.g')
# was just interating through this with for file in os.listdir(the filepath in Path):
    #for path in pathlist:
    Progress_Check_Iterator += 1
    file = open(pathTuple, 'r+')
    subprocess.run(Gap_Path, shell=True, stdin=file, stdout=Out_File)
    #Output_Collator(Out_File_Path)

def parameters():
    #construct list of generator set folders.
    #Now we have the top level _folders_
    #parallelgapcall handles digging the files out of these directories
    generator_set_list = []
    i = 0
    for filename in os.listdir('/home/dhuth/CS_Comps_Parallel/Generator_Storage_Folder'):
        generator_set_list.append(os.getcwd()+'/Generator_Storage_Folder/'+filename)
    return(generator_set_list)

def main():
    finaltime = 0
    starttime = time.time()
    sequencerun(GapCaller,parameters)
    endtime = time.time()
    print("the total run time is: "+ str(endtime-starttime))
if __name__ == '__main__':
    main()
