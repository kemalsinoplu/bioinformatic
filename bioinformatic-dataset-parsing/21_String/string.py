import csv


with open('string_functional_annotations.csv', 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)

    with open('21.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(header)

        for line in csv_reader:
            string_functional_annotations = line[0]
            csv_writer.writerow([string_functional_annotations])


"""
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
"""


