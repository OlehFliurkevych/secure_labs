def sypher_duo(str,k1,k2,k3,k4):
    for i in range(len(k1)):
        if str[0] in k1[i]:
            ind11 = k1[i].index(str[0])
            ind12 = i

        if str[1] in k4[i]:
            ind21 = k4[i].index(str[1])
            ind22 = i

    result = k2[ind12][ind21] + k3[ind22][ind11]
    return result

f = open('keys.txt','r')
text = open('lab_text.txt','r', 100, 'utf-8-sig').read().replace('/n','').replace(' ','').lower()
text = text.replace('j','i')
f1 = open('punct.txt', 'r', 100, 'utf-8-sig')
x = f1.readline().replace('\n', '').split(' ')
for y in x:
    text = text.replace(y, '')

key1 = f.readline().replace('\n','').split(';')
for i in range(len(key1)):
    key1[i] = key1[i].split(',')
key2 = f.readline().replace('\n','').split(';')
for i in range(len(key2)):
    key2[i] = key2[i].split(',')
key3 = f.readline().replace('\n','').split(';')
for i in range(len(key3)):
    key3[i] = key3[i].split(',')
key4 = f.readline().replace('\n','').split(';')
for i in range(len(key4)):
    key4[i] = key4[i].split(',')


groups = [text[i:i+2] for i in range(0, len(text), 2)]
#print(groups)
i=0
sypher = []
for d in groups:
    sypher.append(sypher_duo(d,key1,key2,key3,key4))
    print(sypher_duo(d,key1,key2,key3,key4),end='')
    #print(d,end=', ')
print('\nDesypher\n')
for d in sypher:
    print(sypher_duo(d,key2,key1,key4,key3),end = '')
