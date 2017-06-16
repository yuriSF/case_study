from file_ops import open_csv
from textblob import TextBlob
import numpy
import sys
sys.stdout = open('../case_study_data/sentiment_other.txt', 'w')


data = open_csv('../case_study_data/general/non_wells_fargo.csv')
complaints = [row[5] for row in data[1:]]

sent_data = []
for complaint in complaints:
    complaint = complaint.decode('utf-8')
    blob = TextBlob(complaint)
    sent = blob.sentiment
    pol = sent[0]
    subj = sent[1]
    #print pol, subj
    row = [complaint, pol, subj]
    sent_data.append(row)

pols = [row[1] for row in sent_data]
subj = [row[2] for row in sent_data]

print 'Other banks sentiment: ', numpy.mean(pols)
print 'Other banks subjectivity:', numpy.mean(subj)
