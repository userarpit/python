class car():
    
    def __init__(self,**kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']

audi=car(s=200,c="Red")
bmw=car(s=300,c="white")

print(audi.color)
print(audi.speed)