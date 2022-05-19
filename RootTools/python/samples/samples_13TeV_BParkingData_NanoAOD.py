# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

Charmonium_test = kreator.makePrivateMCComponent('Charmonium_test','/eos/cms/store/group/phys_bphys/ec/RKR3/test/test_files',['NANOAOD_Charmonium_2018_124X.root'])

#part1
crab_data_Run2018A_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part1_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018A_part1/210305_221032/0000/','.*root')
crab_data_Run2018A_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part1_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018A_part1/210305_221032/0001/','.*root')
crab_data_Run2018B_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part1_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018B_part1/210305_221634/0000/','.*root')
crab_data_Run2018B_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part1_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018B_part1/210305_221634/0001/','.*root')
crab_data_Run2018B_part1_0002 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part1_0002','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018B_part1_missingLumis/210329_121225/0000/','.*root')
crab_data_Run2018C_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part1_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018C_part1/210305_222135/0000/','.*root')
crab_data_Run2018C_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part1_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018C_part1/210305_222135/0001/','.*root')
crab_data_Run2018D_part1_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018D_part1/210305_222409/0000/','.*root')
crab_data_Run2018D_part1_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018D_part1/210305_222409/0001/','.*root')
crab_data_Run2018D_part1_0002 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0002','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018D_part1/210305_222409/0002/','.*root')
crab_data_Run2018D_part1_0003 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0003','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018D_part1/210305_222409/0003/','.*root')
crab_data_Run2018D_part1_0004 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0004','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018D_part1/210305_222409/0004/','.*root')
crab_data_Run2018D_part1_0005 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0005','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018D_part1/210305_222409/0005/','.*root')
crab_data_Run2018D_part1_0006 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part1_0006','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH1/crab_data_Run2018D_part1_missingLumis/210329_121409/0000/','.*root')


#part2
crab_data_Run2018A_part2_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part2_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018A_part2/210310_142346/0000/','.*root')
crab_data_Run2018A_part2_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part2_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018A_part2/210310_142346/0001/','.*root')
crab_data_Run2018B_part2_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part2_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018B_part2/210310_142257/0000/','.*root')
crab_data_Run2018B_part2_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part2_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018B_part2/210310_142257/0001/','.*root')
crab_data_Run2018C_part2_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part2_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018C_part2/210310_142431/0000/','.*root')
crab_data_Run2018C_part2_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part2_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018C_part2/210310_142431/0001/','.*root')
crab_data_Run2018D_part2_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part2_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018D_part2/210310_145836/0000/','.*root')
crab_data_Run2018D_part2_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part2_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018D_part2/210310_145836/0001/','.*root')
crab_data_Run2018D_part2_0002 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part2_0002','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018D_part2/210310_145836/0002/','.*root')
crab_data_Run2018D_part2_0003 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part2_0003','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018D_part2/210310_145836/0003/','.*root')
crab_data_Run2018D_part2_0004 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part2_0004','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018D_part2/210310_145836/0004/','.*root')
crab_data_Run2018D_part2_0005 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part2_0005','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar10/ParkingBPH2/crab_data_Run2018D_part2/210310_145836/0005/','.*root')

#part3
crab_data_Run2018A_part3_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part3_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018A_part3/210305_222019/0000/','.*root')
crab_data_Run2018A_part3_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part3_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018A_part3/210305_222019/0001/','.*root')
crab_data_Run2018B_part3_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part3_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018B_part3/210305_221932/0000/','.*root')
crab_data_Run2018B_part3_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part3_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018B_part3/210305_221932/0001/','.*root')
crab_data_Run2018C_part3_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part3_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018C_part3/210305_222100/0000/','.*root')
crab_data_Run2018C_part3_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part3_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018C_part3/210305_222100/0001/','.*root')
crab_data_Run2018D_part3_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part3_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018D_part3/210305_222225/0000/','.*root')
crab_data_Run2018D_part3_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part3_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018D_part3/210305_222225/0001/','.*root')
crab_data_Run2018D_part3_0002 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part3_0002','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018D_part3/210305_222225/0002/','.*root')
crab_data_Run2018D_part3_0003 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part3_0003','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018D_part3/210305_222225/0003/','.*root')
crab_data_Run2018D_part3_0004 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part3_0004','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018D_part3/210305_222225/0004/','.*root')
crab_data_Run2018D_part3_0005 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part3_0005','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH3/crab_data_Run2018D_part3/210305_222225/0005/','.*root')

#part4
crab_data_Run2018A_part4_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part4_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018A_part4/210306_185422/0000/','.*root')
crab_data_Run2018A_part4_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part4_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018A_part4/210306_185422/0001/','.*root')
crab_data_Run2018B_part4_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part4_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018B_part4/210306_185522/0000/','.*root')
crab_data_Run2018B_part4_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part4_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018B_part4/210306_185522/0001/','.*root')
crab_data_Run2018C_part4_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part4_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018C_part4/210306_185621/0000/','.*root')
crab_data_Run2018C_part4_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part4_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018C_part4/210306_185621/0001/','.*root')
crab_data_Run2018D_part4_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part4_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018D_part4/210306_185726/0000/','.*root')
crab_data_Run2018D_part4_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part4_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018D_part4/210306_185726/0001/','.*root')
crab_data_Run2018D_part4_0002 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part4_0002','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018D_part4/210306_185726/0002/','.*root')
crab_data_Run2018D_part4_0003 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part4_0003','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018D_part4/210306_185726/0003/','.*root')
crab_data_Run2018D_part4_0004 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part4_0004','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018D_part4/210306_185726/0004/','.*root')
crab_data_Run2018D_part4_0005 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part4_0005','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar06/ParkingBPH4/crab_data_Run2018D_part4/210306_185726/0005/','.*root')

