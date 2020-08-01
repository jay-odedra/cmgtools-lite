# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()



BuToKJpsi_ToMuMu = kreator.makeDataComponentFromEOS('BuToKJpsiMuMu','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToKJpsi_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_ToMuMu_v0/200213_162954/0000/','.*root')
BuToKMuMu = kreator.makeDataComponentFromEOS('BuToKMuMu','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToK_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKMuMu_v0/200213_163107/0000/','.*root')
BuToKPsi2S_ToMuMu = kreator.makeDataComponentFromEOS('BuToKPsi2SMuMu','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_UnbiasedForTrigger_13_2_2020/Kpsi2SMuMu/','.*root')
BuToKEE_onlyPF = kreator.makeDataComponentFromEOS('BuToKpfEE','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToK_Toee_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKEE_v0/200213_163211/0000/','.*root')
BuToKEE = kreator.makeDataComponentFromEOS('BuToKEE','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToKee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen-ext2/crab_BuToKEE/200216_215022/0000/','.*root')
BuToKEE_filterBiased = kreator.makeDataComponentFromEOS('BuToKEE_filterBiased','/store/cmst3/group/bpark/gkaratha/BToKEE_FilterBiased_OnlyForBDT_MC_05_06_2020/BuToKee_MufilterPt6_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKEE_v2/200605_162055/0000/','.*root')
BuToKJpsi_ToEE_onlyPF = kreator.makeDataComponentFromEOS('BuToKJpsipfEE','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToKJpsi_Toee_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_ToEE_v0/200213_163325/0000/','.*root')
BuToKJpsi_ToEE = kreator.makeDataComponentFromEOS('BuToKJpsiEE','/store/cmst3/group/bpark/gkaratha/NoTrgCut_CentralMC_BtoKll_MC_15_2_2020/BuToKJpsi_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen-ext2/crab_BuToKJpsi_ToEE/200216_215812/0000/','.*root')
BuToKPsi2S_ToEE = kreator.makeDataComponentFromEOS('BuToKPsi2SEE','/store/cmst3/group/bpark/gkaratha/BToPsi2SK_toEE/','.*root')

#crab_BuToKJpsi_ToMuMu_0000 = kreator.makeDataComponentFromEOS('crab_BuToKJpsi_ToMuMu_0000','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_MuFilter_18_12_2019/BParkingNANO_2019Dec16/BuToKJpsi_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKJpsi_ToMuMu/191216_120056/0000/','.*root')
#crab_BuToKMuMu_0000 = kreator.makeDataComponentFromEOS('crab_BuToKMuMu_0000','/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_MuFilter_18_12_2019/BParkingNANO_2019Dec16/BuToK_ToMuMu_MuFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/crab_BuToKMuMu/191216_120214/0000/','.*root')


samples = [BuToKJpsi_ToMuMu, BuToKMuMu, BuToKPsi2S_ToMuMu, BuToKEE_onlyPF, BuToKEE, BuToKJpsi_ToEE_onlyPF, BuToKJpsi_ToEE, BuToKEE_filterBiased,BuToKPsi2S_ToEE] 



if __name__ == "__main__":
	from CMGTools.RootTools.samples.tools import runMain
	runMain(samples, localobjs=locals())
