import webbrowser
def open(text):
    formated = text.replace(" ", ".")
    url = formated.replace("inteligência.abra.o.link.", "").replace("inteligência.abre.o.link.", "").replace("inteligência.abra.o.site.", "").replace("inteligência.abre.o.site.", "")
    webbrowser.open("https://" + url)
