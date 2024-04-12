import requests
from dataclasses import dataclass

"""
Nessa atividade, vamos utilizar uma API, um site que nos permite baixar 
dicionários com dados relevantes.
No caso, os dados serão sobre pokemons, e o site se chama pokeapi.

Comecemos abrindo as seguintes URLs no firefox, para entender a pokeapi.
(é importante abrir no firefox. No chrome, elas ficam bastante mais 
difíceis de ler. Instale o firefox se não tiver. Deixar as URLs legíveis no
chrome dá muito mais trabalho -- ainda não vi uma solução decente)

Alguns exemplos de URLs que podem servir de inspiração:
http://pokeapi.co/api/v2/

http://pokeapi.co/api/v2/pokemon/39/
http://pokeapi.co/api/v2/pokemon/jigglypuff/

http://pokeapi.co/api/v2/pokemon-species/39/
http://pokeapi.co/api/v2/pokemon-species/jigglypuff/

http://pokeapi.co/api/v2/evolution-chain/11/
http://pokeapi.co/api/v2/growth-rate/1/
http://pokeapi.co/api/v2/pokemon-color/2/
"""

"""
Pra você não ficar digitando a mesma url toda hora, criei uma variável global
Aí, você pode completar conforme a necessidade
"""
site_pokeapi = "https://pokeapi.co"
urlBase = "https://pokeapi.co/api/v2/pokemon/"
urlSpecies = "http://pokeapi.co/api/v2/pokemon-species/"


"""
1. Dado o número de um pokémon, qual é o nome dele?

Dica: acesse a URL http://pokeapi.co/api/v2/pokemon/39/
Nessa URL, podemos ver todos os dados do pokemon 39, inclusive o nome

Trocando o número pelo número correto, você vai conseguir achar, para cada pokemon,
o nome dele.

"""

