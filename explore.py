
from file_ops import open_csv
from tree_parser import nouns, verbs, parse_sent

data = open_csv('../case_study_data/general/non_wells_fargo.csv')

complaints = [row[5] for row in data[1:]]
complaints = ' '.join(complaints)

def get_nps():
    nouns(complaints)

def get_vps():
    verbs(complaints)

get_nps()
get_vps()
