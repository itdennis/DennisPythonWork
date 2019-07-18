import os
import re
pattern='INSERT [dbo].[JobInfoes] ([Id], [Status], [SlotId], [ExperimentId], [JobDesc], [Tag], [TrainingEndTime], [Config], [PublishRecord], [SubmitService], [JobType], [Owner], [RetryTime], [CreateDtm], [ModifiedDtm], [InterfaceConfig], [ValidationRecord], [OperationType], [LineCount], [Impressions], [Ctr], [MaxFeatureId]) VALUES (*d,d,19'

sourcepath = os.listdir('InputFiles/')
for file in sourcepath:
    inputfile = 'InputFiles/' + file
    print('Conversion is  ongoing for: ' + inputfile)
    with open(inputfile, 'r') as inputfile:
        filedata = inputfile.readline()
        freq = re.match(pattern, filedata).span()
    destinationpath = 'OutputFiles/' + file
    with open(destinationpath, 'w') as file:
        file.write(filedata)