import pandas as pd
import xml.etree.ElementTree as ET

# miRTarBase ve TRRUST veri kümelerini oku (Excel formatında)
mirtarbase_df = pd.read_excel("miRTarBase.xlsx")
trrust_df = pd.read_excel("trrust_rawdata_human.xlsx", usecols=[1])  # Sadece 2. sütunu (Target Gene) kullanıyoruz

# TRRUST veri kümesinin sütun adını değiştirme (kolaylık sağlamak için)
trrust_df.columns = ["Target Gene"]

# XML dosyasını oku ve kök öğesini al
recon3d_tree = ET.parse("Recon3D.xml")
recon3d_root = recon3d_tree.getroot()

# Recon3D'deki genleri saklayacak bir liste
recon3d_genes = []

# XML'den genleri çıkarma
for gene_product in recon3d_root.findall(".//fbc:geneProduct", namespaces={"fbc": "http://www.sbml.org/sbml/level3/version1/fbc/version2"}):
    gene_name = gene_product.attrib.get("{http://www.sbml.org/sbml/level3/version1/fbc/version2}name")
    if gene_name:
        recon3d_genes.append(gene_name)

# Ortak hedef genleri bulma
common_genes = set(trrust_df["Target Gene"]).intersection(set(mirtarbase_df["Target Gene"])).intersection(set(recon3d_genes))

# Ortak genleri yazdırma
print("Ortak hedef genler:", common_genes)