#part5
crab_data_Run2018A_part5_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part5_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018A_part5/210305_215924/0000/','.*root')
crab_data_Run2018A_part5_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part5_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018A_part5/210305_215924/0001/','.*root')
crab_data_Run2018B_part5_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part5_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018B_part5/210305_220057/0000/','.*root')
crab_data_Run2018B_part5_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part5_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018B_part5/210305_220057/0001/','.*root')
crab_data_Run2018C_part5_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part5_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018C_part5/210305_220217/0000/','.*root')
crab_data_Run2018C_part5_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018C_part5_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018C_part5/210305_220217/0001/','.*root')
crab_data_Run2018D_part5_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part5_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018D_part5/210305_220325/0000/','.*root')
crab_data_Run2018D_part5_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part5_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018D_part5/210305_220325/0001/','.*root')
crab_data_Run2018D_part5_0002 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part5_0002','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018D_part5/210305_220325/0002/','.*root')
crab_data_Run2018D_part5_0003 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part5_0003','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018D_part5/210305_220325/0003/','.*root')
crab_data_Run2018D_part5_0004 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part5_0004','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018D_part5/210305_220325/0004/','.*root')
crab_data_Run2018D_part5_0005 = kreator.makeDataComponentFromEOS('crab_data_Run2018D_part5_0005','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH5/crab_data_Run2018D_part5/210305_220325/0005/','.*root')

#part6
crab_data_Run2018A_part6_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part6_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH6/crab_data_Run2018A_part6/210305_221453/0000/','.*root')
crab_data_Run2018A_part6_0001 = kreator.makeDataComponentFromEOS('crab_data_Run2018A_part6_0001','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH6/crab_data_Run2018A_part6/210305_221453/0001/','.*root')
crab_data_Run2018B_part6_0000 = kreator.makeDataComponentFromEOS('crab_data_Run2018B_part6_0000','/store/group/phys_bphys/bpark/nanoaod_RK2021/BParkingNANO_2021Mar05/ParkingBPH6/crab_data_Run2018B_part6/210305_221938/0000/','.*root')

#BKG partA
bkg_Run2018A_part1_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part1_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH1/crab_data_Run2018A_part1/210502_025149/0000/','.*root')
bkg_Run2018A_part1_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part1_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH1/crab_data_Run2018A_part1/210502_025149/0001/','.*root')
bkg_Run2018A_part2_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part2_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH2/crab_data_Run2018A_part2/210502_025240/0000/','.*root')
bkg_Run2018A_part2_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part2_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH2/crab_data_Run2018A_part2/210502_025240/0001/','.*root')
bkg_Run2018A_part3_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part3_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH3/crab_data_Run2018A_part3/210502_025331/0000/','.*root')
bkg_Run2018A_part3_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part3_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH3/crab_data_Run2018A_part3/210502_025331/0001/','.*root')
bkg_Run2018A_part4_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part4_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH4/crab_data_Run2018A_part4/210502_025421/0000/','.*root')
bkg_Run2018A_part4_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part4_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH4/crab_data_Run2018A_part4/210502_025421/0001/','.*root')
bkg_Run2018A_part5_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part5_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH5/crab_data_Run2018A_part5/210502_025512/0000/','.*root')
bkg_Run2018A_part5_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part5_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH5/crab_data_Run2018A_part5/210502_025512/0001/','.*root')
bkg_Run2018A_part6_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part6_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH6/crab_data_Run2018A_part6/210502_025601/0000/','.*root')
bkg_Run2018A_part6_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018A_part6_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH6/crab_data_Run2018A_part6/210502_025601/0001/','.*root')

#BKG partB
bkg_Run2018B_part1_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part1_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH1/crab_data_Run2018B_part1/210502_024636/0000/','.*root')
bkg_Run2018B_part1_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part1_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH1/crab_data_Run2018B_part1/210502_024636/0001/','.*root')
bkg_Run2018B_part2_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part2_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH2/crab_data_Run2018B_part2/210502_024729/0000/','.*root')
bkg_Run2018B_part2_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part2_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH2/crab_data_Run2018B_part2/210502_024729/0001/','.*root')
bkg_Run2018B_part3_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part3_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH3/crab_data_Run2018B_part3/210502_024821/0000/','.*root')
bkg_Run2018B_part3_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part3_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH3/crab_data_Run2018B_part3/210502_024821/0001/','.*root')
bkg_Run2018B_part4_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part4_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH4/crab_data_Run2018B_part4/210502_024912/0000/','.*root')
bkg_Run2018B_part4_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part4_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH4/crab_data_Run2018B_part4/210502_024912/0001/','.*root')
bkg_Run2018B_part5_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part5_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH5/crab_data_Run2018B_part5/210502_025004/0000/','.*root')
bkg_Run2018B_part5_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part5_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH5/crab_data_Run2018B_part5/210502_025004/0001/','.*root')
bkg_Run2018B_part6_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018B_part6_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH6/crab_data_Run2018B_part6/210502_025055/0000/','.*root')

