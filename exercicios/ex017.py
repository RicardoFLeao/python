#import math
from math import hypot
catop = float(input('qual o comprimento do cateto oposto: '))
catad = float(input('qual o comprimento do cateto adjacente: '))
#hyp = math.hypot(catop, catad)
hyp = hypot(catop, catad)
print('A hypotenusa vai medir {:.2f}'.format(hyp))