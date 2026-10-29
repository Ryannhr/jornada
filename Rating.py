'''
Em um sistema de avaliação de restaurantes com cinco estrelas (⭐️⭐️⭐️⭐️⭐️),
as estrelas representam diferentes níveis de satisfação.
Mas o que cada classificação por estrelas realmente significa?

Comece criando uma ratingvariável e atribua a ela um número decimal entre 0 e 5.

Em seguida, crie um sistema de classificação com um if/ elif/ else:

ratingmaior que 4,5, imprimir'Perfection'
ratingmaior que 4, imprimir'Excellent'
ratingmaior que 3, imprimir'Good'
ratingmaior que 2, imprimir'Fair'
Caso contrário, imprima'Poor'
'''

rating = float(input('How would you rate us?\nRate from 0 to 5:\n'))

if rating >= 4.5:
  print('Perfection')
elif rating >= 4 and rating < 4.5:
  print('Excellent')
elif rating >= 3 and rating < 4:
  print('Good')
elif rating < 3:
  print('Fair')
else:
  print('Poor')