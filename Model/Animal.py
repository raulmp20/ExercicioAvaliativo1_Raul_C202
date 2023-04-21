from Model.Habitat import Habitat
class Animal:
    def __init__(self, nome:str, especie:str, idade:int, habitat: Habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat