# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()


#part1
crab_data_Run2018A_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part1_0000','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018A_part1/200116_150535/0000/','.*root')
crab_data_Run2018A_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part1_0001','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018A_part1/200116_150535/0001/','.*root')
crab_data_Run2018B_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part1_0000','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018B_part1/200116_150810/0000/','.*root')
crab_data_Run2018B_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part1_0001','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018B_part1/200116_150810/0001/','.*root')
crab_data_Run2018C_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part1_0000','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018C_part1/200116_151112/0000/','.*root')
crab_data_Run2018C_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part1_0001','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018C_part1/200116_151112/0001/','.*root')
crab_data_Run2018D_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0000','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018D_part1/200116_151214/0000/','.*root')
crab_data_Run2018D_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0001','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018D_part1/200116_151214/0001/','.*root')
crab_data_Run2018D_part1_0002 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0002','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018D_part1/200116_151214/0002/','.*root')
crab_data_Run2018D_part1_0003 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0003','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018D_part1/200116_151214/0003/','.*root')
crab_data_Run2018D_part1_0004 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0004','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018D_part1/200116_151214/0004/','.*root')
crab_data_Run2018D_part1_0005 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0005','/store/cmst3/group/bpark/BParkingNANO_2020Jan16/ParkingBPH1/crab_data_Run2018D_part1/200116_151214/0005/','.*root')




samples = [crab_data_Run2018A_part1_0000,crab_data_Run2018A_part1_0001,crab_data_Run2018B_part1_0000,crab_data_Run2018B_part1_0001,crab_data_Run2018C_part1_0000,crab_data_Run2018C_part1_0001,crab_data_Run2018D_part1_0000,crab_data_Run2018D_part1_0001,crab_data_Run2018D_part1_0002,crab_data_Run2018D_part1_0003,crab_data_Run2018D_part1_0004,crab_data_Run2018D_part1_0005] 



if __name__ == "__main__":
	from CMGTools.RootTools.samples.tools import runMain
	runMain(samples, localobjs=locals())
