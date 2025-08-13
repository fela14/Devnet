from math import sqrt,tan
from device import Router, Switch
import math
import calendar as cal



print(dir(math))
print(help(math.sqrt))

print(int(math.sqrt(81)))
print(cal.month(2025,4,1,1))
print(sqrt(100))

rtr3 = Router('iosV', '15.8.8.8', '10.10.3.3')
rtr4 = Router('iosV', '15.9.9.9', '10.10.4.4')
sw2 = Switch('iosV', '15.10.10.10', '10.10.6.6')

print(f'Rtr3\n{rtr3.getdesc1()}\n')
print(f'Rtr4\n{rtr4.getdesc1()}\n')
print(f'Sw2\n{sw2.getdesc2()}\n')

