import pyttsx3
import win32clipboard
import speech_recognition as sr
import multiprocessing

import search
import abrirsites as site
import write
import youtube
import jokes
import windowsManipulation as wm

engine = pyttsx3.init();
voices = engine.getProperty('voices');
engine.setProperty('voices', voices[0].id);
engine.setProperty('rate', 180)

def reconhece():
    rec = sr.Recognizer();
    with sr.Microphone() as m:
        rec.adjust_for_ambient_noise(m)
        while True:
            try:
                audio = rec.listen(m)

                entrada = rec.recognize_google(audio, language="pt")
                return entrada
            except sr.UnknownValueError:
                return "O programa não entendeu."

def interruptSpeech():
    interrupt = reconhece()
    if interrupt.lower() == "para inteligência":
        engine.stop()

def execute(oration):
    if "procure por" in oration.lower() or "pesquise" in oration.lower() or "pesquisa" in oration.lower():
        engine.say(search.web(oration.lower()))
        engine.runAndWait();

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
    if ("abra" in oration.lower() or "abre" in oration.lower()):
        a = wm.openPrograms(oration.lower())
        if a == False :
            search.web(oration.lower())

    if "me conte uma piada" in oration.lower():
        engine.say(jokes.get())
        engine.runAndWait()

    if "leia" in oration.lower() or "lê" in oration.lower() or "alheia" in oration.lower() or "ler" in oration.lower():
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if data != "":
            engine.say(data)
            #p1 = multiprocessing.Process(target=interruptSpeech)
            #p1.start()
            #p1.join()
        else:
            engine.say("Não tem nada copiado para mim ler")
        engine.runAndWait()

    if "nada não" in oration.lower():
        print("Otario.")
        continuar = False
