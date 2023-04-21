from ZoologicoCLI import ZoologicoCLI
from pymongo import MongoClient

client = MongoClient("mongodb+srv://raulmp016:5W7QJkZne8DjiJZD@cluster0.16w8hl9.mongodb.net/test")

db = client["BANCO-DE-DADOS-2"]

zoologicoCLI = ZoologicoCLI()
zoologicoCLI.createAnimal()

ZoologicoCLI.run()
