import unittest
import json
from pprint import pprint
from datetime import datetime


def pega_dados():
    with open("ano2018.json") as f:
        dados = json.load(f)
    return dados


dados2018 = pega_dados()


def nome_do_time(dados, id_numerica):
    # Função que rebece o dicionário dos dados do brasileirão e uma ID
    # e retorna o nome do time cuja ID foi recebido no segundo parâmetro
    times = dados["equipes"]
    for id, nome in times.items():
        if id == id_numerica:
            return nome["nome-comum"]

# print(nome_do_time(dados2018, "695"))

def id_campeao(dados):
    """Função que recebe o dicionario dos dados do brasileirão e
    retorna a ID do time que foi campeao.
    """
    ganhador = dados["fases"]["2700"]["classificacao"]['grupo']["Único"]
      
    if ganhador:
        id_campeao = ganhador[0]
        return id_campeao
    
    
id_campeao(dados2018)
# print(campeao)


def nome_campeao(dados):
    """Funcao que recebe o dicionario dos dados do brasileirão e
    retorna o nome-comum do time que foi campeao.
    """
    times = dados["equipes"]
    ganhador = dados["fases"]["2700"]["classificacao"]['grupo']["Único"]

    for id, nome in times.items():
        if ganhador:
            id_campeao = ganhador[0]
        if id == id_campeao:
            return nome["nome-comum"]
            
nome_campeao(dados2018)


def qtos_libertadores(dados):
    """Função que recebe o dicionário dos dados do brasileirão e
    retorna o número de times que o brasileirão qualifica para a Libertadores,
    obtido a partir dos dados do arquivo JSON.
    """
    libertadores = dados['fases']['2700']['faixas-classificacao']['classifica1']
    faixa = libertadores['faixa']
    inicio, fim = map(int, faixa.split("-"))
    
    return fim - inicio + 1     

def ids_dos_melhor_classificados(dados, n):
    """Função que recebe o dicionário de dados e um número inteiro N e
    retorna uma lista com os IDs dos N times melhor classificados
    """
    id_classificados = dados["fases"]["2700"]["classificacao"]['grupo']["Único"]
   
    return id_classificados[:n]

ids_dos_melhor_classificados(dados2018, 6)


def classificados_libertadores(dados):
    """Função que recebe o dicionário de dados do brasileirão e
    retorna uma lista com os ids dos times classificados para a Libertadores pelo brasileirão
    """
    n = qtos_libertadores(dados)
    return ids_dos_melhor_classificados(dados, n)


def nomes_classificados_libertadores(dados):
    ids_classificados = classificados_libertadores(dados)
    nomes = []
    for id in ids_classificados:
        nomes.append(nome_do_time(dados, id))
    return nomes

def ids_dos_times_de_um_jogo(dados, id_jogo):
    """Função que recebe o dicionário de dados e a ID de um jogo e
    retorna os IDs dos dois times participantes no jogo
    """
    jogos = dados["fases"]["2700"]["jogos"]["id"]
    times = dados["equipes"]
    ids_times = []

    for id in jogos:
        if id == id_jogo:
            time1 = jogos[id]["time1"]
            time2 = jogos[id]["time2"]

            if time1 in times and time2 in times:
                ids_times.append(time1)
                ids_times.append(time2)
                return ids_times

    return None  


def nomes_dos_times_de_um_jogo(dados, id_jogo):
    """Função que recebe o dicionário de dados e a ID de um jogo e
    retorna o nome dos dois times participantes no jogo
    """
    jogos = dados["fases"]["2700"]["jogos"]["id"]
    times = dados["equipes"]
    nomes_times = []

    for id in jogos:
        if id == id_jogo:
            time1 = jogos[id]["time1"] 
            time2 = jogos[id]["time2"] 

            if time1 in times and time2 in times:
                nome_time1 = times[time1]["nome-comum"]
                nome_time2 = times[time2]["nome-comum"]
                nomes_times.append(nome_time1)
                nomes_times.append(nome_time2)
                return nomes_times
    return None

nomes_dos_times_de_um_jogo(dados2018, "102094")


def id_do_time(dados, nome_time):
    """Função que recebe o dicionário de dados e o nome comum de um time e
    retorna a ID do respectivo time.

    Se o nome comum não existir, retorna a string 'nao encontrado'
    """

    times = dados["equipes"]
    for id, name in times.items():
        if name["nome-comum"] == nome_time:
            return id
    return "Nao encontrado"

id_do_time(dados2018, "Fluminense")

