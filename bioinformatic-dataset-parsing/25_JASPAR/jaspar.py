from Bio import SeqIO
import os

klasor_yolu = r'C:\Users\Msi\Desktop\test\25\JASPAR2022_CORE_non-redundant_pfms_jaspar'
dosya_listesi = sorted([dosya for dosya in os.listdir(klasor_yolu) if dosya.endswith('.jaspar')])

cikti_dosyasi = 'output.jaspar'

with open(cikti_dosyasi, "w") as cikti_dosyasi:
    for dosya_adi in dosya_listesi:
        dosya_yolu = os.path.join(klasor_yolu, dosya_adi)

        with open(dosya_yolu, 'r') as dosya:
            lines = dosya.readlines()
            cikti_dosyasi.write(lines[0])
            cikti_dosyasi.write(lines[1])

            for line in lines[2:]:
                line = line.strip().split('\t')
                nukleotit, matris = line[0], line[1:]
                matris_str = ' '.join(map(str, map(int, matris)))
                cikti_dosyasi.write(f"{nukleotit} [{matris_str}]\n")

            cikti_dosyasi.write("\n")
        cikti_dosyasi.write("\n")
