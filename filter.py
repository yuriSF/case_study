from file_ops import open_csv, write_csv_rows
import sys
sys.stdout = open('../case_study_data/banks_list.txt', 'w')


data = open_csv('../case_study_data/data.csv')
print 'all rows: ', len(data)
data2 = [row[7] for row in data]

data3 = set(data2)

for row in data3:
    print row

data4 = [row for row in data if row[7] == 'WELLS FARGO BANK, NATIONAL ASSOCIATION']
print 'Wells Fargo rows: ', len(data4)

data5 = [row for row in data if row[7] != 'WELLS FARGO BANK, NATIONAL ASSOCIATION']
print 'non Wells Fargo rows: ', len(data5)

write_csv_rows('../case_study_data/wells_fargo.csv', data4)
write_csv_rows('../case_study_data/non_wells_fargo.csv', data5)
