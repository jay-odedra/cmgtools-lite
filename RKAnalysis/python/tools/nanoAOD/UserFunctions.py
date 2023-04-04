from ROOT import TLorentzVector,TVector3
from math import sqrt
from PhysicsTools.HeppyCore.utils.deltar import deltaR

def TagVars(collections):
  results=[]; Et_ratio=[]; Dphi=[]; projB=[]; DzTagMuK=[]; DzTagMuL1=[]; 
  DzTagMuL2=[]; 
  tracks=collections[0]
  Bcands=collections[2]
  trgmuons=(collections[1])
  trgmuon_vec=TLorentzVector()
  trgmuon_vec.SetPtEtaPhiM(0,0,0,0)
  trgmuon_vz=-99
  for trgmuon in trgmuons:
    if not getattr(trgmuon,"isTriggering"): 
       continue;
    trgmuon_vec.SetPtEtaPhiM(getattr(trgmuon,"pt"),getattr(trgmuon,"eta"),getattr(trgmuon,"phi"),0.105)
    trgmuon_vz=getattr(trgmuon,"vz")
    break
  if trgmuon_vec.M()==0:
    result=[[0], [0], [0], [0], [0], [0]]
    return result
  sum_track_vec=trgmuon_vec;
  sum_track=trgmuon_vec.Pt();
  for track  in tracks:
    track_vec=TLorentzVector();
    track_vec.SetPtEtaPhiM(getattr(track,"pt"),getattr(track,"eta"),getattr(track,"phi"),0.139)
    if trgmuon_vec.DrEtaPhi(track_vec)>0.4: 
       continue
    sum_track_vec=sum_track_vec+track_vec;
    sum_track+=track_vec.Pt()

  for Bcand in Bcands:
    Bcand_vec=TLorentzVector();
    Bcand_vec.SetPtEtaPhiM(getattr(Bcand,"fit_pt"),getattr(Bcand,"fit_eta"),getattr(Bcand,"fit_phi"),getattr(Bcand,"fit_mass"))
    if sum_track>0:
      Et_ratio.append(Bcand_vec.Et()/sum_track)
    else:
      Et_ratio.append(0)
    Dphi.append(Bcand_vec.DeltaPhi(sum_track_vec))
    projB.append(Bcand_vec*sum_track_vec)   
    DzTagMuK.append( abs(trgmuon_vz-getattr(Bcand,"kVz")) )
    DzTagMuL1.append( abs(trgmuon_vz-getattr(Bcand,"l1Vz")) ) 
    DzTagMuL2.append( abs(trgmuon_vz-getattr(Bcand,"l2Vz")) )
    
 
  result=[Et_ratio, Dphi, projB, DzTagMuL1, DzTagMuL2, DzTagMuK]
  return result

