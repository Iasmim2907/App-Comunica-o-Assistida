# Comunicação Assistiva AAC

## Descrição

Aplicação mobile desenvolvida em Python utilizando o framework Kivy, voltada para Comunicação Aumentativa e Alternativa (AAC) com foco em usuários autistas não verbais.

O sistema permite a comunicação por meio de cartões visuais interativos associados à reprodução de áudio, oferecendo uma interface acessível, intuitiva e adaptada para dispositivos móveis.

---

# Objetivos

O projeto possui como principais objetivos:

* Facilitar a comunicação de usuários não verbais;
* Oferecer uma interface visual simplificada;
* Minimizar barreiras de interação;
* Disponibilizar um sistema leve e executável em dispositivos Android;
* Estruturar uma base escalável para futuras funcionalidades AAC.

---

# Funcionalidades

## Comunicação por cartões visuais

Cada ação do usuário é representada por:

* imagem ilustrativa;
* legenda textual;
* reprodução de áudio correspondente.

---

## Organização por categorias

Os elementos de comunicação são separados em categorias semânticas:

* Necessidades;
* Emoções;
* Saúde;
* Social.

---

## Reprodução de áudio

O aplicativo utiliza arquivos de áudio locais para garantir:

* baixa latência;
* funcionamento offline;
* maior estabilidade.

---

## Interface terapêutica

A interface foi projetada considerando:

* paleta de cores suaves;
* contraste adequado;
* elementos visuais grandes;
* organização simplificada;
* legibilidade ampliada.

---

## Navegação simplificada

O fluxo de navegação foi reduzido para minimizar carga cognitiva e facilitar o uso independente.

---

# Tecnologias Utilizadas

| Tecnologia     | Finalidade                        |
| -------------- | --------------------------------- |
| Python         | Linguagem principal               |
| Kivy           | Interface gráfica multiplataforma |
| Buildozer      | Geração de APK Android            |
| Plyer          | Recursos nativos do dispositivo   |
| GitHub Actions | Automação de build                |

---

# Estrutura do Projeto

```plaintext
projeto/
│
├── main.py
│
├── assets/
│   ├── agua.png
│   ├── fome.png
│   └── ...
│
├── audios/
│   ├── agua.mp3
│   ├── fome.mp3
│   └── ...
│
├── fonts/
│   └── BebasNeue-Regular.ttf
│
└── buildozer.spec
```

---

# Arquitetura

O sistema é baseado em:

* `ScreenManager` para gerenciamento de telas;
* componentes personalizados reutilizáveis;
* carregamento dinâmico de categorias;
* renderização responsiva com Kivy.

---

# Estrutura das Categorias

Cada categoria é definida por:

```python
categorias = {
    "Categoria": [
        ("Legenda", "imagem", "audio.mp3")
    ]
}
```

---

# Execução Local

## Instalação das dependências

```bash
pip install kivy
```

---

## Execução do projeto

```bash
python main.py
```

---

# Geração de APK Android

O projeto é compatível com:

* Buildozer;
* GitHub Actions;
* ambientes Linux/WSL.

---

# Requisitos

## Python

* Python 3.10+

## Dependências

* kivy
* pillow
* plyer

---

# Diretrizes de Interface

A interface foi construída seguindo princípios relacionados a:

* acessibilidade;
* comunicação alternativa;
* redução de estímulos excessivos;
* organização visual;
* feedback tátil e visual.

---

# Melhorias Futuras

## Funcionalidades planejadas

* sistema PECS completo;
* construção dinâmica de frases;
* síntese de voz offline;
* múltiplos perfis de usuário;
* sincronização em nuvem;
* histórico de comunicação;
* sistema de favoritos;
* vibração háptica;
* suporte multilíngue;
* modo escuro;
* analytics de uso.

---

# Escalabilidade

A arquitetura atual permite:

* expansão modular;
* separação futura em múltiplos arquivos;
* integração com APIs externas;
* persistência local de dados;
* adaptação para tablets.

---

# Licença

Este projeto está licenciado sob a licença MIT.

---

