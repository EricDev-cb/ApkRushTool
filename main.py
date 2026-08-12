# Principal

from utils.process import run
from config.paths import APK_DIR
from utils.check import check_dependencies
from apk.descompilar import descompilar
from apk.recompilar import recompilar
from apk.assinar import assinar
from apk.pngquant.otimizar import otimizar_imagens

import time 

check_dependencies()

time.sleep(1)

run(["clear"])

def menu():
    print("""
========================
                                         
     ▄▄      ▄▄▄▄▄▄     ▄▄▄▄▄▄▄  
   ▄█▀▀█▄   █▀██▀▀▀█▄  █▀▀██▀▀▀▀ 
   ██  ██     ██▄▄▄█▀     ██     
   ██▀▀██     ██▀▀█▄      ██     
 ▄ ██  ██   ▄ ██  ██      ██     
 ▀██▀  ▀█▄█ ▀██▀  ▀██▀    ▀██▄   
        _Apk Rush Tool
                -By Eric.Dev                    
                                 
========================

          01 - Descompilar APK
          02 - Recompilar APK
          03 - Assinar APK
          04 - Otimizar imagens APK
          00 - Fechar menu
          """)

while True:
    time.sleep(1)
    menu()

    opcao = input("Escolha: ")

    match opcao:
        case "1":
            descompilar()

        case "2":
            recompilar()

        case "3":
            assinar()
        case "4":
            otimizar_imagens()

        case "0":
            break

        case _:
            print("Opção invalida !")


