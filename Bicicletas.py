from Vehiculos import Vehiculo

class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return "{}, de tipo {}".format(super().__str__(),self.tipo)
