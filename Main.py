from kivy.config import Config

# -------------------------
# TAMANHO DA JANELA
# -------------------------
Config.set('graphics', 'width', '430')
Config.set('graphics', 'height', '850')

# -------------------------
# IMPORTS
# -------------------------
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, RoundedRectangle


# -------------------------
# PALETA TERAPÊUTICA
# -------------------------
CORES = {

    # fundo azul terapêutico
    "fundo": (.90, .94, .98, 1),

    # cores pastel suaves
    "Necessidades": (.80, .90, 1, 1),

    "Emoções": (.90, .84, .98, 1),

    "Saúde": (.82, .95, .86, 1),

    "Social": (.99, .90, .80, 1),

    # texto
    "texto": (.20, .24, .32, 1),

    # sombra
    "sombra": (0, 0, 0, 0.10),

    # voltar
    "voltar": (.82, .88, .96, 1)
}


# -------------------------
# FONTE PERSONALIZADA
# -------------------------
FONTE = "fonts/BebasNeue-Regular.ttf"


# -------------------------
# DADOS
# -------------------------
categorias = {

    "Necessidades": [

        ("ÁGUA", "agua", "audios/agua.mp3"),
        ("FOME", "fome", "audios/fome.mp3"),
        ("BANHEIRO", "banheiro", "audios/banheiro.mp3"),
        ("CANSADO", "cansado", "audios/cansado.mp3")
    ],

    "Emoções": [

        ("FELIZ", "feliz", "audios/feliz.mp3"),
        ("TRISTE", "triste", "audios/triste.mp3"),
        ("BRAVO", "bravo", "audios/bravo.mp3"),
        ("ASSUSTADO", "medo", "audios/medo.mp3")
    ],

    "Saúde": [

        ("DOR", "dor", "audios/dor.mp3"),
        ("DOENTE", "doente", "audios/doente.mp3"),
        ("TONTO", "tonto", "audios/tonto.mp3"),
        ("REMÉDIO", "remedio", "audios/remedio.mp3")
    ],

    "Social": [

        ("AJUDA", "ajuda", "audios/ajuda.mp3"),
        ("ABRAÇO", "abraco", "audios/abraco.mp3"),
        ("BRINCAR", "brincar", "audios/brincar.mp3"),
        ("CONVERSAR", "conversar", "audios/conversar.mp3")
    ]
}


# -------------------------
# CARD CLICÁVEL
# -------------------------
class CardBotao(ButtonBehavior, BoxLayout):

    def __init__(self, cor_categoria, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.padding = 12

        self.spacing = 8

        with self.canvas.before:

            # sombra
            Color(*CORES["sombra"])

            self.sombra = RoundedRectangle(
                radius=[40]
            )

            # card colorido
            Color(*cor_categoria)

            self.card = RoundedRectangle(
                radius=[40]
            )

        self.bind(
            pos=self.update_canvas,
            size=self.update_canvas
        )

    def update_canvas(self, *args):

        # sombra
        self.sombra.pos = (
            self.x,
            self.y - 5
        )

        self.sombra.size = self.size

        # card
        self.card.pos = self.pos
        self.card.size = self.size


# -------------------------
# MENU PRINCIPAL
# -------------------------
class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        # fundo
        with root.canvas.before:

            Color(*CORES["fundo"])

            self.rect = RoundedRectangle()

        root.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

        # título
        titulo = Label(

            text="Comunicação Assistiva",

            font_size=30,

            bold=True,

            font_name=FONTE,

            color=CORES["texto"],

            size_hint=(1, .12)
        )

        root.add_widget(titulo)

        # grid categorias
        grid = GridLayout(

            cols=2,

            spacing=20
        )

        for categoria in categorias.keys():

            btn = Button(

                text=categoria,

                font_size=24,

                bold=True,

                font_name=FONTE,

                background_normal="",

                background_color=CORES[categoria],

                color=CORES["texto"]
            )

            btn.bind(
                on_press=lambda x, cat=categoria:
                self.abrir_categoria(cat)
            )

            grid.add_widget(btn)

        root.add_widget(grid)

        self.add_widget(root)

    def update_rect(self, instance, value):

        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def abrir_categoria(self, categoria):

        self.manager.current = categoria


# -------------------------
# TELA CATEGORIA
# -------------------------
class CategoriaScreen(Screen):

    def __init__(self, nome_categoria, **kwargs):
        super().__init__(
            name=nome_categoria,
            **kwargs
        )

        root = BoxLayout(

            orientation="vertical",

            padding=15,

            spacing=15
        )

        # fundo
        with root.canvas.before:

            Color(*CORES["fundo"])

            self.rect = RoundedRectangle()

        root.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

        # título
        titulo = Label(

            text=nome_categoria,

            font_size=28,

            bold=True,

            font_name=FONTE,

            color=CORES["texto"],

            size_hint=(1, .10)
        )

        root.add_widget(titulo)

        # grid cards
        grid = GridLayout(

            cols=2,

            spacing=18,

            size_hint=(1, .80)
        )

        # -------------------------
        # CARDS
        # -------------------------
        for texto, imagem, audio in categorias[nome_categoria]:

            card = CardBotao(
                CORES[nome_categoria]
            )

            # clique
            card.bind(
                on_press=lambda x, a=audio:
                self.tocar_audio(a)
            )

            # -------------------------
            # CONTAINER CENTRALIZADOR
            # -------------------------
            container_imagem = AnchorLayout(

                anchor_x='center',

                anchor_y='center',

                size_hint=(1, .78)
            )

            # -------------------------
            # IMAGEM
            # -------------------------
            img = Image(

                source=f"assets/{imagem}.png",

                size_hint=(.82, .82),

                pos_hint={
                    "center_x": .5,
                    "center_y": .5
                }
            )

            container_imagem.add_widget(img)

            # -------------------------
            # LEGENDA
            # -------------------------
            legenda = Label(

                text=texto,

                font_size=22,

                bold=True,

                font_name=FONTE,

                color=CORES["texto"],

                size_hint=(1, .18)
            )

            # adiciona elementos
            card.add_widget(container_imagem)
            card.add_widget(legenda)

            grid.add_widget(card)

        root.add_widget(grid)

        # -------------------------
        # BOTÃO VOLTAR
        # -------------------------
        voltar = Button(

            text="⬅ Voltar",

            size_hint=(1, .10),

            font_size=22,

            bold=True,

            font_name=FONTE,

            background_normal="",

            background_color=CORES["voltar"],

            color=CORES["texto"]
        )

        voltar.bind(
            on_press=lambda x:
            self.voltar()
        )

        root.add_widget(voltar)

        self.add_widget(root)

    def update_rect(self, instance, value):

        self.rect.pos = instance.pos
        self.rect.size = instance.size

    # -------------------------
    # TOCAR ÁUDIO
    # -------------------------
    def tocar_audio(self, caminho):

        som = SoundLoader.load(caminho)

        if som:
            som.play()

    # -------------------------
    # VOLTAR
    # -------------------------
    def voltar(self):

        self.manager.current = "menu"


# -------------------------
# APP PRINCIPAL
# -------------------------
class ComunicadorApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(
            MenuScreen(name="menu")
        )

        for categoria in categorias.keys():

            sm.add_widget(
                CategoriaScreen(categoria)
            )

        return sm


# -------------------------
# EXECUTAR APP
# -------------------------
if __name__ == "__main__":

    ComunicadorApp().run()