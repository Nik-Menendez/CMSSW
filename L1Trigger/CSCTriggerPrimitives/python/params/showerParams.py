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
    ## 3: cathode and anode showers
    ##    loose -> 'loose anode and loose cathode'
    ##    nominal -> 'nominal anode and nominal cathode'
    ##    tight -> 'tight anode and tight cathode'
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
            27, 55, 40,
            # ME1/3
            10, 20, 19,
            # ME2/1
            16, 35, 28,
            # ME2/2
            15, 29, 25,
            # ME3/1
            16, 35, 28,
            # ME3/2
            12, 25, 22,
            # ME4/1
            18, 40, 28,
            # ME4/2
            13, 30, 25
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
            28, 56, 84,
            # ME1/3
            11, 22, 33,
            # ME2/1
            28, 55, 82,
            # ME2/2
            17, 34, 51,
            # ME3/1
            37, 74, 111,
            # ME3/2
            14, 27, 40,
            # ME4/1
            43, 86, 129,
            # ME4/2
            34, 67, 100
        ),
        showerMinInTBin = cms.uint32(8),
        showerMaxInTBin = cms.uint32(8),
        showerMinOutTBin = cms.uint32(4),
        showerMaxOutTBin = cms.uint32(7),
    )
)
