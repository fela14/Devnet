
class Router:

    def __init__ (self, model, swVersion, ip_add):
        self.model = model
        self.swVersion = swVersion
        self.ip_add = ip_add

    def getdesc1(self):
        desc = (f'Router Model:                    {self.model}\n'
                f'Router Version:                  {self.swVersion}\n'
                f'Router Management Address:       {self.ip_add}')
        return desc
    
class Switch(Router):

    def getdesc2(self):
        desc = (f'Switch Model:                    {self.model}\n'
                f'Switch Version:                  {self.swVersion}\n'
                f'Switch Management Address:       {self.ip_add}\n') 
        return desc
    
rtr1 = Router('iosV', '15.1.1', '10.10.10.1')
rtr2 = Router('iosV', '15.5.5', '10.10.10.5')
sw1 = Switch('iosV', '15.7.7', '10.10.10.7')
sw2 = Switch('iosV', '15.8.8', '10.10.10.8')

print(f'Rtr1\n{rtr1.getdesc1()}\n')
print(f'Rtr2\n{rtr2.getdesc1()}\n')
print(f'Sw1\n{sw1.getdesc2()}\n')
print(f'Sw2\n{sw1.getdesc2()}\n')












"""
rtr1 = Router('iosV', '15.1.1', '10.10.10.1')
rtr2 = Router('iosV', '16.2.2', '10.10.10.5')

print(rtr1.model)
print(rtr1.swVersion)
print(rtr1.ip_add)

rtr1.desc = "Virtual router"
print(rtr1.desc)

print(rtr2.model)
print(rtr2.swVersion)
print(rtr2.ip_add)
"""


