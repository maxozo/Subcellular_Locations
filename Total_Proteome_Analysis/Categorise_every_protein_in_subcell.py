import pandas as pd

GO_IDs = pd.read_csv('/home/mbchpmo2/Documents/Domain_Software_exe2/Total_Proteome_Analysis/Proteome_GO_Terms.csv', skiprows=[0], index_col=False)
file = open("Subcellular_location_final.csv", "w")

for number in range(0, len(GO_IDs)):
    gene=GO_IDs.iloc[number,1]
    go_terms =GO_IDs.iloc[number,2]
    GeneGo = go_terms.split(';')
    print GeneGo
    if 'GO:0022627' in GeneGo or 'GO:0016363' in GeneGo or 'GO:0005882' in GeneGo:
        file.write(str(gene) + ',intracellular\n')
        print str(gene)+' intracellular'
    elif 'GO:0044420' in GeneGo or 'GO:0031012' in GeneGo or 'GO:0005578' in GeneGo or 'GO:1990377' in GeneGo:
        file.write(str(gene)+',ECM\n')
        print str(gene)+' ECM '
    elif 'GO:0005576' in GeneGo or 'GO:0044421' in GeneGo:
        file.write(str(gene)+',extracellular\n')
        print str(gene)+' extracellular'
    else:
        file.write(str(gene) + ',intracellular\n')
        print str(gene)+' intracellular'

file.close()




