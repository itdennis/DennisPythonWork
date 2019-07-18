import os
import re
newslotid = 19
spath = 'metrics_prepare_data_py/InputFiles/'
tpath = 'metrics_prepare_data_py/OutputFiles/'
# 将匹配的数字乘以 slotId * 100000
def refactor(matched):
    jobid = int(matched.group('jobid'))
    newjobid = str(jobid + newslotid * 100000)
    return 'VALUES( N\'' + newjobid + '\''

path = os.listdir(spath)
for file in path:
    if(file == 'Prepare_slot1_add_histroy_jobs.sql'):
        pattern = 'VALUES \(N\'(?P<jobid>\d\d\d\d)\''
        sourceslotid = 'N\'1\''
        targetslotid = 'N\'' + str(newslotid) + '\''
        inputfile = spath + file
        print('Conversion is ongoing for: ' + inputfile)
        with open(inputfile, 'r') as inputfile:
            filedata = inputfile.read()
        # replace old job id to job id + slot id * 100000
        filedata = re.sub(pattern, refactor, filedata)
        # replace old slot id to new slot id
        filedata = filedata.replace(sourceslotid, targetslotid)
        destinationpath = tpath + file
        with open(destinationpath, 'w') as file:
            file.write(filedata)
        print('Conversion finished for: ' + destinationpath)