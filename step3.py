# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: cmsDriver.py step3 --conditions auto:phase2_realistic -n -1 --era Phase2 --eventcontent RECOSIM --runUnscheduled -s RAW2DIGI:RawToDigi_pixelOnly,RECO:reconstruction_pixelTrackingOnly --geometry Extended2023D21 --pileup AVE_200_BX_25ns --pileup_input das:/RelValMinBias_14TeV/CMSSW_10_4_0_pre2-103X_upgrade2023*D21*/GEN-SIM --filein file:output.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2_cff import Phase2

process = cms.Process('RECO',Phase2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D21Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.load("L1Trigger.TrackFindingTracklet.Tracklet_cfi")
L1TRK_PROC  =  process.TTTracksFromTrackletEmulation
L1TRK_NAME  = "TTTracksFromTrackletEmulation"
L1TRK_LABEL = "Level1TTTracks"

process.dump=cms.EDAnalyzer('EventContentAnalyzer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:output.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('cmsDriver.py nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('step3.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.RECOSIMoutput.outputCommands.append('keep  *')

process.L1TrackNtuple = cms.EDAnalyzer('L1PixelTracks',
                                       MyProcess = cms.int32(1),
                                       DebugMode = cms.bool(False),      # printout lots of debug statements
                                       SaveAllTracks = cms.bool(True),   # save *all* L1 tracks, not just truth matched to primary particle
                                       SaveStubs = cms.bool(True),      # save some info for *all* stubs
                                       L1Tk_nPar = cms.int32(4), # use 4 or 5-parameter L1 tracking?
                                       L1Tk_minNStub = cms.int32(3),     # L1 tracks with >= 4 stubs
                                       TP_minNStub = cms.int32(3),       # require TP to have >= X number of stubs associated with it
                                       TP_minNStubLayer = cms.int32(3),  # require TP to have stubs in >= X layers/disks
                                       TP_minPt = cms.double(2.0),       # only save TPs with pt > X GeV
                                       TP_maxEta = cms.double(2.5),      # only save TPs with |eta| < X
                                       TP_maxZ0 = cms.double(30.0),      # only save TPs with |z0| < X cm
                                       L1TrackInputTag = cms.InputTag(L1TRK_NAME, L1TRK_LABEL), # TTTrack input
                                       MCTruthTrackInputTag = cms.InputTag("TTTrackAssociatorFromPixelDigis", L1TRK_LABEL),  ## MCTruth input
                                       # other input collections
                                                   PixelTracksInputTag = cms.InputTag("pixelTracks"),
                                       PixelTracksExtraInputTag = cms.InputTag("pixelTracks"),
                                       L1StubInputTag = cms.InputTag("TTStubsFromPhase2TrackerDigis","StubAccepted"),
                                       MCTruthClusterInputTag = cms.InputTag("TTClusterAssociatorFromPixelDigis", "ClusterAccepted"),
                                       MCTruthStubInputTag = cms.InputTag("TTStubAssociatorFromPixelDigis", "StubAccepted"),
                                       TrackingParticleInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                       TrackingVertexInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                       ## tracking in jets stuff (--> requires AK4 genjet collection present!)
                                       TrackingInJets = cms.bool(True),
                                       GenJetInputTag = cms.InputTag("ak4GenJets", ""),
                                       )

process.ana = cms.Path(process.L1TrackNtuple)

process.TFileService = cms.Service("TFileService", fileName = cms.string('TTbar_PU200_hybrid.root'), closeFileFast = cms.untracked.bool(True))

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(200.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/9F12231D-132F-904F-BCC5-D7B70FD4D0D7.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/3BFB9814-7F8A-4744-A773-773AC28113C4.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/70F5AC85-46E8-8745-A5CF-2B8C47743204.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/553AFA27-C8EB-F044-9591-57F29D90527A.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/974B586D-6800-5B4B-9AEA-78BC8518257F.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/FB25285C-3225-8046-BFF2-D9A10EB9806C.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/F7EAFA17-64E9-D343-A63F-25484924F49B.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/1E161C34-8F0F-0946-983C-443E75A27265.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/06D2C06E-A59F-DC49-9836-56B3409B1B79.root', '/store/relval/CMSSW_10_4_0_pre2/RelValMinBias_14TeV/GEN-SIM/103X_upgrade2023_realistic_v2_2023D21noPU-v1/20000/50C9BEE3-A974-7647-878E-7FBD1B4E6F97.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi_pixelOnly)
process.content = cms.Path(process.dump)
process.reconstruction_step = cms.Path(process.reconstruction_pixelTrackingOnly)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput.outputCommands.append('keep  *')
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.ana,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(4)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
