#!/bin/bash

#DIRS="/eos/cms/store/cmst3/user/gkaratha/cmgTuple_PFeKEE_12B_samesign_v7.0/"
DIRS="/eos/cms/store/cmst3/group/bpark/gkaratha/cmgTuple_LowPtPFeKEE_12B_v7.0"

mkdir $DIRS/addedChunks
for DIR in "$DIRS"/* 
do
# if [[ $DIR != *"Run2018D"* ]]; then
#  continue
# fi
 haddChunks.py -n $DIR
 echo $DIR
 wait
 mv ${DIR}/crab_data_Run2018?_part?_000?.root $DIRS/addedChunks
# mv ${DIR}/kee_bkg_Run2018?_part?_000?.root $DIRS/addedChunks
 #wait
 #rm -rI ${DIR}

done
