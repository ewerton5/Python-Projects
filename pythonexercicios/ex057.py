s = input('Informe seu sexo: [M/F] ').strip().upper()
while s not in 'MF':
    s = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()
print(f'Sexo {s} registrado com sucesso')
