
def SkimCuts(Bdecay,Bcuts):
    BParking_skim_cut = ("Sum$( "+
#                         "BToKMuMu_l_xy_unc>0 && BToKMuMu_l_xy/BToKMuMu_l_xy_unc>-1 && "+
                         Bdecay+"_fit_pt>{ptmin} && "+
                         Bdecay+"_fit_mass>{mmin} && "+
                         Bdecay+"_fit_mass<{mmax} && "+
                         Bdecay+"_l_xy_unc>0 && "+
                         Bdecay+"_l_xy/"+Bdecay+"_l_xy_unc>{slxy} && "+
                         Bdecay+"_fit_cos2D>{cos} && "+
                         Bdecay+"_svprob>{prob} &&"+
                         Bdecay+"_fit_l1_pt>{l1pt} &&"+
                         Bdecay+"_fit_l2_pt>{l2pt} &&"+
                         Bdecay+"_fit_k_pt>{kpt} &&"+
                         Bdecay+"_mll_fullfit>{mllmin} &&"+
                         Bdecay+"_mll_fullfit<{mllmax} && "+
                         "L1_DoubleEG9_er1p2_dR_Max0p7==1 && "+
                         "HLT_DoubleEle6_eta1p22_mMax6==1"
                         " )>0"
            ).format(
                     ptmin=Bcuts["Pt"],     mmin=Bcuts["MinMass"], 
                     mmax=Bcuts["MaxMass"], slxy=Bcuts["LxySign"], 
                     cos=Bcuts["Cos2D"],    prob=Bcuts["Prob"],
                     l1pt=Bcuts["L1Pt"],    l2pt=Bcuts["L2Pt"],
                     kpt=Bcuts["KPt"],      mllmin=Bcuts["Mllmin"],
                     mllmax=Bcuts["Mllmax"]
                    )
    return BParking_skim_cut


def KMuMuData ( process, Bcuts,tag):
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.collectionSkimmer import collectionSkimmer
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.collectionEmbeder import collectionEmbeder
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreator import branchCreator
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper

    BKLLSelection = lambda l : l.fit_pt > Bcuts["Pt" ] and l.fit_cos2D > Bcuts["Cos2D"] and l.svprob > Bcuts["Prob"] and l.l_xy_unc >0 and (l.l_xy)/l.l_xy_unc > Bcuts["LxySign"] and l.mll_fullfit>Bcuts["Mllmin"] and l.fit_mass>Bcuts["MinMass"] and l.fit_mass<Bcuts["MaxMass"] and l.mll_fullfit<Bcuts["Mllmax"]

    BSkim = collectionSkimmer(input = "BToKMuMu",
                            output = "SkimBToKMuMu",
                            selector = BKLLSelection,
                            branches = ["fit_pt","fit_mass","mass","l_xy",
                                        "l_xy_unc","fit_cos2D","svprob",
                                        "l1Idx","l2Idx","kIdx",
                                        "fit_eta","fit_phi",
                                        "mll_fullfit","fit_massErr",
                                        "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                        "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                        "fit_k_pt","fit_k_eta","fit_k_phi",
                                        "charge","k_svip3d","k_svip3d_err"
                                         ],
                            TriggerMuonId = "Muon_isTriggering",
                            selectTagMuons = tag,
                            flat = False
    )   
    process.append(BSkim)
    Mu1 = collectionEmbeder( inputColl = "Muon",
                             embededColl = "SkimBToKMuMu",
                             inputBranches = ["softId","vx","vy","vz","pfRelIso03_all","isTriggering","dxy","dxyErr","charge","mediumId"],
                             embededBranches = ["l1_softId","l1_vx","l1_vy","l1_vz","l1_iso","l1_isTrg","l1_dxy","l1_dxyErr","l1_charge","l1_mediumId"], 
                             embededCollIdx = "l1Idx"
    )
    process.append(Mu1)
    Mu2 = collectionEmbeder( inputColl = "Muon",
                             embededColl = "SkimBToKMuMu",
                             inputBranches = ["softId","vx","vy","vz","pfRelIso03_all","isTriggering","dxy","dxyErr","charge","mediumId"],
                             embededBranches = ["l2_softId","l2_vx","l2_vy","l2_vz","l2_iso","l2_isTrg","l2_dxy","l2_dxyErr","l2_charge","l2_mediumId"], 
                             embededCollIdx = "l2Idx"
    )
    process.append(Mu2)
    K = collectionEmbeder( inputColl = "ProbeTracks",
                           embededColl = "SkimBToKMuMu",
                           inputBranches = ["vx","vy","vz","charge","isMatchedToMuon"],
                           embededBranches = ["k_vx","k_vy","k_vz","k_charge","k_isMatchedToMuon"],  
                           embededCollIdx = "kIdx"
    )
    process.append(K)
    # in case of inf in L_xy/unc produces -99
    CreateVars = branchCreator(
      collection="SkimBToKMuMu",
        inputBranches=[["l_xy","l_xy_unc"],["l1_vz","l2_vz"],
                       ["k_vz","l1_vz","l2_vz"],
                       ["fit_l1_eta","fit_l1_phi","fit_l2_eta","fit_l2_phi"],
                       ["fit_k_eta","fit_k_phi","fit_l1_eta","fit_l1_phi","fit_l2_eta","fit_l2_phi"],
                       ["l1_dxy","l1_dxyErr"],["l2_dxy","l2_dxyErr"]],
        operation=["{0}/{1}","abs({0}-{1})",
                   "min(abs({0}-{1}),abs({0}-{2}))",
                   "deltaR({0},{1},{2},{3})",
                   "min( deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))",
                   "{0}/{1}","{0}/{1}"],
        createdBranches=["l_xy_sig","l1l2_dz","lk_dz","l1l2_dr","lk_dr","l1_dxy_sig","l2_dxy_sig"],
    )
    process.append(CreateVars)
    D0Vars = functionWrapper(
      functionName="D0Vars",
      collections=["SkimBToKMuMu"],
      createdBranches=["SkimBToKMuMu_kl_massKPi","SkimBToKMuMu_kl_massMuMu"],
      nCol="nSkimBToKMuMu"
    )
    process.append(D0Vars)
    return process