def datas_de_jogo(dados):
    """Função que recebe o dicionário de dados e
    retorna uma lista com todas as datas em que houveram jogos.

    DICA: Mantenha as datas no mesmo formato em que se encontram no
    dicionário de dados e busquem em dados['fases']
    """

    datas = dados["fases"]["2700"]["jogos"]["data"]
    lista_datas = []

    for data in datas:
        lista_datas.append(data)
    
    return lista_datas

datas_de_jogo(dados2018)

def data_de_um_jogo(dados, id_jogo):
    '''Função que recebe o dicionario de dados e uma ID de jogo e
    retorna a data em que o jogo ocorreu.

    Se a ID não for válida, retorna a string 'nao encontrado'
    '''
    jogos = dados["fases"]["2700"]["jogos"]["id"]

    for id, jogo in jogos.items():
        if id == id_jogo:
            return jogo["data"]
    
    return 'nao encontrado'

data_de_um_jogo(dados2018, '102132')


def dicionario_id_estadio_e_nro_jogos(dados):
    '''Função que recebe o dicionário de dados e
    retorna outro dicionário contendo a contagem de jogos por estádio.

    Ou seja, as chaves do dicionário de retorno são as IDs dos estádios
    e o valores associados a elas são o número de jogos que ocorreram
    no respectivo estádio.
    '''

    estadios = dados["fases"]["2700"]["jogos"]["id"]
    count = {}

    for id_jogo, info in estadios.items():
        estadio_id = info['estadio_id']
        if estadio_id in count:
            count[estadio_id] += 1
        else:
            count[estadio_id] = 1

    return count

dicionario_id_estadio_e_nro_jogos(dados2018)
      
def busca_imprecisa_por_nome_de_time(dados, nome_parcial_time):
    times = dados["equipes"]
    ids_times_correspondentes = []
   
    for id, time in times.items():
        for campo in ['nome-comum', 'nome-slug', 'sigla', 'nome']:
            if nome_parcial_time.lower() in time[campo].lower():
                ids_times_correspondentes.append(id)
                break  
   
    return ids_times_correspondentes
    pass

busca_imprecisa_por_nome_de_time(dados2018,"Paulo")

def ids_de_jogos_de_um_time(dados, time_id):
    '''Função que recebe o dicionário de dados e a ID de um time e
    retorna uma lista com as IDs de todos os jogos em que o time participou
    '''
    jogo = dados["fases"]["2700"]["jogos"]["id"]

    jogos_time = [jogo_id for jogo_id, jogo_info in jogo.items() if jogo_info['time1'] == time_id or jogo_info['time2'] == time_id]
    return jogos_time

ids_de_jogos_de_um_time(dados2018,'695')


def datas_de_jogos_de_um_time(dados, nome_time):
    '''Função que recebe o dicionário de dados e o nome comum de um time e
    retorna uma lista com as datas em que o time jogou
    '''

    jogos = dados["fases"]["2700"]["jogos"]["id"]
    times = dados["equipes"]
    datas_jogos = []
   
    for jogo_id, jogo in jogos.items():
        for campo in ['time1', 'time2']:
            if jogo[campo] in times:
                nome_time_jogo = times[jogo[campo]]["nome-comum"].lower()
                if nome_time.lower() in nome_time_jogo:
                    datas_jogos.append(jogo['data'])
                    break  # Se encontrou o time, para de procurar no jogo
    return datas_jogos


datas_de_jogos_de_um_time(dados2018, 'Chapecoense')


def dicionario_de_gols(dados):
    '''Função que recebe o dicionário de dados e
    retorna um dicionário com a contagem de gols feitos por cada time.

    Ou seja, as chaves do dicionário de retorno serão os IDs dos times,
    e os valores associados a elas serão a quantidade de gols feitos
    pelo respectivo time.
    '''
    jogo = dados["fases"]["2700"]["jogos"]["id"]
    gols = {}
    for jogo_id, jogo_info in jogo.items():
        if jogo_info['placar1'] is not None:
            gols[jogo_info['time1']] = gols.get(jogo_info['time1'], 0) + int(jogo_info['placar1'])
        if jogo_info['placar2'] is not None:
            gols[jogo_info['time2']] = gols.get(jogo_info['time2'], 0) + int(jogo_info['placar2'])
    return gols

dicionario_de_gols(dados2018)


