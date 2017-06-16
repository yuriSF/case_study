from file_ops import open_csv, write_csv_rows

data = open_csv('../case_study_data/nps_compared_top02.csv')

mortgage = ['mortgage', 'home', 'house', 'property', 'refinance', 'foreclosure', 'lien', 'deed', 'homeowner', 'real estate', 'realtor', 'principle']
loan = ['loan', 'lender', 'principal', 'borrower', 'interest', 'lien']
legal = ['lawyer', 'attorney', 'lawsuit', 'government', 'irs', 'court', 'judge', 'legal', 'vioaltion', 'lie', 'false', 'state', 'tax', 'settlement']
business = ['sale', 'business', 'payment', 'credit', 'income', 'insurance']
service = ['checking', 'savings', 'escrow', 'account']



def check_word(l, phrase):
    for word in l:
        if word in phrase:
            return True

mortgage_phrases = []
loan_phrases = []
legal_phrases = []
business_phrases = []
service_phrases = []

initial_row = ['NP', 'Wells freq', 'Wells normalized freq', 'other banks freq', 'difference']
mortgage_phrases.append(initial_row)
loan_phrases.append(initial_row)
legal_phrases.append(initial_row)
business_phrases.append(initial_row)
service_phrases.append(initial_row)


for row in data:
    #print row[0]
    #print check_word(mortgage, row[0])
    if check_word(mortgage, row[0]):
        print row[0]
        mortgage_phrases.append(row)
    if check_word(loan, row[0]):
        loan_phrases.append(row)
    if check_word(legal, row[0]):
        legal_phrases.append(row)
    if check_word(business, row[0]):
        business_phrases.append(row)
    if check_word(service, row[0]):
        service_phrases.append(row)

print mortgage_phrases
write_csv_rows('../case_study_data/nps_mortgage.csv', mortgage_phrases)
write_csv_rows('../case_study_data/nps_loan.csv', loan_phrases)
write_csv_rows('../case_study_data/nps_legal.csv', legal_phrases)
write_csv_rows('../case_study_data/nps_business.csv', business_phrases)
write_csv_rows('../case_study_data/nps_service.csv', service_phrases)
