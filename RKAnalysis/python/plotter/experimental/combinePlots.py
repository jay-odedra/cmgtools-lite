import os, subprocess 
from argparse import ArgumentParser
import multiprocessing as mp
from ROOT import *
import sys
import time;

sys.path.insert(1, '/afs/cern.ch/work/n/nzipper/public/Rk/Analysis/CMSSW_10_4_0/src/CMGTools/RKAnalysis/python/plotter')
from cms_lumi import  CMS_lumi


def createRatio(h1, h2): #also default plotting style

    h3 = h1.Clone("h3")
    h3.SetLineColor(kBlack)
    h3.SetMarkerStyle(21)
    h3.SetTitle("")
    h3.SetMinimum(0)
    h3.SetMaximum(4)
    # Set up plot for markers and errors
    h3.Divide(h2)
 
    # Adjust y-axis settings
    y = h3.GetYaxis()
    y.SetTitle("ratio")
    y.SetNdivisions(505)
    y.SetTitleSize(0.15)
    y.SetTitleFont(42)
    y.SetTitleOffset(0.4)
    y.SetLabelFont(42)
    y.SetLabelSize(0.12)
 
    # Adjust x-axis settings
    x = h3.GetXaxis()
    x.SetTitleSize(0.15)
    x.SetTitleFont(42)
    x.SetTitleOffset(0.8)
    x.SetLabelFont(42)
    x.SetLabelSize(0.12)
    return h3
 
 
def createCanvasPads():
    c = TCanvas("c", "canvas", 800, 800)
    c.SetBorderSize(0)
    # Upper histogram plot is pad1
    pad1 = TPad("pad1", "pad1", 0, 0.4, 1, 1.0)
    pad1.SetBottomMargin(0)  # joins upper and lower plot
    pad1.SetTopMargin(0.12)
    pad1.SetLeftMargin(0.12)
    pad1.SetRightMargin(0.04)
    pad1.SetGridx()
    pad1.Draw()
    # Lower ratio plot is pad2
    c.cd()  # returns to main canvas before defining pad2
    pad2 = TPad("pad2", "pad2", 0, 0, 1, 0.4)
    pad2.SetTopMargin(0)  # joins upper and lower plot
    pad2.SetLeftMargin(0.12)
    pad2.SetRightMargin(0.04)
    pad2.SetBottomMargin(0.3)
    pad2.SetGridx()
    pad2.Draw()
    return c, pad1, pad2
  
 

def transform( heff, kwds):
      
   for kwd in kwds:          
     value = kwd.split("=")
     if len(value)==1: 
        if value[0]=="Norm":
          heff.Scale(1.0/heff.Integral())
        continue
     if value[0]=="LineColor":
        heff.SetLineColor(float(value[1]))

     if value[0]=="LineWidth": 
        heff.SetLineWidth(float(value[1]))

     if value[0]=="XLabelSize":
        heff.GetXaxis().SetTitleSize(float(value[1]));     

     if value[0]=="YLabelSize":
        heff.GetYaxis().SetTitleSize(float(value[1]));
     if value[0]=="YTitle":
        heff.GetYaxis().SetTitle(value[1]);
     if value[0]=="XTitle":
        heff.GetXaxis().SetTitle(value[1]);
     if value[0]=="YSetMin":
        heff.GetXaxis().SetTitle(value[1]);
     
   return heff



def legPos( options):
  default= (0.7,0.7,0.9,0.9)
  newpos=0
  for option in options:
    if not "LegPos" in option :
       continue;
    pos = (option.split("=") )[1]
    if pos =="BL":
      newpos=(0.2,0.2,0.4,0.4)
    elif pos  =="BR":
      newpos=(0.7,0.1,0.9,0.3) 
    elif pos =="TL":
      newpos= (0.1,0.7,0.3,0.9)
    elif pos  =="TR":
      newpos= (0.7,0.7,0.9,0.9) 

  if newpos ==0:
     return default; 
  else:
     return newpos

def AddOverflow(h1):
  nx=h1.GetNbinsX()
  value=h1.GetBinContent(nx)+ h1.GetBinContent(nx+1);
  h1.SetBinContent(nx,value);
  return h1



def legName( options,default):
  name=default
  for option in options:
    if "LegName" in option:
      name = (option.split("="))[1]
  return name
    


def cms():
  cms_label = TLatex()
  cms_label.SetTextSize(0.04)
  cms_label.DrawLatexNDC(0.16, 0.96, "#bf{ #font[22]{CMS} #font[72]{Preliminary}}")
  return cms_label



def head():
  header = TLatex()
  header.SetTextSize(0.03)
  header.DrawLatexNDC(0.63, 0.96, "#sqrt{s} = 13 TeV, 2018 p-p ")
  return header




