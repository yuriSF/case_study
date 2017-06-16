from file_ops import open_csv, write_csv_rows

def data_breakup(l):
    initial = l[0]
    for n in range(len(l)):
        minitable = []
        start = n
        end = n + 10
        minitable.append(initial)
        for m in range(start, end):
            minitable.append(l[m])
        n = n + 10
        print minitable

data = open_csv('../case_study_data/nps_mortgage.csv')
data_breakup(data)
