import os
import re
#newslotid = 10
newslotidlist = [2,3,4,5,6,7,8,9,10]
multiple = 10000
spath = 'metrics_prepare_data_py/InputFiles/'
tpath = 'metrics_prepare_data_py/OutputFiles/'
basejobhistoryfilename = 'Prepare_slot1_add_histroy_jobs.sql'
basemetrichistoryfilename = 'Prepare_slot1_add_histroy_metrics.sql'
baseslotconfigfilename = 'Prepare_slot1_add_config.sql'
sourceslotid = 'N\'2\', N\'1\''
#targetslotid = 'N\'' + str(newslotid) + '\''
baseowner = 'wenchen'
newowner = 'waspnotification'

# 将匹配的数字乘以 slotId * multiple
def refactorjobrecord(matched):
    jobid = int(matched.group('jobid'))
    newjobid = str(jobid + newslotid * multiple)
    return 'VALUES( N\'' + newjobid + '\''

def refactormetricrecord(matched):
    metricid = int(matched.group('metricid'))
    jobid = int(matched.group('jobid'))
    newmetricid = str(metricid + newslotid * multiple)
    newjobid = str(jobid + newslotid * multiple)
    return 'VALUES( N\'' + newmetricid +'\', N\'' + newjobid + '\''

def refactorconfigrecord(matched):
    caseid = int(matched.group('caseid'))
    newcaseid = newcaseslotid = str(newslotid)
    return newcaseid + ', N\'case' + newcaseid + '.json\', ' + newcaseslotid

path = os.listdir(spath)
for newslotid in newslotidlist:
    targetslotid = 'N\'2\', N\'' + str(newslotid) + '\''
    for file in path:
        if(file == basejobhistoryfilename):
            pattern = 'VALUES \(N\'(?P<jobid>\d+)\''
            inputfile = spath + file
            print('Conversion is ongoing for: ' + inputfile)
            with open(inputfile, 'r') as inputfile:
                filedata = inputfile.read()
            filedata = re.sub(pattern, refactorjobrecord, filedata)
            # replace old slot id to new slot id
            filedata = filedata.replace(sourceslotid, targetslotid)
            destinationpath = tpath + 'Prepare_slot' + str(newslotid) + '_add_histroy_jobs.sql'
            with open(destinationpath, 'w') as file:
                file.write(filedata)
            print('Conversion finished for: ' + destinationpath)

        if(file == basemetrichistoryfilename):
            pattern = 'VALUES\( N\'(?P<metricid>\d+)\', N\'(?P<jobid>\d+)\''
            inputfile = spath + file
            print('Conversion is ongoing for: ' + inputfile)
            with open(inputfile, 'r') as inputfile:
                filedata = inputfile.read()
            filedata = re.sub(pattern, refactormetricrecord, filedata)
            # replace old slot id to new slot id
            # filedata = filedata.replace(sourceslotid, targetslotid)
            destinationpath = tpath + 'Prepare_slot' + str(newslotid) + '_add_histroy_metrics.sql'
            with open(destinationpath, 'w') as file:
                file.write(filedata)
            print('Conversion finished for: ' + destinationpath)

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