def KEEData ( process, Bcuts,use_PF=False,use_1LowPt_1PF=False):
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.collectionSkimmer import collectionSkimmer
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.collectionEmbeder import collectionEmbeder
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreator import branchCreator

    BKLLSelection = lambda l : l.fit_pt > Bcuts["Pt" ] and l.fit_cos2D > Bcuts["Cos2D"] and l.svprob > Bcuts["Prob"] and l.l_xy_unc >0 and (l.l_xy)/l.l_xy_unc > Bcuts["LxySign"] and l.mll_fullfit>Bcuts["Mllmin"] and l.fit_mass>Bcuts["MinMass"] and l.fit_mass<Bcuts["MaxMass"] and l.mll_fullfit<Bcuts["Mllmax"]
    
    if use_PF and not use_1LowPt_1PF:
      BKLLSelection = lambda l : l.fit_pt > Bcuts["Pt" ] and l.fit_cos2D > Bcuts["Cos2D"] and l.svprob > Bcuts["Prob"] and l.l_xy_unc >0 and (l.l_xy)/l.l_xy_unc > Bcuts["LxySign"] and l.mll_fullfit>Bcuts["Mllmin"] and l.fit_mass>Bcuts["MinMass"] and l.fit_mass<Bcuts["MaxMass"] and l.mll_fullfit<Bcuts["Mllmax"] and l.l1isPF == 1 and l.l2isPF == 1 and l.l1PFId>-30.5 and l.l2PFId>-50.0
    elif use_1LowPt_1PF and not use_PF:
      BKLLSelection = lambda l : l.fit_pt > Bcuts["Pt" ] and l.fit_cos2D > Bcuts["Cos2D"] and l.svprob > Bcuts["Prob"] and l.l_xy_unc >0 and (l.l_xy)/l.l_xy_unc > Bcuts["LxySign"] and l.mll_fullfit>Bcuts["Mllmin"] and l.fit_mass>Bcuts["MinMass"] and l.fit_mass<Bcuts["MaxMass"] and l.mll_fullfit<Bcuts["Mllmax"] and ( (l.l1isPF == 1 and l.l2isPF == 0 and l.l2isPFoverlap==0 and l.l1PFId>-2.0 and l.l2LowPtId>0.0) or (l.l1isPF == 0 and l.l2isPF == 1 and l.l1isPFoverlap==0 and l.l2PFId>-2.0 and l.l1LowPtId>0.0) )
    else:
      BKLLSelection = lambda l : l.fit_pt > Bcuts["Pt" ] and l.fit_cos2D > Bcuts["Cos2D"] and l.svprob > Bcuts["Prob"] and l.l_xy_unc >0 and (l.l_xy)/l.l_xy_unc > Bcuts["LxySign"] and l.mll_fullfit>Bcuts["Mllmin"] and l.fit_mass>Bcuts["MinMass"] and l.fit_mass<Bcuts["MaxMass"] and l.mll_fullfit<Bcuts["Mllmax"]
    
    BSkim = collectionSkimmer(input = "BToKEE",
                            output = "SkimBToKEE",
                            importedVariables = [
                                "Electron_isPF","Electron_isPF",
                                "Electron_isPFoverlap","Electron_isPFoverlap",
                                "Electron_pfmvaId","Electron_pfmvaId",
                                "Electron_mvaId","Electron_mvaId", 
                                "Electron_LooseID", "Electron_LooseID", 
                                "Electron_MediumID","Electron_MediumID",
                                "Electron_TightID","Electron_TightID",
                                "Electron_convVeto","Electron_convVeto"],
                            importIds = ["l1Idx","l2Idx",
                                         "l1Idx","l2Idx",
                                         "l1Idx","l2Idx",
                                         "l1Idx","l2Idx",
                                         "l1Idx","l2Idx",
                                         "l1Idx","l2Idx",
                                         "l1Idx","l2Idx",
                                         "l1Idx","l2Idx"],
                            varnames = ["l1isPF","l2isPF",
                                        "l1isPFoverlap","l2isPFoverlap",
                                        "l1PFId","l2PFId",
                                        "l1LowPtId","l2LowPtId",
                                        "l1LooseId","l2LooseId",
                                        "l1MediumId","l2MediumId",
                                        "l1TightId","l2TightId",
                                        "l1ConvVeto","l2ConvVeto"],
                            selector = BKLLSelection,
                            branches = ["fit_pt","fit_eta","fit_phi",
                                        "fit_mass","l_xy","l_xy_unc",
                                        "fit_cos2D","svprob","fit_massErr",
                                        "b_iso04","mll_fullfit",
                                        "vtx_x","vtx_y","vtx_z",
                                        "l1Idx","l2Idx","kIdx",
                                        "fit_k_pt","fit_k_eta","fit_k_phi",
                                        "k_iso04",
                                        "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                        "l1_iso04",
                                        "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                        "l2_iso04",
                                        "l1isPF","l2isPF","l1PFId","l2PFId",
                                        "l1LowPtId","l2LowPtId",
                                        "b_iso04_dca","l1_iso04_dca",
                                        "l2_iso04_dca","k_iso04_dca",
                                        "k_svip3d","k_svip3d_err",
                                        "l1_n_isotrk_dca","l2_n_isotrk_dca",
                                        "k_n_isotrk_dca"
                                        ],
                            flat = False
    )
    process.append(BSkim)
    El1 = collectionEmbeder( inputColl = "Electron",
                             embededColl = "SkimBToKEE",
                             inputBranches = ["vx","vy","vz","charge"],
                             embededBranches = ["l1_vx","l1_vy","l1_vz","l1_charge"], 
                             embededCollIdx = "l1Idx"
    )
    process.append(El1)
    El2 = collectionEmbeder( inputColl = "Electron",
                             embededColl = "SkimBToKEE",
                             inputBranches = ["vx","vy","vz","charge"],
                             embededBranches = ["l2_vx","l2_vy","l2_vz","l2_charge"],
                             embededCollIdx = "l2Idx"
    )
    process.append(El2)
    K = collectionEmbeder( inputColl = "ProbeTracks",
                           embededColl = "SkimBToKEE",
                           inputBranches = ["vx","vy","vz","DCASig","dzTrg","isMatchedToMuon","charge"],
                           embededBranches = ["k_vx","k_vy","k_vz","k_dca_sig","k_dz","kMu_matched","k_charge"],
                           embededCollIdx = "kIdx"
    )
    process.append(K)
    # in case of inf in L_xy/unc produces -99
    CreateVars = branchCreator(
        collection="SkimBToKEE",
        inputBranches=[["l_xy","l_xy_unc"],["l1_vz","l2_vz"],["k_vz","l1_vz","l2_vz"]
                      ,["fit_l1_eta","fit_l1_phi","fit_l2_eta","fit_l2_phi"],
                       ["fit_k_eta","fit_k_phi","fit_l1_eta","fit_l1_phi","fit_l2_eta","fit_l2_phi"]],
        operation=["{0}/{1}","abs({0}-{1})","min(abs({0}-{1}),abs({0}-{2}))",
                   "deltaR({0},{1},{2},{3})",
                   "min( deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))"],
        createdBranches=["l_xy_sig","l1l2Dz","lKDz","l1l2Dr","lKDr"],
    )
    process.append(CreateVars)
    from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper
    # TagVars = functionWrapper(
    #   functionName="TagVars",
    #   collections=["ProbeTracks","Muon","SkimBToKEE"],
    #   createdBranches=["SkimBToKEE_TagMuEtRatio","SkimBToKEE_TagMuDphi","SkimBToKEE_TagMu4Prod","SkimBToKEE_l1_dz","SkimBToKEE_l2_dz","SkimBToKEE_k_dz"],
    #   nCol="nSkimBToKEE"
    # )
    # process.append(TagVars)
    # ClosestTrkVars = functionWrapper(
    #   functionName="ClosestTrkVars",
    #   collections=["ProbeTracks","SkimBToKEE","Electron"],
    #   createdBranches=["SkimBToKEE_l1_trk_mass","SkimBToKEE_l2_trk_mass",
    #                    "SkimBToKEE_trk_minxy1","SkimBToKEE_trk_minxy2",
    #                    "SkimBToKEE_trk_minxy3","SkimBToKEE_trk_mean"],
    #   nCol="nSkimBToKEE"
    # )
    # process.append(ClosestTrkVars)
    D0Vars = functionWrapper(
      functionName="D0Vars",
      collections=["SkimBToKEE"],
      createdBranches=["SkimBToKEE_kl_massKPi"],
      nCol="nSkimBToKEE"
    )
    process.append(D0Vars)
    PAssymVar = functionWrapper(
      functionName="PAssymVar",
      collections=["PV_x","PV_y","PV_z","SkimBToKEE"],
      createdBranches=["SkimBToKEE_p_assymetry"],
      nCol="nSkimBToKEE"
    )
    process.append(PAssymVar)
    return process

