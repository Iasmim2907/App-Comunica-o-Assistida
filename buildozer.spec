[app]

# Nome exibido no Android
title = Comunicacao Assistiva

# Nome interno do pacote
package.name = comunicador

# Identificador único
package.domain = org.davi

# Diretório do código
source.dir = .

# Arquivos incluídos
source.include_exts = py,png,jpg,jpeg,mp3,ttf,kv

# Arquivos a excluir
source.exclude_dirs = .git,__pycache__,.venv

# Versão do aplicativo
version = 1.0

# Dependências Python
requirements = python3==3.14.2,kivy==2.3.1,pillow==11.2.1

# Orientação
orientation = portrait

# Tela cheia
fullscreen = 0

# Permissões
android.permissions = INTERNET

# Configuração Android
android.api = 33
android.minapi = 21
android.ndk = 25c

# Aceitar licenças automaticamente
android.accept_sdk_license = True

# Ícone do aplicativo
icon.filename = assets/icon.png

[buildozer]

log_level = 2
warn_on_root = 1
