import speech_recognition as sr

import search
import abrirsites as site
import write
import youtube
import windowsManipulation as wm

def reconhece():
    print("Espere...")
    rec = sr.Recognizer();
    with sr.Microphone() as m:
        rec.adjust_for_ambient_noise(m)
        while True:
            try:
                print("Fale teu comando.")
                audio = rec.listen(m)

                entrada = rec.recognize_google(audio, language="pt")
                return entrada
            except sr.UnknownValueError:
                return "O programa não entendeu."

oration = reconhece()

continuar = True

while continuar:
    oration = reconhece()
    print(oration)
    if oration.lower() == "minha inteligência":
        print("O programa está pronto para executar um comando.")
        oration = reconhece()

        if "procure por" in oration.lower() or "pesquise" in oration.lower():
            search.web(oration.lower())

        if "abra um vídeo sobre" in oration.lower():
            search.web(oration.lower())

        if oration.lower() == "nada não":
            print("Otario.")
            continuar = False

    elif "minha inteligência" in oration.lower() or "inteligência" in oration.lower():
        if "procure por" in oration.lower() or "pesquise" in oration.lower():
            search.web(oration.lower())

        if "abra um vídeo sobre" in oration.lower():
            search.web(oration.lower())

        if "abra o link" in oration.lower() or "abre o link" in oration.lower() or "abra o site" in oration.lower() or "abre o site" in oration.lower():
            site.open(oration.lower())

        if "escreva" in oration.lower():
            write.escrever(oration.lower())

        if "da play" in oration.lower() or "da pause" in oration.lower():
            youtube.playPause()

        if "diminui o volume" in oration.lower() or "diminua o volume" in oration.lower():
            wm.diminuiVolume(oration.lower())

        if "aumenta o volume" in oration.lower() or "aumente o volume" in oration.lower():
            wm.aumentaVolume(oration.lower())

        if "feche" in oration.lower() or "fecha" in oration.lower():
            wm.closePrograms(oration.lower())
        if ("abra" in oration.lower() or "abre" in oration.lower()) & ("link" in oration.lower() != True or "site" in oration.lower() != True):
            wm.openPrograms(oration.lower())

        if "nada não" in oration.lower():
            print("Otario.")
            continuar = False
