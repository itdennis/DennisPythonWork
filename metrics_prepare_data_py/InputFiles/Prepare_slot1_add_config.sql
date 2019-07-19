SET IDENTITY_INSERT [dbo].[ConfigInfoes] ON
INSERT INTO [dbo].[ConfigInfoes] ([Id], [ConfigName], [SlotId], [ConfigPayload], [Desc], [Owner], [IsActive], [SubmitIntervalHours], [CreateDtm], [ModifiedDtm], [InterfaceConfigPayload], [JobType]) VALUES (1, N'Case1.json', 1, N'{
    "ExperimentInfo": {
        "OverrideDate": null,
        "RunAsAccountName": null,
        "RunAsAccountPwd": null,
        "TimeOutInMins": 0,
        "JobType": 1,
        "JobTag": "WoodblocksAdsFedP",
        "SubmitSchedule": {
            "Minute": "*",
            "Hour": "*",
            "Day": "*",
            "Month": "*",
            "Week": "*",
            "MaxIntervalInMinutes": 0
        },
        "ExperimentParameters": {
            "BaseExperimentId": "e90cf751-c088-4ec5-9502-680a284affe4",
            "JobName": "string.Format(\"[{0}][Download WASP UnitTest Fake Data From Cosmos]\",DateTime.UtcNow.ToString(\"yyyy-MM-dd\"))",
            "MailFrom": null,
            "AetherPriority": 3,
            "CosmosPriority": 999
        },
        "ModificationItems": [
            {
                "Tag": "Fake Data Date",
                "Parameter": "DateVersion",
                "ValueTemplate": "DateTime.UtcNow.AddDays(-1).ToString(\"yyyyMMdd\").Substring(0, 7)"
            },
			{
                "Tag": "Fake Data Version",
                "Parameter": "CaseVersion",
                "ValueTemplate": "\"Case1\""
            }
        ]
    },
    "PublishInfo": {
        "IsPublish": false,
        "ModelTarget": 2,
        "ModelType": 1,
        "ModelFormat": 3,
        "TargetRepo": 2,
        "TargetEnv": 4,
        "PrimarySlotId": 1,
        "ModelInfoes": [
            {
                "SlotId": 1,
                "PartitionNum": 1,
                "ModelFilePattern": "WoodblocksLego/Slot19/#",
                "IsFolder": false,
                "ModelOutPut": {
                    "NodeId": "1a98f847",
                    "Tag": "CosmosSpec",
                    "OutputName": "CosmosSpec",
                    "ValidationDataPath": null
                },
                "CheckSumOutPut": null,
                "Commnets": null
            }
        ],
        "AdditionalOutputs": null
    },
    "Metrics": {
        "MetricsItems": [
            {
                "NodeId": "b36ece3f",
                "Tag": "OfflineMetrics_1",
                "OutputName": "TSV",
                "ValidationDataPath": "string.Format(\"[{0}][OfflineMetrics_1]\", DateTime.UtcNow.AddDays(1).ToString(\"yyyy-MM-dd\"))"                
            },
            {
                "NodeId": "2b5393b0",
                "Tag": "OfflineMetrics_2",
                "OutputName": "TSV",
                "ValidationDataPath": "string.Format(\"[{0}][OfflineMetrics_2]\", DateTime.UtcNow.AddDays(1).ToString(\"yyyy-MM-dd\"))"   

            },
            {
                "NodeId": "5250da3f",
                "Tag": "OfflineMetrics_3",
                "OutputName": "TSV",
                "ValidationDataPath": "string.Format(\"[{0}][OfflineMetrics_3]\", DateTime.UtcNow.ToString(\"yyyy-MM-dd\"))"   
            },
            {
                "NodeId": "b6220155",
                "Tag": "OfflineMetrics_4",
                "OutputName": "TSV",
                "ValidationDataPath": "string.Format(\"[{0}][OfflineMetrics_4]\", DateTime.UtcNow.ToString(\"yyyy-MM-dd\"))"   
            },
            {
                "NodeId": "da03781d",
                "Tag": "TrainingStatus",
                "OutputName": "TSV",
                "ValidationDataPath": null
            }
        ],
        "MetricsValidationgInfo": {
            "ModelPath": "",
            "ValidationDataPath": "",
            "ValidationDataHeaderPath": "",
            "SavingTag": "WB_ADSFEDP_SLOT19_LEGO",
            "MetricThresholds": [
                {
                    "Key": "m_DisplayLocation=sb-1:auc:OfflineMetrics_1",
                    "Value": 0.01
                },
                {
                    "Key": "m_DisplayLocation=sb-1,m_ProviderId=0:auc:OfflineMetrics_1",
                    "Value": 0.01
                },
                {
                    "Key": "m_DisplayLocation=sb-1,m_ProviderId=1:auc:OfflineMetrics_1",
                    "Value": 0.01
                },
                {
                    "Key": "m_DisplayLocation=sb-1,m_DeviceTypeId=1:auc:OfflineMetrics_1",
                    "Value": 0.01
                },
                {
                    "Key": "TrainingDataBing:impressions:OfflineMetrics_3",
                    "Value": 0.08
                },
                {
                    "Key": "TrainingDataBing:ctr:OfflineMetrics_3",
                    "Value": 0.1
                },
                {
                    "Key": "TrainingDataYahoo:impressions:OfflineMetrics_4",
                    "Value": 0.08
                },
                {
                    "Key": "TrainingDataYahoo:ctr:OfflineMetrics_4",
                    "Value": 0.1
                }
            ]
        }
    },
    "MailInfo": {
        "MailFrom": "wbsrv",
        "MailTo": "wenchen"
    },
    "TrainingParam": null,
    "ValidationParam": null
}', N'Case1.json', N'fareast\wenchen', 1, 1440, N'2018-01-02 03:21:56', N'2018-01-02 03:21:56', NULL, 1)
SET IDENTITY_INSERT [dbo].[ConfigInfoes] OFF

GO