from math import gcd
import os
import random
from ParallelGapCall import GapCaller
#from Cleaning_Script import Cleaning_Script

#For Professor Li: 
# All I  care about are cases 1 and 2, the other cases are not set up for parallelization.
# 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Variables: The user is asked to input a base value, A, for the generator sets, and a number of values which are relatively prime to A to compute. 
#Description of Bound_Format function: This function takes a tuple representing a generator set, and adds the necessary formatting for GAP to compute the periodicity bound of its delta set.
#Description of Format_For_Gap function: This function takes the same arguments as boundformat, but adds the necessary formatting for GAP to compute the delta set of the generator set tuple.
#Description of gensetgen function: This function takes a base value, A, and a value, M, which represents the number of Bs we wish to find. It then computes M bs, which are relatively prime
#   to A, and stores them in a list. It then asks the user which case of generator set they wish to calculate the delta set/bound of. Within these cases, the user specifies the following:
#   1st - The bound for the coefficient of the b^n term in the nonminimal generator.
#   2nd - the number of generated sets the user wants to calculate
#   gensetgen then passes these generated sets to another function, gapCaller, which uses python subprocesses to call GAP to compute the delta sets of these values.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Base_A_Value = int(input('Input a here: '))
Num_Relative_Primes = int(input('input the number of bs you wish to find here: '))
Generator_Set_Filename= input('Where would you like to store the generator sets? \n Input here: ')
Generator_Set_File_Path= os.path.join(os.getcwd() + '/Generator_Storage_Folder')
Number_To_Generate = 24*int(input('k for k*24 where k is the number of cores you have access to: '))




def Bound_Format(S):
    S_As_String = str(S);
    Bracket_S_String = (S_As_String[:1] + '[' + S_As_String[1:len(S_As_String)-1]+ ']' +S_As_String[len(S_As_String)-1:])
    Bracket_S_String = ('Read("prelimcoderuntime.g"); \n'+'DeltaSetPeriodicityBoundForGeneratorList' + Bracket_S_String + ';\n')
    return(Bracket_S_String)


def FastDeltaSetGeometricSquare_Format(S):
    S_As_String = str(S);
    Bracket_S_String = (S_As_String[:1] + '[' + S_As_String[1:len(S_As_String)-1]+ ']' +S_As_String[len(S_As_String)-1:])
    Bracket_S_String = ('Read("prelimcode1.g"); \n'+'FastDeltaSetGeometricSquare' + Bracket_S_String + ';\n')
    return(Bracket_S_String)


def Format_For_Gap(S):                                                            
    S_As_String = str(S);
    Bracket_S_String = (S_As_String[:1] + '[' + S_As_String[1:len(S_As_String)-1]+ ']' +S_As_String[len(S_As_String)-1:])
    Bracket_S_String = ('Read("prelimcoderuntime.g"); \n'+'DeltaSetOfGeneratingSet' + Bracket_S_String + ';\n')
    return(Bracket_S_String)

def Format_For_Gap_With_Bound(S):                                                            
    S_As_String = str(S);
    Bracket_S_String = (S_As_String[:1] + '[' + S_As_String[1:len(S_As_String)-1]+ ']' +S_As_String[len(S_As_String)-1:])
    Bracket_S_String = ('Read("prelimcoderuntime.g"); \n'+'DeltaSetOfGeneratingSet' + Bracket_S_String + ';\n'+'DeltaSetPeriodicityBoundForGeneratorList' + Bracket_S_String + ';\n')
    
    return(Bracket_S_String)


