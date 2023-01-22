from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__)


@app.route('/<poke>')
def pokemon(poke):
    requisicao = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke}')
    pokemon = json.loads(requisicao.text)
    id = pokemon['id']
    nome = pokemon['forms'][0]['name']

    for tipo in pokemon['types']:
        tipos = tipo['type']['name']

    hp = pokemon['stats'][0]['base_stat']

    ataque = pokemon['stats'][1]['base_stat']

    defesa = pokemon['stats'][2]['base_stat']

    ataque_especial = pokemon['stats'][3]['base_stat']

    defesa_especial = pokemon['stats'][4]['base_stat']

    velocidade = pokemon['stats'][5]['base_stat']

    foto = pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_default']

    return render_template('pokemon.html', nome=nome, id=id, hp=hp, ataque=ataque, defesa=defesa,
                           ataque_especial=ataque_especial,
                           defesa_especial=defesa_especial, velocidade=velocidade, foto=foto)


if __name__ == '__main__':
    app.run()
