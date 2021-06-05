import os
import webbrowser

def web(text):
    research = ""
    assunto = ""
    assuntoNum = 0
    splitted = text.split(" ")

    for i in range(len(splitted)):
        if splitted[i] != 0:
            if splitted[i - 1] == "procure" or splitted[i - 1] == "pesquise":
                assunto = splitted[i]
                assuntoNum = i
                research = research + assunto

    for i in range(len(splitted) - assuntoNum):
        print(splitted[assuntoNum + i])
        if len(splitted) >= assuntoNum + i:
            if splitted[assuntoNum + i] != assunto:
                research = research+" "+splitted[assuntoNum + i]


    if "no google" in text:
        print("gg")
        url = "https://www.google.com/search?q=" + research
    elif "no youtube" in text or "do youtube" in text:
        url = "https://www.youtube.com/results?search_query=" + research
    else:
        url = "https://www.google.com/search?q=" + research
    webbrowser.open(url)