def KMuMuMC (process,Jpsi=[],tag=False,trgUnbiased=False,dimuon=False):
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genDecayConstructorPython import genDecayConstructorPython
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genRecoMatcher import genRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.compositeRecoMatcher import compositeRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreatorMC import branchCreatorMC
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genTriggerMuon import genTriggerMuon
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper
  
   path_list=[]
   pt_cut=-1.
   print dimuon
   if dimuon == False:
       path_list=["HLT_Mu9_IP6"]
       pt_cut=8.5
   else:
       path_list=["HLT_DoubleMu4_JpsiTrk_Displaced"]
       pt_cut=4.
   skip_tag=False
   skip_probe=False
   if not tag or trgUnbiased:
     path_list=[]
     pt_cut=None
     skip_tag=True if not trgUnbiased else False
     skip_probe=False

   cuts_on_B = "True"
   cuts_on_B_vars = []
   GenDecay = genDecayConstructorPython( momPdgId = 521,
                                   daughtersPdgId = [13, -13, 321],
                                   outputMomColl = "genB",
                                   intermediateDecay = Jpsi,
                                   trgMuonPtEtaThresholds = [], #best for training - probe/tag side kinematics no trigger eff reduction
                                   selectTrgMuon = False,
                                   excludeTrgMuon = False,
                                   outputDaughterColls = ["genMu1","genMu2","genK"] 
    )                             
   process.append(GenDecay)   
   RecoMu1 = genRecoMatcher( recoInput="Muon",
                             genInput = "genMu1",
                             output = "recoMu1",
                             branches = ["pt","eta","phi","charge","softId","vx","vy","vz","pfRelIso03_all","dxy","dxyErr","mediumId"],
                             addChargeMatching=False,
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoMu1)
   RecoMu2 = genRecoMatcher( recoInput="Muon",
                             genInput = "genMu2",
                             output = "recoMu2",
                             branches = ["pt","eta","phi","charge","softId","vx","vy","vz","pfRelIso03_all","dxy","dxyErr","mediumId"],
                             addChargeMatching=False,
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoMu2)
   #deal with trg muon
   TriggerObj= genTriggerMuon( trgBranch="Muon_isTriggering", 
                               skipNoTrgEvt=False, 
                               skipProbe=False, 
                               skipTag=False, 
                               selectionPathList=path_list,
                               outputColl="trgMu", 
                               recoIdx=["recoMu1_Idx","recoMu2_Idx"], 
                               trgMuMinPt=pt_cut,
                               branches=["pt","eta","phi","dxy","dxyErr"]
   )
   process.append(TriggerObj)
   RecoK = genRecoMatcher( recoInput="ProbeTracks",
                             genInput = "genK",
                             output = "recoK",
                             branches = ["vx","vy","vz","isMatchedToMuon","charge"],
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoK)
   RecoB = compositeRecoMatcher(   compositeColl = "BToKMuMu",
                             lepCompositeIdxs = ["l1Idx","l2Idx"],
                             hadronCompositeIdxs = ["kIdx"],
                             lepMatchedRecoIdxs = ["recoMu1_Idx","recoMu2_Idx"],
                             hadronMatchedRecoIdxs = ["recoK_Idx"],
                             outputColl = "recoB",
                             cuts_vars=cuts_on_B_vars,
                             cuts=cuts_on_B,
                             branches = ["fit_pt","fit_eta","fit_phi",
                                         "fit_mass","mll_fullfit","l_xy",
                                         "l_xy_unc","fit_cos2D","svprob",
                                         "fit_massErr","b_iso04",
                                          "vtx_x","vtx_y","vtx_z",
                                         "l1Idx","l2Idx","kIdx",
                                         "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                         "l1_iso04","n_l1_used",
                                         "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                         "l2_iso04","n_l2_used",
                                         "fit_k_pt","fit_k_eta","fit_k_phi",
                                         "k_iso04","n_k_used"
                                        ],
                             sortTwoLepByIdx=True,
                             lepLabelsToSort = ["l1","l2"]# branches need to have lep labels between "_" eg fit_l1_pt or l1_iso - lep indexes also sorted
   )                                  
   process.append(RecoB)
   # in case of inf in L_xy/unc produces -99
   CreateVars = branchCreatorMC(
      inputBranches=[["recoB_l_xy","recoB_l_xy_unc"],
                     ["recoMu1_vz","recoMu2_vz"],
                     ["recoK_vz","recoMu1_vz","recoMu2_vz"],
                     ["recoB_fit_l1_eta","recoB_fit_l1_phi","recoB_fit_l2_eta","recoB_fit_l2_phi"], 
                     ["recoB_fit_k_eta","recoB_fit_k_phi","recoB_fit_l1_eta","recoB_fit_l1_phi","recoB_fit_l2_eta","recoB_fit_l2_phi"],
                     ["recoMu1_dxy","recoMu1_dxyErr"],
                     ["recoMu2_dxy","recoMu2_dxyErr"]
                   ],
      operation=["{0}/{1}","abs({0}-{1})",
                 "min(abs({0}-{1}),abs({0}-{2}))","deltaR({0},{1},{2},{3})",
                 "min(deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))",
                 "{0}/{1}","{0}/{1}"
                ],
      createdBranches=["recoB_l_xy_sig","recoB_l1l2Dz","recoB_lKDz","recoB_l1l2Dr","recoB_lKDr","recoMu1_dxy_sig","recoMu2_dxy_sig"],
      checkForBCandBranch="recoB_l_xy" #if provided branch puts -99 when branch value is -99. eg Useful for evt where recoK is found but B not
    )
   process.append(CreateVars)
   D0VarsMC = functionWrapper(
     functionName="D0VarsMC",
     collections=["recoMu1_charge","recoB_fit_l1_pt","recoB_fit_l1_eta","recoB_fit_l1_phi","recoMu2_charge","recoB_fit_l2_pt","recoB_fit_l2_eta","recoB_fit_l2_phi","recoK_charge","recoB_fit_k_pt","recoB_fit_k_eta","recoB_fit_k_phi"],
#     collections=["recoB","recoB_Idx","recoMu1_charge","recoMu2_charge","recoK_charge"],
     createdBranches=["recoB_kl_massKPi","recoB_kl_massMuMu"],
   )
   process.append(D0VarsMC)
   FONLL = functionWrapper(
     functionName="FONLL",
     collections=["genB_pt"],
     createdBranches=["FONLL_Weight"],
   )
   process.append(FONLL)
   muon1_mediumID_SF = functionWrapper(
     functionName="muon_mediumID_SF",
     collections=["recoMu1_pt","recoMu1_eta"],
     createdBranches=["recoMu1_mediumID_SF"],
   )
   process.append(muon1_mediumID_SF)
   muon2_mediumID_SF = functionWrapper(
     functionName="muon_mediumID_SF",
     collections=["recoMu2_pt","recoMu2_eta"],
     createdBranches=["recoMu2_mediumID_SF"],
   )
   process.append(muon2_mediumID_SF)

   return process  

