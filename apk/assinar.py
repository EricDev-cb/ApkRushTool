from config.paths import SIGNER
from utils.process import run
#from apk.procurar import procurar_projeto
from apk.procurar import procurar_apk


def assinar():
    apk = procurar_apk()

    if apk is None:
        return

    print(f"Assinando {apk.name}...")

    run([
        "java",
        "-jar",
        SIGNER,
        "sign",
        "--apk",
        str(apk)
    ])
