import requests

class apiRickandMorty:

    def __init__(self, id, name, status, species, location, image):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.location = location
        self.image = image

    def to_json(self):
        return {
          "id": self.id,
          "name" : self.name,
          "status": self.status,
          "species": self.species,
          "location" : self.location,
          "image" : self.image
        }


    def getall_characters():
        listaall = []
        for i in range(1,22,1):
            result = requests.get(f'https://rickandmortyapi.com/api/character?page={i}')
            resultx= result.json()
            listaxpagina = resultx['results']
            listaall.append(listaxpagina)
        return listaall

