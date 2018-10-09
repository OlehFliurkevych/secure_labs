def create_dictionary(text):
    alpa = open(text,'r').readline().replace('\n','').split(', ')
    result = {}
    i=0
    for c in alpa:
        result[c] = i
        i+=1

    return result


def sypher(text,key,dict,de):
    result = ''
    k=0
    i=0
    for c in text:
        if de is False:
            k = dict[c] + dict[key[i]]
        else:
            k = dict[c] - dict[key[i]]
        if k>32:
            k-=32
        if k<0:
            k+=32
        result += list(dict.keys())[list(dict.values()).index(k)]
    return result


ukr_dict = create_dictionary('alphabet.txt')
key = 'техніка'
text = open('text.txt','r').read().replace('\n',' ').replace(' ','').lower()
f1 = open('punct.txt', 'r')
x = f1.readline().replace('\n', '').split(' ')
for c in x:
    text = text.replace(c,'')
k = len(text)/len(key)
key = key*int(k)
k = len(text) - len(key)
for i in range(k):
    key += key[i]

syphert = sypher(text,key,ukr_dict,False)
print(syphert)
print('\nDesypher\n')
print(sypher(syphert,key,ukr_dict,True))


