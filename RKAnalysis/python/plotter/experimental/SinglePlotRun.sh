python plotter.py -p plots_kee_MC_MCDataStudy.txt -i mca_PFeKee_MC_MCDataStudy.txt -o eek_MC_MCData -f

python plotter.py -p plots_kee_Data_MCDataStudy.txt -i mca_PFeKee_Data_MCDataStudy.txt -o eek_Data_MCData -f

wait

python operatePlots.py -i eek_Data_MCData --histo1Names *sgnbkg --histo2Names *bkg --histo2ScaleYield 26757 --operationSymbol - --ext _sgn

wait

python combinePlots.py -i eek_Data_MCData/Operated eek_MC_MCData -p all -l Data MC --two-plot-ratio -c Norm -o eek_MCData