def ClosestTrkVars(collections):
  results=[]
  mll_e1_trk=[]
  mll_e2_trk=[]
  minxy1_b_trk=[]
  minxy2_b_trk=[]
  minxy3_b_trk=[]
  meanxy_b_trk=[]
  tracks=collections[0]
  Bcands=collections[1]
  Electrons=collections[2]

  for Bcand in Bcands:
    e1_vec=TLorentzVector();   e2_vec=TLorentzVector(); 
    trk1_vec=TLorentzVector(); trk2_vec=TLorentzVector();
    k_idx=getattr(Bcand,"kIdx")
    recoE1=Electrons[getattr(Bcand,"l1Idx")]
    recoE2=Electrons[getattr(Bcand,"l2Idx")]
    recoK=tracks[k_idx]
    e1_vec.SetPtEtaPhiM(getattr(recoE1,"pt"),getattr(recoE1,"eta"),getattr(recoE1,"phi"),0.0005)
    e2_vec.SetPtEtaPhiM(getattr(recoE2,"pt"),getattr(recoE2,"eta"),getattr(recoE2,"phi"),0.0005)
    k_eta=getattr(recoK,"eta");       k_phi=getattr(recoK,"phi")
    b_eta=getattr(Bcand,"fit_eta");   b_phi=getattr(Bcand,"fit_phi")

    vx_e1=getattr(Bcand,"l1Vx");   vy_e1=getattr(Bcand,"l1Vy")
    vx_e2=getattr(Bcand,"l2Vx");   vy_e2=getattr(Bcand,"l2Vy")
    vx_b=getattr(Bcand,"vtx_x");   vy_b=getattr(Bcand,"vtx_y")

    min_distance_trk_e1=100;   
    min_distance_trk_e2=100;
    imin_distance_trk_e1=-1;        
    imin_distance_trk_e2=-1;     
    distances_b_trk=[]         
    mean_b_trk=0;      
    imean_b_trk=0. 
    
    for itrk,track in enumerate(tracks):
      if k_idx==itrk:  continue
      vx_trk=getattr(track,"vx")   
      vy_trk=getattr(track,"vy")
      vz_trk=getattr(track,"vz")
      trk_eta=getattr(track,"eta")  
      trk_phi=getattr(track,"phi")
      
      if deltaR(e1_vec.Eta(),e1_vec.Phi(),trk_eta,trk_phi)<0.03 or \
         deltaR(e2_vec.Eta(),e2_vec.Phi(),trk_eta,trk_phi)<0.03 or \
         deltaR(k_eta,k_phi,trk_eta,trk_phi)<0.03:
           continue;
      if min_distance_trk_e1> sqrt( (vx_e1-vx_trk)**(2) + (vy_e1-vy_trk)**(2) ):
         min_distance_trk_e1 = sqrt( (vx_e1-vx_trk)**(2) + (vy_e1-vy_trk)**(2) )
         imin_distance_trk_e1=itrk
      if min_distance_trk_e2> sqrt( (vx_e2-vx_trk)**(2) + (vy_e2-vy_trk)**(2) ):
         min_distance_trk_e2 = sqrt( (vx_e2-vx_trk)**(2) + (vy_e2-vy_trk)**(2) )
         imin_distance_trk_e2=itrk
      distances_b_trk.append(sqrt( (vx_b-vx_trk)**(2) + (vy_b-vy_trk)**(2) ) )
      if deltaR(b_eta,b_phi,trk_eta,trk_phi)<0.4:
         mean_b_trk+= sqrt( (vx_b-vx_trk)**(2) + (vy_b-vy_trk)**(2) )
         imean_b_trk+=1.0
    distances_b_trk=sorted(distances_b_trk)     

    if imin_distance_trk_e1>-1:
      trk1_vec.SetPtEtaPhiM(getattr(tracks[imin_distance_trk_e1],"pt"),getattr(tracks[imin_distance_trk_e1],"eta"),getattr(tracks[imin_distance_trk_e1],"phi"),0.139)
      mll_e1_trk.append( (trk1_vec+e1_vec).M() )
    else:
      mll_e1_trk.append(-1. )

    if imin_distance_trk_e2>-1:
      trk2_vec.SetPtEtaPhiM(getattr(tracks[imin_distance_trk_e2],"pt"),getattr(tracks[imin_distance_trk_e2],"eta"),getattr(tracks[imin_distance_trk_e2],"phi"),0.139)
      mll_e2_trk.append( (trk2_vec+e2_vec).M() )
    else:
      mll_e2_trk.append( -1. )


    if len(distances_b_trk)>0: minxy1_b_trk.append(distances_b_trk[0])
    else: minxy1_b_trk.append(10)
    if len(distances_b_trk)>1: minxy2_b_trk.append(distances_b_trk[1])
    else: minxy2_b_trk.append(10)
    if len(distances_b_trk)>2: minxy3_b_trk.append(distances_b_trk[2])
    else: minxy3_b_trk.append(10)
    if imean_b_trk>0: meanxy_b_trk.append(mean_b_trk/imean_b_trk)
    else: meanxy_b_trk.append(10)

  results=[ mll_e1_trk, mll_e2_trk, minxy1_b_trk, minxy2_b_trk, minxy3_b_trk,\
            meanxy_b_trk ]
  return results


