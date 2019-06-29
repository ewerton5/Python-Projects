from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
r = radians(a)
print('O ângulo de {0} tem o SENO de {1:.2f}\nO ângulo de {0} tem o COSSENO de {2:.2f}\nO ângulo de {0} tem o TANGENTE de {3:.2f}\n'.format(a, sin(r), cos(r), tan(r)))
