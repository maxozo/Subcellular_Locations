""" This script loops throught every human gene and retrieves a GO terms for each of them""";
import httplib2
import time

f = open('Proteome_GO_Terms.csv', 'w')
date_and_time=time.strftime("%c");
f.write('###Go term extraction date and time: '+str(date_and_time)+'###\n')


with open('/home/mbchpmo2/Documents/Domain_Software_exe2/bin/uniprot-all.list') as f:
    Human_Proteome = f.read().splitlines()

f = open('Proteome_GO_Terms.csv', 'a')
count=0;
for element in Human_Proteome:
    print count
    count=count+1;
    String_extract = 'http://www.ebi.ac.uk/QuickGO/GAnnotation?protein='+element+'&format=tsv&col=goID'
    Anotations_extract = 'http://www.ebi.ac.uk/QuickGO/GAnnotation?protein=' + element + '&format=tsv&col=proteinID,proteinSymbol'

    """anotation extraction"""
    resp1, anotation = httplib2.Http().request(Anotations_extract)
    a1 = anotation.split('\n')
    a1 = a1[1]
    anotation = a1.replace("\t", ",")

    """GO term extraction"""
    resp, content = httplib2.Http().request(String_extract)
    g = content.split('\t'); g=g[0]; g = g.split('\n'); g.pop(0)
    myset = set(g)
    g = ";".join(myset)
    Go_Term = g[1:]

    Protein_total_GO_String = anotation+','+Go_Term
    if len(Protein_total_GO_String)>1:
        print anotation
        f.write(Protein_total_GO_String+'\n')

f.close()

