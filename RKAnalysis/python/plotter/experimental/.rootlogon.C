
{

 TStyle* mcStyle = new TStyle("mcStyle",""); 
  TGaxis::SetMaxDigits(3);
 mcStyle->SetPalette(1,0); 
 mcStyle->SetLineWidth(3);
 mcStyle->SetOptTitle(0);
// mcStyle->SetOptStat(0); 
// mcStyle->SetOptTitle(0);
// mcStyle->SetOptDate(0);
 mcStyle->SetCanvasDefW(700); 
 mcStyle->SetCanvasDefH(700); 
 mcStyle->SetCanvasColor(0);
 mcStyle->SetCanvasBorderMode(0);
 mcStyle->SetCanvasBorderSize(0);
 mcStyle->SetPadTopMargin(0.08); 
 mcStyle->SetPadLeftMargin(0.12); 
 mcStyle->SetPadRightMargin(0.04);
 mcStyle->SetPadBottomMargin(0.12);
 mcStyle->SetTitleFont(42,"xy");
 mcStyle->SetTitleSize(0.06,"xy");
 mcStyle->SetTitleOffset(0.8,"x");
 mcStyle->SetTitleOffset(1.0,"y");
 mcStyle->SetLabelFont(42,"xy");
mcStyle->SetLabelSize(0.045,"xy");
 mcStyle->SetLabelOffset(0.007);
 mcStyle->SetPadGridX(0); 
 mcStyle->SetPadGridY(0);
 mcStyle->SetPadTickX(1);
 mcStyle->SetPadTickY(1);
 mcStyle->SetFrameBorderMode(0);
 mcStyle->SetFrameFillStyle(0);
 gROOT->SetStyle("mcStyle");
 
}

