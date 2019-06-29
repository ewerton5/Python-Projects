#----------solução com string----------
n = str(input('Digite um número: '))
print('''unidade: {}
dezena: {}
centena: {}
milhar: {}'''.format(n[-1], n[-2], n[-3], n[-4]))

#----------solução matemática----------
n = int(input('Digite um número: '))
m = int(n/1000)
c = int((n-m*1000)/100)
d = int((n-m*1000-c*100)/10)
u = int(n-m*1000-c*100-d*10)
print('''unidade: {}
dezena: {}
centena: {}
milhar: {}'''.format(u, d, c, m))
