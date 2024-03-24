import unittest
import json
from pprint import pprint
from datetime import datetime


def pega_dados():
    with open("ano2018.json") as f:
        dados = json.load(f)
    return dados


dados2018 = pega_dados()

def datas_de_jogos_de_um_time(dados, nome_time):
    '''Função que recebe o dicionário de dados e o nome comum de um time e
    retorna uma lista com as datas em que o time jogou
    '''

    jogos = dados["fases"]["2700"]["jogos"]["id"]
    times = dados["equipes"]
    datas_jogos = []
   
    for jogo_id, jogo_info in jogos.items():
        for campo in ['time1', 'time2']:
            if jogo_info[campo] in times:
                nome_time_jogo = times[jogo_info[campo]]["nome-comum"].lower()
                if nome_time.lower() in nome_time_jogo:
                    datas_jogos.append(jogo_info['data'])
                    break  # Se encontrou o time, para de procurar no jogo
    return datas_jogos


print(datas_de_jogos_de_um_time(dados2018, 'Chapecoense'))


