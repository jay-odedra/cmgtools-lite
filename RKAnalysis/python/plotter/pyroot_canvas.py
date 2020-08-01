import ROOT as rt
from cms_lumi import CMS_lumi

def defalut_canvas(name):
  c1=rt.TCanvas(name,name,700,700)
#  c1.SetCanvasDefW(700)
#  c1.SetCanvasDefH(700);
#  c1.SetCanvasColor(0);
#  c1.SetCanvasBorderMode(0)
  c1.SetBorderSize(0)
  c1.SetTopMargin(0.08)
  c1.SetLeftMargin(0.12)
  c1.SetRightMargin(0.04)
  c1.SetBottomMargin(0.12)
  return c1

def default_plot(histo,xaxis="",yaxis=""):
  if xaxis!="": histo.GetXaxis().SetTitle(xaxis)
  if yaxis!="": histo.GetYaxis().SetTitle(yaxis)
  histo.SetLineWidth(2)
  histo.SetMarkerStyle(20)
  histo.SetMarkerSize(2)
  histo.GetXaxis().SetTitleSize(0.06)
  histo.GetYaxis().SetTitleSize(0.06)
  histo.GetXaxis().SetTitleFont(42)
  histo.GetYaxis().SetTitleFont(42)
  histo.GetXaxis().SetTitleOffset(0.8)
  histo.GetYaxis().SetTitleOffset(0.95)
  histo.GetXaxis().SetLabelOffset(0.007)
  histo.GetYaxis().SetLabelOffset(0.007)
  histo.GetYaxis().SetLabelSize(0.040)
  histo.GetXaxis().SetLabelSize(0.045)
  return histo


def canvas_Nplots(plots,name,Norm=False,logY=False,ymin=-1,ymax=-1,xaxis="",yaxis="",legs=[],colors=[]):
  c1=defalut_canvas(name)
  tleg=rt.TLegend(0.75,0.80,0.95,0.95)
  plot1=default_plot(plots[0],xaxis,yaxis)
  if ymin!=-1 and ymax==-1: plot1.GetYaxis().SetMinimum(ymin)
  if ymin==-1 and ymax!=-1: plot1GetYaxis().SetMinimum(ymax)
  if ymin!=-1 and ymax!=-1: plot1.GetYaxis().SetRangeUser(ymin,ymax)
  if logY: c1.SetLogy()
  if Norm: plot1.Scale(1./plot1.Integral())
  plot1.Draw("HIST")
  if len(plots)==1: return c1
  if len(legs)>0: tleg.AddEntry(plot1,legs[0])
  if len(colors)>0: plot1.SetLineColor(colors[0])
  for iplot,plt in enumerate(plots):
    if iplot==0: continue
    plot=default_plot(plt)
    if Norm: plot.Scale(1./plot.Integral())
    plot.Draw("HIST sames")
    if len(legs)>0: tleg.AddEntry(plot,legs[iplot])
    if len(colors)>0: plot.SetLineColor(colors[iplot])
    else: plot.SetLineColor(iplot)
  tleg.Draw("sames")
  CMS_lumi(c1,  4,  0 , aLittleExtra=0.04)

  return c1

def canvas_Ngraphs(graphs,name,logY=False,xmin=-1,xmax=-1,ymin=-1,ymax=-1,xaxis="",yaxis="",legs=[],colors=[]):
  c1=defalut_canvas(name)
  tleg=rt.TLegend(0.75,0.80,0.95,0.95)
  graph1=default_plot(graphs[0],xaxis,yaxis)
  if ymin!=-1 and ymax==-1: graph1.GetYaxis().SetMinimum(ymin)
  if ymin==-1 and ymax!=-1: graph1.SetMaximum(ymax)
  if ymin!=-1 and ymax!=-1: graph1.GetYaxis().SetLimits(ymin,ymax)
  if xmin!=-1 and xmax==-1: graph1.GetXaxis().SetMinimum(xmin)
  if xmin==-1 and xmax!=-1: graph1.GetXaxis().SetMinimum(xmax)
  if xmin!=-1 and xmax!=-1: graph1.GetXaxis().SetLimits(xmin,xmax)
  if logY: c1.SetLogy()
  graph1.Draw("AP")

  if len(graphs)==1: return c1
  if len(legs)>0: tleg.AddEntry(graph1,legs[0])
  if len(colors)>0: graph1.SetMarkerColor(colors[0])

  for igr,gr in enumerate(graphs):
    graph=default_plot(gr)
    if len(legs)>0: tleg.AddEntry(graph,legs[igr])
    if len(colors)>0: graph.SetMarkerColor(colors[igr])
    else: graph.SetMarkerColor(igr)
    graph.Draw("P sames")
    
  tleg.Draw("sames")
  CMS_lumi(c1,  4,  0 , aLittleExtra=0.04)
  graph.SetTitle("")
  return c1

 
