import pandas as pd
fO = open("Sustained_Threat.csv", 'w')
data = pd.read_csv("Sustained_Threat_sentences.csv")
#print(data)
#idx = data.groupby(['pmid'])['predictions'].transform(max).head(2)
#== data['predictions']
#print(data[idx])
#data[idx].to_csv(fO, sep=',', encoding='utf-8')
g = data.groupby(["pmid"]).apply(lambda x: x.sort_values(["predictions"], ascending = False)).reset_index(drop=True)
f = g.groupby('pmid').head(2)
f.to_csv(fO, sep=',', encoding='utf-8')