from os import listdir,system,walk

Dir="/eos/cms/store/group/cmst3/user/gkaratha/cmgTuple_TagKJpsiMuMu_MC_v3.0_HLTfired/BuToKJpsiMuMu/"
for (dirpath,dirnames, filenames) in walk(Dir):
  for filename in filenames:
    newname=filename.split(".")[0]+".root"
    system("mv "+dirpath+"/"+filename+" "+dirpath+"/"+newname)
  
#  print dirpath
 # print dirnames
#  print filenames

