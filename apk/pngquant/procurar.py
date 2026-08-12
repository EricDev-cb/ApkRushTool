import os
from config.paths import OUTPUT_DIR


def procurar_projeto():
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

    return projetos[0]


def encontrar_imagens(pasta):
    extensoes = (".png", ".jpg", ".jpeg")
    arquivos = []

    for root, dirs, files in os.walk(pasta):
        for arquivo in files:

            if arquivo.endswith(".9.png"):
                continue

            if arquivo.lower().endswith(extensoes):
                arquivos.append(os.path.join(root, arquivo))

    return arquivos