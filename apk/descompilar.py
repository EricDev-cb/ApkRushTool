# esse arquivo ficara responsavel pela verificação dos apk na pasta apk_dir !
from pathlib import Path
from config.paths import APK_DIR
from config.paths import OUTPUT_DIR
from config.paths import APKTOOL
from utils.process import run

def descompilar():
    apks = list(APK_DIR.glob("*.apk"))
    if len(apks) == 0:
        print("""
1. Coloque o APK na pasta input_apk/
2. Execute o APTool
3. Escolha "Descompilar"1. Coloque o APK na pasta apk/
2. Execute o APTool
3. Escolha "Descompilar"
              """)
    elif len(apks) > 1:
        print("Existe mais de um apk na pasta.")
    else:
        apk = apks[0]
        nome = apk.stem
        saida = OUTPUT_DIR / nome
        saida.mkdir(parents=True, exist_ok=True)
        print(f"Extraindo {apk} aguarde...")
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
        print(comando)
        run([
            "java",
            "-jar",
            APKTOOL,
            "d",
            str(apk),
            "-o",
            str(saida),
            "-f"
            ])

