#!/bin/bash

DIR=$1
shift;

set success=0
set running=0
set killed=0
set total=0
set validurl=0
brokenurl=()
RESUBMIT=false

for folder in "$DIR"/*
do
  url=$( ls -lh $folder/*.url | wc -l )
  if [ $url == 1 ]
  then
     let "validurl++"
  else
     brokenurl+=($folder)
  fi
  for file in "$folder"/*
  do
     
     if [ ${file: -4} == ".log" ]
     then
#         echo "check",$file
         let "total++"
         RESULT=$(condor_history -userlog $file )
         if [[ $RESULT == *" C "* ]]
         then 
           let "success++"
         fi
         if [[ $RESULT == *" I "* ]]
         then 
           let "running++"
         fi
         if [[ $RESULT == *" X "* ]]
         then 
           let "killed++"
         fi                  
     fi
  done
done

echo "success  "$success," running "$running," killed "$killed," total ",$total
echo "logical urls in",$validurl," chunks"
echo "bad url list"
for i in "${brokenurl[@]}"; 
do
   echo $i
done

if $RESUBMIT
then
  for i in "${brokenurl[@]}"
  do
   echo "resubmiting", $i
   cd $i
   condor_submit job_desc.cfg
   cd -
  done
fi
