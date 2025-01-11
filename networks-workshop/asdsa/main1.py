import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Örnek: miRTarBase datasetini yükleyin (veriyi indirmeniz ve yüklemeniz gerekebilir)
# Örnek olarak 'miRTarBase.xlsx' dosya adını kullanıyoruz, siz gerçek dosya adınıza göre güncelleyin.
mirbase_df = pd.read_excel('miRTarBase.xlsx')

# Örnek: CSD2_transcript geninin repressed olduğu miRNA'ları filtreleyin
csd2_transcript_repressed = mirbase_df[mirbase_df['Target Gene'] == 'BAX_transcript']

# NetworkX ağını oluşturun
G = nx.Graph()

# Her bir miRNA'yı düğüm olarak ekleyin
for index, row in csd2_transcript_repressed.iterrows():
    G.add_node(row['miRNA'])

# CSD2_transcript geni ile repressed olduğu miRNA'ları bağlayın
for index, row in csd2_transcript_repressed.iterrows():
    G.add_edge('BAX_transcript', row['miRNA'])

# Ağı çiz
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=800, node_color='lightblue', font_size=8)
plt.title('miRNA Repression Network for BAX_transcript')
plt.show()
