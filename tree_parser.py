import csv
import nltk
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
from nltk.tokenize import sent_tokenize
import operator
from grammar import grammar_vp, grammar_np
from file_ops import write_csv_rows
import pickle

cp = nltk.RegexpParser(grammar_np)
cp = nltk.RegexpParser(grammar_vp)

def reassemble_constituent(tree):
    leaves = tree.leaves()
    reassembled = [leaf[0] for leaf in leaves]
    reassembled = ' '.join(reassembled)
    return reassembled

def find_np(parsed, XP):
    XPs = []
    for item in parsed:
        if hasattr(item, 'label') == True:
            if item.label() == XP:
                #print 'item', item
                xp = item.leaves()
                #print XP, xp
                XPs.append(xp)
    return XPs

def parse_sent(sent, XP):
    tokens = nltk.word_tokenize(sent)
    tokens2 = [token.lower() for token in tokens]
    tagged_tuples = nltk.pos_tag(tokens2)
    print tagged_tuples
    parsed = cp.parse(tagged_tuples)
    print parsed
    return find_np(parsed, XP)

def get_data(data):
    data = data.decode('utf-8')
    sent_list = nltk.sent_tokenize(data)
    return sent_list

def extract_xps(sent_list, XP):
    all_phrases = []
    print 'length sents: ', len(sent_list)
    for ind, sent in enumerate(sent_list):
        xp = parse_sent(sent, XP)
        print xp
        all_phrases.append(xp)
        print ind, sent
    return all_phrases

def get_front_nps(all_nps):
    front_nps = []
    for np_list in all_nps:
        print np_list
        if np_list:
            front_np = np_list[0]
            front_nps.append(front_np)
    return front_nps

def stringify(l):
    strings = []
    for sub in l:
        phrase = [item[0] for item in sub]
        phrase = ' '.join(phrase)
        phrase = phrase.replace('] ', '')
        if phrase != '':
            strings.append(phrase)
    return strings

def calculate(l):
    freq_counts = {}
    uniq = set(l)
    print uniq
    for u in uniq:
        freq_counts[u] = l.count(u)
        print u
    sorted_fq = sorted(freq_counts.items(), key=operator.itemgetter(1))
    return sorted_fq[::-1]

def flatten_nps(l):
    flat_nps = []
    for sent in l:
        for np in sent:
            flat_nps.append(np)
    return flat_nps

def find_def_nps(flats):
    from grammar import def_dets
    definites = []
    for tuple_list in flats:
        if tuple_list[0][0] in def_dets:
            #print tuple_list
            definites.append(tuple_list)
    return definites

def convert_csv(l):
    temp = []
    for t in l:
        row = [t[0], t[1]]
        temp.append(row)
    return temp

def nouns(data):
    sent_list = get_data(data)
    all_nps = extract_xps(sent_list, 'NP')
    flat_nps = flatten_nps(all_nps)

    flat_nps_strings = stringify(flat_nps)
    sorted_freq = calculate(flat_nps_strings)
    write_csv_rows('../case_study_data/other_banks/all_nps.csv', sorted_freq)
    pickle.dump(sorted_freq, open("../case_study_data/other_banks/all_nps.p", "wb"))

    #DEFINITES
    defs = find_def_nps(flat_nps)
    print 'DEFS', defs
    defs_flat = stringify(defs)
    defs_flat_strings = calculate(defs_flat)
    write_csv_rows('../case_study_data/other_banks/def_nps.csv', defs_flat_strings)
    pickle.dump(sorted_freq, open("../case_study_data/other_banks/def_nps.p", "wb"))

    #INITIALS
    initial_nps = get_front_nps(all_nps)
    #print 'Initial', initial_nps
    initial_nps_flat = stringify(initial_nps)
    #print initial_nps_flat
    initial_nps_flat_strings = calculate(initial_nps_flat)
    write_csv_rows('../case_study_data/other_banks/initial_nps.csv', initial_nps_flat_strings)
    pickle.dump(sorted_freq, open("../case_study_data/other_banks/initial_nps.p", "wb"))

def verbs(data):
    sent_list = get_data(data)
    all_vps = extract_xps(sent_list, 'VP')
    flat_vps = flatten_nps(all_vps)
    print 'flat is done'
    flat_vp_strings = stringify(flat_vps)
    print 'vp_strings_done'
    sorted_freq = calculate(flat_vp_strings)
    print 'sorted freq done'
    pickle.dump(sorted_freq, open("../case_study_data/other_banks/vps.p", "wb"))
    write_csv_rows('../case_study_data/other_banks/vps.csv', sorted_freq)