def KstarPiMuMuMC (process,Jpsi=[],tag=False,trgUnbiased=False):
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genDecayConstructorPython import genDecayConstructorPython
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genRecoMatcher import genRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.compositeRecoMatcher import compositeRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreatorMC import branchCreatorMC
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genTriggerMuon import genTriggerMuon
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper
  
   path_list=["HLT_Mu9_IP6"]
   pt_cut=8.5
   skip_tag=False
   skip_probe=True
   if not tag or trgUnbiased:
     path_list=[]
     pt_cut=None
     skip_tag=True if not trgUnbiased else False
     skip_probe=False

   cuts_on_B = "True"
   cuts_on_B_vars = []
   GenDecay = genDecayConstructorPython( momPdgId = 511,
                                   daughtersPdgId = [13, -13, 321,-211],
                                   outputMomColl = "genB",
                                   intermediateDecay = Jpsi,
                                   trgMuonPtEtaThresholds = [], #best for training - probe/tag side kinematics no trigger eff reduction
                                   selectTrgMuon = False,
                                   excludeTrgMuon = False,
                                   outputDaughterColls = ["genMu1","genMu2","genK","genPi"] 
    )                             
   process.append(GenDecay)   
   RecoMu1 = genRecoMatcher( recoInput="Muon",
                             genInput = "genMu1",
                             output = "recoMu1",
                             branches = ["pt","eta","phi","charge","softId","vx","vy","vz","pfRelIso03_all","dxy","dxyErr","mediumId"],
                             addChargeMatching=False,
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoMu1)
   RecoMu2 = genRecoMatcher( recoInput="Muon",
                             genInput = "genMu2",
                             output = "recoMu2",
                             branches = ["pt","eta","phi","charge","softId","vx","vy","vz","pfRelIso03_all","dxy","dxyErr","mediumId"],
                             addChargeMatching=False,
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoMu2)
   #deal with trg muon
   TriggerObj= genTriggerMuon( trgBranch="Muon_isTriggering", 
                               skipNoTrgEvt=False, 
                               skipProbe=False, 
                               skipTag=False, 
                               selectionPathList=path_list,
                               outputColl="trgMu", 
                               recoIdx=["recoMu1_Idx","recoMu2_Idx"], 
                               trgMuMinPt=pt_cut,
                               branches=["pt","eta","phi","dxy","dxyErr"]
   )
   process.append(TriggerObj)
   RecoPi = genRecoMatcher( recoInput="ProbeTracks",
                             genInput = "genPi",
                             output = "recoK",
                             branches = ["vx","vy","vz","isMatchedToMuon","charge"],
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoPi)
   RecoB = compositeRecoMatcher(   compositeColl = "BToKMuMu",
                             lepCompositeIdxs = ["l1Idx","l2Idx"],
                             hadronCompositeIdxs = ["kIdx"],
                             lepMatchedRecoIdxs = ["recoMu1_Idx","recoMu2_Idx"],
                             hadronMatchedRecoIdxs = ["recoK_Idx"],
                             outputColl = "recoB",
                             cuts_vars=cuts_on_B_vars,
                             cuts=cuts_on_B,
                             branches = [
                                        "fit_pt","fit_eta","fit_phi",
                                         "fit_mass","mll_fullfit","l_xy",
                                         "l_xy_unc","fit_cos2D","svprob",
                                         "fit_massErr","b_iso04",
                                          "vtx_x","vtx_y","vtx_z",
                                         "l1Idx","l2Idx","kIdx",
                                         "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                         "l1_iso04","n_l1_used",
                                         "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                         "l2_iso04","n_l2_used",
                                         "fit_k_pt","fit_k_eta","fit_k_phi",
                                         "k_iso04","n_k_used"
                                        ],
                             sortTwoLepByIdx=True,
                             lepLabelsToSort = ["l1","l2"]# branches need to have lep labels between "_" eg fit_l1_pt or l1_iso - lep indexes also sorted
   )                                  
   process.append(RecoB)
   # in case of inf in L_xy/unc produces -99
   CreateVars = branchCreatorMC(
      inputBranches=[["recoB_l_xy","recoB_l_xy_unc"],
                     ["recoMu1_vz","recoMu2_vz"],
                     ["recoK_vz","recoMu1_vz","recoMu2_vz"],
                     ["recoB_fit_l1_eta","recoB_fit_l1_phi","recoB_fit_l2_eta","recoB_fit_l2_phi"], 
                     ["recoB_fit_k_eta","recoB_fit_k_phi","recoB_fit_l1_eta","recoB_fit_l1_phi","recoB_fit_l2_eta","recoB_fit_l2_phi"],
                     ["recoMu1_dxy","recoMu1_dxyErr"],
                     ["recoMu2_dxy","recoMu2_dxyErr"]
                   ],
      operation=["{0}/{1}","abs({0}-{1})",
                 "min(abs({0}-{1}),abs({0}-{2}))","deltaR({0},{1},{2},{3})",
                 "min(deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))",
                 "{0}/{1}","{0}/{1}"
                ],
      createdBranches=["recoB_l_xy_sig","recoB_l1l2Dz","recoB_lKDz","recoB_l1l2Dr","recoB_lKDr","recoMu1_dxy_sig","recoMu2_dxy_sig"],
      checkForBCandBranch="recoB_l_xy" #if provided branch puts -99 when branch value is -99. eg Useful for evt where recoK is found but B not
    )
   process.append(CreateVars)
   D0VarsMC = functionWrapper(
     functionName="D0VarsMC",
     collections=["recoMu1_charge","recoB_fit_l1_pt","recoB_fit_l1_eta","recoB_fit_l1_phi","recoMu2_charge","recoB_fit_l2_pt","recoB_fit_l2_eta","recoB_fit_l2_phi","recoK_charge","recoB_fit_k_pt","recoB_fit_k_eta","recoB_fit_k_phi"],
#     collections=["recoB","recoB_Idx","recoMu1_charge","recoMu2_charge","recoK_charge"],
     createdBranches=["recoB_kl_massKPi","recoB_kl_massMuMu"],
   )
   process.append(D0VarsMC)
   FONLL = functionWrapper(
     functionName="FONLL",
     collections=["genB_pt"],
     createdBranches=["FONLL_Weight"],
   )
   process.append(FONLL)
   muon1_mediumID_SF = functionWrapper(
     functionName="muon_mediumID_SF",
     collections=["recoMu1_pt","recoMu1_eta"],
     createdBranches=["recoMu1_mediumID_SF"],
   )
   process.append(muon1_mediumID_SF)
   muon2_mediumID_SF = functionWrapper(
     functionName="muon_mediumID_SF",
     collections=["recoMu2_pt","recoMu2_eta"],
     createdBranches=["recoMu2_mediumID_SF"],
   )
   process.append(muon2_mediumID_SF)
 
   return process  


