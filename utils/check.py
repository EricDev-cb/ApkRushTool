import sys
import shutil


# verificar
def check_dependencies():
    jadx = shutil.which("jadx")
    pngquant = shutil.which("pngquant")
    java = shutil.which("java")
    if jadx is None:
        print("jadx não encontrado, encerrando...")
    else:
        print(f"jadx encontrado em {jadx}")

    if pngquant is None:
        print("pngquant não encontrado, encerrando...")
        sys.exit(1)
    else:
        print(f"pngquant encontrado em {pngquant}")

    if java is None:
        print("Java não encontrado, encerrando...")
        sys.exit(1)
    else:
        print(f"Java encontrado em {java}")
