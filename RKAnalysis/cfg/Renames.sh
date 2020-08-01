#!/bin/bash

Files=/eos/cms/store/group/cmst3/user/gkaratha/cmgTuple_TagKMuMu_Charmonium17B_v4.2/Run2017B_Charmonium_0000/
Name=Run2017B_Charmonium


J=0

for i in "$Files"/*; do
  if [[ -f $i ]]
  then
    echo "$i is file"
    mv $i $Files/${Name}_$J.root
  fi
  if [[ -d $i ]]
  then
    echo "$i is folder. Files:"
    sub_j=0
    for sub_i in "$i"/*; do
      echo "   - $sub_i"
      mv $sub_i $i/${Name}_part${J}_chunk${sub_j}.root
      let sub_j=sub_j+1
    done
  fi
  
  #mv $i /eos/cms/store/cmst3/group/bpark/gkaratha/BToKMuMu_BToKJPsi_ToMuMu_UnbiasedForTrigger_11_2_2020/KJpsiMuMu/BParkNANO_mc_$J.root
  let J=J+1
done