#BKG part C
bkg_Run2018C_part1_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part1_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH1/crab_data_Run2018C_part1/210502_025732/0000/','.*root')
bkg_Run2018C_part1_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part1_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH1/crab_data_Run2018C_part1/210502_025732/0001/','.*root')
bkg_Run2018C_part2_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part2_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH2/crab_data_Run2018C_part2/210502_025823/0000/','.*root')
bkg_Run2018C_part2_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part2_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH2/crab_data_Run2018C_part2/210502_025823/0001/','.*root')
bkg_Run2018C_part3_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part3_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH3/crab_data_Run2018C_part3/210502_025914/0000/','.*root')
bkg_Run2018C_part3_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part3_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH3/crab_data_Run2018C_part3/210502_025914/0001/','.*root')
bkg_Run2018C_part4_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part4_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH4/crab_data_Run2018C_part4/210502_030004/0000/','.*root')
bkg_Run2018C_part4_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part4_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH4/crab_data_Run2018C_part4/210502_030004/0001/','.*root')
bkg_Run2018C_part5_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part5_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH5/crab_data_Run2018C_part5/210502_030056/0000/','.*root')
bkg_Run2018C_part5_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018C_part5_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May02/ParkingBPH5/crab_data_Run2018C_part5/210502_030056/0001/','.*root')

#BKG part D 1
bkg_Run2018D_part1_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part1_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH1/crab_data_Run2018D_part1/210506_210709/0000/','.*root')
bkg_Run2018D_part1_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part1_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH1/crab_data_Run2018D_part1/210506_210709/0001/','.*root')
bkg_Run2018D_part1_0002 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part1_0002','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH1/crab_data_Run2018D_part1/210506_210709/0002/','.*root')
bkg_Run2018D_part1_0003 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part1_0003','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH1/crab_data_Run2018D_part1/210506_210709/0003/','.*root')
bkg_Run2018D_part1_0004 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part1_0004','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH1/crab_data_Run2018D_part1/210506_210709/0004/','.*root')
bkg_Run2018D_part1_0005 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part1_0005','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH1/crab_data_Run2018D_part1/210506_210709/0005/','.*root')

#BKG part D 2
bkg_Run2018D_part2_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part2_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH2/crab_data_Run2018D_part2/210506_210824/0000/','.*root')
bkg_Run2018D_part2_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part2_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH2/crab_data_Run2018D_part2/210506_210824/0001/','.*root')
bkg_Run2018D_part2_0002 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part2_0002','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH2/crab_data_Run2018D_part2/210506_210824/0002/','.*root')
bkg_Run2018D_part2_0003 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part2_0003','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH2/crab_data_Run2018D_part2/210506_210824/0003/','.*root')
bkg_Run2018D_part2_0004 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part2_0004','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH2/crab_data_Run2018D_part2/210506_210824/0004/','.*root')
bkg_Run2018D_part2_0005 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part2_0005','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH2/crab_data_Run2018D_part2/210506_210824/0005/','.*root')

#BKG part D 3
bkg_Run2018D_part3_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part3_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH3/crab_data_Run2018D_part3/210506_211310/0000/','.*root')
bkg_Run2018D_part3_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part3_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH3/crab_data_Run2018D_part3/210506_211310/0001/','.*root')
bkg_Run2018D_part3_0002 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part3_0002','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH3/crab_data_Run2018D_part3/210506_211310/0002/','.*root')
bkg_Run2018D_part3_0003 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part3_0003','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH3/crab_data_Run2018D_part3/210506_211310/0003/','.*root')
bkg_Run2018D_part3_0004 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part3_0004','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH3/crab_data_Run2018D_part3/210506_211310/0004/','.*root')
bkg_Run2018D_part3_0005 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part3_0005','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May06/ParkingBPH3/crab_data_Run2018D_part3/210506_211310/0005/','.*root')

#BKG part D 4
bkg_Run2018D_part4_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part4_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH4/crab_data_Run2018D_part4/210502_224842/0000/','.*root')
bkg_Run2018D_part4_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part4_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH4/crab_data_Run2018D_part4/210502_224842/0001/','.*root')
bkg_Run2018D_part4_0002 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part4_0002','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH4/crab_data_Run2018D_part4/210502_224842/0002/','.*root')
bkg_Run2018D_part4_0003 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part4_0003','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH4/crab_data_Run2018D_part4/210502_224842/0003/','.*root')
bkg_Run2018D_part4_0004 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part4_0004','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH4/crab_data_Run2018D_part4/210502_224842/0004/','.*root')
bkg_Run2018D_part4_0005 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part4_0005','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH4/crab_data_Run2018D_part4/210502_224842/0005/','.*root')

