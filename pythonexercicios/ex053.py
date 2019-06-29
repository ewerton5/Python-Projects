f = input('Digite uma frase: ').lower().strip()
f = ''.join(f.split())
nf = ''
for c in range(len(f) - 1, -1, -1):
    nf = nf + f[c]
if f == nf.strip():
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
