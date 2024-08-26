import csv

with open('events.csv', mode = 'r') as infile:
    csv_reader = csv.DictReader(infile)
    rows = [row for row in csv_reader]


    with open('events.csv', mode = 'w', newline = '') as outfile:
        try:
            fieldnames = rows[0].keys()
        except:
            pass
        csv_writer = csv.DictWriter(outfile, fieldnames = fieldnames)
        
        csv_writer.writeheader()