def Generator_Set_Generator(Base_A_Value, Num_Relative_Primes):
    Base_A_Value = Base_A_Value
    Num_Relative_Primes = Num_Relative_Primes
    b = Base_A_Value 
    List_Of_A_Relative_Primes = []
    while len(List_Of_A_Relative_Primes) < Num_Relative_Primes:
        if gcd(Base_A_Value,b)==1:
            List_Of_A_Relative_Primes.append(b)
        b += 1
    Generator_Style_Case = int(input(' Enter 1 to test the <a,b,kb, kb^2> case: \n Enter 2 to test the <a^2, ab,b^2, S> \n Enter 3 to test the <a^2, ab, b^2, ia^2 + jab + kb^2> with mod conditions case \n Enter 4 to test the <a^3, a^2b,ab^2,b^3, S cubic term> case\n Here: '))
    
    if(Generator_Style_Case ==1):
        #file = open(Generator_Set_Filename,'w')
        Lower_Bound_Of_X2 = int(input('input K bound lower\n Here: '))
        Upper_Bound_Of_X2 = int(input('input K bound upper\n Here: '))
        if((Upper_Bound_Of_X2 - Lower_Bound_Of_X2)*len(List_Of_A_Relative_Primes)< Number_To_Generate):
            print('Currently there are: '+ str(Num_Relative_Primes)+' integers relatively prime to'+str(Base_A_Value)+' and: '+str(Upper_Bound_Of_X2 - Lower_Bound_Of_X2)+' possible values of k. k*(#b) must be >= ' + str(Number_To_Generate))
            Lower_Bound_Of_X2 = int(input('Input a new K lower bound here: '))
            Upper_Bound_Of_X2 = int(input('input a new K upper bound Here: '))
        X2_List = range(Lower_Bound_Of_X2, Upper_Bound_Of_X2)
        AllGenSets = []
        if not (os.path.exists(Generator_Set_File_Path)):
            os.makedirs(Generator_Set_File_Path)
        for i in range(0, len(List_Of_A_Relative_Primes)):
            for j in range(0, len(X2_List)):
                    AllGenSets.append((Base_A_Value, List_Of_A_Relative_Primes[i], X2_List[j]*List_Of_A_Relative_Primes[i]))
                    #file = open(Generator_Set_File_Path+'/'+Generator_Set_Filename+iteratorstring+'.g','w')
        SetsToTest = random.sample(AllGenSets,Number_To_Generate)
        for i in range(0,len(SetsToTest)):
            iteratorstring = str(i)
            file = open(Generator_Set_File_Path+'/'+Generator_Set_Filename+iteratorstring+'.g','w')
            S = Format_For_Gap_With_Bound(SetsToTest[i])
            file.write(S)
        output_filename = '/outdeltas.txt'
        outputfile = open(Generator_Set_File_Path+output_filename,'w')
        outputfile.close()

    if(Generator_Style_Case == 2):
        file = open(Generator_Set_Filename,'w')
        Lower_Bound_Of_X2 = int(input('input K bound lower\n Here: '))
        Upper_Bound_Of_X2 = int(input('input K bound upper\n Here: '))
        X0_List = range(0,b)
        X1_List = range(0,b)
        X2_List = range(Lower_Bound_Of_X2, Upper_Bound_Of_X2)
        AllGenSets = []
        for i in range(0, len(List_Of_A_Relative_Primes)):
            for j in range(0, len(X0_List)):
                for k in range(0,len(X1_List)):
                    for l in range(0,len(X2_List)):
                        if(X0_List[j] <= List_Of_A_Relative_Primes[i] & X1_List[k] <= List_Of_A_Relative_Primes[i]):
                            AllGenSets.append((Base_A_Value**2, Base_A_Value*List_Of_A_Relative_Primes[i], List_Of_A_Relative_Primes[i]**2,X0_List[j]*Base_A_Value + X1_List[k]*Base_A_Value*List_Of_A_Relative_Primes[i] + X2_List[l]*List_Of_A_Relative_Primes[i]**2))
                            
        SetsToTest = random.sample(AllGenSets, Number_To_Generate)
        
        corenumber = str(0)
        for i in range(len(SetsToTest)):
            if(i%24 == 0):
                corenumber = str(i//24)
                if not (os.path.exists(Generator_Set_File_Path+corenumber)):
                    os.makedirs(Generator_Set_File_Path+corenumber)
                output_filename = '/outdeltas'+corenumber+'.txt'
                outputfile = open(Generator_Set_File_Path+corenumber+output_filename,'w')
                outputfile.close()
            
            iteratorstring = str(i)
            file = open(Generator_Set_File_Path+corenumber+'/'+Generator_Set_Filename+iteratorstring+'.g','w')
            S = Format_For_Gap_With_Bound(SetsToTest[i])
            file.write(S)
            
            
    if(Generator_Style_Case == 3):
        file = open(Generator_Set_Filename,'w')
        Lower_Bound_Of_X2 = int(input('input K bound lower\n Here: '))
        Upper_Bound_Of_X2 = int(input('input K bound upper\n Here: '))
        X0_List = range(0,b)
        X1_List = range(0,b)
        X2_List = range(Lower_Bound_Of_X2, Upper_Bound_Of_X2)
        AllGenSets = []
        for i in range(0, len(List_Of_A_Relative_Primes)):
            for j in range(0, len(X0_List)):
                for k in range(0,len(X1_List)):
                    for l in range(0,len(X2_List)):
                        if X0_List[j] <= List_Of_A_Relative_Primes[i] & X1_List[k]<= List_Of_A_Relative_Primes[i]:
                            Sterm = X0_List[j]*Base_A_Value**2 + X1_List[k]*Base_A_Value*List_Of_A_Relative_Primes[i] + X2_List[l]*List_Of_A_Relative_Primes[i]**2
                            if(Sterm % (List_Of_A_Relative_Primes[i]-Base_A_Value) == Base_A_Value**2 % (List_Of_A_Relative_Primes[i]-Base_A_Value) or  Sterm % (List_Of_A_Relative_Primes[i] + Base_A_Value) == Base_A_Value**2 % (List_Of_A_Relative_Primes[i] + Base_A_Value)):
                                AllGenSets.append((Base_A_Value**2, Base_A_Value*List_Of_A_Relative_Primes[i], List_Of_A_Relative_Primes[i]**2, Sterm))
        SetsToTest = AllGenSets 
        for i in range(len(SetsToTest)):
            iteratorstring = str(i)
            file = open(Generator_Set_File_Path+Generator_Set_Filename+iteratorstring+'.g','w')
            S = Format_For_Gap(SetsToTest[i])
            file.write(S)

    if(Generator_Style_Case == 4):
        file = open(Generator_Set_Filename,'w')
        lowerL = int(input('input L bound lower\n Here:'))
        upperL = int(input('input L bound upper\n Here:'))
        X0_List = range(0,b)
        X1_List = range(0,b)
        X2_List = range(0,b)
        X3_List = random.sample(range(lowerL, upperL), (upperL-lowerL)-1)
        Number_Of_Gen_Sets_To_Generate = 24*int(input('k for k*24 where k is the number of cores you have access 2'))
        AllGenSets = []
        for i in range(0, len(List_Of_A_Relative_Primes)):
            for j in range(0, len(X0_List)):
                for k in range(0,len(X1_List)):
                    for l in range(0,len(X2_List)):
                        for m in range(0,len(X3_List)):
                            if(X0_List[j] <= List_Of_A_Relative_Primes[i] & X1_List[k] <= List_Of_A_Relative_Primes[i] & X2_List[l] <= List_Of_A_Relative_Primes[i]):
                                Sterm = X0_List[j]*Base_A_Value**3 + X1_List[k]*Base_A_Value**2*List_Of_A_Relative_Primes[i] + X2_List[l]*Base_A_Value*List_Of_A_Relative_Primes[i]**2 + X3_List[m]*List_Of_A_Relative_Primes[i]**3
                                if(Sterm % List_Of_A_Relative_Primes[i]-Base_A_Value == 0):
                                    AllGenSets.append((Base_A_Value**3, Base_A_Value**2*List_Of_A_Relative_Primes[i], Base_A_Value*List_Of_A_Relative_Primes[i]**2,List_Of_A_Relative_Primes[i]**3,Sterm))
        SetsToTest = random.sample(AllGenSets,Number_Of_Gen_Sets_To_Generate) 
        for i in range(Number_Of_Gen_Sets_To_Generate):
            iteratorstring = str(i)
            file = open(Generator_Set_File_Path+corenumber+Generator_Set_Filename+iteratorstring+'.g','w')
            S = Format_For_Gap(SetsToTest[i])
            file.write(S)

#Cleaning_Script(Generator_Set_File_Path)
Generator_Set_Generator(Base_A_Value, Num_Relative_Primes)
#for i in range (0,(Number_To_Generate//24)-1):
#    pathTuple = (Generator_Set_File_Path+str(i), Generator_Set_File_Path+str(i)+'/'+'outdeltas'+str(i)+'.txt')
#    GapCaller(pathTuple)