#BKG part D 5
bkg_Run2018D_part5_0000 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part5_0000','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH5/crab_data_Run2018D_part5/210502_224927/0000/','.*root')
bkg_Run2018D_part5_0001 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part5_0001','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH5/crab_data_Run2018D_part5/210502_224927/0001/','.*root')
bkg_Run2018D_part5_0002 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part5_0002','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH5/crab_data_Run2018D_part5/210502_224927/0002/','.*root')
bkg_Run2018D_part5_0003 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part5_0003','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH5/crab_data_Run2018D_part5/210502_224927/0003/','.*root')
bkg_Run2018D_part5_0004 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part5_0004','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH5/crab_data_Run2018D_part5/210502_224927/0004/','.*root')
bkg_Run2018D_part5_0005 = kreator.makeDataComponentFromEOS('kee_bkg_Run2018D_part5_0005','/store/cmst3/group/bpark/gkaratha/BParkingNANO_2021May03/ParkingBPH5/crab_data_Run2018D_part5/210502_224927/0005/','.*root')


#bkg kmumu
#part1
kmumu_bkg_Run2018A_part1_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part1_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018A_part1/210626_084419/0000/','.*root')
kmumu_bkg_Run2018A_part1_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part1_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018A_part1/210626_084419/0001/','.*root')
kmumu_bkg_Run2018B_part1_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part1_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018B_part1/210626_084048/0000/','.*root')
kmumu_bkg_Run2018B_part1_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part1_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018B_part1/210626_084048/0001/','.*root')
kmumu_bkg_Run2018C_part1_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part1_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018C_part1/210626_083747/0000/','.*root')
kmumu_bkg_Run2018C_part1_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part1_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018C_part1/210626_083747/0001/','.*root')
kmumu_bkg_Run2018D_part1_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part1_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018D_part1/210626_083103/0000/','.*root')
kmumu_bkg_Run2018D_part1_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part1_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018D_part1/210626_083103/0001/','.*root')
kmumu_bkg_Run2018D_part1_0002 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part1_0002','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018D_part1/210626_083103/0002/','.*root')
kmumu_bkg_Run2018D_part1_0003 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part1_0003','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018D_part1/210626_083103/0003/','.*root')
kmumu_bkg_Run2018D_part1_0004 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part1_0004','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018D_part1/210626_083103/0004/','.*root')
kmumu_bkg_Run2018D_part1_0005 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part1_0005','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH1/crab_data_Run2018D_part1/210626_083103/0005/','.*root')

#part2
kmumu_bkg_Run2018A_part2_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part2_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018A_part2/210626_084455/0000/','.*root')
kmumu_bkg_Run2018A_part2_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part2_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018A_part2/210626_084455/0001/','.*root')
kmumu_bkg_Run2018B_part2_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part2_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018B_part2/210626_084123/0000/','.*root')
kmumu_bkg_Run2018B_part2_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part2_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018B_part2/210626_084123/0001/','.*root')
kmumu_bkg_Run2018C_part2_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part2_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018C_part2/210626_083823/0000/','.*root')
kmumu_bkg_Run2018C_part2_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part2_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018C_part2/210626_083823/0001/','.*root')
kmumu_bkg_Run2018D_part2_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part2_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018D_part2/210626_083139/0000/','.*root')
kmumu_bkg_Run2018D_part2_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part2_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018D_part2/210626_083139/0001/','.*root')
kmumu_bkg_Run2018D_part2_0002 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part2_0002','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018D_part2/210626_083139/0002/','.*root')
kmumu_bkg_Run2018D_part2_0003 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part2_0003','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018D_part2/210626_083139/0003/','.*root')
kmumu_bkg_Run2018D_part2_0004 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part2_0004','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018D_part2/210626_083139/0004/','.*root')
kmumu_bkg_Run2018D_part2_0005 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part2_0005','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH2/crab_data_Run2018D_part2/210626_083139/0005/','.*root')


#part3
kmumu_bkg_Run2018A_part3_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part3_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018A_part3/210626_084531/0000/','.*root')
kmumu_bkg_Run2018A_part3_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part3_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018A_part3/210626_084531/0001/','.*root')
kmumu_bkg_Run2018B_part3_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part3_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018B_part3/210626_084158/0000/','.*root')
kmumu_bkg_Run2018B_part3_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part3_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018B_part3/210626_084158/0001/','.*root')
kmumu_bkg_Run2018C_part3_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part3_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018C_part3/210626_083858/0000/','.*root')
kmumu_bkg_Run2018C_part3_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part3_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018C_part3/210626_083858/0001/','.*root')
kmumu_bkg_Run2018D_part3_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part3_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018D_part3/210626_083214/0000/','.*root')
kmumu_bkg_Run2018D_part3_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part3_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018D_part3/210626_083214/0001/','.*root')
kmumu_bkg_Run2018D_part3_0002 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part3_0002','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018D_part3/210626_083214/0002/','.*root')
kmumu_bkg_Run2018D_part3_0003 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part3_0003','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018D_part3/210626_083214/0003/','.*root')
kmumu_bkg_Run2018D_part3_0004 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part3_0004','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018D_part3/210626_083214/0004/','.*root')
kmumu_bkg_Run2018D_part3_0005 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part3_0005','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH3/crab_data_Run2018D_part3/210626_083214/0005/','.*root')


