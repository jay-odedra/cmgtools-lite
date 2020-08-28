#!/bin/bash

FOLDER=$1
shift;

details='false'

while getopts 'd' flag; do
  case "${flag}" in
    d) details='true' ;;
  esac
done


SZ=$(du -hs ${FOLDER})
echo total size ${SZ}

NF=$(find ${FOLDER} -type f | wc -l)

echo total files ${NF}

if ! ${details} ; then
   exit 0;
fi

for FLD in ${FOLDER}/*; do
  FLD_SZ=$(du -hs ${FLD})
  FLD_NF=$(find ${FLD} -type f | wc -l)
  
  echo files ${FLD_NF} size ${FLD_SZ}
done  
