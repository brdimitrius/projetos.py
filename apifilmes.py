import requests
import json

filme = input("Coloque o nome do filme : ")
filme_api = requests.get("http://www.omdbapi.com/?t=%a&apikey=e0533b6c"%(filme))
filme_dict = json.loads(filme_api.text)
#Nome do Filme
print("Nome : ",filme_dict['Title'])
#Ano do Lançamento
print("Ano de lançamento :",filme_dict['Year'])
#Nomes dos atores
print("Atores :",filme_dict['Actors'])
#Nome(s) do(s) diretor(es)
print("Diretor :",filme_dict["Director"])
