# esse arquivo ficara responsavel pela verificação dos apk na pasta apk_dir !
from pathlib import Path
from config.paths import APK_DIR
from config.paths import OUTPUT_DIR
from config.paths import APKTOOL
from utils.process import run
from apk.procurar import procurar_apk

def descompilar():
    apk = procurar_apk()

    if apk is None:
        return

    nome = apk.stem
    saida = OUTPUT_DIR / nome

    saida.mkdir(parents=True, exist_ok=True)

    comando = [
        "java",
        "-jar",
        APKTOOL,
        "d",
        str(apk),
        "-o",
        str(saida),
        "-f"
    ]

    run(comando)