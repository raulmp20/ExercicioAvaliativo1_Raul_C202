from Model.Cuidador import Cuidador
from Model.Habitat import Habitat
from Model.Animal import Animal
from ZoologicoDAO import ZoologicoDAO
from database import Database

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class ZoologicoCLI(SimpleCLI):
    def __init__(self):
        super().__init__()
        self.add_command("create",self.createAnimal())
        self.add_command("read",self.readAnimal())
        self.add_command("update",self.updateAnimal())
        self.add_command("delete",self.deleteAnimal())

    def createAnimal(self):
        cuidador_nome = input("Entre com o nome do Cuidador: ")
        cuidador_documento = input("Entre com o documento do passageiro: ")
        cuidador = Cuidador(cuidador_nome, cuidador_documento)
        habitat_nome = str(input("Entre com o nome do Habitat: "))
        habitat_tipoAmbiente = str(input("Entre com o tipo de ambiente: "))
        habitat = Habitat(habitat_nome,habitat_tipoAmbiente,cuidador)
        animal_nome = str(input("Entre com o Nome do Animal: "))
        animal_especie = str(input("Entre com a Especie do animal: "))
        animal_idade = int(input("Entre com a Idade do animal: "))
        animal = Animal(animal_nome,animal_especie,animal_idade,habitat)
        con_banco = ZoologicoDAO(Database("zoologico", "animais"))
        con_banco.createAnimal(animal)

    def readAnimal(self, animal=None):
        animal_id = str(input("Entre com o id do animal que você deseja procurar: "))
        con_banco = ZoologicoDAO(Database("zoologico", "animais"))
        animal = con_banco.readAnimal(animal_id)
        if animal:
            print("Animal encontrado!")
            print(animal)
        else:
            print("Animal não encontrado.")
        pass
    def updateAnimal(self):
        animal_id = str(input("Entre com o ID do animal que você deseja atualizar: "))
        con_banco = ZoologicoDAO(Database("zoologico", "animais"))
        animal = con_banco.readAnimal(animal_id)
        if animal:
            print("Animal encontrado!")
            animal_nome = str(input("Entre com o novo nome: "))
            animal_especie = str(input("Entre com a nova especie: "))
            animal_idade = int(input("Entre com a nova idade: "))
            habitat_nome = str(input("Entre com o nome do novo habitat: "))
            habitat_tipoAmbiente = str(input("Entre com o novo tipo de ambiente: "))
            cuidador_nome = str(input("Entre com o nome do novo cuidador: "))
            cuidador_documento = str(input("Entre com o documento do novo cuidador: "))
            animal.nome = animal_nome
            animal.especie = animal_especie
            animal.idade = animal_idade
            animal.habitat.nome = habitat_nome
            animal.habitat.tipoAmbiente = habitat_tipoAmbiente
            animal.habitat.cuidador.nome = cuidador_nome
            animal.habitat.cuidador.documento = cuidador_documento
            con_banco.updateAnimal(animal)
            print("Animal atualizado!")
        else:
            print("Animal não encontrado.")
        pass

    def deleteAnimal(self):
        animal_id = int(input("Entre com o id do animal que você deseja deletar: "))
        con_banco = ZoologicoDAO(Database("zoologico", "animais"))
        animal = con_banco.readAnimal(animal_id)
        if animal:
            print("Animal encontrado!")
            con_banco.deleteAnimal(animal)
            print("Animal deletado!")
        else:
            print("Animal nao encontrado.")
        pass

    def run(self):
        print("Welcome to the Animal CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()