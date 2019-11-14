import os
from ParallelGapCall import GapCaller
def pathtuplecreator():

    generator_set_list = []
    #construct list of generator set folders.
    #Now we have the top level _folders_  
    #parallelgapcall handles digging the files out of these directories
    for i in range(0,10): 
        generator_storage_i = os.getcwd+"/Generator_Storage_Folder"+str(i)
        generator_set_list.append(generator_storage_i)
    return(generator_set_list)
pathTuple = (pathtuplecreator(),os.getcwd()+"/outputfile")

sequencerun(GapCaller(pathTuple),pathTuple)
