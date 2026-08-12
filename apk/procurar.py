from pathlib import Path 
from config.paths import OUTPUT_DIR

def procurar_apk_compilado():
    projetos = []

    for pasta in OUTPUT_DIR.iterdir():
        if pasta.is_dir() and (pasta / "apktool.yml").exists():
            projetos.append(pasta)

        if len(projetos) == 0:
            print("Nenhum projeto encontrado.")
            return None

        if len(projetos) > 1:
            print("Existe mais de um projeto.")
            return None

        projeto = projetos[0]

        apks = list((projeto / "dist").glob("*.apk"))

        if len(apks) == 0:
            print("Nenhum APK recompilado encontrado.")
            return None

        return apks[0]
