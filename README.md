# Comunicação Assistiva

Aplicativo Android desenvolvido com **Python** e **Kivy** para auxiliar pessoas com dificuldades de comunicação por meio de pictogramas e reprodução de áudio.

## Sobre o Projeto

O Comunicação Assistiva é uma ferramenta de Comunicação Aumentativa e Alternativa (CAA) que permite ao usuário expressar necessidades, emoções, condições de saúde e interações sociais através de uma interface simples, intuitiva e visual.

Ao tocar em uma imagem, o aplicativo reproduz um áudio correspondente, facilitando a comunicação com familiares, cuidadores, professores e profissionais da saúde.

## Funcionalidades

* Interface visual simples e acessível
* Navegação por categorias
* Reprodução de áudio ao selecionar um pictograma
* Layout adaptado para dispositivos móveis
* Design com cores terapêuticas
* Transições suaves entre telas
* Funciona offline

## Categorias Disponíveis

### Necessidades

* Água
* Fome
* Banheiro
* Cansado

### Emoções

* Feliz
* Triste
* Bravo
* Assustado

### Saúde

* Dor
* Doente
* Tonto
* Remédio

### Social

* Ajuda
* Abraço
* Brincar
* Conversar

## Tecnologias Utilizadas

* Python
* Kivy
* Buildozer
* Python-for-Android (p4a)

## Estrutura do Projeto

```text
.
├── assets/
│   ├── necessidades.png
│   ├── emocoes.png
│   ├── saude.png
│   ├── social.png
│   └── demais pictogramas
│
├── audios/
│   ├── agua.mp3
│   ├── fome.mp3
│   ├── banheiro.mp3
│   └── demais áudios
│
├── fonts/
│   └── BebasNeue-Regular.ttf
│
├── main.py
├── buildozer.spec
└── README.md
```

## Instalação

### Clonar o repositório

```bash
git clone https://github.com/Iasmim2907/App-Comunica-o-Assistida.git
cd App-Comunica-o-Assistida
```

### Instalar dependências

```bash
pip install kivy
```

### Executar localmente

```bash
python main.py
```

## Gerar APK

### Linux

```bash
buildozer android debug
```

O APK será gerado em:

```text
bin/
```

## Público-Alvo

* Pessoas com Transtorno do Espectro Autista (TEA)
* Pessoas com deficiência na fala
* Crianças em processo de desenvolvimento da comunicação
* Instituições educacionais
* Clínicas e centros terapêuticos

## Objetivo

Promover inclusão, autonomia e acessibilidade por meio da tecnologia, permitindo uma comunicação mais rápida, simples e eficiente.

## Autores

Projeto desenvolvido por:

* Iasmim Silva
* Equipe de Desenvolvimento do Projeto Comunicação Assistiva

## Licença

Este projeto é destinado para fins educacionais e sociais.