def time_que_fez_mais_gols(dados):
    '''Função que recebe o dicionário de dados e
    retorna a ID do time que fez o maior número de gols no campeonato'''

    jogo = dados["fases"]["2700"]["jogos"]["id"]
    goals_count = {}
   
    for game_id, game_data in jogo.items():
        team1 = game_data["time1"]
        team2 = game_data["time2"]
        score1 = int(game_data["placar1"])
        score2 = int(game_data["placar2"])
       
        if team1 in goals_count:
            goals_count[team1] += score1
        else:
            goals_count[team1] = score1
       
        if team2 in goals_count:
            goals_count[team2] += score2
        else:
            goals_count[team2] = score2
   
    max_goals_team = max(goals_count, key=goals_count.get)
   
    return max_goals_team

time_que_fez_mais_gols(dados2018)


# def rebaixados(dados):
#     '''Função que recebe o dicionário de dados e
#     retorna uma lista com as IDs dos times rebaixados para a série B
#     '''
#     id_classificados = dados["fases"]["2700"]["classificacao"]['grupo']["Único"]
#     return id_classificados[-4:]

def rebaixados(dados):
    '''Função que recebe o dicionário de dados e
    retorna uma lista com as IDs dos times rebaixados para a série B
    '''
    id_classificados = dados["fases"]["2700"]["classificacao"]['grupo']["Único"]
    
    posicao_rebaixamento = 16
    
    return id_classificados[posicao_rebaixamento:]


print(rebaixados(dados2018))


def classificacao_do_time_por_id(dados, time_id):
    '''Função que recebe o dicionario de dados e uma ID de time e
    retorna a classificacao desse time no campeonato.

    Se a ID não for válida, retorna a string 'nao encontrado'
    '''    
    id_classificados = dados["fases"]["2700"]["classificacao"]['grupo']["Único"]
    for i, jogo in enumerate(id_classificados):
        if jogo == time_id:
            return i + 1
    return 'nao encontrado'

classificacao_do_time_por_id(dados2018, '695')