def D0Vars(collections):
    Bcands=collections[0]
    trk_opp_l_kpi_mass=[]
       
    for Bcand in Bcands:
      vK=TLorentzVector()
      vL=TLorentzVector()
      kcharge=getattr(Bcand,"k_charge")
      
      if getattr(Bcand,"l1_charge") == getattr(Bcand,"l2_charge"):
         if getattr(Bcand,"l1_charge") == getattr(Bcand,"k_charge"):
            trk_opp_l_kpi_mass.append(-1)
            continue;
         else:    
            vL.SetPtEtaPhiM( getattr(Bcand,"fit_l1_pt"), getattr(Bcand,"fit_l1_eta"), getattr(Bcand,"fit_l1_phi"),0.493)
      else:
         if getattr(Bcand,"l1_charge") != kcharge:
            vL.SetPtEtaPhiM( getattr(Bcand,"fit_l1_pt"), getattr(Bcand,"fit_l1_eta"), getattr(Bcand,"fit_l1_phi"),0.493)
         else:
            vL.SetPtEtaPhiM( getattr(Bcand,"fit_l2_pt"), getattr(Bcand,"fit_l2_eta"), getattr(Bcand,"fit_l2_phi"),0.493)

      vK.SetPtEtaPhiM( getattr(Bcand,"fit_k_pt"), getattr(Bcand,"fit_k_eta"), getattr(Bcand,"fit_k_phi"),0.139)
      k_l_mass_hypoth1=(vL+vK).M()
      vL.SetPtEtaPhiM( vL.Pt(),vL.Eta(),vL.Phi(),0.139)
      vK.SetPtEtaPhiM( vK.Pt(),vK.Eta(),vK.Phi(),0.493)
      if k_l_mass_hypoth1> (vL+vK).M():
         trk_opp_l_kpi_mass.append((vL+vK).M())
      else:
         trk_opp_l_kpi_mass.append(k_l_mass_hypoth1)
     
    return [trk_opp_l_kpi_mass]

def FONLL(collections):
    genB_pt=collections[0]
