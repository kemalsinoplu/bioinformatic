import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt



mirbase = pd.read_excel('miRTarBase.xlsx')
trrust = pd.read_excel('trrust_rawdata_human.xlsx')

combined_data = pd.concat([mirbase, trrust])
#combined_data.to_excel('output.xlsx', index=False)

G = nx.Graph()

for index, row in combined_data.iterrows():
    G.add_node(row['miRNA'])

for index, row in combined_data.iterrows():
    if row['AATF'] != None:
        G.add_edge(row['miRNA'], row['AATF'])


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

nx.write_edgelist(G, 'cikti.txt')