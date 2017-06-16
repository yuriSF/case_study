assess = ['unfair', 'incorrect', 'unacceptable', 'not able']
employees = ['denied', 'deny', 'advise']
wrongful = ['did nothing', 'mistake', 'is fraud', 'not true' ]
pay = ['paid on time', 'made a payment']
inconvenient = ['made me', 'causing']


from file_ops import open_csv, write_csv_rows

data = open_csv('../case_study_data/vps_compared_top02.csv')


def check_word(l, phrase):
    for word in l:
        if word in phrase:
            return True

assess_phrases = []
employees_phrases = []
wrongful_phrases = []
pay_phrases = []
inconvenient_phrases = []

initial_row = ['NP', 'Wells freq', 'Wells normalized freq', 'other banks freq', 'difference']
assess_phrases.append(initial_row)
employees_phrases.append(initial_row)
wrongful_phrases.append(initial_row)
pay_phrases.append(initial_row)
inconvenient_phrases.append(initial_row)


for row in data:
    #print row[0]
    #print check_word(assess, row[0])
    if check_word(assess, row[0]):
        print row[0]
        assess_phrases.append(row)
    if check_word(employees, row[0]):
        employees_phrases.append(row)
    if check_word(wrongful, row[0]):
        wrongful_phrases.append(row)
    if check_word(pay, row[0]):
        pay_phrases.append(row)
    if check_word(inconvenient, row[0]):
        inconvenient_phrases.append(row)

print assess_phrases
write_csv_rows('../case_study_data/vps_assess.csv', assess_phrases)
write_csv_rows('../case_study_data/vps_employees.csv', employees_phrases)
write_csv_rows('../case_study_data/vps_wrongful.csv', wrongful_phrases)
write_csv_rows('../case_study_data/vps_pay.csv', pay_phrases)
write_csv_rows('../case_study_data/vps_inconvenient.csv', inconvenient_phrases)
