from config.paths import SIGNER
from utils.process import run
from apk.procurar import procurar_apk_compilado


def assinar():
    apk = procurar_apk_compilado()

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
