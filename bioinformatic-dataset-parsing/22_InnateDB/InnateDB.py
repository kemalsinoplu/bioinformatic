import pandas as pd

mitab_path = "innatedb_ppi.mitab"
df = pd.read_csv(mitab_path, delimiter='\t', header=None, dtype=str, low_memory=False)

taxid_sutunu = df[9]

human = df[taxid_sutunu.str.contains('taxid:9606', na=False)]
mouse = df[taxid_sutunu.str.contains('taxid:10090', na=False)]

print("Data of Human: ")
print(human)

print("\nData of Mouse")
print(mouse)

"""human.to_csv("human_output.mitab", index=False)
mouse.to_csv("mouse_output.mitab", index=False)"""

"""import csv


def parse_mitab_file(file_path):
    interactions = []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')

        for row in reader:
            # İlgili sütunlardan gerekli bilgileri çıkarma
            protein_a = row['#unique_identifier_A']
            protein_b = row['unique_identifier_B']
            # Diğer gerekli bilgileri buradan da çıkarabilirsiniz.

            interactions.append((protein_a, protein_b))

    return interactions


# Örnek kullanım
file_path = 'innatedb_ppi.mitab'
interactions = parse_mitab_file(file_path)

for interaction in interactions:
    print(f"Protein A: {interaction[0]}, Protein B: {interaction[1]}")

"""