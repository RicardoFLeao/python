#import math
from math import sin, cos, tan, radians
ang = int(input('Digite o ângulo que você deseja: '))
#seno = math.sin(math.radians(ang))
#coss = math.cos(math.radians(ang))
#tang = math.tan(math.radians(ang))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('O ângulo de {} tem um seno {:.2f}'.format(ang, seno))
print('O ângulo de {} tem um cosseno {:.2f}'.format(ang, coss))
print('O ângulo de {} tem um tangente {:.2f}'.format(ang, tang))
