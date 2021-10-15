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
            23, 46, 69,
            # ME1/3
            9, 19, 28,
            # ME2/1
            18, 37, 55,
            # ME2/2
            14, 28, 42,
            # ME3/1
            17, 35, 52,
            # ME3/2
            13, 26, 39,
            # ME4/1
            19, 38, 57,
            # ME4/2
            15, 30, 45
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
            24, 49, 73,
            # ME1/3
            10, 20, 30,
            # ME2/1
            30, 60, 90,
            # ME2/2
            13, 26, 39,
            # ME3/1
            28, 59, 87,
            # ME3/2
            12, 24, 36,
            # ME4/1
            33, 66, 99,
            # ME4/2
            17, 35, 52
        ),
        showerMinInTBin = cms.uint32(8),
        showerMaxInTBin = cms.uint32(8),
        showerMinOutTBin = cms.uint32(4),
        showerMaxOutTBin = cms.uint32(7),
    )
)