def KstarKMuMuMC (process,Jpsi=[],tag=False,trgUnbiased=False):
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genDecayConstructorPython import genDecayConstructorPython
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genRecoMatcher import genRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.compositeRecoMatcher import compositeRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreatorMC import branchCreatorMC
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genTriggerMuon import genTriggerMuon
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper
  
   path_list=["HLT_Mu9_IP6"]
   pt_cut=8.5
   skip_tag=False
   skip_probe=True
   if not tag or trgUnbiased:
     path_list=[]
     pt_cut=None
     skip_tag=True if not trgUnbiased else False
     skip_probe=False

   cuts_on_B = "True"
   cuts_on_B_vars = []
   GenDecay = genDecayConstructorPython( momPdgId = 511,
                                   daughtersPdgId = [13, -13, 321,-211],
                                   outputMomColl = "genB",
                                   intermediateDecay = Jpsi,
                                   trgMuonPtEtaThresholds = [], #best for training - probe/tag side kinematics no trigger eff reduction
                                   selectTrgMuon = False,
                                   excludeTrgMuon = False,
                                   outputDaughterColls = ["genMu1","genMu2","genK","genPi"] 
    )                             
   process.append(GenDecay)   
   RecoMu1 = genRecoMatcher( recoInput="Muon",
                             genInput = "genMu1",
                             output = "recoMu1",
                             branches = ["pt","eta","phi","charge","softId","vx","vy","vz","pfRelIso03_all","dxy","dxyErr","mediumId"],
                             addChargeMatching=False,
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoMu1)
   RecoMu2 = genRecoMatcher( recoInput="Muon",
                             genInput = "genMu2",
                             output = "recoMu2",
                             branches = ["pt","eta","phi","charge","softId","vx","vy","vz","pfRelIso03_all","dxy","dxyErr","mediumId"],
                             addChargeMatching=False,
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoMu2)
   #deal with trg muon
   TriggerObj= genTriggerMuon( trgBranch="Muon_isTriggering", 
                               skipNoTrgEvt=False, 
                               skipProbe=False, 
                               skipTag=False, 
                               selectionPathList=path_list,
                               outputColl="trgMu", 
                               recoIdx=["recoMu1_Idx","recoMu2_Idx"], 
                               trgMuMinPt=pt_cut,
                               branches=["pt","eta","phi","dxy","dxyErr"]
   )
   process.append(TriggerObj)
   RecoK = genRecoMatcher( recoInput="ProbeTracks",
                             genInput = "genK",
                             output = "recoK",
                             branches = ["vx","vy","vz","isMatchedToMuon","charge"],
                             skipNotMatched=False,
                             DRcut=0.1
   )                             
   process.append(RecoK)
   RecoB = compositeRecoMatcher(   compositeColl = "BToKMuMu",
                             lepCompositeIdxs = ["l1Idx","l2Idx"],
                             hadronCompositeIdxs = ["kIdx"],
                             lepMatchedRecoIdxs = ["recoMu1_Idx","recoMu2_Idx"],
                             hadronMatchedRecoIdxs = ["recoK_Idx"],
                             outputColl = "recoB",
                             cuts_vars=cuts_on_B_vars,
                             cuts=cuts_on_B,
                             branches = [
                                         "fit_pt","fit_eta","fit_phi",
                                         "fit_mass","mll_fullfit","l_xy",
                                         "l_xy_unc","fit_cos2D","svprob",
                                         "fit_massErr","b_iso04",
                                          "vtx_x","vtx_y","vtx_z",
                                         "l1Idx","l2Idx","kIdx",
                                         "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                         "l1_iso04","n_l1_used",
                                         "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                         "l2_iso04","n_l2_used",
                                         "fit_k_pt","fit_k_eta","fit_k_phi",
                                         "k_iso04","n_k_used"
                                        ],
                             sortTwoLepByIdx=True,
                             lepLabelsToSort = ["l1","l2"]# branches need to have lep labels between "_" eg fit_l1_pt or l1_iso - lep indexes also sorted
   )                                  
   process.append(RecoB)
   # in case of inf in L_xy/unc produces -99
   CreateVars = branchCreatorMC(
      inputBranches=[["recoB_l_xy","recoB_l_xy_unc"],
                     ["recoMu1_vz","recoMu2_vz"],
                     ["recoK_vz","recoMu1_vz","recoMu2_vz"],
                     ["recoB_fit_l1_eta","recoB_fit_l1_phi","recoB_fit_l2_eta","recoB_fit_l2_phi"], 
                     ["recoB_fit_k_eta","recoB_fit_k_phi","recoB_fit_l1_eta","recoB_fit_l1_phi","recoB_fit_l2_eta","recoB_fit_l2_phi"],
                     ["recoMu1_dxy","recoMu1_dxyErr"],
                     ["recoMu2_dxy","recoMu2_dxyErr"]                
                   ],
      operation=["{0}/{1}","abs({0}-{1})",
                 "min(abs({0}-{1}),abs({0}-{2}))","deltaR({0},{1},{2},{3})",
                 "min(deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))",
                 "{0}/{1}","{0}/{1}"
                ],
      createdBranches=["recoB_l_xy_sig","recoB_l1l2Dz","recoB_lKDz","recoB_l1l2Dr","recoB_lKDr","recoMu1_dxy_sig","recoMu2_dxy_sig"],
      checkForBCandBranch="recoB_l_xy" #if provided branch puts -99 when branch value is -99. eg Useful for evt where recoK is found but B not
    )
   process.append(CreateVars)
   D0VarsMC = functionWrapper(
     functionName="D0VarsMC",
     collections=["recoMu1_charge","recoB_fit_l1_pt","recoB_fit_l1_eta","recoB_fit_l1_phi","recoMu2_charge","recoB_fit_l2_pt","recoB_fit_l2_eta","recoB_fit_l2_phi","recoK_charge","recoB_fit_k_pt","recoB_fit_k_eta","recoB_fit_k_phi"],
#     collections=["recoB","recoB_Idx","recoMu1_charge","recoMu2_charge","recoK_charge"],
     createdBranches=["recoB_kl_massKPi","recoB_kl_massMuMu"],
   )
   process.append(D0VarsMC)
   FONLL = functionWrapper(
     functionName="FONLL",
     collections=["genB_pt"],
     createdBranches=["FONLL_Weight"],
   )
   process.append(FONLL)
   muon1_mediumID_SF = functionWrapper(
     functionName="muon_mediumID_SF",
     collections=["recoMu1_pt","recoMu1_eta"],
     createdBranches=["recoMu1_mediumID_SF"],
   )
   process.append(muon1_mediumID_SF)
   muon2_mediumID_SF = functionWrapper(
     functionName="muon_mediumID_SF",
     collections=["recoMu2_pt","recoMu2_eta"],
     createdBranches=["recoMu2_mediumID_SF"],
   )
   process.append(muon2_mediumID_SF)
   return process  




