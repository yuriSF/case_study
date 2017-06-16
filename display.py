import pickle

def convert_list(dist):
    temp = []
    for k,v in dist.items():
        print k,v
        row = [k,v]
        temp.append(row)
    return temp


fargo_words = pickle.load(open('../case_study_data/fargo_dist.p', 'rb'))
other_words = pickle.load(open('../case_study_data/other_dist.p', 'rb'))
print fargo_words == other_words
pickle.dump(convert_list(fargo_words), open('../case_study_data/fargo_dist_l.p', 'wb'))
pickle.dump(convert_list(other_words), open('../case_study_data/other_dist_l.p', 'wb'))

fargo_bi = pickle.load(open('../case_study_data/fargo_bigrams.p', 'rb'))
other_bi = pickle.load(open('../case_study_data/other_bigrams.p', 'rb'))
fargo_bi_l = pickle.dump(convert_list(fargo_bi), open('../case_study_data/fargo_bigrams_l.p', 'wb'))
other_bi_l = pickle.dump(convert_list(other_bi), open('../case_study_data/other_bigrams_l.p', 'wb'))

fargo_tri = pickle.load(open('../case_study_data/fargo_trigrams.p', 'rb'))
other_tri = pickle.load(open('../case_study_data/other_trigrams.p', 'rb'))
fargo_tri_l = pickle.dump(convert_list(fargo_tri), open('../case_study_data/fargo_trigrams_l.p', 'wb'))
other_tri_l = pickle.dump(convert_list(other_tri), open('../case_study_data/other_trigrams_l.p', 'wb'))
