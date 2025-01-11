import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Excel dosyasını okuma
df = pd.read_excel('trrust_rawdata_human.xlsx')

# Ağ oluştur
G = nx.Graph()

# Genleri ve etkileşimleri ağa ekle
for index, row in df.iterrows():
    G.add_node(row['AATF'])
    G.add_node(row['BAX'])
    G.add_edge(row['AATF'], row['BAX'])

# Ağı çiz
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=800, node_color='lightblue', font_size=8)
plt.title('Genetik Etkileşim Ağı')
plt.show()