dic = {1:'JAN', 2:'FEV', 3:'MAR', 4:'ABR', 5:'MAI'}

print len(dic)
print 'Chaves:',dic.keys()
print 'Valores:', dic.values()
print dic[5]

# print dic[33333333] - error
print dic.get(3333) # solution using get(x)

print dic.items()
print dic.pop(1)
print dic

# dic.clear() - limpa o dicionario
dic2 = dic.copy()

print dic2