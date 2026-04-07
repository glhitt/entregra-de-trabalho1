import pyautogui as pyag
import time as tm
import os
from datetime import datetime

hora_atual=datetime.now().strftime("%H")
if hora_atual < ('12'):
    saudacao=('Bom dia')
elif hora_atual < ('18'):
    saudacao=('Boa tarde')
else:
    saudacao=('Boa noite')

nome_cliente=input('Digite seu nome completo: ')
os.system('cls')
cidade_destino=input('Digite a cidade de destino: ')
os.system('cls')
data_inicio_viagem=input('Digite a data de inicio da viagem: ')
os.system('cls')
data_termino_viagem=input('Digite a data de termino da viagem: ')
os.system('cls')
celular=input('Digite seu numero de celular, em formato internacional, sem espaco ou acentos (por exemplo, 5511911111111): ')
os.system('cls')

pyag.press ("win")
tm.sleep(1)
pyag.write ('chrome')
tm.sleep(1)
pyag.press ("enter")
tm.sleep(5)
pyag.hotkey("ctrl", "l")
tm.sleep(1)
pyag.write ('https://chatgpt.com/')
tm.sleep(1)
pyag.press ("enter")
tm.sleep(10)
pyag.write (f'Ola, ChatGPT! Lhe enviarei as seguintes informacoes: nome completo, cidade de destino e data de inicio e termino da viagem. Preciso que voce utilize essas informacoes, pesquisando sobre os principais pontos turisticos, com base na cidade de destino, e quais roupas utilizar nesta cidade. XX' + saudacao + ', Sr(a). ' + nome_cliente + '. Cidade de destino: ' + cidade_destino + '. Data de inicio da viagem: ' + data_inicio_viagem + '. Data de termino da viagem: ' + data_termino_viagem + '. Principais pontos turisticos: (pontos turisticos). Quais roupas utilizar: (roupas a utilizar)XX. Alem disso, quero que voce remova os dois X da mensagem. Por fim, quero que escreva um roteiro semanal, com lugares para se visitar ou recomendacoes no geral. Importante frisar que nao quero que voce escreva NADA, apenas gere um link que contenha, dentro dele, um QR Code, gerado pela API QRServer que, ao escanear, exibe um texto formatado, como um e-Card, com a mensagem solicitada. Entretanto, nao quero que voce encurte este link, mas, sim, envie ele inteiro, para mim, como um link clicavel. Alem disso, nao quero que voce digite nada em sua resposta, apenas o link.')
tm.sleep(5)
pyag.press ("enter")
tm.sleep(30)
pyag.click(611, 296)
tm.sleep(1)
pyag.scroll (-1500)
tm.sleep(1)
pyag.click(1101, 403)
tm.sleep(5)
pyag.press ("tab")
tm.sleep(1)
pyag.press ("tab")
tm.sleep(1)
pyag.press ("enter")