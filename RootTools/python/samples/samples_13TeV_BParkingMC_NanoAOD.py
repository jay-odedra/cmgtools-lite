# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()



BuToKJpsi_ToMuMu = kreator.makeDataComponentFromEOS('BuToKJpsiMuMu','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToKJpsi_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_ToMuMu_v0/200213_162954/0000/','.*root')
BuToKMuMu = kreator.makeDataComponentFromEOS('BuToKMuMu','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToK_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKMuMu_v0/200213_163107/0000/','.*root')
BuToKMuMu_trgtest = kreator.makeDataComponentFromEOS('BuToKMuMu_trgtest','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_UnbiasedForTrigger_13_2_2020/KMuMu/','.*root')
BuToKJPsiMuMu_trgtest = kreator.makeDataComponentFromEOS('BuToKJPsiMuMu_trgtest','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_UnbiasedForTrigger_13_2_2020/KJpsiMuMu/','.*root')
BuToKPsi2S_ToMuMu_unbiased = kreator.makeDataComponentFromEOS('BuToKPsi2SMuMu_unbiased','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_UnbiasedForTrigger_13_2_2020/Kpsi2SMuMu/','.*root')

BuToKPsi2S_ToMuMu_biased = kreator.makeDataComponentFromEOS('BuToKPsi2SMuMu_biased','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar07/BuToKPsi2S_ToMuMu_probefilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKPsi2S_ToMuMu/210307_022449/0000/','.*root')

BdToKstarPsi2S_ToMuMu_biased = kreator.makeDataComponentFromEOS('BdToKstarPsi2SMuMu_biased','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar07/BdToKstarPsi2S_ToKPiMuMu_probefilterPt2_SoftQCDnonD_TuneCP5_13Tev-pythia8-evtgen/crab_BdToKstarPsi2S_ToMuMu/210307_022929/0000/','.*root')

BdToKstarJpsiMuMu_part1 = kreator.makeDataComponentFromEOS('BdToKstarJpsiMuMu_part1','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar07/BdToKstarJpsi_ToKPiMuMu_probefilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BdToKstarJpsi_ToMuMu/210307_021931/0000/','.*root')

BdToKstarJpsiMuMu_part2 = kreator.makeDataComponentFromEOS('BdToKstarJpsiMuMu_part2','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar07/BdToKstarJpsi_ToKPiMuMu_probefilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BdToKstarJpsi_ToMuMu_v2/210307_022107/0000/','.*root')


######################################## kee / kjpsi ee #####################
BuToKEE_onlyPF_part1 = kreator.makeDataComponentFromEOS('BuToKpfEE_part1','/store/cmst3/group/bpark/gkaratha/Nano_PFeKEE_v3.0_10_3_2021/BuToKee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKee_mcpart1/210412_164415/0000/','.*root')
BuToKEE_onlyPF_part2 = kreator.makeDataComponentFromEOS('BuToKpfEE_part2','/store/cmst3/group/bpark/gkaratha/Nano_PFeKEE_v3.0_10_3_2021/BuToKee_MufilterPt6_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKee_mcpart2/210412_164239/0000/','.*root')
BuToKJpsi_ToEE_onlyPF_part1 = kreator.makeDataComponentFromEOS('BuToKJpsipfEE_part1','/store/cmst3/group/bpark/gkaratha/Nano_PFeKEE_v3.0_10_3_2021/BuToKJpsi_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_Toee_mcpart1/210412_164144/0000/','.*root')
BuToKJpsi_ToEE_onlyPF_part2 = kreator.makeDataComponentFromEOS('BuToKJpsipfEE_part2','/store/cmst3/group/bpark/gkaratha/Nano_PFeKEE_v3.0_10_3_2021/BuToKJpsi_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_Toee_mcpart2/210412_164600/0000/','.*root')

BuToKJpsi_ToEE_LowpTPF = kreator.makeDataComponentFromEOS('BuToKJpsi_ToEE_LowpTPF','/store/group/phys_bphys/bpark/nanoaod_RK2021/mc_noSkim/BParkingNANO_2021Mar23/BuToKJpsi_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_Toee_v2/210323_222415/0000/','.*root')

BuToKEE_onlyLowpTPF_part1 = kreator.makeDataComponentFromEOS('BuToKEE_onlyLowpTPF_part1','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May13/BuToKee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKee_mcpart1/210513_062301/0000/','.*root')

BuToKEE_onlyLowpTPF_part2 = kreator.makeDataComponentFromEOS('BuToKEE_onlyLowpTPF_part2','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May13/BuToKee_MufilterPt6_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKee_mcpart2/210513_062129/0000/','.*root')

BuToKEE_bothE_correctPU_biased = kreator.makeDataComponentFromEOS('BuToKEE_bothE_correctPU_biased','/store/cmst3/group/bpark//gkaratha/Nano_BothEKEE_correctPU_v3.0_26_08_2021/BuToKee_MufilterPt6Eta1p6_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKee_mcpart3/210825_223758/0000/','.*root')

BuToKJpsiEE_bothE_correctPU_unbiased = kreator.makeDataComponentFromEOS('BuToKJpsiEE_bothE_correctPU_unbiased','/store/cmst3/group/bpark//gkaratha/Nano_BothEKEE_KJpsiEE_correctPU_unbiased_v3.0_29_08_2021/BuToKJpsi_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_Toee_mcpart3/210829_194150/0000/','.*root')

