import FWCore.ParameterSet.Config as cms

#Parameterset for the hadronic shower trigger for Run-3
showerPSet = cms.PSet(
    ## what kind of shower triggers the logic?
    ## 0: cathode-only (TMB/OTMB)
    ## 1: anode-only (from ALCT board)
    ## 2: cathode or anode showers
    ##    loose -> 'loose anode or loose cathode'
    ##    nominal -> 'nominal anode or nominal cathode'
    ##    tight -> 'tight anode or tight cathode'
    source  = cms.uint32(0),

    ## settings for cathode showers (counting CSCComparatorDigi)
    cathodeShower = cms.PSet(
        ## {loose, nominal, tight} thresholds for hit counters
        ## loose ~ 0.75 kHz
        ## nominal ~ 0.5  kHz
        ## tight ~ 0.25 kHz
        showerThresholds = cms.vuint32(
            # ME1/1
            100, 100, 100,
            # ME1/2
            21, 42, 46,
            # ME1/3
            8, 15, 19,
            # ME2/1
            19, 35, 37,
            # ME2/2
            12, 24, 28,
            # ME3/1
            16, 33, 35,
            # ME3/2
            11, 22, 26,
            # ME4/1
            18, 36, 38,
            # ME4/2
            13, 26, 30
        ),
        showerMinInTBin = cms.uint32(6),
        showerMaxInTBin = cms.uint32(8),
        showerMinOutTBin = cms.uint32(2),
        showerMaxOutTBin = cms.uint32(5),
    ),
    ## settings for anode showers (counting CSCWireDigi)
    anodeShower = cms.PSet(
        ## {loose, nominal, tight} thresholds for hit counters
        showerThresholds = cms.vuint32(
            # ME1/1
            140, 140, 140,
            # ME1/2
            22, 45, 49,
            # ME1/3
            8, 16, 20,
            # ME2/1
            29, 58, 60,
            # ME2/2
            11, 22, 26,
            # ME3/1
            27, 57, 59,
            # ME3/2
            10, 20, 24,
            # ME4/1
            32, 64, 66,
            # ME4/2
            15, 31, 35
        ),
        showerMinInTBin = cms.uint32(8),
        showerMaxInTBin = cms.uint32(8),
        showerMinOutTBin = cms.uint32(4),
        showerMaxOutTBin = cms.uint32(7),
    )
)
