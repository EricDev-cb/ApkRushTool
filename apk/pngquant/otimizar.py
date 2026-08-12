from .procurar import procurar_projeto
from .procurar import encontrar_imagens
from .comprimir import comprimir_png


def otimizar_imagens():
    projeto = procurar_projeto()

    if projeto is None:
        return

    imagens = encontrar_imagens(projeto)

    for imagem in imagens:
        if imagem.lower().endswith(".png"):
            comprimir_png(imagem)