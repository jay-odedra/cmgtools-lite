from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()
test = kreator.makeDataComponentFromEOS("test","/store/group/phys_bphys/DiElectronX/jodedra/singulartestmc/", ".*root")

#Signal Process MC
BuToKee_v1_postEE = kreator.makeDataComponentFromEOS("BuToKee_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKee_v1_postEE/230310_173557/0000/", ".*root")
BuToKee_v1_preEE = kreator.makeDataComponentFromEOS("BuToKee_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKee_v1_preEE/230310_173544/0000/", ".*root")
#CC resonance MC
BuToKJpsi_Toee_v1_postEE = kreator.makeDataComponentFromEOS("BuToKJpsi_Toee_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKJPsi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKJpsi_Toee_v1_postEE/230310_173627/0000/", ".*root")
BuToKJpsi_Toee_v1_preEE = kreator.makeDataComponentFromEOS("BuToKJpsi_Toee_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKJPsi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKJpsi_Toee_v1_preEE/230310_173612/0000/", ".*root")
BuToKPsi2S_Toee_v1_postEE = kreator.makeDataComponentFromEOS("BuToKPsi2S_Toee_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKPsi2s_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKPsi2S_Toee_v1_postEE/230310_173700/0000/", ".*root")
BuToKPsi2S_Toee_v1_preEE = kreator.makeDataComponentFromEOS("BuToKPsi2S_Toee_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar10/BuToKPsi2s_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKPsi2S_Toee_v1_preEE/230310_173641/0000/", ".*root")

#Background MC
BdToK0starEE_v1_postEE = kreator.makeDataComponentFromEOS("BdToK0starEE_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starEE_K0starToKPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starEE_v1_postEE/230314_133717/0000/", ".*root")
BdToK0starEE_v1_preEE = kreator.makeDataComponentFromEOS("BdToK0starEE_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starEE_K0starToKPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starEE_v1_preEE/230314_133710/0000/", ".*root")
BdToK0starJpsi_Toee_v1_postEE = kreator.makeDataComponentFromEOS("BdToK0starJpsi_Toee_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starJPsi_K0starToKPi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starJpsi_Toee_v1_postEE/230314_133730/0000/", ".*root")
BdToK0starJpsi_Toee_v1_preEE = kreator.makeDataComponentFromEOS("BdToK0starJpsi_Toee_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starJPsi_K0starToKPi_JPsiToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starJpsi_Toee_v1_preEE/230314_133723/0000/", ".*root")
BdToK0starPsi2S_Toee_v1_postEE = kreator.makeDataComponentFromEOS("BdToK0starPsi2S_Toee_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starPsi2s_K0starToKPi_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starPsi2S_Toee_v1_postEE/230314_133742/0000/", ".*root")
BdToK0starPsi2S_Toee_v1_preEE = kreator.makeDataComponentFromEOS("BdToK0starPsi2S_Toee_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BdToK0starPsi2s_K0starToKPi_Psi2sToEE_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BdToK0starPsi2S_Toee_v1_preEE/230314_133736/0000/", ".*root")
BuToKstarEE_v1_postEE = kreator.makeDataComponentFromEOS("BuToKstarEE_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarEE_KstarToK0Pi_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarEE_v1_postEE/230314_170320/0000/", ".*root")
BuToKstarEE_v1_preEE = kreator.makeDataComponentFromEOS("BuToKstarEE_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarEE_KstarToK0Pi_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarEE_v1_preEE/230314_170302/0000/", ".*root")
BuToKstarJpsi_Toee_v1_postEE = kreator.makeDataComponentFromEOS("BuToKstarJpsi_Toee_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarJPsi_KstarToK0Pi_JPsiToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarJpsi_Toee_v1_postEE/230314_170359/0000/", ".*root")
BuToKstarJpsi_Toee_v1_preEE = kreator.makeDataComponentFromEOS("BuToKstarJpsi_Toee_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarJPsi_KstarToK0Pi_JPsiToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarJpsi_Toee_v1_preEE/230314_170338/0000/", ".*root")
BuToKstarPsi2S_Toee_v1_postEE = kreator.makeDataComponentFromEOS("BuToKstarPsi2S_Toee_v1_postEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarPsi2s_KstarToK0Pi_Psi2sToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarPsi2S_Toee_v1_postEE/230314_170442/0000/", ".*root")
BuToKstarPsi2S_Toee_v1_preEE = kreator.makeDataComponentFromEOS("BuToKstarPsi2S_Toee_v1_preEE","/store/group/phys_bphys/DiElectronX/production/samples/BParkingNANO_2023Mar14/BuToKstarPsi2s_KstarToK0Pi_Psi2sToEE_K0ToPiPi_SoftQCD_TuneCP5_13p6TeV_pythia8-evtgen/crab_BuToKstarPsi2S_Toee_v1_preEE/230314_170417/0000/", ".*root")

samples = [test,BuToKee_v1_postEE,BuToKee_v1_preEE,BuToKJpsi_Toee_v1_postEE,BuToKJpsi_Toee_v1_preEE,
           BuToKPsi2S_Toee_v1_postEE,BuToKPsi2S_Toee_v1_preEE,BdToK0starEE_v1_postEE,
           BdToK0starEE_v1_preEE,BdToK0starJpsi_Toee_v1_postEE,BdToK0starJpsi_Toee_v1_preEE,
           BdToK0starPsi2S_Toee_v1_postEE,BdToK0starPsi2S_Toee_v1_preEE,BuToKstarEE_v1_postEE,
           BuToKstarEE_v1_preEE,BuToKstarJpsi_Toee_v1_postEE,BuToKstarJpsi_Toee_v1_preEE,
           BuToKstarPsi2S_Toee_v1_postEE,BuToKstarPsi2S_Toee_v1_preEE]

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples, localobjs=locals())
