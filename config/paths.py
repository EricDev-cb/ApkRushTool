# diretorios importantes aqui
import tomllib
from pathlib import Path 
# with open abre um arquivo
# "b" é  o argumento informa como o arquivo sera aberto
with open("config/config.toml", "rb") as arquivo:
    config = tomllib.load(arquivo)

#APKTOOL = "./tools/apktool.jar"
#APKSIGNER = "./tools/apk-signer.jar"
#OUTPUT_DIR = "./output"
#TOOLS_DIR = "./tools"

JAVA = config["tools"]["java"]

JADX = config["tools"]["jadx"]

PNGQ = config["tools"]["pngquant"]

APKTOOL = config["apk"]["apktool"]

SIGNER = config["apk"]["signer"]

OUTPUT_DIR = Path(config["project"]["output"])

APK_DIR = Path(config["apk"]["apk_dir"])

