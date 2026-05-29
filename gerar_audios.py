from gtts import gTTS
import os
import time


frases = {
    "agua": "Estou com sede",
    "fome": "Estou com fome",
    "banheiro": "Preciso ir ao banheiro",
    "cansado": "Estou cansado",

    "feliz": "Estou feliz",
    "triste": "Estou triste",
    "bravo": "Estou bravo",
    "medo": "Estou com medo",

    "dor": "Estou sentindo dor",
    "doente": "Não estou me sentindo bem",
    "tonto": "Estou tonto",
    "remedio": "Preciso do meu remédio",

    "ajuda": "Preciso de ajuda",
    "abraco": "Quero um abraço",
    "brincar": "Quero brincar",
    "conversar": "Quero conversar"
}


os.makedirs("audios", exist_ok=True)

for nome, texto in frases.items():
    try:
        print(f"Gerando {nome}...")

        tts = gTTS(
            text=texto,
            lang="pt-br",
            slow=False
        )

        tts.save(f"audios/{nome}.mp3")

        time.sleep(2)

    except Exception as e:
        print(f"Erro em {nome}: {e}")

print("Áudios gerados.")