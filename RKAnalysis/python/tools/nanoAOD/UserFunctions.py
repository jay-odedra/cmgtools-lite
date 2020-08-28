from ROOT import TLorentzVector
from math import sqrt
from PhysicsTools.HeppyCore.utils.deltar import deltaR

def TagVars(collections):
  results=[]; Et_ratio=[]; Dphi=[]; projB=[]
  tracks=collections[0]
  Bcands=collections[2]
  trgmuon=(collections[1])[0]
  
  trgmuon_vec=TLorentzVector()
  trgmuon_vec.SetPtEtaPhiM(getattr(trgmuon,"pt"),getattr(trgmuon,"eta"),getattr(trgmuon,"phi"),0.105)
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
  result=[Et_ratio,Dphi,projB]
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
    
    trk1_vec.SetPtEtaPhiM(getattr(tracks[imin_distance_trk_e1],"pt"),getattr(tracks[imin_distance_trk_e1],"eta"),getattr(tracks[imin_distance_trk_e1],"phi"),0.139)
    trk2_vec.SetPtEtaPhiM(getattr(tracks[imin_distance_trk_e2],"pt"),getattr(tracks[imin_distance_trk_e2],"eta"),getattr(tracks[imin_distance_trk_e2],"phi"),0.139)

    mll_e1_trk.append( (trk1_vec+e1_vec).M() )               
    mll_e2_trk.append( (trk2_vec+e2_vec).M() )

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


def TagVarsMC(collections):
  results=[]; Et_ratio=[]; Dphi=[]; projB=[]
  tracks=collections[0]
  trgmuons=collections[1]
  recoB_pt=collections[2]
  recoB_eta=collections[3]
  recoB_phi=collections[4]
  recoB_mass=collections[5]
  if len(trgmuons)==0:
     default=[-99.,-99.,-99.]
     return default
  trgmuon=trgmuons[0]  
  trgmuon_vec=TLorentzVector()
  trgmuon_vec.SetPtEtaPhiM(getattr(trgmuon,"pt"),getattr(trgmuon,"eta"),getattr(trgmuon,"phi"),0.105)
  sum_track_vec=trgmuon_vec;
  sum_track=trgmuon_vec.Pt();
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
  result=[Et_ratio,Dphi,projB]
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
  trk1_vec.SetPtEtaPhiM(getattr(tracks[itrk_e1],"pt"),getattr(tracks[itrk_e1],"eta"),getattr(tracks[itrk_e1],"phi"),0.139)
  trk2_vec.SetPtEtaPhiM(getattr(tracks[itrk_e2],"pt"),getattr(tracks[itrk_e2],"eta"),getattr(tracks[itrk_e2],"phi"),0.139)
  mll_e1_trk= (trk1_vec+e1_vec).M()
  mll_e2_trk= (trk2_vec+e2_vec).M()

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

