import csv

# TSV dosyasının adı
tsv_file_path = 'trrust_rawdata.human.tsv'

target_activation = "Activation"
target_repression = "Repression"
target_unkown = "Unknown"

# TSV dosyasını aç ve okuyarak verileri elde et
with open(tsv_file_path, 'r', newline='', encoding='utf-8') as tsvfile:
    # TSV dosyasını bir csv.reader nesnesine geçir
    tsvreader = csv.reader(tsvfile, delimiter='\t')

    activation_rows = []
    repression_rows = []
    unkown_rows = []

    # Her bir satırı işle
    for row in tsvreader:
        if len(row) >= 3:
            keyword_in_third_column = row[2]

            if keyword_in_third_column == target_activation:
                activation_rows.append(row)
            elif keyword_in_third_column == target_repression:
                repression_rows.append(row)
            else:
                unkown_rows.append(row)




    print(f"{target_activation}:")
    for row in activation_rows:
        print('\t'.join(row))

    print(f"\n{target_repression}:")
    for row in repression_rows:
        print('\t'.join(row))

    print(f"\n{unkown_rows}:")
    for row in unkown_rows:
        print('\t'.join(row))