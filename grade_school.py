'''
Instruções
O ensino médio nos EUA geralmente dura quatro anos, do primeiro ao último ano. 🚌💨

Primeiro, peça ao usuário para inserir sua nota como um número inteiro.

Crie um sistema de notas para o ensino médio de quatro anos usando uma declaração if/ elif/ :else

gradeé 9, imprimir'Freshman'
gradeé 10, imprima'Sophomore'
gradeé 11, imprimir'Junior'
gradeé 12, imprimir'Senior'
Todo o resto é'TBD'
'''

usuario = {'Mario': '1234'}
credential = input('Eter your license plate:\n')

if credential in usuario.values():
  nota = int(input('Enter your nota:\n'))
  if nota == 9:
    print('Freshman')
  elif nota == 10:
    print('Sophomore')
  elif nota == 11:
    print('Junior')
  elif nota == 12:
    print('Senior')
  else:
    print('TBD')
else:
  print('Error/InvalidCredential')
