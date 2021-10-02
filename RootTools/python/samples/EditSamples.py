import os, subprocess, sys
import re
from os import listdir
from os.path import isfile, join
import argparse

def loop_subdir(mypath,output):
    print "loop",mypath
    if "000" not in mypath:
       for subdir in listdir(mypath):
           print "subdir call",mypath+"/"+subdir
           loop_subdir(mypath+"/"+subdir,output)
    else:
       print "save"       
       path=mypath.split("/")[3:]
       with open(output,'a') as txt:
         text="{name} = kreator.makeDataComponentFromEOS('{name}','/{path}/','.*root')\n".format(name=path[-3]+"_"+path[-1],path="/".join(path))
         txt.write(text+"\n")
       txt.close()
       

if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument("-p", dest="mypaths", default=[],nargs='+', type=str, help="Main folder in eos that contains other folders ")
  parser.add_argument("-f","--eraFilter", dest="eraFilter", default=[],nargs='+', type=str, help="If only some folders needed, put them here ")
  parser.add_argument("-o","--outputName", dest="outputName", default='test', type=str, help="output name (.py automatically added)")


  options = parser.parse_args()
  if "py" not in options.outputName:
    options.outputName+=".py"

  with open(options.outputName,'w') as txt:
     txt.write("# COMPONENT CREATOR\nfrom CMGTools.RootTools.samples.ComponentCreator import ComponentCreator\nkreator = ComponentCreator()\n\n\n\n")
  txt.close()

  for mypath in options.mypaths:
    for dir1 in listdir(mypath):
      print "subdir call ",mypath+"/"+dir1
      loop_subdir(mypath+"/"+dir1,options.outputName)
    print "ok"
  
  samples=[]
  with open(options.outputName,'r') as txt:
    lines = txt.readlines()
    for line in lines:
      if "=" in line.split() and not "kreator" in line.split():
        samples.append( line.split()[0] )
  txt.close()
  with open(options.outputName,'a') as txt:
    text="\n\nsamples = ["+(",".join(samples))+"] \n\n\n\n"
    text+='if __name__ == "__main__":\n\tfrom CMGTools.RootTools.samples.tools import runMain\n\trunMain(samples, localobjs=locals())'  
    txt.write(text)
  txt.close()
  print "ready"
