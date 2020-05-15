from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'LLP_MC'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'CSCTPEmulator_analyzer_MC_cfg.py'

config.Data.inputDataset = '/ppTohToSSTo4b/nimenend-ppTohToSSTo4b_DIGI_L1-a596ea383b59a86946582bc7b3e1da7f/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/nimenend/All_LCT/'
config.Data.publication = True
config.Data.outputDatasetTag = 'ppTohToSSTo4b_ALL_LCT_Analyzed'

config.Site.storageSite = 'T3_US_FNALLPC'