#    genB_pt=getattr(genB,"pt")
#    FONLL_Weight=[]
    weight=1.
    if(genB_pt>=0 and genB_pt<1):weight=1.23129
    elif(genB_pt<2):weight=1.24869
    elif(genB_pt<3):weight=1.21966
    elif(genB_pt<4):weight=1.17165
    elif(genB_pt<5):weight=1.12232
    elif(genB_pt<6):weight=1.00289
    elif(genB_pt<7):weight=0.881216
    elif(genB_pt<8):weight=0.781735
    elif(genB_pt<9):weight=0.738323
    elif(genB_pt<10):weight=0.697129
    elif(genB_pt<11):weight=0.677508
    elif(genB_pt<12):weight=0.676085
    elif(genB_pt<13):weight=0.673541
    elif(genB_pt<14):weight=0.68323
    elif(genB_pt<15):weight=0.689577
    elif(genB_pt<16):weight=0.685095
    elif(genB_pt<17):weight=0.718314
    elif(genB_pt<18):weight=0.707634
    elif(genB_pt<19):weight=0.710804
    elif(genB_pt<20):weight=0.728134
    elif(genB_pt<21):weight=0.741782
    elif(genB_pt<22):weight=0.750555
    elif(genB_pt<23):weight=0.772471
    elif(genB_pt<24):weight=0.771538
    elif(genB_pt<25):weight=0.776254
    elif(genB_pt<26):weight=0.795407
    elif(genB_pt<27):weight=0.790832
    elif(genB_pt<28):weight=0.80981
    elif(genB_pt<29):weight=0.805832
    elif(genB_pt<30):weight=0.817697
    elif(genB_pt<31):weight=0.825468
    elif(genB_pt<32):weight=0.830348
    elif(genB_pt<33):weight=0.852276
    elif(genB_pt<34):weight=0.863482
    elif(genB_pt<35):weight=0.845245
    elif(genB_pt<36):weight=0.833868
    elif(genB_pt<37):weight=0.846842
    elif(genB_pt<38):weight=0.857164
    elif(genB_pt<39):weight=0.847861
    elif(genB_pt<40):weight=0.894865
    elif(genB_pt<41):weight=0.796462
    elif(genB_pt<42):weight=0.953703
    elif(genB_pt<43):weight=0.879786
    elif(genB_pt<44):weight=0.809249
    elif(genB_pt<45):weight=0.801929
    elif(genB_pt<46):weight=0.92993
    elif(genB_pt<47):weight=0.84823
    elif(genB_pt<48):weight=0.976552
    elif(genB_pt<49):weight=0.83234
    elif(genB_pt<50):weight=0.875064
    elif(genB_pt<51):weight=0.904693
    elif(genB_pt<52):weight=0.97148
    elif(genB_pt<53):weight=0.898738
    elif(genB_pt<54):weight=0.906998
    elif(genB_pt<55):weight=0.861127
    elif(genB_pt<56):weight=0.977243
    elif(genB_pt<57):weight=1.0723
    elif(genB_pt<58):weight=0.911046
    elif(genB_pt<59):weight=0.899243
    elif(genB_pt<60):weight=0.940553
    elif(genB_pt<61):weight=0.684617
    elif(genB_pt<62):weight=0.888701
    elif(genB_pt<63):weight=0.970108
    elif(genB_pt<64):weight=0.962083
    elif(genB_pt<65):weight=1.3151
    elif(genB_pt<66):weight=0.656013
    elif(genB_pt<67):weight=1.08272
    elif(genB_pt<68):weight=0.936489
    elif(genB_pt<69):weight=1.0848
    elif(genB_pt<70):weight=1.14986
    elif(genB_pt<71):weight=0.800469
    elif(genB_pt<72):weight=0.743639
    elif(genB_pt<73):weight=0.745061
    elif(genB_pt<74):weight=0.819657
    elif(genB_pt<75):weight=0.989314
    elif(genB_pt<76):weight=0.978881
    elif(genB_pt<77):weight=1.12579
    elif(genB_pt<78):weight=1.13739
    elif(genB_pt<79):weight=0.671662
    elif(genB_pt<80):weight=0.918632
    elif(genB_pt<81):weight=0.860115
    elif(genB_pt<82):weight=0.805388
    elif(genB_pt<83):weight=0.892166
    elif(genB_pt<84):weight=1.14984
    elif(genB_pt<85):weight=0.664142
    elif(genB_pt<86):weight=1.15791
    elif(genB_pt<87):weight=0.693787
    elif(genB_pt<88):weight=1.43214
    elif(genB_pt<89):weight=0.421746
    elif(genB_pt<90):weight=0.905503
    elif(genB_pt<91):weight=0.996583
    elif(genB_pt<92):weight=0.805506
    elif(genB_pt<93):weight=1.06347
    elif(genB_pt<94):weight=2.50994
    elif(genB_pt<95):weight=0.593067
    elif(genB_pt<96):weight=1.11704
    elif(genB_pt<97):weight=2.11593
    elif(genB_pt<98):weight=4.01005
    elif(genB_pt<99):weight=0.540705
    elif(genB_pt<100):weight=1.79186
    else:weight=1.
    
    return [weight]

