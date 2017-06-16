import pickle

data = pickle.load(open('../case_study_data/general/initial_nps.p'))

def calc(l, col_num):
    temp = []
    vals = [float(row[col_num]) for row in l]
    s = float(sum(vals))
    print s
    for row in l:
        #print row[col_num]
        freq = float(row[col_num])
        #print 'freq ', freq
        per = (freq /s ) * 100
        #print 's ', s
        #print 'per ', per
        new_row = [row[0], row[1], s, per]
        temp.append(new_row)
    return temp


init = calc(data, 1)
print init[0:10]
