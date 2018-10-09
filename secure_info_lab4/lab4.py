def msum(m,i):
    res = 0
    for a in range(i+1):
        res += m[a]
    return res

def desypher(text, rows):
    matrix = []
    result = []
    IsUp = True
    i = rows - 1
    for i in range(rows):
        matrix.append(0)
    for c in text:
        if c is not ' ':
            matrix[i] +=1
        if i == 0 and IsUp is True:
            IsUp = False
        if i == rows - 1 and IsUp is False:
            IsUp = True
        if IsUp is True:
            i -= 1
        else:
            i += 1

    for i in range(rows):
        if i == 0:
            result.append(list(text[:matrix[i]]))
        elif i == rows-1:
            result.append(list(text[matrix[i]*(-1):]))
        else:
            result.append(list(text[msum(matrix,i-1):msum(matrix,i)]))

        i=rows-1
        isUp = True
    for c in text:
        print(result[i][0],end='')
        del result[i][0]
        if i == 0 and IsUp is True:
            IsUp = False
        if i == rows - 1 and IsUp is False:
            IsUp = True
        if IsUp is True:
            i -= 1
        else:
            i += 1



text = open('lab_text.txt','r').read().replace('\n','')
print('Input rows: ', end='')
rows = int(input())
IsUp = True
i=rows-1
result = []
for i in range(rows):
    result.append([])
for c in text:
    if c is not ' ':
        result[i].append(c)
        if i==0 and IsUp is True:
            IsUp = False
        if i==rows-1 and IsUp is False:
            IsUp = True
        if IsUp is True:
            i-=1
        else:
            i+=1

#for i in result:
    #print(''.join(i))

print('\n----')
result_string = ''
for i in range(len(result)):
    for j in range(len(result[i])):
        result_string+=result[i][j]
print(result_string)

print('\n\nDesypher\n')
print(desypher(result_string,rows))