def muon_mediumID_SF(collections):
    pt=collections[0]
    eta=collections[1]
    weight1=1.0
    
    if(abs(eta)<0.9):
      if(pt<2.5):weight1=1.
      elif(pt<2.75):weight1=1.
      elif(pt<3.):weight1=1.
      elif(pt<3.25):weight1=1.382072183780116
      elif(pt<3.5):weight1=1.0321035483620598
      elif(pt<3.75):weight1=0.9791694908122722
      elif(pt<4.):weight1=0.9954328088450396
      elif(pt<4.5):weight1=0.9941658736497387
      elif(pt<5.):weight1=0.9974417269229903
      elif(pt<6.):weight1=0.9957181140682222
      elif(pt<8.):weight1=0.9904021562380856
      elif(pt<10.):weight1=0.9928698256706819
      elif(pt<15.):weight1=0.9960358510695144
      elif(pt<20.):weight1=0.9969411479771049
      elif(pt<30.):weight1=0.9969656134496612
      else:weight1=0.9755435392968379
    elif(abs(eta)<1.2):
      if(pt<2.5):weight1=0.7289067586216103
      elif(pt<2.75):weight1=0.6537739889363587
      elif(pt<3.):weight1=0.887122351214275
      elif(pt<3.25):weight1=1.3749633027704775
      elif(pt<3.5):weight1=1.0866589410865806
      elif(pt<3.75):weight1=1.0267594540658824
      elif(pt<4.):weight1=1.0083060799582022
      elif(pt<4.5):weight1=0.991486107586366
      elif(pt<5.):weight1=0.9891940960009618
      elif(pt<6.):weight1=0.987903453148778
      elif(pt<8.):weight1=0.9921567436386026
      elif(pt<10.):weight1=0.9894439353437793
      elif(pt<15.):weight1=0.9912291156332008
      elif(pt<20.):weight1=0.9962640329485886
      elif(pt<30.):weight1=0.9933117383009565
      else:weight1=1.0148297598640408
    elif(abs(eta)<2.1):
      if(pt<2.5):weight1=0.9865506972081618
      elif(pt<2.75):weight1=0.9826955440506251
      elif(pt<3.):weight1=0.9774168750310419
      elif(pt<3.25):weight1=0.9807997604030826
      elif(pt<3.5):weight1=0.9908701769819768
      elif(pt<3.75):weight1=0.9879807232447103
      elif(pt<4.):weight1=0.9912455979946263
      elif(pt<4.5):weight1=0.9923876847693323
      elif(pt<5.):weight1=0.995576192402731
      elif(pt<6.):weight1=0.9963656549765838
      elif(pt<8.):weight1=0.9953629006376794
      elif(pt<10.):weight1=0.998257212639415
      elif(pt<15.):weight1=0.9990739155301513
      elif(pt<20.):weight1=1.007003846164823
      elif(pt<30.):weight1=0.9908884046823371
      else:weight1=0.9473670683191981
    elif(abs(eta)<2.4):
      if(pt<2.5):weight1=0.9933722370034499
      elif(pt<2.75):weight1=0.9847946575038667
      elif(pt<3):weight1=0.9940226537143696
      elif(pt<3.25):weight1=0.9895322467466758
      elif(pt<3.5):weight1=0.989563309135598
      elif(pt<3.75):weight1=0.994616205578823
      elif(pt<4.):weight1=0.9869882673527878
      elif(pt<4.5):weight1=0.9854168637103492
      elif(pt<5.):weight1=0.983405035052089
      elif(pt<6.):weight1=0.992865101640911
      elif(pt<8.):weight1=0.9910717727029733
      elif(pt<10.):weight1=0.9875450367957237
      elif(pt<15.):weight1=0.9676717601696864
      elif(pt<20.):weight1=1.
      elif(pt<30.):weight1=1.
      else:weight1=1.
    else:
      weight1=-99.0
    return [weight1]