def KEEMC (process,Jpsi=[],use_PF=False,use_1lowPt_1PF=False):
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genDecayConstructorPython import genDecayConstructorPython
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genRecoMatcher import genRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.compositeRecoMatcher import compositeRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreatorMC import branchCreatorMC

   cuts_on_lep = lambda l: True
   cuts_on_B = "True"
   cuts_on_B_vars = []
   if use_PF and not use_1lowPt_1PF:
     cuts_on_lep= lambda l: l.isPF == 1 and l.pfmvaId>-5000
     cuts_on_B_vars = ["recoE1_pfmvaId","recoE2_pfmvaId"]
     cuts_on_B = cuts_on_B+" and ( {0}>-300.5 or {1}>-300.5 )"
   elif use_1lowPt_1PF and not use_PF:
     cuts_on_lep= lambda l: ( (l.isPF == 1 and l.pfmvaId>-20.0) or ( l.isPF == 0 and l.isPFoverlap==0 and l.mvaId>-20.0) )
     cuts_on_B_vars = ["recoE1_isPF","recoE2_isPF"]
     cuts_on_B = cuts_on_B+" and ( ({0}==1 and {1}==0) or  ( {0}==0 and {1}==1) )"
   
   GenDecay = genDecayConstructorPython( momPdgId = 521,
                                   daughtersPdgId = [11, -11, 321],
                                   outputMomColl = "genB",
                                   intermediateDecay = Jpsi,
                                   trgMuonPtEtaThresholds = [], #was 7,1.6
                                   outputDaughterColls = ["genE1","genE2","genK"] 
    )                             
   process.append(GenDecay)   
   RecoE1 = genRecoMatcher( recoInput="Electron",
                             genInput = "genE1",
                             output = "recoE1",
                             branches = ["pt","eta","phi","vx","vy","vz","isPF","pfmvaId","isPFoverlap","mvaId","charge","LooseID","MediumID","TightID","convVeto"],
                             cuts=cuts_on_lep,
                             skipNotMatched=False
   )                             
   process.append(RecoE1)
   RecoE2 = genRecoMatcher( recoInput="Electron",
                             genInput = "genE2",
                             output = "recoE2",
                             branches = ["pt","eta","phi","vx","vy","vz","isPF","pfmvaId","isPFoverlap","mvaId","charge","LooseID","MediumID","TightID","convVeto"],
                             cuts=cuts_on_lep,
                             skipNotMatched=False
   )                             
   process.append(RecoE2)
   RecoK = genRecoMatcher( recoInput="ProbeTracks",
                             genInput = "genK",
                             output = "recoK",
                             branches = ["pt","eta","phi","vx","vy","vz","DCASig","dzTrg","isMatchedToMuon","charge"],
                             skipNotMatched=False
   )                             
   process.append(RecoK)
   RecoB = compositeRecoMatcher(   compositeColl = "BToKEE",
                             lepCompositeIdxs = ["l1Idx","l2Idx"],
                             hadronCompositeIdxs = ["kIdx"],
                             lepMatchedRecoIdxs = ["recoE1_Idx","recoE2_Idx"],
                             hadronMatchedRecoIdxs = ["recoK_Idx"],
                             outputColl = "recoB",
                             cuts_vars=cuts_on_B_vars,
                             cuts=cuts_on_B,
                             branches =["fit_pt","fit_eta","fit_phi","fit_mass",
                                         "l_xy","l_xy_unc","fit_cos2D","svprob",
                                         "fit_massErr","b_iso04", "mll_fullfit",
                                         "l1Idx","l2Idx","kIdx",
                                         "vtx_x","vtx_y","vtx_z",
                                         "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                         "l1_iso04",
                                         "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                         "l2_iso04",
                                         "fit_k_pt","fit_k_eta","fit_k_phi",
                                         "k_iso04",
                                         "b_iso04_dca","l1_iso04_dca",
                                         "l2_iso04_dca","k_iso04_dca",
                                         "k_svip3d","k_svip3d_err",
                                        "l1_n_isotrk_dca","l2_n_isotrk_dca",
                                        "k_n_isotrk_dca"
                                        ],
                             sortTwoLepByIdx=True,
                             lepLabelsToSort = ["l1","l2"]# branches need to have lep labels between "_" eg fit_l1_pt or l1_iso - lep indexes also sorted
   )                                  
   process.append(RecoB)
   # in case of inf in L_xy/unc produces -99
   CreateVars = branchCreatorMC(
      inputBranches=[["recoB_l_xy","recoB_l_xy_unc"], ["recoE1_vz","recoE2_vz"],
                     ["recoK_vz","recoE1_vz","recoE2_vz"], 
                     ["recoE1_eta","recoE1_phi","recoE2_eta","recoE2_phi"], 
                     ["recoK_eta","recoK_phi","recoE1_eta","recoE1_phi","recoE2_eta","recoE2_phi"] ],
      operation=["{0}/{1}","abs({0}-{1})",
                 "min(abs({0}-{1}),abs({0}-{2}))",
                 "deltaR({0},{1},{2},{3})",
                 "min(deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))"],
      createdBranches=["recoB_l_xy_sig","recoB_l1l2Dz","recoB_lKDz","recoB_l1l2Dr","recoB_lKDr"],
      checkForBCandBranch="recoB_l_xy" #if provided branch puts -99 when branch value is -99. eg Useful for evt where recoK is found but
    )
   process.append(CreateVars)
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper
  #  TagVars = functionWrapper(
  #     functionName="TagVarsMC",
  #     collections=["ProbeTracks","Muon","recoB_fit_pt","recoB_fit_eta","recoB_fit_phi","recoB_fit_mass","recoE1_vz","recoE2_vz","recoK_vz"],
  #     createdBranches=["recoB_TagMuEtRatio","recoB_TagMuDphi","recoB_TagMu4Prod","recoB_l1_dz","recoB_l2_dz","recoB_k_dz"],
  #   )
  #  process.append(TagVars)
  #  ClosestTrkVars = functionWrapper(
  #    functionName="ClosestTrkVarsMC",
  #    collections=["ProbeTracks","BToKEE","recoB_Idx","Electron","recoB_l1Idx","recoB_l2Idx"],
  #    createdBranches=["recoB_l1_trk_mass","recoB_l2_trk_mass","recoB_trk_minxy1","recoB_trk_minxy2","recoB_trk_minxy3","recoB_trk_mean"],
  #   )
  #  process.append(ClosestTrkVars)
   D0Vars = functionWrapper(
     functionName="D0VarsMC",
     collections=["BToKEE","recoE1_charge","recoE2_charge","recoK_charge","recoB_Idx"],
     createdBranches=["recoB_k_opp_l_mass"]
   )
   process.append(D0Vars)
   PAssymVar = functionWrapper(
     functionName="PAssymVarMC",
     collections=["PV_x","PV_y","PV_z","BToKEE","recoB_Idx"],
     createdBranches=["recoB_p_assymetry"]

   )
   process.append(PAssymVar)

   return process  


