from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
import os
import psutil

def diminuiVolume(text):
    splitted = text.split(" ")
    numero = 0
    if splitted[4] == 'em':
        numero = int(splitted[5])
    elif splitted[3] == 'volume':
        numero = int(splitted[4])

    while (volume.GetMasterVolumeLevel() - numero * 0.15) <= -64:
        numero+=1

    volume.SetMasterVolumeLevel(volume.GetMasterVolumeLevel() - numero * 0.15, None)

    print(volume.GetVolumeRange())
def aumentaVolume(text):
    splitted = text.split(" ")
    numero = 0
    for i in range(len(splitted)):
        if splitted[i - 1] == "em":
            numero = int(splitted[i])

    while (volume.GetMasterVolumeLevel() + numero * 0.15) > 0:
        numero-=1
    volume.SetMasterVolumeLevel(volume.GetMasterVolumeLevel() + numero * 0.15, None)

def GetTaskExe(text):

    if text == "chrome" or text == "google chrome":
        return "chrome.exe"
    if text == "ópera" or text == "ópera gx" or text == "oópera" or text == "pera":
        return "opera.exe"
    if text == "steam":
        return "steam.exe"
    else:
        return text + ".exe"



def closePrograms(text):

    task = ""
    taskName = ""
    nameNum = 0
    splitted = text.split(" ")

    for i in range(len(splitted)):
        if splitted[i] != 0:
            if splitted[i - 1] == "programa" or splitted[i - 1] == "o" or ((splitted[i - 1] == "fecha") & (splitted[i] != "o")) or ((splitted[i - 1] == "feche") & (splitted[i] != "o")) or splitted[i - 1] == "ou":
                taskName = splitted[i]
                nameNum = i
                task = task + taskName

    for i in range(len(splitted) - nameNum):
        print(splitted[nameNum + i])
        if len(splitted) >= nameNum + i:
            if splitted[nameNum + i] != taskName:
                task = task+" "+splitted[nameNum + i]

    print(task)
    taskExe = GetTaskExe(task)

    os.system("taskkill /f " + taskExe)

def openPrograms(text):
    programsNames = os.listdir(r"C:\Users\aliss\AppData\Roaming\Microsoft\Windows\Start Menu\Programs")

    program = ""
    programName = ""
    programNum = 0
    splitted = text.split(" ")

    for i in range(len(splitted)):
        if splitted[i] != 0:
            if splitted[i - 1] == "programa" or splitted[i - 1] == "o" or splitted[i - 1] == "ou":
                programName = splitted[i]
                programNum = i
                program = program + programName

    for i in range(len(splitted) - programNum):
        print(splitted[programNum + i])
        if len(splitted) >= programNum + i:
            if splitted[programNum + i] != programName:
                program = program+" "+splitted[programNum + i]

    print(program)
    print(programsNames)

    os.system(r"cd C:\Users\aliss\AppData\Roaming\Microsoft\Windows\Start Menu\Programs")
    for programName in programsNames:
        if program.replace("program" , "") in programName.lower():
            if ".lnk" in programName:
                print('"'+programName+'"')
                os.startfile (r"C:\Users\aliss\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\\" + programName)

            else:
                print("vai entrar em " + programName)
                programsNames2 = os.listdir(r"C:\Users\aliss\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\\" + programName)
                dir = r"C:\Users\aliss\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\\" + programName + "\\"
                for programName in programsNames2:
                    if program in programName.lower():
                        os.startfile (dir + programName)
