#!/bin/bash

DIRS="/eos/cms/store/cmst3/user/gkaratha/cmgTuple_PFeKEE_COMB_BKG_v5.4/"

mkdir $DIRS/addedChunks
for DIR in "$DIRS"/* 
do
# if [[ $DIR != *"Run2018D"* ]]; then
#  continue
# fi
 haddChunks.py -n $DIR
 echo $DIR
 wait
 mv ${DIR}/crab_data_Run2018?_part?_????.root $DIRS/addedChunks
 #wait
 #rm -rI ${DIR}

done
