def create_dictionary(file, re):
    f = open(file, 'r', 100, 'utf-8-sig')
    a = f.readline().replace('\n', '').split(' ')
    b = f.readline().replace('\n', '').split(' ')
    dic = {}
    i = 0
    if re is False:
        for c in a:
            dic[c] = b[i]
            i += 1
    else:
        for c in b:
            dic[c] = a[i]
            i += 1
    return dic


def sypher(text, dict):
    f = open('punct.txt', 'r', 100, 'utf-8-sig')
    x = f.readline().replace('\n', '').split(' ')
    for y in x:
        text = text.replace(y, '')
    str = ''
    text = text.lower()
    for c in text:
        if c is ' ':
            str += ' '
        else:
            str += dict[c]
    return str


f = open('ukr_text.txt', 'r', 100, 'utf-8-sig')
text = f.read().strip().replace(' ', '')

print('Ukrainian text\n')
ukr_sypher = sypher(text, create_dictionary('ukr_dic.txt', False))
print(ukr_sypher)
print('\nEnglish text\n')
text = open('eng_text.txt', 'r', 100, 'utf-8-sig').read().strip()
eng_sypher = sypher(text, create_dictionary('eng_dict.txt', False))
print(eng_sypher)
print('\nUkrainian desypher\n')
print(sypher(ukr_sypher, create_dictionary('ukr_dic.txt', True)))
print('\nEnglish desypher\n')
print(sypher(eng_sypher, create_dictionary('eng_dict.txt', True)))