def retornoPadrao(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        dados = resp.json()
        return dados
    else:
        raise PokemonNaoExisteException("O Pokémon não foi encontrado.")

def retornaDadosPorDados(nome):
    nome = nome.lower()
    url = urlBase + nome
    return retornoPadrao(url)

def retornaDadosPorSpecies(nome):
    nome = nome.lower()
    url = urlSpecies + nome
    return retornoPadrao(url)


# ============================================================================

# Exercicios


def nome_do_pokemon(numero):
    url = urlBase + str(numero)
    dados = retornoPadrao(url)
    return dados["name"]


"""
Abaixo, criamos uma excessão com nome personalizado, que será utilizada do exercicio 2 
em diante.
"""


class PokemonNaoExisteException(Exception):
    pass  # nao faça nada aqui. Essa exception
    # já está pronta, só é um "nome" novo


"""
2. Dado o nome de um pokémon, qual é o número dele?

Dica: consulte as URLs úteis no começo do arquivo. Uma delas te permite colocar o
nome e descobrir o número.

Dica2: A pokeapi espera todos os nomes apenas com minúsculas. Mas eu
posso mandar nomes maiúsculos (PIKACHU) ou misturados (PikaChu)
Trate esse problema (nessa função e nas próximas)

Dica3: Se o status_code vier inválido, lance a excessão PokemonNaoExisteException,
que já está definida nesse arquivo. Lembre-se que o status_code de sucesso é o 200

Dica4: Para entender como ver o status_code usando a biblioteca requests,
olhe o arquivo requests_exemplo

"""
# def tratamentodedados(dados):


def numero_do_pokemon(nome):
    dados = retornaDadosPorDados(nome)
    return dados["id"]

"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?

Dica: consulte as URLs úteis no começo do arquivo.A URL que vamos usar dessa vez é nova, ainda
não utilizamos

Dica: Ainda esperamos a PokemonNaoExisteException quando apropriado.
Não vou mais te avisar disso.
"""


def color_of_pokemon(nome):
    dados = retornaDadosPorSpecies(nome)
    return dados["color"]["name"]


dic_cores = {  # esse dicionário pode te ajudar com o exercicio 4
    "brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto",
}


"""
4. Dado o nome ou número de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são:
"marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Talvez o dic_cores acima
seja útil.
"""


def cor_do_pokemon(nome):
    name = color_of_pokemon(nome)
    if name in dic_cores:
        return dic_cores[name]


dic_tipos = {  # esse dicionário pode te ajudar com o exercicio 5
    "normal": "normal",
    "fighting": "lutador",
    "flying": "voador",
    "poison": "veneno",
    "ground": "terra",
    "rock": "pedra",
    "bug": "inseto",
    "ghost": "fantasma",
    "steel": "aço",
    "fire": "fogo",
    "water": "água",
    "grass": "grama",
    "electric": "elétrico",
    "psychic": "psíquico",
    "ice": "gelo",
    "dragon": "dragão",
    "dark": "noturno",
    "fairy": "fada",
}


"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são:
 "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço",
 "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista
contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.

Dica: novamente, dê uma olhada nas URL que separei. Elas bastam.
Isso será verdade para todo o arquivo.
"""


def tipos_do_pokemon(nome):
    tipos = []
    dados = retornaDadosPorDados(nome)
    for dado in dados["types"]:
        tipo = dado["type"]["name"]
        if tipo in dic_tipos:
            tipos.append(dic_tipos[tipo])
    return tipos


"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. 

Por exemplo, 
evolucao_anterior('bulbasaur') == None
"""


def evolucao_anterior(nome):
    detalhes = retornaDadosPorSpecies(nome)
    evolucao = detalhes["evolves_from_species"]
    if evolucao != None:
        return evolucao["name"]
    else:
        return None


"""
Pulamos o exercicio 7. Depois te conto mais. Vá direto para o 8
"""

"""
8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
dica: na URL pokemon-species, procure growth rate
"""


# dados da experiencia
def nivel_do_pokemon(nome, experiencia):
    species = retornaDadosPorSpecies(nome)
    url_growth = species["growth_rate"]["url"]
    growth = requests.get(url_growth)

    if growth.status_code == 200:
        resp = growth.json()
        detalhes_growth = resp["levels"]

        for detalhes in detalhes_growth:
            if detalhes["experience"] <= experiencia:
                dados = detalhes["level"]
        return dados


# ===============================================================================================

"""

9. Dado um nome de treinador, cadastre-o na API de treinador.
Retorne True se um treinador com esse nome foi criado e 
        False em caso contrário (já existia).

Dicas teste 9: Use o verbo PUT, URL {site_treinador}/treinador/{nome}
para criar um treinador. Se ele já existe, será retornado um cod de status
303. Se não existe, cod status 202.

dica: considere as linhas 
      r = requests.put(url)
      status_code = r.status_code

      nelas você vê como usar o verbo put e como verificar o status code
"""

site_treinador = "http://127.0.0.1:9000"  # quando você estiver executando o servidor do treinador, essa URL estará ativa
get_treinador = f"{site_treinador}/treinador"

# def recuperaDadosURL(url, nome):
#     urlBase = f"{url}/{nome}"
#     resp = requests.put(put_treinador)


def tratamentoDeDados(dado):
    dado = dado.lower()


def cadastrar_treinador(nome):
    put_treinador = f"{get_treinador}/{nome}"
    resp = requests.put(put_treinador)

    if resp.status_code == 202:
        return True
    elif resp.status_code == 303:
        return False
    else:
        return False


cadastrar_treinador("Ash Ketchum")
cadastrar_treinador("Misty")


# cadastrar_treinador('Ash Ketchum')
# nao precisa mexer nas proximas excessões
# São só erros pra você lançar nas próximas funções
# Leia os nomes delas, e use quando apropriado.
class PokemonNaoCadastradoException(Exception):
    pass


class TreinadorNaoCadastradoException(Exception):
    pass


class PokemonJaCadastradoException(Exception):
    pass


"""
10. Imagine que você capturou dois pokémons do mesmo tipo. 
Para diferenciá-los, você dá nomes diferentes (apelidos) para eles.
Logo, um treinador pode ter mais do que um pokémon de um determinado tipo, 
mas não pode ter dois pokémons diferentes com o mesmo apelido.

Dados: um nome de treinador, um apelido de pokémon, um tipo de pokémon e uma quantidade de experiência, 

cadastre o pokémon com o tipo correspondente, na lista do treinador que foi passado,
usando a API (o servidor) do treinador.
Certifique-se de que todos os dados são válidos.
Inicio teste 10 -- para passar o 10a
* Para cadastrar um pokemon, usar a url 
{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}, enviando um arquivo json 
com a chave tipo (por exemplo tipo=pikachu) e a chave experiência
* Para enviar um dicionario pra uma URL, usando o verbo put, faça o seguinte:
requests.put(url,json = {"tipo":"pikachu","experiencia"...})


Mais dicas teste 10: 
* Pode ser necessário usar a pokeapi para verificar se um pokemon existe -- se
eu falar que o geremias é dono de um pokemon do tipo homer, deve ocorrer 
uma excessao, porque homer não é uma espécie válida de pokemon
* Se voce receber um status 404, isso indica um treinador nao encontrado
* Se voce receber um status 409, isso indica que o pokemon já existia e você
está fazendo um cadastro dobrado
* Se voce receber um status 202, isso indica criação bem sucedida
"""


def cadastrar_pokemon(nome_treinador, apelido_pokemon, tipo_pokemon, experiencia):
    url = urlBase + tipo_pokemon.lower()
    resp = requests.get(url)
    if resp.status_code != 200:
        raise PokemonNaoExisteException()

    url_treinador = f"{get_treinador}/{nome_treinador}/{apelido_pokemon}"
    resp_treinador = requests.get(url_treinador)

    if resp_treinador.status_code == 200:
        raise PokemonJaCadastradoException("Pokemon já cadastrado")

    else:
        payload = {"tipo": tipo_pokemon, "experiencia": experiencia}
        resp_treinador = requests.put(url_treinador, json=payload)

        if resp_treinador.status_code == 202:
            return True

        if resp_treinador.status_code == 404:
            raise TreinadorNaoCadastradoException("Treinador não cadastrado")

        if resp_treinador.status_code == 409:
            raise PokemonJaCadastradoException()


"""
11. Dado um nome de treinador, um apelido de pokémon e uma quantidade de experiência, localize esse pokémon e acrescente-lhe a experiência ganha.
Dicas ex 11:
utilize a URL {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}/exp
Por exemplo, se for o pokemon com apelido terra
do treinador lucas, a URL ficaria: {site_treinador}/treinador/lucas/terra/exp


Utilize o verbo POST, enviando um arquivo json com a chave experiencia (o valor dessa chave é o tanto de xp que eu quero acrescentar)

Para enviar um request com o verbo post, use requests.post(url,...)

Um cod de status 404 pode significar 2 coisas distintas: ou o treinador não existe,
ou o treinador existe mas o pokemon não. Isso pode verificado acessando a resposta.text
(em vez do usual, que seria resposta.json())

O cod de status de sucesso é o 204
"""


def ganhar_experiencia(nome_treinador, apelido_pokemon, experiencia):

    url = f"{get_treinador}/{nome_treinador}/{apelido_pokemon}/exp"
    result = requests.post(url, json={"experiencia": experiencia})

    if result.status_code == 204:
        return True
    elif result.status_code == 404:
        if "Treinador" in result.text:
            raise TreinadorNaoCadastradoException("Treinador não encontrado!")
        else:
            raise PokemonNaoCadastradoException(
                "Pokémon não cadastrado para este treinador"
            )


"""
Esta classe será utilizada no exercício 12 abaixo.
"""


@dataclass()
class Pokemon:
    nome_treinador: str
    apelido: str
    tipo: str
    experiencia: int
    nivel: int
    cor: str
    evoluiu_de: str


"""
12. Dado um nome de treinador e um apelido de pokémon, localize esse pokémon na API do treinador e retorne um objeto da classe Pokemon, prenchida com os atributos definidos na classe
Dicas 12:
pegar os dados na url "{site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}"
acessada com o verbo GET
para preencher o objeto Pokemon, voce vai fornecer
* nome treinador (veio como argumento da funcao)
* apelido pokemon (veio como argumento da funcao)
* tipo (veio do get que você fez -- chave tipo do dicionário)
* experiencia (veio do request que você fez -- chave experiencia do dicionário)
* nivel do pokemon (calcular usando a pokeapi -- voce ja fez essa funcao, use ela)
* cor do pokemon (em portugues, pegar da pokeapi -- voce ja fez essa funcao, use ela)
* evolucao anterior (pegar da pokeapi -- voce ja fez essa funcao, use ela)
Retornar o objeto pokemon
Erros 404 podem ser treinador nao existe ou pokemon nao existe -- verifique resposta.text para ver qual dos dois -- já fizemos isso antes

para criar o objeto do tipo pokemon, já temos uma classe

Podemos construir um objeto do tipo pokemon assim:

Pokemon(nome_treinador, apelido_pokemon, tipo, experiencia, nivel_do_pokemon(tipo, experiencia), cor_do_pokemon(tipo), evolucao_anterior(tipo))
"""


def localizar_pokemon(nome_treinador, apelido_pokemon):

    url = f"{get_treinador}/{nome_treinador}/{apelido_pokemon}"
    result = requests.get(url)

    if result.status_code == 200:
        dados = result.json()
        tipo = dados["tipo"]
        experiencia = dados["experiencia"]
        nivel = nivel_do_pokemon(tipo, experiencia)
        cor = cor_do_pokemon(tipo)
        evolucao = evolucao_anterior(tipo)
        return Pokemon(
            nome_treinador, apelido_pokemon, tipo, experiencia, nivel, cor, evolucao
        )
    if result.status_code == 404:
        if "Treinador" in result.text:
            raise TreinadorNaoCadastradoException("Treinador não encontrado!")
        else:
            raise PokemonNaoCadastradoException("Pokémon não cadastrado para este treinador")


# Utilize a função localizar_pokemon para encontrar o Pokémon desejado


"""
13. Dado o nome de um treinador, localize-o na API do treinador e retorne um dicionário dos seus pokemons. 
As chaves do dicionário serão os apelidos dos pokémons dele, e os valores serão os tipos (pikachu, bulbasaur ...)
 deles.

Essas informações estão na URL "{site_treinador}/treinador/{nome_treinador}",
acessiveis com o verbo GET
Consulte ela com seu navegador e veja o que tem lá! (talvez você queira usar
as funções anteriores para criar um treinador e seus pokemons...)
"""


def detalhar_treinador(nome_treinador):
    # nome_treinador = nome_treinador.lower()

    url = f"{get_treinador}/{nome_treinador}"
    dado = requests.get(url)
    if dado.status_code == 200:
        result = dado.json()
        pokemons = {}
        for apelido, tipo  in  result['pokemons'].items():
            tipo = tipo['tipo']
            pokemons[apelido] = tipo
        return  pokemons
    else:
        raise TreinadorNaoCadastradoException("Treinador não encontrado!")

"""
14. Dado o nome de um treinador, localize-o na API do treinador e exclua-o, juntamente com todos os seus pokémons.

Usar o verbo delete na url do treinador. A mesma que a gente já usou várias vezes.
O status code vai de informar se o treinador não existia (com qual status code?)

Para enviar um request com o verbo delete, use requests.delete(url)
"""


def excluir_treinador(nome_treinador):
    url = f"{get_treinador}/{nome_treinador}"
    dado = requests.delete(url)
    if dado.status_code == 200:
        return True
    elif dado.status_code == 404:
        raise TreinadorNaoCadastradoException("Treinador não encontrado!")

"""
15. Dado o nome de um treinador e o apelido de um de seus pokémons, localize o pokémon na API do treinador e exclua-o.

Usar o verbo delete na url do pokemon: {site_treinador}/treinador/{nome_treinador}/{apelido_pokemon}
O status code vai de informar se o treinador não existe, ou se o pokemon nao existe 
(status code 404, não deixe de verificar se foi o pokemon ou treinador que não existia)
"""


def excluir_pokemon(nome_treinador, apelido_pokemon):
    # nome_treinador = nome_treinador.lower()

    url = f"{get_treinador}/{nome_treinador}/{apelido_pokemon}"
    dado = requests.delete(url)
    if dado.status_code == 200:
        return True
    if dado.status_code == 404:
        if "Treinador" in dado.text:
            raise TreinadorNaoCadastradoException("Treinador não encontrado!")
        else:
            raise PokemonNaoCadastradoException("Pokémon não cadastrado para este treinador")

# cadastrar_treinador("Ash Ketchum")
# cadastrar_pokemon("Ash Ketchum", "P", "pikachu", 50000)
excluir_pokemon("Ash Ketchum", "P")

"""
O próximo exercício é um desafio, não tem nada a ver com o treinador.py, 
usa somente a pokeapi

16. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
Note que esta função dá como resultado somente o próximo passo evolutivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []

O exercicio 16 é bastante dificil e opcional.
Talvez seja útil procurar e aprender sobre recursão.    
"""
