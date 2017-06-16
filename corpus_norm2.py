import pickle
from file_ops import write_csv_rows


def normalize(freq, norm_size, actual_size):
    norm_freq = (float(freq) * float(norm_size)) / float(actual_size)
    return norm_freq

def match_rank(wells, other, wells_freq_total, other_freq_total):
    temp = []
    initial_row = ['np', 'wells freq', 'wells norm', 'other freq', 'diff']
    temp.append(initial_row)
    for wells_row in wells:
        for other_row in other:
            if wells_row[0] == other_row[0]:
                #print wells_row[0]
                other_freq = float(other_row[1])
                wells_freq = float(wells_row[1])
                wells_freq_norm = normalize(wells_freq, other_freq_total, wells_freq_total)
                #print wells_freq, wells_freq_norm, other_freq
                if wells_freq_norm > other_freq:
                    diff = wells_freq_norm - other_freq
                    row = [wells_row[0], wells_freq, wells_freq_norm, other_freq, diff]
                    temp.append(row)
                    print row
    return temp

def compare(wells_list, other_list, outfile_csv, outfile_p):
    wells_data = pickle.load(open(wells_list, 'rb'))
    other_data = pickle.load(open(other_list, 'rb'))
    print wells_data == other_data
    wells_freq_total = sum([row[1] for row in wells_data])
    other_freq_total = sum([row[1] for row in other_data])
    print wells_freq_total
    print other_freq_total
    output = match_rank(wells_data, other_data, wells_freq_total, other_freq_total)
    write_csv_rows(outfile_csv, output)
    pickle.dump(output, open(outfile_p, 'wb'))

compare('../case_study_data/fargo_dist_l.p', '../case_study_data/other_dist_l.p', '../case_study_data/compared_words.csv', '../case_study_data/compared_words.p')
#compare('../case_study_data/fargo_bigrams_l.p', '../case_study_data/other_bigrams_l.p', '../case_study_data/compared_bigrams.csv', '../case_study_data/compared_bigrams.p')
#compare('../case_study_data/fargo_trigrams_l.p', '../case_study_data/other_trigrams_l.p', '../case_study_data/compared_trigrams.csv', '../case_study_data/compared_trigrams.p')