def PAssymVar(collections):
    pv_x=collections[0]
    pv_y=collections[1]
    pv_z=collections[2]
    Bcands=collections[3]

    assym=[]
    pv_vtx=TVector3()
    pv_vtx.SetXYZ(pv_x,pv_y,pv_z) 

    for Bcand in Bcands:
      b_vtx=TVector3()
      b_vtx.SetXYZ(getattr(Bcand,"vtx_x"), getattr(Bcand,"vtx_y"), getattr(Bcand,"vtx_z"))
      k_p=TVector3()
      e1_p=TVector3()
      e2_p=TVector3()
      k_p.SetPtEtaPhi(getattr(Bcand,"fit_k_pt"), getattr(Bcand,"fit_k_eta"), getattr(Bcand,"fit_k_phi"))
      e1_p.SetPtEtaPhi(getattr(Bcand,"fit_l1_pt"), getattr(Bcand,"fit_l1_eta"), getattr(Bcand,"fit_l1_phi"))
      e2_p.SetPtEtaPhi(getattr(Bcand,"fit_l2_pt"), getattr(Bcand,"fit_l2_eta"), getattr(Bcand,"fit_l2_phi"))
      assym.append( (((e1_p+e2_p).Cross(pv_vtx-b_vtx)).Mag()-(k_p.Cross(pv_vtx-b_vtx)).Mag())/(((e1_p+e2_p).Cross(pv_vtx-b_vtx)).Mag()+(k_p.Cross(pv_vtx-b_vtx)).Mag()) )

    return [assym]


def TagVarsMC(collections):
  results=[]; Et_ratio=-99.; Dphi=-99.; projB=-99.
  tracks=collections[0]
  trgmuons=collections[1]
  recoB_pt=collections[2]
  recoB_eta=collections[3]
  recoB_phi=collections[4]
  recoB_mass=collections[5]
  recoE1_vz=collections[6]
  recoE2_vz=collections[7]
  recoK_vz=collections[8]
  trgmuon_vec=TLorentzVector()
  trgmuon_vec.SetPtEtaPhiM(0,0,0,0)
  for trgmuon in trgmuons:
    if getattr(trgmuon,"isTriggering")==0:
       continue
    trgmuon_vec.SetPtEtaPhiM(getattr(trgmuon,"pt"),getattr(trgmuon,"eta"),getattr(trgmuon,"phi"),0.105)
    break
  if trgmuon_vec.M()==0:
    result=[-99.,-99.,-99.,-99.,-99.,-99.]
    return result 
  sum_track_vec=trgmuon_vec;
  sum_track=trgmuon_vec.Pt();
  trgmuon_vz=getattr(trgmuon,"vz")
  for track  in tracks:
    track_vec=TLorentzVector();
    track_vec.SetPtEtaPhiM(getattr(track,"pt"),getattr(track,"eta"),getattr(track,"phi"),0.139)
    if trgmuon_vec.DrEtaPhi(track_vec)>0.4: 
       continue
    sum_track_vec=sum_track_vec+track_vec;
    sum_track+=track_vec.Pt()

  recoB_vec=TLorentzVector();
  recoB_vec.SetPtEtaPhiM(recoB_pt,recoB_eta,recoB_phi,recoB_mass)
  if sum_track>0:
    Et_ratio=recoB_vec.Et()/sum_track
  else:
    Et_ratio=0
  Dphi=recoB_vec.DeltaPhi(sum_track_vec)
  projB=recoB_vec*sum_track_vec
  result=[Et_ratio,Dphi,projB,abs(trgmuon_vz-recoE1_vz),abs(trgmuon_vz-recoE2_vz),abs(trgmuon_vz-recoK_vz)]
  return result


