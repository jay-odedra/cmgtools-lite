#!/bin/bash



for VAR in hminBtrk1 hminBtrk2 hminBtrk3 hl1Bmass hl2Bmass
do
   python combinePlots.py -i NewVarsData NewVarsMC -p ${VAR} -o NewVarsMCData -l Bkg Sgn -c Norm LogY Over
done
