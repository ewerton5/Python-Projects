p = ('aprender', 'programar', 'linguagem', 'python',
     'curso', 'gratis', 'estudar', 'praticar',
     'trabalhar', 'mercado', 'programador', 'futuro')
for n in p:
    print(f'\nNa palavra {n.upper()} temos', end=' ')
    for c in n:
        if c in 'aeiou':
            print(c, end=' ')