if __name__ == "__main__":

    # availiable plotting options
    parser = ArgumentParser()

    parser.add_argument("-i","--inputPaths",dest="inputPaths", nargs='+',type=str,   default=["plots.root"], help="input directories to find histos.root, same number as plots or only 1 file")

    parser.add_argument("-p","--plots", nargs='+', dest="plotNames", default=["SimplePlots"],type=str, help="plot names to be superimposed. same order as dir. If only ONE name is provided it will search for that in all files.With option 'all' it will take all histos in the file. all takes all plots in the root ")
    parser.add_argument("-c","--cfgPlots" ,dest="cfg",nargs='+',default=["None"],type=str, help="")
    parser.add_argument("--colors" ,dest="colors",nargs="+",  default=None,type=int, help="")
    parser.add_argument("-l","--legends" ,nargs='+',dest="legends",  default=["None"],type=str, help="legend per plot")
    parser.add_argument("--two-plot-ratio",dest="ratio",  default=False, action="store_true", help="")
    parser.add_argument("-o","--output",dest="outputName",  default="PlotsComp", type=str, help="folder name to save plots. Default=Plots_Date")
    
   
    args = parser.parse_args()
    print args.legends, args.plotNames
     #  create output folder to save plots
    os.system("mkdir -p "+args.outputName)
      
    
    if len(args.plotNames)==0 :
       print " histo name is not provided"
       exit()

    if len(args.legends) != len(args.plotNames) and len(args.plotNames)!=1:
       print "legends for all plots not defined"
       exit()    

    if len(args.plotNames)==1 and args.plotNames[0]=="all":
      args.plotNames=[]
      file_in=TFile(args.inputPaths[0]+"/histos.root","READ")
      file_in2=TFile(args.inputPaths[1]+"/histos.root","READ")
      plt1= [ hst.GetName() for hst in file_in.GetListOfKeys()]
      plt2= [ hst.GetName() for hst in file_in2.GetListOfKeys()] 
      print plt1,plt2
      args.plotNames= list(set(plt1).intersection(plt2))
     
    if len(args.inputPaths)==1:
      print "auto changing the number of files to match plots- every plot taken from the same file" 
      fl=args.inputPaths[0]
      for i in range(len(args.plotNames)-1):
        args.inputPaths.append(fl)
    
    gROOT.SetBatch(True)
     
    for jdx,plot in enumerate(args.plotNames):
      leg = TLegend(legPos(args.cfg))
      histos=[]
      hstack= THStack("hs","histos")
      if args.ratio and len(args.inputPaths)==2:
         c, pad1, pad2 = createCanvasPads()
         pad1.cd()
      else: c = TCanvas( "cnv2","cnv2", 700,700);
      for idx,path in enumerate(args.inputPaths):
        file_in= TFile(path+"/histos.root","READ")
        histo=file_in.Get(plot)
        histo.SetDirectory(0)
        if args.colors != None and len(args.colors) == len(args.inputPaths):
          histo.SetLineColor(args.colors[idx])
          histo.SetMarkerColor(args.colors[idx])
        else:
          histo.SetLineColor(idx+1)
          histo.SetMarkerColor(idx+1)
        histo.SetLineWidth(3)
#        hstack.GetYaxis().SetTitleSize(0.15)
#        hstack.GetYaxis().SetTitleFont(42)
#        histo.GetYaxis().SetTitleOffset(0.4)
#        histo.GetYaxis().SetTitleFont(42)
        histo.GetYaxis().SetLabelFont(42)
        histo.GetYaxis().SetLabelSize(0.2)
        if "Over" in args.cfg:
           histo=AddOverflow(histo)
        histo=transform(histo, args.cfg)
        leg.AddEntry(histo,args.legends[idx])
        gROOT.cd()
        h1=histo.Clone()
        h1.GetYaxis().SetLabelFont(42)
        h1.GetYaxis().SetLabelSize(0.2)
        hstack.Add(h1)
        histos.append(h1)
     
      if "marker" in args.cfg:   
        hstack.Draw("nostack,e1p")
      else:
        hstack.Draw("nostack,hist")
      leg.Draw("sames")
#      cms().Draw("sames")
#      head().Draw("sames")     
      CMS_lumi(c, 4,  0 , aLittleExtra=0.07)
      print plot
      ks_test = histos[0].KolmogorovTest(histos[1])
      print "   KolmogorovTest =",ks_test
      # draw everything
      if "LogY" in args.cfg:  c.SetLogy()  
      if "LogX" in args.cfg:  c.SetLogx()
      if args.ratio and len(args.inputPaths)==2:     
        ks_test = histos[0].KolmogorovTest(histos[1])
        print "   KolmogorovTest =",ks_test
        plot+="_ks_"+str(ks_test)
        hratio = createRatio( histos[0], histos[1])
        pad2.cd()
        hratio.Draw("p")
       

      c.SaveAs(args.outputName+"/"+plot+".png");
      # c.SaveAs(args.outputName+"/"+plot+".pdf"); 
      del c
           
         
        
        
    
        
    print "finished !"
  
