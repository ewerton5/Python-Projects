frase = input('Digite uma frase: ').strip()
print('Sua frase tem {} letras A'. format(frase.lower().count('a')))
print('A primeira está na posição {}'.format(frase.lower().find('a')+1))
print('A última está na posição {}'.format(frase.lower().rfind('a')+1))