class TestStringMethods(unittest.TestCase):
    def test_000_nome_do_time(self):
        dados = pega_dados()
        global dados2018
        dados2018 = pega_dados()

        time1 = nome_do_time(dados, '1')
        self.assertEqual(time1, 'Flamengo')
        time2 = nome_do_time(dados, '695')
        self.assertEqual(time2, 'Chapecoense')

    def test_001_id_campeao(self):
        dados = pega_dados()
        try:
            self.assertEqual(id_campeao(dados), '17')
        except NameError as e:
            if 'dados2018' in str(e):
                self.fail(
                    "lembre-se de não usar a variavel dados2018, "
                    "mas sim a variavel dados que a função recebeu")
            else:
                raise e
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(id_campeao(dados), '1')

    def test_002_nome_campeao(self):
        dados = pega_dados()
        self.assertEqual(nome_campeao(dados), 'Palmeiras')
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['classificacao']['grupo']['Único'].pop(0)
        self.assertEqual(nome_campeao(dados), 'Flamengo')

    def test_003_qtos_libertadores(self):
        dados = pega_dados()
        # self.assertEqual('banana','bamana')

        self.assertEqual(qtos_libertadores(dados), 6)
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
        self.assertEqual(qtos_libertadores(dados), 8)

    def test_004_ids_dos_melhor_classificados(self):
        dados = pega_dados()
        self.assertEqual(ids_dos_melhor_classificados(dados, 10), [
                         "17", "1", "15", "13", "24", "4", "3", "9", "5", "22"])
        self.assertEqual(ids_dos_melhor_classificados(
            dados, 5), ["17", "1", "15", "13", "24"])
        self.assertEqual(ids_dos_melhor_classificados(
            dados, 3), ["17", "1", "15"])

    def test_005_classificados_libertadores(self):
        dados = pega_dados()
        self.assertEqual(classificados_libertadores(dados),
                         ["17", "1", "15", "13", "24", "4"])
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
        self.assertEqual(classificados_libertadores(dados), [
                         "17", "1", "15", "13", "24", "4", "3", "9"])

    def test_006_nomes_classificados_libertadores(self):
        dados = pega_dados()
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-3'
        self.assertEqual(nomes_classificados_libertadores(dados), [
                         "Palmeiras", "Flamengo", "Internacional"])

    def test_007_ids_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1, t2 = ids_dos_times_de_um_jogo(dados, '102099')
        self.assertTrue(t1 in ['5', '17'])
        self.assertTrue(t2 in ['5', '17'])
        t1, t2 = ids_dos_times_de_um_jogo(dados, '102109')
        self.assertTrue(t1 in ['1', '26'])
        self.assertTrue(t2 in ['1', '26'])

    def test_008_nomes_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1, t2 = nomes_dos_times_de_um_jogo(dados, '102099')
        self.assertTrue(t1 in ['Botafogo', 'Palmeiras'])
        self.assertTrue(t2 in ['Botafogo', 'Palmeiras'])
        t1, t2 = nomes_dos_times_de_um_jogo(dados, '102106')
        self.assertTrue(t1 in ['Chapecoense', 'Vasco'])
        self.assertTrue(t2 in ['Chapecoense', 'Vasco'])

    def test_009_id_do_time(self):
        dados = pega_dados()
        self.assertEqual(id_do_time(dados, 'Cruzeiro'), '9')
        self.assertEqual(id_do_time(dados, 'Athletico'), '3')

    def test_010_datas_de_jogo(self):
        dados = pega_dados()
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 107)
        self.assertTrue('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_011_datas_de_jogo_teste_2(self):
        dados = pega_dados()
        # deleto a data '14 de abril'
        del dados['fases']['2700']['jogos']['data']['2018-04-14']
        # e todos os jogos que ocorreram nela
        del dados['fases']['2700']['jogos']['id']['102094']
        del dados['fases']['2700']['jogos']['id']['102097']
        del dados['fases']['2700']['jogos']['id']['102101']
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 106)
        self.assertFalse('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_012_data_de_um_jogo(self):
        dados = pega_dados()
        self.assertEqual(data_de_um_jogo(dados, '102132'), '2018-05-06')
        self.assertEqual(data_de_um_jogo(dados, '102187'), '2018-06-06')
        self.assertEqual(data_de_um_jogo(dados, '102540'), 'nao encontrado')

    def test_013_dicionario_id_estadio_e_nro_jogos(self):
        dados = pega_dados()
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'], 16)
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102097']['estadio_id'] = '72'
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'], 17)

    def test_014_busca_imprecisa_por_nome_de_time(self):
        dados = pega_dados()
        ids_times = busca_imprecisa_por_nome_de_time(dados, 'Paulo')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados, 'SPA')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados, 'anto')
        self.assertTrue('22' in ids_times)

    def test_015_ids_de_jogos_de_um_time(self):
        dados = pega_dados()
        jogos_chapeco = ids_de_jogos_de_um_time(dados, '695')
        self.assertEqual(len(jogos_chapeco), 38)
        self.assertTrue('102330' in jogos_chapeco)
        self.assertTrue('102422' in jogos_chapeco)
        jogos_santos = ids_de_jogos_de_um_time(dados, '22')
        self.assertEqual(len(jogos_santos), 38)
        self.assertTrue('102208' in jogos_santos)
        self.assertTrue('102259' in jogos_santos)

    def test_016_datas_de_jogos_de_um_time(self):
        dados = pega_dados()
        datas_santos = datas_de_jogos_de_um_time(dados, 'Santos')
        self.assertEqual(len(datas_santos), 38)
        self.assertTrue('2018-04-21' in datas_santos)
        self.assertTrue('2018-10-13' in datas_santos)
        datas_chapeco = datas_de_jogos_de_um_time(dados, 'Chapecoense')
        self.assertEqual(len(datas_chapeco), 38)
        self.assertTrue('2018-11-25' in datas_chapeco)
        self.assertTrue('2018-12-02' in datas_chapeco)

    def test_017_dicionario_de_gols(self):
        dados = pega_dados()
        dic_gols = dicionario_de_gols(dados)

        self.assertEqual(dic_gols['695'], 34)
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102330']['placar2'] = 1
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 35)
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = 2
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 36)
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = 12
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 46)

    def test_018_time_que_fez_mais_gols(self):
        dados = pega_dados()
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time, '17')
        # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = 120
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time, '695')

    # def test_019_rebaixados(self):
        # dados = pega_dados()
        # self.assertEqual(rebaixados(dados), ['76', '26', '21', '18'])
        # # vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        # dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa'] = '15-20'
        # self.assertEqual(rebaixados(dados), [
        #                  '33', '25', '76', '26', '21', '18'])

    def test_020_classificacao_do_time_por_id(self):
        dados = pega_dados()
        self.assertEqual(classificacao_do_time_por_id(dados, '17'), 1)
        self.assertEqual(classificacao_do_time_por_id(dados, '30'), 11)
        self.assertEqual(classificacao_do_time_por_id(dados, '695'), 14)
        self.assertEqual(classificacao_do_time_por_id(
            dados, '1313'), 'nao encontrado')

    # as próximas funcões nao são testes
    def setUp(self):
        global dados2018
        del dados2018
        return super().setUp()

    def tearDown(self):
        global dados2018
        dados2018 = pega_dados()
        return super().tearDown()


def run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


if __name__ == '__main__':
    run_tests()