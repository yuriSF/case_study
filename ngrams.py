import nltk
from nltk.collocations import *
import pickle

def bigrams_dist(tokens):
    bigrams = nltk.bigrams(tokens)
    fdist = nltk.FreqDist(bigrams)
    return fdist

def trigrams_dist(tokens):
    trigrams = nltk.trigrams(tokens)
    fdist = nltk.FreqDist(trigrams)
    return fdist


fargo_tokens = pickle.load(open('../case_study_data/fargo_tokens.p', 'rb'))
other_tokens = pickle.load(open('../case_study_data/other_tokens.p', 'rb'))

print 'opened data'

fargo_bi = bigrams_dist(fargo_tokens)
other_bi = bigrams_dist(other_tokens)
pickle.dump(fargo_bi, open('../case_study_data/fargo_bigrams.p', 'wb'))
pickle.dump(other_bi, open('../case_study_data/other_bigrams.p', 'wb'))

fargo_tri = trigrams_dist(fargo_tokens)
other_tri = trigrams_dist(other_tokens)
pickle.dump(fargo_tri, open('../case_study_data/fargo_trigrams.p', 'wb'))
pickle.dump(other_tri, open('../case_study_data/other_trigrams.p', 'wb'))
