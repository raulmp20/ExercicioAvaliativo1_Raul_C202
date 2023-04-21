from Model.Cuidador import Cuidador
class Habitat:
    def __init__(self, nome:str, tipoAmbiente:str, cuidador:Cuidador):
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador