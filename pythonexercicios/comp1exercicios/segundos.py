segundos = int(input('Quantos segundos deseja converter? '))
horas = segundos//3600
minutos = (segundos - horas*3600)//60
segundos = segundos - horas*3600 - minutos*60
print(horas, 'hr', minutos, 'min', segundos, 'seg')
print('{}:{:0>2}:{:0>2}'.format(horas, minutos, segundos))