BuToKEE_bothE_correctPU_unbiased = kreator.makeDataComponentFromEOS('BuToKEE_bothE_correctPU_unbiased','/store/cmst3/group/bpark//gkaratha/Nano_BothEKEE_KJpsiEE_correctPU_unbiased_v3.0_29_08_2021/BuToKee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKee_mcpart3_unbiased/210829_194252/0000/','.*root')


################################  KstarJpsiEE, BKG for KJpsiEE ##########
BdToKstarJpsiEE_part1 = kreator.makeDataComponentFromEOS('BdToKstarJpsiEE_part1','/store/cmst3/group/bpark/gkaratha/Nano_BToKstarJpsi_ToKPiEE_MuFilter_29_05_2021/BdToKstarJpsi_ToKPiee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BdToKstarJpsi_ToKPiee_mcpart1/210529_005739/0000/','.*root')
BdToKstarJpsiEE_part2 = kreator.makeDataComponentFromEOS('BdToKstarJpsiEE_part2','/store/cmst3/group/bpark/gkaratha/Nano_BToKstarJpsi_ToKPiEE_MuFilter_29_05_2021/BdToKstarJpsi_ToKPiee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BdToKstarJpsi_ToKPiee_mcpart2/210529_005651/0000/','.*root')
BdToKstarJpsiLowPtEE_part1 = kreator.makeDataComponentFromEOS('BdToKstarJpsiLowPtEE_part1','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar07/BdToKstarJpsi_ToKPiee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BdToKstarJpsi_Toee/210307_021655/0000/','.*root')
BdToKstarJpsiLowPtEE_part2 = kreator.makeDataComponentFromEOS('BdToKstarJpsiLowPtEE_part2','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar07/BdToKstarJpsi_ToKPiee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BdToKstarJpsi_Toee_v2/210307_021804/0000/','.*root')


#old
BuToKPsi2S_ToEE = kreator.makeDataComponentFromEOS('BuToKPsi2SEE','/store/cmst3/group/bpark/gkaratha/BToPsi2SK_toEE/','.*root')
#old
BuToKPsi2S_ToEE_part1 = kreator.makeDataComponentFromEOS('BuToKPsi2SEE_part1','/store/cmst3/group/bpark/gkaratha/Nano_MC_Kpsi2See_PFeOnly_2020Nov16/BuToKPsi2S_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKPsi2S_Toee/201116_200105/0000/','.*root')
BuToKPsi2S_ToEE_part2 = kreator.makeDataComponentFromEOS('BuToKPsi2SEE_part2_filterBiased','/store/cmst3/group/bpark/gkaratha/Nano_MC_Kpsi2See_PFeOnly_2020Nov16/BuToKPsi2S_Toee_MufilterPt6_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKPsi2S_Toee_part1/201116_200153/0000/','.*root')

#new
BuToKPsi2S_ToEE_bothE = kreator.makeDataComponentFromEOS('BuToKPsi2See_bothE','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021May07/BuToKPsi2S_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKPsi2S_Toee_v2/210507_133638/0000/','.*root')

#K*psi(2S)
BdToKstarPsi2S_ToEE_bothE = kreator.makeDataComponentFromEOS('BdToKstarPsi2See_bothE','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021May07/BdToKstarPsi2S_ToKPiee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BdToKstarPsi2S_Toee_v2/210507_133823/0000/','.*root')


#crab_BuToKJpsi_ToMuMu_0000 = kreator.makeDataComponentFromEOS('crab_BuToKJpsi_ToMuMu_0000','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_MuFilter_18_12_2019/BParkingNANO_2019Dec16/BuToKJpsi_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_ToMuMu/191216_120056/0000/','.*root')
#crab_BuToKMuMu_0000 = kreator.makeDataComponentFromEOS('crab_BuToKMuMu_0000','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_MuFilter_18_12_2019/BParkingNANO_2019Dec16/BuToK_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKMuMu/191216_120214/0000/','.*root')


samples = [BuToKJpsi_ToMuMu, BuToKMuMu, BuToKPsi2S_ToMuMu_unbiased, BuToKEE_onlyPF_part1,BdToKstarJpsiMuMu_part1, BdToKstarJpsiMuMu_part2, BuToKEE_onlyPF_part2, BuToKJpsi_ToEE_onlyPF_part1, BuToKJpsi_ToEE_onlyPF_part2, BuToKPsi2S_ToEE,BuToKMuMu_trgtest, BuToKJPsiMuMu_trgtest, BuToKPsi2S_ToEE_part1, BuToKPsi2S_ToEE_part2, BuToKEE_onlyLowpTPF_part1, BuToKEE_onlyLowpTPF_part2, BuToKJpsi_ToEE_LowpTPF, BdToKstarJpsiEE_part1, BdToKstarJpsiEE_part2,BdToKstarJpsiLowPtEE_part1, BdToKstarJpsiLowPtEE_part2, BuToKPsi2S_ToEE_bothE, BdToKstarPsi2S_ToEE_bothE, BuToKEE_bothE_correctPU_biased, BuToKJpsiEE_bothE_correctPU_unbiased, BuToKEE_bothE_correctPU_unbiased, BuToKPsi2S_ToMuMu_biased, BdToKstarPsi2S_ToMuMu_biased ] 



if __name__ == "__main__":
	from CMGTools.RootTools.samples.tools import runMain
	runMain(samples, localobjs=locals())