def KstarPiEEMC (process,Jpsi=[],use_PF=False,use_1lowPt_1PF=False):
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genDecayConstructorPython import genDecayConstructorPython
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genRecoMatcher import genRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.compositeRecoMatcher import compositeRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreatorMC import branchCreatorMC

   cuts_on_lep = lambda l: True
   cuts_on_B = "True"
   cuts_on_B_vars = []
   if use_PF and not use_1lowPt_1PF:
     cuts_on_lep= lambda l: l.isPF == 1 and l.pfmvaId>-5000
     cuts_on_B_vars = ["recoE1_pfmvaId","recoE2_pfmvaId"]
     cuts_on_B = cuts_on_B+" and ( {0}>-300.5 or {1}>-300.5 )"
   elif use_1lowPt_1PF and not use_PF:
     cuts_on_lep= lambda l: ( (l.isPF == 1 and l.pfmvaId>-20.0) or ( l.isPF == 0 and l.isPFoverlap==0 and l.mvaId>-20.0) )
     cuts_on_B_vars = ["recoE1_isPF","recoE2_isPF"]
     cuts_on_B = cuts_on_B+" and ( ({0}==1 and {1}==0) or  ( {0}==0 and {1}==1) )"
   
   GenDecay = genDecayConstructorPython( momPdgId = 511,
                                   daughtersPdgId = [11, -11, 321,-211],
                                   outputMomColl = "genB",
                                   intermediateDecay = Jpsi,
                                   trgMuonPtEtaThresholds = [], #was 7,1.6
                                   outputDaughterColls = ["genE1","genE2","genK","genPi"] 
    )                             
   process.append(GenDecay)   
   RecoE1 = genRecoMatcher( recoInput="Electron",
                             genInput = "genE1",
                             output = "recoE1",
                             branches = ["pt","eta","phi","vx","vy","vz","isPF","pfmvaId","isPFoverlap","mvaId","charge"],
                             cuts=cuts_on_lep,
                             skipNotMatched=False
   )                             
   process.append(RecoE1)
   RecoE2 = genRecoMatcher( recoInput="Electron",
                             genInput = "genE2",
                             output = "recoE2",
                             branches = ["pt","eta","phi","vx","vy","vz","isPF","pfmvaId","isPFoverlap","mvaId","charge"],
                             cuts=cuts_on_lep,
                             skipNotMatched=False
   )                             
   process.append(RecoE2)
   RecoPi = genRecoMatcher( recoInput="ProbeTracks",
                             genInput = "genPi",
                             output = "recoK",
                             branches = ["pt","eta","phi","vx","vy","vz","DCASig","dzTrg","isMatchedToMuon","charge"],
                             skipNotMatched=False
   )
   process.append(RecoPi)
   RecoB = compositeRecoMatcher(   compositeColl = "BToKEE",
                             lepCompositeIdxs = ["l1Idx","l2Idx"],
                             hadronCompositeIdxs = ["kIdx"],
                             lepMatchedRecoIdxs = ["recoE1_Idx","recoE2_Idx"],
                             hadronMatchedRecoIdxs = ["recoK_Idx"],
                             outputColl = "recoB",
                             cuts_vars=cuts_on_B_vars,
                             cuts=cuts_on_B,
                             branches =["fit_pt","fit_eta","fit_phi","fit_mass",
                                         "l_xy","l_xy_unc","fit_cos2D","svprob",
                                         "fit_massErr","b_iso04", "mll_fullfit",
                                         "l1Idx","l2Idx","kIdx",
                                         "vtx_x","vtx_y","vtx_z",
                                         "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                         "l1_iso04",
                                         "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                         "l2_iso04",
                                         "fit_k_pt","fit_k_eta","fit_k_phi",
                                         "k_iso04",
                                         "b_iso04_dca","l1_iso04_dca",
                                         "l2_iso04_dca","k_iso04_dca",
                                         "k_svip3d","k_svip3d_err",
                                         "l1_n_isotrk_dca","l2_n_isotrk_dca",
                                        "k_n_isotrk_dca"
                                        ],
                             sortTwoLepByIdx=True,
                             lepLabelsToSort = ["l1","l2"]# branches need to have lep labels between "_" eg fit_l1_pt or l1_iso - lep indexes also sorted
   )                                  
   process.append(RecoB)
   # in case of inf in L_xy/unc produces -99
   CreateVars = branchCreatorMC(
      inputBranches=[["recoB_l_xy","recoB_l_xy_unc"], ["recoE1_vz","recoE2_vz"],
                     ["recoK_vz","recoE1_vz","recoE2_vz"], 
                     ["recoE1_eta","recoE1_phi","recoE2_eta","recoE2_phi"], 
                     ["recoK_eta","recoK_phi","recoE1_eta","recoE1_phi","recoE2_eta","recoE2_phi"] ],
      operation=["{0}/{1}","abs({0}-{1})",
                 "min(abs({0}-{1}),abs({0}-{2}))",
                 "deltaR({0},{1},{2},{3})",
                 "min(deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))"],
      createdBranches=["recoB_l_xy_sig","recoB_l1l2Dz","recoB_lKDz","recoB_l1l2Dr","recoB_lKDr"],
      checkForBCandBranch="recoB_l_xy" #if provided branch puts -99 when branch value is -99. eg Useful for evt where recoK is found but
    )
   process.append(CreateVars)
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper
   TagVars = functionWrapper(
      functionName="TagVarsMC",
      collections=["ProbeTracks","Muon","recoB_fit_pt","recoB_fit_eta","recoB_fit_phi","recoB_fit_mass","recoE1_vz","recoE2_vz","recoK_vz"],
      createdBranches=["recoB_TagMuEtRatio","recoB_TagMuDphi","recoB_TagMu4Prod","recoB_l1_dz","recoB_l2_dz","recoB_k_dz"],
    )
   process.append(TagVars)
   ClosestTrkVars = functionWrapper(
      functionName="ClosestTrkVarsMC",
      collections=["ProbeTracks","BToKEE","recoB_Idx","Electron","recoB_l1Idx","recoB_l2Idx"],
      createdBranches=["recoB_l1_trk_mass","recoB_l2_trk_mass","recoB_trk_minxy1","recoB_trk_minxy2","recoB_trk_minxy3","recoB_trk_mean"],
   )
   process.append(ClosestTrkVars)
   D0Vars = functionWrapper(
     functionName="D0VarsMC",
     collections=["Muon","BToKEE","recoB_Idx","recoE1_charge","recoE2_charge","recoK_charge"],
     createdBranches=["recoB_k_opp_l_mass","recoB_k_mu_d0_mass","recoB_k_mu_jpsi_mass"]

   )
   process.append(D0Vars)
   PAssymVar = functionWrapper(
     functionName="PAssymVarMC",
     collections=["PV_x","PV_y","PV_z","BToKEE","recoB_Idx"],
     createdBranches=["recoB_p_assymetry"]

   )
   process.append(PAssymVar)
   return process  


