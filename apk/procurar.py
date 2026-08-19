from config.paths import OUTPUT_DIR
from config.paths import APK_DIR


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

def procurar_apk():
    apks = list(APK_DIR.glob("*.apk"))

    if len(apks) == 0:
        print("Nenhum APK encontrado !")
        return None
    if len(apks) == 1:
        return apks[0]

    print("APKs encontrados:\n")

    for i, apk in enumerate(apks, start=1):
        print(f"[{i}] {apk.name}")

    print("[0] Voltar")

    while True:
        try:
            escolha = int(input("\nEscolha um apk: "))

            if escolha == 0:
                return None

            if 1 <= escolha <= len(apks):
                return apks [escolha - 1]

            print("Opção inválida !")

        except ValueError:
            print("Digite um numero.")