# Short description 

CMG is a general analysis tool developed and maintained by CMS. Is being used by many analysis. CMG provides several common tools and functionallities and each analysis developing their code using those tools. The present code is dedicated to B physics in general and in particular Rk analysis.
For the general recipe, [follow these instructions](https://twiki.cern.ch/twiki/bin/view/CMS/CMGToolsReleasesExperimental).

--------------

## Installation 

#### CMSSW version
```
SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_4_0
cd CMSSW_10_4_0/src
cmsenv
git cms-init
```
#### Add centrall CMG
```
git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git -f  -t heppy_104X_dev
git checkout -b heppy_104X_dev cmg-central/heppy_104X_dev
git cms-addpkg PhysicsTools/Heppy
git cms-addpkg PhysicsTools/HeppyCore
cd $CMSSW_BASE/src/PhysicsTools
```
#### Add B Parking code
```
git clone -b NanoToolsBPark https://github.com/gkaratha/nanoAOD-tools NanoAODTools
cd $CMSSW_BASE/src
git clone -b bpark_cmg https://github.com/gkaratha/cmgtools-lite CMGTools
cd $CMSSW_BASE/src
```
#### Compile
```
scram b -j 8
```
## Basic code
```
NanoAOD ntuples definition: CMGTools/RootTools/python/samples/samples_13TeV_BParkingData_NanoAOD.py
Module sequence and structure: CMGTools/RKAnalysis/python/tools/nanoAOD/BParking_modules.py
Configuration: CMGTools/RKAnalysis/cfg/run_RK_fromNanoAOD_cfg.py
Plotting: CMGTools/RKAnalysis/python/plotter/experimental/plotter2.py
```
## Usage
```
```
#### Skimming NanoAOD
```
Main code (ie modules to run and running order) defined in BParking_modules.py
Local run: nanopy.py <folder>  run_RK_fromNanoAOD_cfg.py -N <evts per dataset> -o xxx=yyy
Batch run: nanopy_batch.py -o <localOutput> -r /eos/space/<remoteOutput> -b 'run_condor_simple.sh -t 1200' run_RK_fromNanoAOD_cfg.py --option <xxx>=<yyy>
Options:
- mc to run on MC
- data to run on data
- njobs number of chuncks to create
- kmumu to run on B -> Kmumu
- kee to run on B -> Kee
- kstarmumu to run on B ->K*mumu
- onlyPFe runs kee channel only with 2PF
- onlyLowPtAndPFe runs kee channel only with 1PF & 1 Low pT
- jpsi when run on mc (only in mc used) requires e to come from Jpsi mother
- psi2s same for excited jpsi
- test to take one file per dataset
- single for single threaded run. this needs "--single"


```
#### Proxy error
```
In the following error, during submission in condor, is encountered:

Submitting job(s)ERROR: use_x509userproxy=/afs/cern.ch/work/r/ratramon/CMSSW_10_4_0/src/CMGTools/RKAnalysis/cfg/X509_USER_PROXY is invalid, must eval to a boolean

go to PhysicsTools/HeppyCore/scripts and comment out the line use_x509userproxy = \$ENV(X509_USER_PROXY) from both run_condor.sh and run_condor_simple.sh
then re-compile
