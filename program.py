import pyttsx3

tts = pyttsx3.init()

while True:
    text = input("Wpisz tekst, który ma zostać wypowiedzialny, albo KONIEC żeby zakończyć program: ")
    if text.upper == "KONIEC":
        print("Koniec działania programu.")
        break

    tts.say(text)
    tts.runAndWait()