#part4
kmumu_bkg_Run2018A_part4_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part4_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018A_part4/210626_084607/0000/','.*root')
kmumu_bkg_Run2018A_part4_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part4_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018A_part4/210626_084607/0001/','.*root')
kmumu_bkg_Run2018B_part4_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part4_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018B_part4/210626_084234/0000/','.*root')
kmumu_bkg_Run2018B_part4_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part4_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018B_part4/210626_084234/0001/','.*root')
kmumu_bkg_Run2018C_part4_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part4_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018C_part4/210626_083935/0000/','.*root')
kmumu_bkg_Run2018C_part4_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part4_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018C_part4/210626_083935/0001/','.*root')
kmumu_bkg_Run2018D_part4_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part4_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018D_part4/210626_083250/0000/','.*root')
kmumu_bkg_Run2018D_part4_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part4_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018D_part4/210626_083250/0001/','.*root')
kmumu_bkg_Run2018D_part4_0002 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part4_0002','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018D_part4/210626_083250/0002/','.*root')
kmumu_bkg_Run2018D_part4_0003 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part4_0003','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018D_part4/210626_083250/0003/','.*root')
kmumu_bkg_Run2018D_part4_0004 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part4_0004','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018D_part4/210626_083250/0004/','.*root')
kmumu_bkg_Run2018D_part4_0005 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part4_0005','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH4/crab_data_Run2018D_part4/210626_083250/0005/','.*root')



#part5
kmumu_bkg_Run2018A_part5_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part5_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018A_part5/210626_084643/0000/','.*root')
kmumu_bkg_Run2018A_part5_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018A_part5_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018A_part5/210626_084643/0001/','.*root')
kmumu_bkg_Run2018B_part5_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part5_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018B_part5/210626_084309/0000/','.*root')
kmumu_bkg_Run2018B_part5_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018B_part5_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018B_part5/210626_084309/0001/','.*root')
kmumu_bkg_Run2018C_part5_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part5_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018C_part5/210626_084010/0000/','.*root')
kmumu_bkg_Run2018C_part5_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018C_part5_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018C_part5/210626_084010/0001/','.*root')
kmumu_bkg_Run2018D_part5_0000 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part5_0000','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018D_part5/210626_083325/0000/','.*root')
kmumu_bkg_Run2018D_part5_0001 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part5_0001','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018D_part5/210626_083325/0001/','.*root')
kmumu_bkg_Run2018D_part5_0002 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part5_0002','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018D_part5/210626_083325/0002/','.*root')
kmumu_bkg_Run2018D_part5_0003 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part5_0003','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018D_part5/210626_083325/0003/','.*root')
kmumu_bkg_Run2018D_part5_0004 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part5_0004','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018D_part5/210626_083325/0004/','.*root')
kmumu_bkg_Run2018D_part5_0005 = kreator.makeDataComponentFromEOS('kmumu_bkg_Run2018D_part5_0005','/store/cmst3/group/bpark/gmelachr/same_sign_muons/BParkingNANO_2021Jun26/ParkingBPH5/crab_data_Run2018D_part5/210626_083325/0005/','.*root')




#2017 Charmonium
#crab_data_Run2017B_Charmonium_0000 = kreator.makeDataComponentFromEOS('Run2017B_Charmonium_0000','/store/cmst3/group/bpark/gkaratha/Charmonium_2017_2/BParkingNANO_2020Apr21/Charmonium/crab_data_Run2017B/200421_120220/0000/','.*root')
#crab_data_Run2017C_Charmonium_0000 = kreator.makeDataComponentFromEOS('Run2017C_Charmonium_0000','/store/cmst3/group/bpark/gkaratha/Charmonium_2017_2/BParkingNANO_2020Apr21/Charmonium/crab_data_Run2017C/200421_120340/0000/','.*root')
#crab_data_Run2017D_Charmonium_0000 = kreator.makeDataComponentFromEOS('Run2017D_Charmonium_0000','/store/cmst3/group/bpark/gkaratha/Charmonium_2017_2/BParkingNANO_2020Apr21/Charmonium/crab_data_Run2017D/200421_120612/0000/','.*root')
#crab_data_Run2017E_Charmonium_0000 = kreator.makeDataComponentFromEOS('Run2017E_Charmonium_0000','/store/cmst3/group/bpark/gkaratha/Charmonium_2017_2/BParkingNANO_2020Apr21/Charmonium/crab_data_Run2017E/200421_120710/0000/','.*root')
#crab_data_Run2017F_Charmonium_0000 = kreator.makeDataComponentFromEOS('Run2017F_Charmonium_0000','/store/cmst3/group/bpark/gkaratha/Charmonium_2017_2/BParkingNANO_2020Apr21/Charmonium/crab_data_Run2017F/200421_120805/0000/','.*root')

