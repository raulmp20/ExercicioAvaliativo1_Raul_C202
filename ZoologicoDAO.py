from Model.Cuidador import Cuidador
from Model.Habitat import Habitat
from Model.Animal import Animal
from database import Database
from bson.objectid import ObjectId

class ZoologicoDAO:

    def __init__(self, database):
        self.db = database

    def createAnimal(self, animal: Animal) -> str:
        try:
            res = self.db.collection.insert_one({"nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": [{
                "nome": animal.habitat.nome, "tipoAmbiente": animal.habitat.tipoAmbiente, "cuidador": [{"nome": animal.habitat.cuidador.nome, "documento": animal.habitat.cuidador.documento}]
            }]})
            print(f"Animal created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as error:
            print(f"An error occurred while creating Animal: {error}")
            return None

    def readAnimal(self, id: str) -> dict:
        try:
            ani = self.db.collection.find_one({"_id": ObjectId(id)})
            if ani:
                print(f"Animal found: {ani}")
                return ani
            else:
                print(f"No Animal found with id {id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")
            return None

    def updateAnimal(self, animal: Animal) -> str:
        try:
            result = self.db.collection.update_one({"_id": ObjectId(animal.id)}, {"$set": {"nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": [{
                "nome": animal.habitat.nome, "tipoAmbiente": animal.habitat.tipoAmbiente,
                "cuidador": [{"nome": animal.habitat.cuidador.nome, "documento": animal.habitat.cuidador.documento}]}]}})
            if result.modified_count:
                print(f"Animal {animal.id} updated with name {animal.nome}, especie {animal.especie}, age {animal.idade}, and habitat {animal.habitat}")
            else:
                print(f"No Animal found with id {animal.id}")
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None

    def deleteAnimal(self, id: str) -> str:
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                print(f"Animal {id} deleted")
            else:
                print(f"No Animal found with id {id}")
        except Exception as error:
            print(f"An error occurred while deleting animal: {id}")
            return None


