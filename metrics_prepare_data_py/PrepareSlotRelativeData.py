import os
import re
newslotid = 19
multiple = 10000
spath = 'metrics_prepare_data_py/InputFiles/'
tpath = 'metrics_prepare_data_py/OutputFiles/'
basejobhistoryfilename = 'Prepare_slot1_add_histroy_jobs.sql'
basemetrichistoryfilename = 'Prepare_slot1_add_histroy_metrics.sql'
sourceslotid = 'N\'1\''
targetslotid = 'N\'' + str(newslotid) + '\''

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

path = os.listdir(spath)
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
        filedata = filedata.replace(sourceslotid, targetslotid)
        destinationpath = tpath + 'Prepare_slot' + str(newslotid) + '_add_histroy_metrics.sql'
        with open(destinationpath, 'w') as file:
            file.write(filedata)
        print('Conversion finished for: ' + destinationpath)    