#2017 DoubleMuon LowMass
#crab_data_Run2017B_DoubleMuon_0000 = kreator.makeDataComponentFromEOS('Run2017B_DoubleMuon_0000','/store/cmst3/group/bpark/gkaratha/DoubleMuonLowMass_2017_2/BParkingNANO_2020Apr21/DoubleMuonLowMass/crab_doubleMuon_Run2017B/200421_134716/0000/','.*root')
#crab_data_Run2017C_DoubleMuon_0000 = kreator.makeDataComponentFromEOS('Run2017C_DoubleMuon_0000','/store/cmst3/group/bpark/gkaratha/DoubleMuonLowMass_2017_2/BParkingNANO_2020Apr21/DoubleMuonLowMass/crab_doubleMuon_Run2017C/200421_134828/0000/','.*root')
#crab_data_Run2017D_DoubleMuon_0000 = kreator.makeDataComponentFromEOS('Run2017D_DoubleMuon_0000','/store/cmst3/group/bpark/gkaratha/DoubleMuonLowMass_2017_2/BParkingNANO_2020Apr21/DoubleMuonLowMass/crab_doubleMuon_Run2017D/200421_134941/0000/','.*root')
#crab_data_Run2017E_DoubleMuon_0000 = kreator.makeDataComponentFromEOS('Run2017E_DoubleMuon_0000','/store/cmst3/group/bpark/gkaratha/DoubleMuonLowMass_2017_2/BParkingNANO_2020Apr21/DoubleMuonLowMass/crab_doubleMuon_Run2017E/200421_135201/0000/','.*root')
#crab_data_Run2017F_DoubleMuon_0000 = kreator.makeDataComponentFromEOS('Run2017F_DoubleMuon_0000','/store/cmst3/group/bpark/gkaratha/DoubleMuonLowMass_2017_2/BParkingNANO_2020Apr21/DoubleMuonLowMass/crab_doubleMuon_Run2017F/200421_135317/0000/','.*root')

#2016 Charmonium
#crab_data_Run2016B_Charmonium = kreator.makeDataComponentFromEOS('Run2016B_Charmonium','/store/cmst3/group/bpark/gkaratha/Charmonium_2016/BParkingNANO_2020Apr29/Charmonium/crab_charmonium_Run2016B/200429_102824/0000/','.*root')
#crab_data_Run2016C_Charmonium = kreator.makeDataComponentFromEOS('Run2016C_Charmonium','/store/cmst3/group/bpark/gkaratha/Charmonium_2016/BParkingNANO_2020Apr29/Charmonium/crab_charmonium_Run2016C/200429_102928/0000/','.*root')
#crab_data_Run2016D_Charmonium = kreator.makeDataComponentFromEOS('Run2016D_Charmonium','/store/cmst3/group/bpark/gkaratha/Charmonium_2016/BParkingNANO_2020Apr29/Charmonium/crab_charmonium_Run2016D/200429_103117/0000/','.*root')
#crab_data_Run2016E_Charmonium = kreator.makeDataComponentFromEOS('Run2016E_Charmonium','/store/cmst3/group/bpark/gkaratha/Charmonium_2016/BParkingNANO_2020Apr29/Charmonium/crab_charmonium_Run2016E/200429_103309/0000/','.*root')
#crab_data_Run2016F_Charmonium = kreator.makeDataComponentFromEOS('Run2016F_Charmonium','/store/cmst3/group/bpark/gkaratha/Charmonium_2016/BParkingNANO_2020Apr29/Charmonium/crab_charmonium_Run2016F/200429_103518/0000/','.*root')
#crab_data_Run2016G_Charmonium = kreator.makeDataComponentFromEOS('Run2016G_Charmonium','/store/cmst3/group/bpark/gkaratha/Charmonium_2016/BParkingNANO_2020Apr29/Charmonium/crab_charmonium_Run2016G/200429_103623/0000/','.*root')
#crab_data_Run2016H_Charmonium = kreator.makeDataComponentFromEOS('Run2016H_Charmonium','/store/cmst3/group/bpark/gkaratha/Charmonium_2016/BParkingNANO_2020Apr29/Charmonium/crab_charmonium_Run2016H/200429_103724/0000/','.*root')


#2017 DoubleMuon LowMass
#crab_data_Run2016B_DoubleMuon = kreator.makeDataComponentFromEOS('Run2016B_DoubleMuon','/store/cmst3/group/bpark/gkaratha/DoubleMuon_2016/BParkingNANO_2020Apr29/DoubleMuonLowMass/crab_doublemuon_Run2016B/200429_103916/0000/','.*root')
#crab_data_Run2016C_DoubleMuon = kreator.makeDataComponentFromEOS('Run2016C_DoubleMuon','/store/cmst3/group/bpark/gkaratha/DoubleMuon_2016/BParkingNANO_2020Apr29/DoubleMuonLowMass/crab_doublemuon_Run2016C/200429_104206/0000/','.*root')
#crab_data_Run2016D_DoubleMuon = kreator.makeDataComponentFromEOS('Run2016D_DoubleMuon','/store/cmst3/group/bpark/gkaratha/DoubleMuon_2016/BParkingNANO_2020Apr29/DoubleMuonLowMass/crab_doublemuon_Run2016D/200429_104307/0000/','.*root')
#crab_data_Run2016E_DoubleMuon = kreator.makeDataComponentFromEOS('Run2016E_DoubleMuon','/store/cmst3/group/bpark/gkaratha/DoubleMuon_2016/BParkingNANO_2020Apr29/DoubleMuonLowMass/crab_doublemuon_Run2016E/200429_104409/0000/','.*root')
#crab_data_Run2016F_DoubleMuon = kreator.makeDataComponentFromEOS('Run2016F_DoubleMuon','/store/cmst3/group/bpark/gkaratha/DoubleMuon_2016/BParkingNANO_2020Apr29/DoubleMuonLowMass/crab_doublemuon_Run2016F/200429_104543/0000/','.*root')
#crab_data_Run2016G_DoubleMuon = kreator.makeDataComponentFromEOS('Run2016G_DoubleMuon','/store/cmst3/group/bpark/gkaratha/DoubleMuon_2016/BParkingNANO_2020Apr29/DoubleMuonLowMass/crab_doublemuon_Run2016G/200429_104659/0000/','.*root')
#crab_data_Run2016H_DoubleMuon = kreator.makeDataComponentFromEOS('Run2016H_DoubleMuon','/store/cmst3/group/bpark/gkaratha/DoubleMuon_2016/BParkingNANO_2020Apr29/DoubleMuonLowMass/crab_doublemuon_Run2016H/200429_104801/0000/','.*root')



