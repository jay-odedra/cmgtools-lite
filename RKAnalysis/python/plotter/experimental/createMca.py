# usage: python -p <path/to/sample -o ouput
# produces mca with samples inside the folder

from os import walk
from os import listdir
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--paths", dest="paths", nargs='+', type=str, help="paths of directories of files")
    parser.add_argument("-o","--outputName", dest="output", default="testmca", type=str, help="output txt name (dont put .txt exists)")

    args = parser.parse_args()
    lines=""
    for path in args.paths:
        subdirs = listdir(path)

        nroot=0
        for item in subdirs: 
            if ".root" in item: nroot+=1
                                  
        if nroot>0:
            for item in subdirs:
                if ".root" in item: lines+=path+"/"+item+"\n"
        else:
            for item in subdirs:
                for dirpath,dirnames,filenames in walk(path+"/"+item):
                   if ("/000" in dirpath) and (not ("log" in dirpath)):
                       lines+=dirpath+"/*.root\n"

    with open(args.output+".txt","w") as out:
        out.write(lines)
    
    out.close()
