import os
import re
newslotidlist = [302,303,304]
spath = 'metrics_prepare_data_py/InputFiles/'
tpath = 'metrics_prepare_data_py/OutputFiles/'
baseslotconfigfilename = 'Prepare_slot1_add_config.sql'
sourceslotid = 'N\'2\', N\'1\''
baseowner = 'wenchen'
newowner = 'waspnotification'

def refactorconfigrecord(matched):
    caseid = int(matched.group('caseid'))
    newcaseid = newcaseslotid = str(newslotid)
    return newcaseid + ', N\'case' + newcaseid + '.json\', ' + newcaseslotid

path = os.listdir(spath)
for newslotid in newslotidlist:
    targetslotid = 'N\'2\', N\'' + str(newslotid) + '\''
    for file in path:
        if(file == baseslotconfigfilename):
            pattern = '(?P<caseid>1), N\'Case1.json\', (?P<caseslotid>1)'
            inputfile = spath + file
            print('Conversion is ongoing for: ' + inputfile)
            with open(inputfile, 'r') as inputfile:
                filedata = inputfile.read()
            filedata = re.sub(pattern, refactorconfigrecord, filedata)
            filedata = filedata.replace(baseowner, newowner)
            filedata = filedata.replace('Case1', 'Case'+str(newslotid))
            filedata = filedata.replace('"PrimarySlotId": 1,', '"PrimarySlotId": ' + str(newslotid) + ',')
            filedata = filedata.replace('"SlotId": 1,', '"SlotId": ' + str(newslotid) + ',')
            destinationpath = tpath + 'Prepare_slot' + str(newslotid) + '_add_config.sql'
            with open(destinationpath, 'w') as file:
                file.write(filedata)
            print('Conversion finished for: ' + destinationpath)