def ClosestTrkVarsMC(collections):
 
  mll_e1_trk=-99
  mll_e2_trk=-99
  minxy1_b_trk=-99
  minxy2_b_trk=-99
  minxy3_b_trk=-99
  meanxy_b_trk=-99
  results=[mll_e1_trk,mll_e2_trk,minxy1_b_trk,minxy2_b_trk,minxy3_b_trk, meanxy_b_trk]
  tracks=collections[0]
  Bcands=collections[1]
  Bidx=collections[2]
  reco_electrons=collections[3]
  idx_e1=collections[4]
  idx_e2=collections[5]
  


  if Bidx<0:
    return results
  recoB=Bcands[Bidx]; 
  idx_k=getattr(recoB,"kIdx");
  recoE1=reco_electrons[idx_e1];  
  recoE2=reco_electrons[idx_e2];
  recoK=tracks[idx_k]
  e1_vec=TLorentzVector();   
  e2_vec=TLorentzVector();
  e1_vec.SetPtEtaPhiM(getattr(recoE1,"pt"),getattr(recoE1,"eta"),getattr(recoE1,"phi"),0.0005)
  e2_vec.SetPtEtaPhiM(getattr(recoE2,"pt"),getattr(recoE2,"eta"),getattr(recoE2,"phi"),0.0005)
  
  k_eta=getattr(recoK,"eta");       k_phi=getattr(recoK,"phi")
  b_eta=getattr(recoB,"fit_eta");   b_phi=getattr(recoB,"fit_phi")
  vx_b=getattr(recoB,"vtx_x");      vy_b=getattr(recoB,"vtx_y")
  vx_e1=getattr(recoE1,"vx");       vy_e1=getattr(recoE1,"vy");
  vx_e2=getattr(recoE2,"vx");       vy_e2=getattr(recoE2,"vy");


  min_dist_e1=100;   min_dist_e2=100;
  itrk_e1=-1;        itrk_e2=-1;     
  distance_b_trk=[]
  mean_b_trk=0.
  imean_b_trk=0.
  for itrk,track in enumerate(tracks):
      if itrk==idx_k:
         continue
      vx_trk=getattr(track,"vx")   
      vy_trk=getattr(track,"vy")
      trk_eta=getattr(track,"eta")  
      trk_phi=getattr(track,"phi")
      if deltaR(e1_vec.Eta(),e1_vec.Phi(),trk_eta,trk_phi)<0.03 or \
         deltaR(e2_vec.Eta(),e2_vec.Phi(),trk_eta,trk_phi)<0.03 or \
         deltaR(k_eta,k_phi,trk_eta,trk_phi)<0.03:
           continue;
      if min_dist_e1> sqrt( (vx_e1-vx_trk)**(2) + (vy_e1-vy_trk)**(2) ): 
         min_dist_e1 = sqrt( (vx_e1-vx_trk)**(2) + (vy_e1-vy_trk)**(2) )
         itrk_e1=itrk
      if min_dist_e2> sqrt( (vx_e2-vx_trk)**(2) + (vy_e2-vy_trk)**(2) ):
         min_dist_e2 = sqrt( (vx_e2-vx_trk)**(2) + (vy_e2-vy_trk)**(2) )
         itrk_e2=itrk
      distance_b_trk.append(sqrt( (vx_b-vx_trk)**(2) + (vy_b-vy_trk)**(2) ) )
      if deltaR(b_eta,b_phi,trk_eta,trk_phi)<0.4:
         mean_b_trk+= sqrt( (vx_b-vx_trk)**(2) + (vy_b-vy_trk)**(2) )
         imean_b_trk+=1.0
  distance_b_trk=sorted(distance_b_trk)     
  minxy_e1_trk=min_dist_e1;  
  minxy_e2_trk=min_dist_e2; 
  trk1_vec=TLorentzVector();
  trk2_vec=TLorentzVector();
  if itrk_e1>-1:
    trk1_vec.SetPtEtaPhiM(getattr(tracks[itrk_e1],"pt"),getattr(tracks[itrk_e1],"eta"),getattr(tracks[itrk_e1],"phi"),0.139)
    mll_e1_trk= (trk1_vec+e1_vec).M()
  else:
    mll_e1_trk=-1.

  if itrk_e2>-1:
    trk2_vec.SetPtEtaPhiM(getattr(tracks[itrk_e2],"pt"),getattr(tracks[itrk_e2],"eta"),getattr(tracks[itrk_e2],"phi"),0.139)
    mll_e2_trk= (trk2_vec+e2_vec).M()
  else:
    mll_e2_trk=-1.

  if len(distance_b_trk)>0: minxy1_b_trk=distance_b_trk[0]
  else: minxy1_b_trk=10
  if len(distance_b_trk)>1: minxy2_b_trk=distance_b_trk[1]
  else: minxy2_b_trk=10
  if len(distance_b_trk)>2: minxy3_b_trk=distance_b_trk[2]
  else: minxy3_b_trk=10
  if imean_b_trk>0:
    meanxy_b_trk=mean_b_trk/imean_b_trk
  else:
    meanxy_b_trk=10

  results=[ mll_e1_trk, mll_e2_trk, minxy1_b_trk, minxy2_b_trk, minxy3_b_trk,\
            meanxy_b_trk]
  return results


