from config.paths import APKTOOL
from utils.process import run
from apk.procurar import procurar_projeto
#from apk.procurar import procurar_apk_compilado


def recompilar():
    projeto = procurar_projeto()
    print(f"[DEBUG] Projeto selecionado: {projeto}")
    print(f"[DEBUG] Dist: {projeto / 'dist'}")
    print(f"[DEBUG] Dist existe: {(projeto / 'dist').exists()}")

    if projeto is None:
        return

    print(f"Recompilando: {projeto}")

    run([
        "java",
        "-jar",
        APKTOOL,
        "b",
        str(projeto)
    ])

    apk = procurar_projeto()

    if apk is None:
        return

    print(f"APK recompilado: {apk}")