# read files
f = open('text.txt', 'r', 100, 'utf-8-sig')
text = open('text.txt', 'r', 100, 'utf-8-sig').read().replace('/n', '').replace(' ', '').lower()
f1 = open('punct.txt', 'r', 100, 'utf-8-sig')
x = f1.readline().replace('\n', '').split(' ')
for y in x:
    text = text.replace(y, '')

# innitialisation
key = 'секрет'
res = []
text_decryp = text
y = text_decryp

# text to array
k = len(key)
z = len(text)
max = int(z / k) + 1
for i in range(max):
    res.append(text[i * k:i * k + k])
res[-1] += '   '
print(res)

# creating key
key_dict = []
i = 0
for c in key:
    key_dict.append([c, i])
    i += 1
    key_dict.sort()
# print('\n',key_dict, '\n')

text_decryp = text
# output sypher
print('\nsypher \n-------------')
syphered_text = ''
for e in key_dict:
    for w in res:
        syphered_text += w[e[1]]
        if w[e[1]] is not ' ':
            print(w[e[1]], end='')

print('\n')
# desypher
count = z // k + 1

desypher_dict = []
for i in range(count):
    desypher_dict.append(list('      '))

i = 0
key_num = 0
for c in syphered_text:
    desypher_dict[i][key_dict[key_num][1]] = c
    # print(desypher_dict[8][1]+'o')
    i += 1
    if i == count:
        key_num += 1
        i = 0
print('Desypher \n-------------')
for i in range(len(desypher_dict)):
    desypher_dict[i] = "".join(desypher_dict[i])
print(''.join(desypher_dict))