def D0VarsMC(collections):
    
    Bcands = collections[0]
    L1charge = collections[1]
    L2charge = collections[2]
    Kcharge  = collections[3]
    Bidx=collections[4]
    
    trk_opp_l_kpi_mass=-99
    if (L1charge<-1 or L2charge<-1 or Kcharge<-1or Bidx<0):
       return [trk_opp_l_kpi_mass]

    Bcand=Bcands[Bidx]
    L1Pt=getattr(Bcand,"fit_l1_pt")
    L1Eta=getattr(Bcand,"fit_l1_eta")
    L1Phi=getattr(Bcand,"fit_l1_phi")
    L2Pt=getattr(Bcand,"fit_l2_pt")
    L2Eta=getattr(Bcand,"fit_l2_eta")
    L2Phi=getattr(Bcand,"fit_l2_phi")
    KPt=getattr(Bcand,"fit_k_pt")
    KEta=getattr(Bcand,"fit_k_eta")
    KPhi=getattr(Bcand,"fit_k_phi")

    vK=TLorentzVector()
    vL=TLorentzVector()
    if L1charge != Kcharge:
       vL.SetPtEtaPhiM(L1Pt,L1Eta,L1Phi,0.493)
    else:
       vL.SetPtEtaPhiM(L2Pt,L2Eta,L2Phi,0.493) 
    vK.SetPtEtaPhiM(KPt,KEta,KPhi,0.139)  # getattr(Bcand,"fit_k_pt"), getattr(Bcand,"fit_k_eta"), getattr(Bcand,"fit_k_phi"),0.139)
    trk_opp_l_kpi_mass= (vL+vK).M()
    vL.SetPtEtaPhiM(vL.Pt(),vL.Eta(),vL.Phi(),0.139)
    vK.SetPtEtaPhiM(vK.Pt(),vK.Eta(),vK.Phi(),0.493)
    if trk_opp_l_kpi_mass>(vL+vK).M():
       trk_opp_l_kpi_mass=(vL+vK).M()
        
    return [trk_opp_l_kpi_mass]

def PAssymVarMC(collections):
    pv_x=collections[0]
    pv_y=collections[1]
    pv_z=collections[2]
    Bcands=collections[3]
    Bidx=collections[4]

    assym=-99.
    if Bidx<0:
       return [assym]
    pv_vtx=TVector3()
    pv_vtx.SetXYZ(pv_x,pv_y,pv_z)

    Bcand=Bcands[Bidx]
    b_vtx=TVector3()
    b_vtx.SetXYZ(getattr(Bcand,"vtx_x"), getattr(Bcand,"vtx_y"), getattr(Bcand,"vtx_z"))
    k_p=TVector3()
    e1_p=TVector3()
    e2_p=TVector3()
    k_p.SetPtEtaPhi(getattr(Bcand,"fit_k_pt"), getattr(Bcand,"fit_k_eta"), getattr(Bcand,"fit_k_phi"))
    e1_p.SetPtEtaPhi(getattr(Bcand,"fit_l1_pt"), getattr(Bcand,"fit_l1_eta"), getattr(Bcand,"fit_l1_phi"))
    e2_p.SetPtEtaPhi(getattr(Bcand,"fit_l2_pt"), getattr(Bcand,"fit_l2_eta"), getattr(Bcand,"fit_l2_phi"))
    assym= (((e1_p+e2_p).Cross(pv_vtx-b_vtx)).Mag()-(k_p.Cross(pv_vtx-b_vtx)).Mag())/(((e1_p+e2_p).Cross(pv_vtx-b_vtx)).Mag()+(k_p.Cross(pv_vtx-b_vtx)).Mag()) 

    return [assym]
