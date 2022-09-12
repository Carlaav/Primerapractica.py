from Vehiculos import Vehiculo

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "{}, {}km/h, {}cc".format(super().__str__(),self.velocidad,self.cilindrada)