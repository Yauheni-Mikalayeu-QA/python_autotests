import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '086fd0990690f3882b508a01f70b96a3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "name": "Беларус",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
new_name = {
    "pokemon_id": "26849",
    "name": "Чечня",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}

pokeball = {
    "pokemon_id": "26849"
}


# response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
# print(response.text)

# smena_imeni = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = new_name)
# print(smena_imeni.text)

# slovit_pokemona = requests.post(url =f'{URL}/trainers/add_pokeball',headers = HEADER, json = pokeball)
# print(slovit_pokemona.text)