samples = [Charmonium_test,
crab_data_Run2018A_part1_0000,crab_data_Run2018A_part1_0001,crab_data_Run2018B_part1_0000,crab_data_Run2018B_part1_0001,crab_data_Run2018C_part1_0000,crab_data_Run2018C_part1_0001,crab_data_Run2018D_part1_0000,crab_data_Run2018D_part1_0001,crab_data_Run2018D_part1_0002,crab_data_Run2018D_part1_0003,crab_data_Run2018D_part1_0004,crab_data_Run2018D_part1_0005,crab_data_Run2018B_part1_0002,crab_data_Run2018D_part1_0006,
crab_data_Run2018A_part2_0000,crab_data_Run2018A_part2_0001,crab_data_Run2018B_part2_0000,crab_data_Run2018B_part2_0001,crab_data_Run2018C_part2_0000,crab_data_Run2018C_part2_0001,crab_data_Run2018D_part2_0000,crab_data_Run2018D_part2_0001,crab_data_Run2018D_part2_0002,crab_data_Run2018D_part2_0003,crab_data_Run2018D_part2_0004,crab_data_Run2018D_part2_0005,
crab_data_Run2018A_part3_0000,crab_data_Run2018A_part3_0001,crab_data_Run2018B_part3_0000,crab_data_Run2018B_part3_0001,crab_data_Run2018C_part3_0000,crab_data_Run2018C_part3_0001,crab_data_Run2018D_part3_0000,crab_data_Run2018D_part3_0001,crab_data_Run2018D_part3_0002,crab_data_Run2018D_part3_0003,crab_data_Run2018D_part3_0004,crab_data_Run2018D_part3_0005,
crab_data_Run2018A_part4_0000,crab_data_Run2018A_part4_0001,crab_data_Run2018B_part4_0000,crab_data_Run2018C_part4_0000,crab_data_Run2018B_part4_0001,crab_data_Run2018C_part4_0001,crab_data_Run2018D_part4_0000,crab_data_Run2018D_part4_0001,crab_data_Run2018D_part4_0002,crab_data_Run2018D_part4_0003,crab_data_Run2018D_part4_0004,crab_data_Run2018D_part4_0005,
crab_data_Run2018A_part5_0000,crab_data_Run2018A_part5_0001,crab_data_Run2018B_part5_0000,crab_data_Run2018B_part5_0001,crab_data_Run2018C_part5_0000,crab_data_Run2018C_part5_0001,crab_data_Run2018D_part5_0000,crab_data_Run2018D_part5_0001,crab_data_Run2018D_part5_0002,crab_data_Run2018D_part5_0003,crab_data_Run2018D_part5_0004,crab_data_Run2018D_part5_0005,
crab_data_Run2018A_part6_0000,crab_data_Run2018A_part6_0001,crab_data_Run2018B_part6_0000,
#crab_data_Run2017B_Charmonium_0000,crab_data_Run2017C_Charmonium_0000,
#crab_data_Run2017D_Charmonium_0000,crab_data_Run2017E_Charmonium_0000,
#crab_data_Run2017F_Charmonium_0000,
#crab_data_Run2017B_DoubleMuon_0000,crab_data_Run2017C_DoubleMuon_0000,
#crab_data_Run2017D_DoubleMuon_0000,crab_data_Run2017E_DoubleMuon_0000,
#crab_data_Run2017F_DoubleMuon_0000,
#crab_data_Run2016B_Charmonium,crab_data_Run2016C_Charmonium,
#crab_data_Run2016D_Charmonium,crab_data_Run2016E_Charmonium,
#crab_data_Run2016F_Charmonium,crab_data_Run2016G_Charmonium,
#crab_data_Run2016H_Charmonium,
#crab_data_Run2016B_DoubleMuon,crab_data_Run2016C_DoubleMuon,
#crab_data_Run2016D_DoubleMuon,crab_data_Run2016E_DoubleMuon,
#crab_data_Run2016F_DoubleMuon,crab_data_Run2016G_DoubleMuon,
#crab_data_Run2016H_DoubleMuon,
bkg_Run2018A_part1_0000, bkg_Run2018A_part1_0001, bkg_Run2018A_part2_0000,
bkg_Run2018A_part2_0001, bkg_Run2018A_part3_0000, bkg_Run2018A_part3_0001, 
bkg_Run2018A_part4_0000, bkg_Run2018A_part4_0001, bkg_Run2018A_part5_0000,
bkg_Run2018A_part5_0001, bkg_Run2018A_part6_0000, bkg_Run2018A_part6_0001,
bkg_Run2018B_part1_0000, bkg_Run2018B_part1_0001, bkg_Run2018B_part2_0000,
bkg_Run2018B_part2_0001, bkg_Run2018B_part3_0000, bkg_Run2018B_part3_0001, 
bkg_Run2018B_part4_0000, bkg_Run2018B_part4_0001, bkg_Run2018B_part5_0000, 
bkg_Run2018B_part5_0001, bkg_Run2018B_part6_0000, bkg_Run2018C_part1_0000, 
bkg_Run2018C_part1_0001, bkg_Run2018C_part2_0000, bkg_Run2018C_part2_0001, 
bkg_Run2018C_part3_0000, bkg_Run2018C_part3_0001, bkg_Run2018C_part4_0000, 
bkg_Run2018C_part4_0001, bkg_Run2018C_part5_0000, bkg_Run2018C_part5_0001,
bkg_Run2018D_part1_0000, bkg_Run2018D_part1_0001, bkg_Run2018D_part1_0002,
bkg_Run2018D_part1_0003, bkg_Run2018D_part1_0004, bkg_Run2018D_part1_0005,
bkg_Run2018D_part2_0000, bkg_Run2018D_part2_0001, #bkg_Run2018D_part2_0002,
#bkg_Run2018D_part2_0003, bkg_Run2018D_part2_0004, bkg_Run2018D_part2_0005,
bkg_Run2018D_part3_0000, bkg_Run2018D_part3_0001, bkg_Run2018D_part3_0002,
bkg_Run2018D_part3_0003, bkg_Run2018D_part3_0004, bkg_Run2018D_part3_0005,
bkg_Run2018D_part4_0000, bkg_Run2018D_part4_0001, bkg_Run2018D_part4_0002,
bkg_Run2018D_part4_0003, bkg_Run2018D_part4_0004, bkg_Run2018D_part4_0005,
bkg_Run2018D_part5_0000, bkg_Run2018D_part5_0001, bkg_Run2018D_part5_0002,
bkg_Run2018D_part5_0003, bkg_Run2018D_part5_0004, bkg_Run2018D_part5_0005,
kmumu_bkg_Run2018A_part1_0000, kmumu_bkg_Run2018A_part1_0001, kmumu_bkg_Run2018A_part2_0000,
kmumu_bkg_Run2018A_part2_0001, kmumu_bkg_Run2018A_part3_0000, kmumu_bkg_Run2018A_part3_0001,
kmumu_bkg_Run2018A_part4_0000, kmumu_bkg_Run2018A_part4_0001, kmumu_bkg_Run2018A_part5_0000,
kmumu_bkg_Run2018A_part5_0001, 
kmumu_bkg_Run2018B_part1_0000, kmumu_bkg_Run2018B_part1_0001, kmumu_bkg_Run2018B_part2_0000,
kmumu_bkg_Run2018B_part2_0001, kmumu_bkg_Run2018B_part3_0000, kmumu_bkg_Run2018B_part3_0001,
kmumu_bkg_Run2018B_part4_0000, kmumu_bkg_Run2018B_part4_0001, kmumu_bkg_Run2018B_part5_0000,
kmumu_bkg_Run2018B_part5_0001, kmumu_bkg_Run2018C_part1_0000,
kmumu_bkg_Run2018C_part1_0001, kmumu_bkg_Run2018C_part2_0000, kmumu_bkg_Run2018C_part2_0001,
kmumu_bkg_Run2018C_part3_0000, kmumu_bkg_Run2018C_part3_0001, kmumu_bkg_Run2018C_part4_0000,
kmumu_bkg_Run2018C_part4_0001, kmumu_bkg_Run2018C_part5_0000, kmumu_bkg_Run2018C_part5_0001,
kmumu_bkg_Run2018D_part1_0000, kmumu_bkg_Run2018D_part1_0001, kmumu_bkg_Run2018D_part1_0002,
kmumu_bkg_Run2018D_part1_0003, kmumu_bkg_Run2018D_part1_0004, kmumu_bkg_Run2018D_part1_0005,
kmumu_bkg_Run2018D_part2_0000, kmumu_bkg_Run2018D_part2_0001, kmumu_bkg_Run2018D_part2_0002,
kmumu_bkg_Run2018D_part2_0003, kmumu_bkg_Run2018D_part2_0004, kmumu_bkg_Run2018D_part2_0005,
kmumu_bkg_Run2018D_part3_0000, kmumu_bkg_Run2018D_part3_0001, kmumu_bkg_Run2018D_part3_0002,
kmumu_bkg_Run2018D_part3_0003, kmumu_bkg_Run2018D_part3_0004, kmumu_bkg_Run2018D_part3_0005,
kmumu_bkg_Run2018D_part4_0000, kmumu_bkg_Run2018D_part4_0001, kmumu_bkg_Run2018D_part4_0002,
kmumu_bkg_Run2018D_part4_0003, kmumu_bkg_Run2018D_part4_0004, kmumu_bkg_Run2018D_part4_0005,
kmumu_bkg_Run2018D_part5_0000, kmumu_bkg_Run2018D_part5_0001, kmumu_bkg_Run2018D_part5_0002,
kmumu_bkg_Run2018D_part5_0003, kmumu_bkg_Run2018D_part5_0004, kmumu_bkg_Run2018D_part5_0005
] 



if __name__ == "__main__":
	from CMGTools.RootTools.samples.tools import runMain
	runMain(samples, localobjs=locals())
