# ⚡ ART — APK RUSH TOOL

<p align="center">
  <img src="assets/banner.png" alt="ART Banner" width="800">
</p>

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)
<img src="http://estruyf-github.azurewebsites.net/api/VisitorHit?user=Eric.Dev&repo=https://github.com/EricDev-cb/ApkRushTool&countColorcountColor&countColor=%237B1E7B"/>

ART é uma ferramenta em Python criada para automatizar a modificação de arquivos de aplicativos descompilados (APK), com foco em otimização e criação de versões "lite".

Ela permite aplicar patches em massa, editar arquivos JSON automaticamente, remover recursos pesados e acelerar o processo de modding.

---

## 🚀 Features
- Descompilar e Recompilar apks
- Backup automático antes de qualquer alteração  
- Patch em múltiplos arquivos simultaneamente  
- Scanner inteligente de diretórios  
- Estrutura preparada para novos patches  
- Código simples e fácil de expandir  
- Permite diminuir a qualidade de todas as imagens do apk descompilado
- Ideal para mods de performance
- Suporta adição de patch personalizado em json
---

## 📦 Requisitos

- Python **3.8+**
- Sistema Linux ou Android com termux

Instalação para linux:

```bash
sudo apt install git
git clone https://github.com/EricDev-cb/ApkRushTool.git
cd ApkRushTool
python3 main.py
```
Instalação para Android (Termux)
```bash
pkg install git
git clone https://github.com/EricDev-cb/ApkRushTool.git
cd ApkRushTool
python3 main.py
```
⚠️ Se você estiver usando termux, é necessário mover o apk para o diretório home, caso contrário você não conseguirá recompilar o apk.

## ❤️ Creditos

O ApkRushTool utiliza ferramentas de terceiros:

## Apktool

Apktool é utilizado pelo Apk rush tool para descompilação e recompilação de APKs.

Copyright © Apktool contributors:
- brut.all
- iBotPeaches
- JesusFreke

Licensed under the Apache License, Version 2.0.

https://www.apache.org/licenses/LICENSE-2.0

## Uber APK Signer

Uber APK Signer é utilizado pelo Apk rush tool para assinatura de APKs.

Copyright © 2016 Patrick Favre-Bulle

Licensed under the Apache License, Version 2.0.

https://www.apache.org/licenses/LICENSE-2.0

Source:
https://github.com/patrickfav/uber-apk-signer

# icons do banner por:
Android icon by The Icon Tree - Flaticon:
https://www.flaticon.com/free-icon/technology_15784769?term=android&page=1&position=11&origin=search&related_id=15784769

APK icon by J703 - Flaticon:
https://www.flaticon.com/free-icon/apk-file_18236138?term=apk&page=1&position=5&origin=search&related_id=18236138

## 🤝 Contribuição

Contribuições são bem-vindas!

Se quiser melhorar a ferramenta:

1. Faça um fork
2. Crie uma branch (`git checkout -b feature-minha-ideia`)
3. Commit (`git commit -m 'Minha melhoria'`)
4. Push (`git push origin feature-minha-ideia`)
5. Abra um Pull Request 🚀

Se curtir o projeto, deixa uma ⭐ no repositório!

# FIM !