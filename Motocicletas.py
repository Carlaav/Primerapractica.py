from Bicicletas import Bicicleta

class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "{}, alcanza una velocidad de {}Km/h y tiene {} cilindros".format(super().__str__(),self.velocidad,self.cilindrada)