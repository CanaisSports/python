from iqoptionapi.stable_api import IQ_Option
from colorama import init, Fore, Back
import time, json, logging, configparser
from datetime import datetime, date, timedelta
from dateutil import tz
import sys

#Dados candles ultimas 100 barras

open,close,max,min,volume,times = API.edsg_get_over_candles_return_all(1,100,config['paridade'],60)

def configuracao():
    arquivo = configparser.RawConfigParser()
    arquivo.read('config.txt')  
        
    return {'inverter_sinal': arquivo.get('GERAL', 'inverter_sinal'),'op_binario_turbo': arquivo.get('GERAL', 'op_binario_turbo'),'op_digital': arquivo.get('GERAL', 'op_digital'),'op_binario': arquivo.get('GERAL', 'op_binario'),'seguir_ids': arquivo.get('GERAL', 'seguir_ids'),'stop_win': arquivo.get('GERAL', 'stop_win'), 'stop_loss': arquivo.get('GERAL', 'stop_loss'), 'payout': 0, 'banca_inicial': banca(), 'filtro_diferenca_sinal': arquivo.get('GERAL', 'filtro_diferenca_sinal'), 'martingale': arquivo.get('GERAL', 'martingale'), 'sorosgale': arquivo.get('GERAL', 'sorosgale'), 'niveis': arquivo.get('GERAL', 'niveis'), 'filtro_pais': arquivo.get('GERAL', 'filtro_pais'), 'filtro_top_traders': arquivo.get('GERAL', 'filtro_top_traders'), 'valor_minimo': arquivo.get('GERAL', 'valor_minimo'), 'paridade': arquivo.get('GERAL', 'paridade'), 'valor_entrada': arquivo.get('GERAL', 'valor_entrada'), 'timeframe': arquivo.get('GERAL', 'timeframe'), 'tipo_martingale': arquivo.get('GERAL', 'tipo_martingale'), 'taxa_martingale': arquivo.get('GERAL', 'taxa_martingale')}

logging.disable(level=(logging.DEBUG))
init(convert=True, autoreset=True)

API = IQ_Option('rodrigo.ramilo@hotmail.com','R0dr1g0')
API.connect()

API.change_balance('PRACTICE') # PRACTICE / REAL
 
print(Fore.CYAN + '\nRobo Rodrigo R. Bernardo')
print(Fore.CYAN + 'Versão: 2.0')
 
while True: # Responsável pela conexão com a IQOPTION
    if API.check_connect() == False:
        print(Fore.RED + 'Falha ao se Conectar....')
        
        API.connect()
    else:
        print(Fore.GREEN + '\nConectado com Sucesso')
        break
    
    time.sleep(1)
        
def banca():
    return API.get_balance()
       
def entradas_digital(config, entrada, direcao, timeframe):

#
# condicao de compra ou venda seria aqui danrley ai preciso puxar
# um canal de keltner 
#
# 
        id = API.buy_digital_spot(config['paridade'], entrada, direcao, timeframe) # ENTRADAS DIGITAL
        