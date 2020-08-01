{
  TStyle* mcStyle = new TStyle("mcStyle","GK Root Styles");
  mcStyle->SetCanvasBorderMode(0);
  mcStyle->SetCanvasColor(kWhite);
  mcStyle->SetCanvasDefH(600); //Height of canvas
  mcStyle->SetCanvasDefW(600); //Width of canvas
  mcStyle->SetCanvasDefX(0);   //POsition on screen
  mcStyle->SetCanvasDefY(0);

// For the Pad:
  mcStyle->SetPadBorderMode(0);
  // mcStyle->SetPadBorderSize(Width_t size = 1);
  mcStyle->SetPadColor(kWhite);
  mcStyle->SetPadGridX(false);
  mcStyle->SetPadGridY(false);
  mcStyle->SetGridColor(0);
  mcStyle->SetGridStyle(3);
  mcStyle->SetGridWidth(1);

// For the frame:
  mcStyle->SetFrameBorderMode(0);
  mcStyle->SetFrameBorderSize(1);
  mcStyle->SetFrameFillColor(0);
  mcStyle->SetFrameFillStyle(0);
  mcStyle->SetFrameLineColor(1);
  mcStyle->SetFrameLineStyle(1);
  mcStyle->SetFrameLineWidth(1);

// For the histo:
  if (force) {
      // mcStyle->SetHistFillColor(1);
      // mcStyle->SetHistFillStyle(0);
      mcStyle->SetHistLineColor(1);
      mcStyle->SetHistLineStyle(0);
      mcStyle->SetHistLineWidth(1);
      // mcStyle->SetLegoInnerR(Float_t rad = 0.5);
      // mcStyle->SetNumberContours(Int_t number = 20);
  }

  mcStyle->SetEndErrorSize(2);
  //mcStyle->SetErrorMarker(20);
  mcStyle->SetErrorX(0.);
  
  mcStyle->SetMarkerStyle(20);

//For the fit/function:
  mcStyle->SetOptFit(1);
  mcStyle->SetFitFormat("5.4g");
  mcStyle->SetFuncColor(2);
  mcStyle->SetFuncStyle(1);
  mcStyle->SetFuncWidth(1);

//For the date:
  mcStyle->SetOptDate(0);
  // mcStyle->SetDateX(Float_t x = 0.01);
  // mcStyle->SetDateY(Float_t y = 0.01);

// For the statistics box:
  mcStyle->SetOptFile(0);
  //mcStyle->SetOptStat(0);
  mcStyle->SetOptStat("mr");
  mcStyle->SetStatColor(kWhite);
  mcStyle->SetStatFont(42);
  mcStyle->SetStatFontSize(0.04);///---> mcStyle->SetStatFontSize(0.025);
  mcStyle->SetStatTextColor(1);
  mcStyle->SetStatFormat("6.4g");
  mcStyle->SetStatBorderSize(1);
  mcStyle->SetStatH(0.1);
  mcStyle->SetStatW(0.2);///---> mcStyle->SetStatW(0.15);

  // mcStyle->SetStatStyle(Style_t style = 1001);
  // mcStyle->SetStatX(Float_t x = 0);
  // mcStyle->SetStatY(Float_t y = 0);

// Margins:
  mcStyle->SetPadTopMargin(0.05);
  mcStyle->SetPadBottomMargin(0.13);
  mcStyle->SetPadLeftMargin(0.18);
  mcStyle->SetPadRightMargin(0.04);

// For the Global title:

  mcStyle->SetOptTitle(0);
  mcStyle->SetTitleFont(42);
  mcStyle->SetTitleColor(1);
  mcStyle->SetTitleTextColor(1);
  mcStyle->SetTitleFillColor(10);
  mcStyle->SetTitleFontSize(0.05);
  // mcStyle->SetTitleH(0); // Set the height of the title box
  // mcStyle->SetTitleW(0); // Set the width of the title box
  // mcStyle->SetTitleX(0); // Set the position of the title box
  // mcStyle->SetTitleY(0.985); // Set the position of the title box
  // mcStyle->SetTitleStyle(Style_t style = 1001);
  // mcStyle->SetTitleBorderSize(2);

// For the axis titles:

  mcStyle->SetTitleColor(1, "XYZ");
  mcStyle->SetTitleFont(42, "XYZ");
  mcStyle->SetTitleSize(0.06, "XYZ");
  // mcStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // mcStyle->SetTitleYSize(Float_t size = 0.02);
  mcStyle->SetTitleXOffset(0.9);
  mcStyle->SetTitleYOffset(1.35);
  // mcStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

// For the axis labels:

  mcStyle->SetLabelColor(1, "XYZ");
  mcStyle->SetLabelFont(42, "XYZ");
  mcStyle->SetLabelOffset(0.007, "XYZ");
  mcStyle->SetLabelSize(0.05, "XYZ");

// For the axis:

  mcStyle->SetAxisColor(1, "XYZ");
  mcStyle->SetStripDecimals(kTRUE);
  mcStyle->SetTickLength(0.03, "XYZ");
  mcStyle->SetNdivisions(510, "XYZ");
  mcStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  mcStyle->SetPadTickY(1);

// Change for log plots:
  mcStyle->SetOptLogx(0);
  mcStyle->SetOptLogy(0);
  mcStyle->SetOptLogz(0);

// Postscript options:
  mcStyle->SetPaperSize(20.,20.);
  gROOT->SetStyle("mcStyle");
  return;
}
