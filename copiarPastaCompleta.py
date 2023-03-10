#Exemplo de como copiar uma pasta completa pela Wi-fi
import os
import shutil
import ctypes
from tqdm import tqdm
import time

#cxfreeze CopiarTodaPasta.py --target-dir CopiarTodaPasta

try:
    print('')
    #Primeiro vou acessar a wi-fi
    os.system('netsh wlan add profile filename=avell-infra-ultra.xml')
    # Esperar enquanto a wi-fi reage -5 segundos
    for i in tqdm(range(5)):
        time.sleep(1)

    #Agora vou trazer toda a pasta para a máquina
    shutil.copytree('\\\\avellweb\\ProjetosOK\\2-PROJETOS_DESENVOLVIMENTO\\1.2-TESTES_AVELL\\TESTES_AVELL', 'C:\\Temp\\TESTES_AVELL')

except:
    print('Não foi possivel copiar a pasta ou ela já existe e não foi possivel sobrescrever!')