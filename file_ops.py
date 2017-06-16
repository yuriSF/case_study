import csv

def open_file(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
    return data

def open_csv(f):
    with open(f, 'r') as f:
        reader = csv.reader(f)
        temp = [row for row in reader]
        return temp

def write_csv_row(f, row):
    with open(f, 'a') as csvfile:
        csv.writer(csvfile).writerow(row)

def write_csv_rows(f, rows):
    with open(f, 'wb') as csvfile:
        csv.writer(csvfile).writerows(rows)
