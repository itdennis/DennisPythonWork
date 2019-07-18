import os
import re
texttofind='N\'1\''
texttoreplace='N\'19\''
sourcepath = os.listdir('InputFiles/')
for file in sourcepath:
    if(file == 'Prepare_slot1_add_histroy_jobs.sql'):
        inputfile = 'InputFiles/' + file
        print('Conversion is  ongoing for: ' + inputfile)
        with open(inputfile, 'r') as inputfile:
            filedata = inputfile.read()
            freq = 0
            freq = filedata.count(texttofind) 
        destinationpath = 'OutputFiles/' + file
        filedata = filedata.replace(texttofind, texttoreplace)
        with open(destinationpath, 'w') as file:
            file.write(filedata)
        print('Total %d Record Replaced' %freq)