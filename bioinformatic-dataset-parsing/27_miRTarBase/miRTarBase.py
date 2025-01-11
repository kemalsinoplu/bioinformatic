import pandas as pd

dosya = 'miRTarBase_MTI.xlsx'
veri = pd.read_excel(dosya)

homo_sapiens_verileri = veri[veri['Species (miRNA)'] == 'Homo sapiens']

yeni_dosya = 'output.xlsx'
homo_sapiens_verileri.to_excel(yeni_dosya, index=False)
print(f'Homo sapiens türündeki veriler "{yeni_dosya}" dosyasına yazıldı.')