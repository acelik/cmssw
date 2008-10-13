import FWCore.ParameterSet.Config as cms

TrackHitFilter = cms.EDFilter("TrackHitFilter",
    theBadModules = cms.vuint32(369329156, 369329160, 369329164, 369328388, 369328392, 
        369328396, 369328644, 369328648, 369328652, 369328900, 
        369328904, 369328908, 369199365, 369199366, 369199369, 
        369199370, 369199373, 369199374, 369263877, 369263878, 
        369263881, 369263882, 369263885, 369263886, 369279237, 
        369279238, 369279241, 369279242, 369279245, 369279246, 
        369214469, 369214470, 369214473, 369214474, 369214477, 
        369214478, 436373509, 436373510, 436373513, 436373514, 
        436373517, 436373518, 436373521, 436373522, 436373525, 
        436373526, 436373529, 436373530, 436569348, 436569352, 
        436569356, 436569360, 436569364, 436569368, 436437508, 
        436437512, 436437516, 436437520, 436437524, 436437528, 
        436440580, 436440584, 436440588, 436440592, 436440596, 
        436440600, 436570628, 436570632, 436570636, 436570640, 
        436570644, 436570648, 486998949, 486998950, 486998953, 
        486998954, 486998957, 486998958, 486999012, 486999016, 
        486999020, 486999024, 486999028, 486802341, 486802342, 
        486802345, 486802346, 486802349, 486802350, 486802404, 
        486802408, 486802412, 486802416, 486802420, 369348100, 
        369345544, 419562288, 419562284, 419627570, 486802246, 
        436306950, 486671092, 486671092),
    src = cms.InputTag("ctfWithMaterialTracks"),
    minHitsForRefit = cms.uint32(2),
    hitSelection = cms.string('all'),
    rejectBadMods = cms.bool(False),
	rejectBadStoNHits = cms.bool(False),
    theStoNthreshold = cms.double(20.0),
    CommonModeNoiseSubtractionMode = cms.string('Median') # "TT6"

)


