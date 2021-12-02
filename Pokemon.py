import requests
class BasePokemon:
    def __init__(self,name):
        self.name = str(name)

    def __str__(self):
        return f'name={self.name}'
class Pokemon(BasePokemon):
    def __init__(self, name, id, height, weight):
        BasePokemon.__init__(self, name)
        self.__name = self.name
        self.__id = id
        self.__height = height
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f'name={self.__name}, id={self.__id}, height={self.__height}, weight={self.__weight}'

class PokeAPI:
    def get_pokemon(self,name_id):
        url = "https://pokeapi.co/api/v2/pokemon/" + name_id + "/"
        result = requests.get(url).json()
        return Pokemon(result["name"], result["id"], result["height"], result["weight"])

    def get_all(self, max_counter, get_full=False):
        counter = 1
        while counter <= max_counter:
            url = "https://pokeapi.co/api/v2/pokemon/" + str(counter) + "/"
            result = requests.get(url).json()
            if get_full == False:
                yield BasePokemon(result["name"])
            else:
                yield Pokemon(result["name"], result["id"], result["height"], result["weight"])
            counter += 1

print(PokeAPI().get_pokemon("ditto"))

maxx_weight = 0
name = ""
for i in PokeAPI().get_all(50,True):
    if maxx_weight < i.weight:
        maxx_weight = i.weight
        name = i.name
print(maxx_weight,name)