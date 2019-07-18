import os
import re
newslotid = 19
spath = 'InputFiles/'
tpath = 'OutputFiles/'
# 将匹配的数字乘以 slotId * 10000
def refactor(matched):
    metricid = int(matched.group('metricid'))
    jobid = int(matched.group('jobid'))
    newmetricid = str(metricid + newslotid * 100000)
    newjobid = str(jobid + newslotid * 100000)
    return 'VALUES( N\'' + newmetricid +'\', N\'' + newjobid + '\''

path = os.listdir(spath)
for file in path:
    if(file == 'test.sql'):
        # jobid = 'N\'(?P<value>\d\d\d\d)\''
        metricid = 'VALUES\( N\'(?P<metricid>\d\d\d\d\d)\', N\'(?P<jobid>\d\d\d\d)\''
        sourceslotid='N\'1\''
        targetslotid='N\'' + str(newslotid) + '\''
        inputfile = spath + file
        print('Conversion is ongoing for: ' + inputfile)
        with open(inputfile, 'r') as inputfile:
            filedata = inputfile.read()
        
        # replace old job id to job id + slot id * 10000
        filedata = re.sub(metricid, refactor, filedata)

        # replace old metric id to metric id + slot id * 10000
        # filedata = re.sub(metricid, refactor, filedata)
        
        # replace old slot id to new slot id
        filedata = filedata.replace(sourceslotid, targetslotid)

        destinationpath = tpath + file
        with open(destinationpath, 'w') as file:
            file.write(filedata)