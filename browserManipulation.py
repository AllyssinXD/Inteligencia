from selenium import webdriver

browser = webdriver.Opera('c:/Users/aliss/Downloads/operadriver.exe')

def selectElement(text):
    splitted = text.split(" ")
    element = ""
    assunto = ""
    assuntoNum = 0
    splitted = text.split(" ")

    for i in range(len(splitted)):
        if splitted[i] != 0:
            if splitted[i - 1] == "em" or splitted[i - 1] == "clique":
                assunto = splitted[i]
                assuntoNum = i
                element = element + assunto

    for i in range(len(splitted) - assuntoNum):
        print(splitted[assuntoNum + i])
        if len(splitted) >= assuntoNum + i:
            if splitted[assuntoNum + i] != assunto:
                element = element+" "+splitted[assuntoNum + i]

    element = browser.find_element_by_link_text("assunto")
    element.click()
