# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

BuToKEE = kreator.makeDataComponentFromEOS('BuToKEE', '/store/group/phys_bphys/DiElectronX/nzipper/BParking/samples/BParkingNANO_2023Mar02/BuTOjpsiKEE20221103FIFTYM/crab_BuToKJpsi_Toee/230302_132816/0000/', '.*root')

samples = [BuToKEE]

if __name__ == "__main__":
	from CMGTools.RootTools.samples.tools import runMain
	runMain(samples, localobjs=locals())
