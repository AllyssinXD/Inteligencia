import speech_recognition as sr
import pyttsx3
import win32clipboard

import commands

engine = pyttsx3.init();
voices = engine.getProperty('voices');
engine.setProperty('voices', voices[0].id);
engine.setProperty('rate', 180)

print("Vozes disponiveis : \n" + voices[0].id +"\n"+ voices[1].id)

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
continuar = True

while continuar:
    oration = reconhece()
    print(oration)
    if oration.lower() == "inteligência":
        engine.say("Pode falar")
        engine.runAndWait();
        oration = reconhece()
        commands.execute(oration)

    elif "minha inteligencia" in oration.lower() or "inteligência" in oration.lower():
        commands.execute(oration)
