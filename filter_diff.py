#from corpus_norm import normalize
from file_ops import write_csv_rows
import pickle

# wells_data = pickle.load(open('../case_study_data/general/all_nps.p', 'rb'))
# other_data = pickle.load(open('../case_study_data/other_banks/all_nps.p', 'rb'))

# def normalize(freq, norm_size, actual_size):
#     norm_freq = (float(freq) * float(norm_size)) / float(actual_size)
#     return norm_freq

#print normalize(100, len(other_data), len(wells_data))

def filter(data):
    temp = []
    temp.append(['VP', 'Wells freq', 'Wells normalized freq', 'other banks freq', 'difference'])
    for row in data[1:]:
        if row[1] > 30 and row[3] > 60 and row[4] > 30:
            temp.append(row)
    return temp

data = pickle.load(open('../case_study_data/vps_compared02.p', 'rb'))
output = filter(data)
print 'length output ', len(output)
write_csv_rows('../case_study_data/vps_compared_top02.csv', output)


'''
100, 263
50, 132

'''
