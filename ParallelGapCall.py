import subprocess
import os
import re
import time
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
    Generator_Set_File_Path = pathTuple[0]
    Out_File_Path = pathTuple[1]
    Out_File = open(Out_File_Path, 'w+')
    Gap_Path = r'/home/dhuth/CS_Comps_Parallel/.git/gap-4.10.2/./bin/gap.sh -o 9g -K 8g'
    Progress_Check_Iterator = 0
    for filename in os.listdir(Generator_Set_File_Path):
        Progress_Check_Iterator += 1
        if filename.endswith(r'.g'):
            file = open(Generator_Set_File_Path+'/'+filename, 'r+')
            subprocess.run(Gap_Path, shell=True, stdin=file, stdout=Out_File)
            print(Progress_Check_Iterator)
    Output_Collator(Out_File_Path)

        
    Out_File.close()
    #Cleaning_Script(Generator_Set_File_Path)
#GapCaller('outdelta.g')