def KstarKEEMC (process,Jpsi=[],use_PF=False,use_1lowPt_1PF=False):
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genDecayConstructorPython import genDecayConstructorPython
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.genRecoMatcher import genRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.compositeRecoMatcher import compositeRecoMatcher
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.branchCreatorMC import branchCreatorMC

   cuts_on_lep = lambda l: True
   cuts_on_B = "True"
   cuts_on_B_vars = []
   if use_PF and not use_1lowPt_1PF:
     cuts_on_lep= lambda l: l.isPF == 1 and l.pfmvaId>-5000
     cuts_on_B_vars = ["recoE1_pfmvaId","recoE2_pfmvaId"]
     cuts_on_B = cuts_on_B+" and ( {0}>-300.5 or {1}>-300.5 )"
   elif use_1lowPt_1PF and not use_PF:
     cuts_on_lep= lambda l: ( (l.isPF == 1 and l.pfmvaId>-20.0) or ( l.isPF == 0 and l.isPFoverlap==0 and l.mvaId>-20.0) )
     cuts_on_B_vars = ["recoE1_isPF","recoE2_isPF"]
     cuts_on_B = cuts_on_B+" and ( ({0}==1 and {1}==0) or  ( {0}==0 and {1}==1) )"
   
   GenDecay = genDecayConstructorPython( momPdgId = 511,
                                   daughtersPdgId = [11, -11, 321,-211],
                                   outputMomColl = "genB",
                                   intermediateDecay = Jpsi,
                                   trgMuonPtEtaThresholds = [], #was 7,1.6
                                   outputDaughterColls = ["genE1","genE2","genK","genPi"] 
    )                             
   process.append(GenDecay)   
   RecoE1 = genRecoMatcher( recoInput="Electron",
                             genInput = "genE1",
                             output = "recoE1",
                             branches = ["pt","eta","phi","vx","vy","vz","isPF","pfmvaId","isPFoverlap","mvaId","charge"],
                             cuts=cuts_on_lep,
                             skipNotMatched=False
   )                             
   process.append(RecoE1)
   RecoE2 = genRecoMatcher( recoInput="Electron",
                             genInput = "genE2",
                             output = "recoE2",
                             branches = ["pt","eta","phi","vx","vy","vz","isPF","pfmvaId","isPFoverlap","mvaId","charge"],
                             cuts=cuts_on_lep,
                             skipNotMatched=False
   )                             
   process.append(RecoE2)
   RecoK = genRecoMatcher( recoInput="ProbeTracks",
                             genInput = "genK",
                             output = "recoK",
                             branches = ["pt","eta","phi","vx","vy","vz","DCASig","dzTrg","isMatchedToMuon","charge"],
                             skipNotMatched=False
   )                             
   process.append(RecoK)
   RecoB = compositeRecoMatcher(   compositeColl = "BToKEE",
                             lepCompositeIdxs = ["l1Idx","l2Idx"],
                             hadronCompositeIdxs = ["kIdx"],
                             lepMatchedRecoIdxs = ["recoE1_Idx","recoE2_Idx"],
                             hadronMatchedRecoIdxs = ["recoK_Idx"],
                             outputColl = "recoB",
                             cuts_vars=cuts_on_B_vars,
                             cuts=cuts_on_B,
                             branches =["fit_pt","fit_eta","fit_phi","fit_mass",
                                         "l_xy","l_xy_unc","fit_cos2D","svprob",
                                         "fit_massErr","b_iso04", "mll_fullfit",
                                         "l1Idx","l2Idx","kIdx",
                                         "vtx_x","vtx_y","vtx_z",
                                         "fit_l1_pt","fit_l1_eta","fit_l1_phi",
                                         "l1_iso04",
                                         "fit_l2_pt","fit_l2_eta","fit_l2_phi",
                                         "l2_iso04",
                                         "fit_k_pt","fit_k_eta","fit_k_phi",
                                         "k_iso04",
                                         "b_iso04_dca","l1_iso04_dca",
                                         "l2_iso04_dca","k_iso04_dca",
                                         "k_svip3d","k_svip3d_err",
                                        "l1_n_isotrk_dca","l2_n_isotrk_dca",
                                        "k_n_isotrk_dca"
                                        ],
                             sortTwoLepByIdx=True,
                             lepLabelsToSort = ["l1","l2"]# branches need to have lep labels between "_" eg fit_l1_pt or l1_iso - lep indexes also sorted
   )                                  
   process.append(RecoB)
   # in case of inf in L_xy/unc produces -99
   CreateVars = branchCreatorMC(
      inputBranches=[["recoB_l_xy","recoB_l_xy_unc"], ["recoE1_vz","recoE2_vz"],
                     ["recoK_vz","recoE1_vz","recoE2_vz"], 
                     ["recoE1_eta","recoE1_phi","recoE2_eta","recoE2_phi"], 
                     ["recoK_eta","recoK_phi","recoE1_eta","recoE1_phi","recoE2_eta","recoE2_phi"] ],
      operation=["{0}/{1}","abs({0}-{1})",
                 "min(abs({0}-{1}),abs({0}-{2}))",
                 "deltaR({0},{1},{2},{3})",
                 "min(deltaR({0},{1},{2},{3}),deltaR({0},{1},{4},{5}))"],
      createdBranches=["recoB_l_xy_sig","recoB_l1l2Dz","recoB_lKDz","recoB_l1l2Dr","recoB_lKDr"],
      checkForBCandBranch="recoB_l_xy" #if provided branch puts -99 when branch value is -99. eg Useful for evt where recoK is found but
    )
   process.append(CreateVars)
   from PhysicsTools.NanoAODTools.postprocessing.modules.bpark.functionWrapper import functionWrapper
   TagVars = functionWrapper(
      functionName="TagVarsMC",
      collections=["ProbeTracks","Muon","recoB_fit_pt","recoB_fit_eta","recoB_fit_phi","recoB_fit_mass","recoE1_vz","recoE2_vz","recoK_vz"],
      createdBranches=["recoB_TagMuEtRatio","recoB_TagMuDphi","recoB_TagMu4Prod","recoB_l1_dz","recoB_l2_dz","recoB_k_dz"],
    )
   process.append(TagVars)
   ClosestTrkVars = functionWrapper(
      functionName="ClosestTrkVarsMC",
      collections=["ProbeTracks","BToKEE","recoB_Idx","Electron","recoB_l1Idx","recoB_l2Idx"],
      createdBranches=["recoB_l1_trk_mass","recoB_l2_trk_mass","recoB_trk_minxy1","recoB_trk_minxy2","recoB_trk_minxy3","recoB_trk_mean"],
   )
   process.append(ClosestTrkVars)
   D0Vars = functionWrapper(
     functionName="D0VarsMC",
     collections=["Muon","BToKEE","recoB_Idx","recoE1_charge","recoE2_charge","recoK_charge"],
     createdBranches=["recoB_k_opp_l_mass","recoB_k_mu_d0_mass","recoB_k_mu_jpsi_mass"]

   )
   process.append(D0Vars)
   PAssymVar = functionWrapper(
     functionName="PAssymVarMC",
     collections=["PV_x","PV_y","PV_z","BToKEE","recoB_Idx"],
     createdBranches=["recoB_p_assymetry"]

   )
   process.append(PAssymVar)
  


   return process  



