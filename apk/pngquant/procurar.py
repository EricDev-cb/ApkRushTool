import os
from config.paths import OUTPUT_DIR


def procurar_projeto():
    projetos = []

    for pasta in OUTPUT_DIR.iterdir():
        if pasta.is_dir() and (pasta / "apktool.yml").exists():
            projetos.append(pasta)

    if not projetos:
        print("Nenhum projeto encontrado.")
        return None

    if len(projetos) == 1:
        return projetos[0]

    print("Projetos encontrados:\n")

    for i, projeto in enumerate(projetos, start=1):
        print(f"[{i}] {projeto.name}")

    while True:
        try:
            escolha = int(input("\nEscolha um projeto: "))

            if 1 <= escolha <= len(projetos):
                return projetos[escolha - 1]

            print("Opção inválida.")

        except ValueError:
            print("Digite um número.")


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