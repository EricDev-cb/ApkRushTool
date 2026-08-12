from pathlib import Path 
from config.paths import OUTPUT_DIR
from config.paths import APKTOOL
from utils.process import run
from apk.procurar import procurar_apk_compilado

def recompilar():
    projeto = procurar_projetos()

    if projeto is None:
        return

    print("Recompilando projeto...")
    run([
        "java",
        "-jar",
        APKTOOL,
        "b",
        str(projeto)
    ])
