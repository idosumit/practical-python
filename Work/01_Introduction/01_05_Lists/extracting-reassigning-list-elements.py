# 1.19

symbols = 'HPQ, AAPL, IBM, MSFT, YHOO, DOA, GOOG'

symlist = symbols.split(',')

print(symlist)

symlist[2] = 'AIG'

print(symlist)

mysyms = []
mysyms.append('GOOG')
print(mysyms)

symlist[-2:] = mysyms
print(symlist)
print(mysyms)
