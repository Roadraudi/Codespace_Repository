import time
import winsound
def setAlarm():
    weckzeit = input("Gib deine Uhrzeit an, wann du geweckt werden möchtest. Bitte im Format HH:MM (z.B 23:11): ")
    print(weckzeit)
    return weckzeit

def runAlarm(weckzeit):
    sound_file = "DailyCoding/WeckerSound.mp3"
    go = True
    while go:
        aktuelleZeit = time.strftime("%H:%M")
        if aktuelleZeit == weckzeit:
            print("Aufwachen! Es ist Zeit aufzustehen.")
            #winsound.Beep(500, 100)
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
            break
        time.sleep(1)

action = str(input("Möchtest du einen Wecker stellen: "))

if action in ["Ja", "ja"]:
    alarm_time = setAlarm()
    print("Dein Wecker wurde auf " + str(alarm_time) + " gestellt")
    runAlarm(alarm_time)
else:
    print("Tschüss, bis zum nächsten mal!")
