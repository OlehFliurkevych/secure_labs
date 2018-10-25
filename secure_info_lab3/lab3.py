import random


def create_dictionary(file):
    result = {}
    with open(file, 'r', 100, 'utf-8-sig') as f:
        for l in f:
            temp = l.replace('(', '').replace(')', '').replace('\n', '').split('=')
            temp[1] = temp[1].split(',')
            result[temp[0]] = temp[1]
    return result


ukr_dict = create_dictionary('ukr_dict.txt')


def sypher(text, dic):
    f = open('punct.txt', 'r', 100, 'utf-8-sig')
    x = f.readline().replace('\n', '').split(' ')
    for y in x:
        text = text.replace(y, '')
    str = ''
    text = text.lower()
    for c in text:
        str += random.choice(dic[c]) + ' '
    return str


# def desypher(text,)

text = open('ukr_text.txt', 'r', 100, 'utf-8-sig').read().replace('\n', '').replace('.', '')
result = sypher(text, ukr_dict)
print(result.replace(' ', ''))
print('\nDesypher\n')
result = result.split(' ')
# print(result)
for d in result:
    for i in ukr_dict:
        # print(i,end = ' ')
        if d in ukr_dict[i]:
            print(i, end='')
            break
