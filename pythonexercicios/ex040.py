n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1+n2)/2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {m:.1f}')
if m < 5:
    print('O aluno está REPROVADO.')
elif m >= 7:
    print('O aluno está APROVADO.')
else:
    print('O aluno está em RECUPERAÇÂO.')
