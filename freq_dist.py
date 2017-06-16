from file_ops import open_csv
from tree_parser import nouns, verbs, parse_sent
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle

def get_text(f):
    data = open_csv(f)
    complaints = [row[5] for row in data[1:]]
    complaints = ' '.join(complaints)
    complaints = complaints.decode('utf-8')
    return complaints



def get_tokens(text):
    tokens = nltk.word_tokenize(text)
    tokens2 = [token.lower() for token in tokens if token not in stopwords.words('english')]
    tokens3 = [lemmatizer.lemmatize(token) for token in tokens2]
    return tokens3

def get_dist(tokens):
    fdist = nltk.FreqDist(tokens)
    print fdist['get']
    return fdist


text_fargo = get_text('../case_study_data/general/wells_fargo.csv')
text_other = get_text('../case_study_data/general/non_wells_fargo.csv')
print 'opened data'

print text_fargo == text_other

fargo_tokens = get_tokens(text_fargo)
other_tokens = get_tokens(text_other)
print fargo_tokens == other_tokens
pickle.dump(fargo_tokens, open('../case_study_data/fargo_tokens.p', 'wb'))
pickle.dump(other_tokens, open('../case_study_data/other_tokens.p', 'wb'))

fargo_dist = get_dist(fargo_tokens)
other_dist = get_dist(other_tokens)
print fargo_dist == other_dist
pickle.dump(fargo_dist, open('../case_study_data/fargo_dist.p', 'wb'))
pickle.dump(other_dist, open('../case_study_data/other_dist.p', 'wb'))
