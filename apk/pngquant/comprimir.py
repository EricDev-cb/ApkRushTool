import os
import shutil
import subprocess


def comprimir_png(img):
    backup = img + ".bak"
    shutil.copy2(img, backup)

    tamanho_antes = os.path.getsize(img)

    print(f"[>] Comprimindo: {img}")

    resultado = subprocess.run(
        [
            "pngquant",
            "--force",
            "--output", img,
            "--quality=20-40",
            "--colors=64",
            img,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )

    if resultado.returncode != 0:
        os.replace(backup, img)

        print(f"[!] Falha: {img}")

        if resultado.stderr:
            print(f"    {resultado.stderr.strip()}")

        return False

    tamanho_depois = os.path.getsize(img)

    if tamanho_depois >= tamanho_antes:
        os.replace(backup, img)

        print(f"[-] Sem redução: {img}")

        return False

    os.remove(backup)

    economia = tamanho_antes - tamanho_depois

    print(
        f"[+] {img} "
        f"({tamanho_antes / 1024:.1f} KB → "
        f"{tamanho_depois / 1024:.1f} KB)"
    )

    print(f"    Economia: {economia / 1024:.1f} KB")

    return True