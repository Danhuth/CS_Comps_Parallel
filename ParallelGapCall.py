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
    for i in range(len(pathTuple)):
        Generator_Set_File_Path = pathTuple[i][0]
        Out_File_Path = pathTuple[1]
        Out_File = open(Out_File_Path, 'w+')
        Gap_Path = r'/home/dhuth/gap-4.10.2/bin/gap.sh -o 9g -K 8g'
        Progress_Check_Iterator = 0
        for filename in os.listdir('/home/dhuth/CS_Comps_Prallel/Generator_Storage_Folder'+str(i)):
            Progress_Check_Iterator += 1
            if filename.endswith(r'.g'):
                file = open('/home/dhuth/CS_Comps_Parallel/Generator_Storage_Folder+str(i)'+'/'+filename, 'r+')
                subprocess.run(Gap_Path, shell=True, stdin=file, stdout=Out_File)
                print(Progress_Check_Iterator)
    Output_Collator(Out_File_Path)


    Out_File.close()
    #Cleaning_Script(Generator_Set_File_Path)
#GapCaller('outdelta.g')
