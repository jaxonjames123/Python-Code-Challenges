# Jaxon Terrell
# 8/7/20
# Script to combine multiple csv files as a new file, and retain all fields and data within them
import csv

def merge_csv(*files, output_file):
    fieldnames = list()
    for file in files:
        with open(file, 'r') as input_file:
            fields = csv.DictReader(input_file).fieldnames
            fieldnames.extend(i for i in fields if i not in fieldnames)
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.DcitWrite(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in files:
            with open(file, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    writer.writerow(row)
