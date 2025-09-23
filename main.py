import win32com.client as wincom #for text-to-speech #pip install pywin32 #pyWin32 will directly speak the text using the built-in microsoft engine

if __name__ == '__main__':

    print("Welcome to Robo Speaker 1.1. Created by Krupali")

    while True:

        x = input("Enter what you what me to speak: ")

        if x == "q":

            speak = wincom.Dispatch("SAPI.SpVoice") #creates the voice dispatcher object
            speak.speak("bye bye friend") #send the text to be spoken to the dispatcher object

            break

        speak = wincom.Dispatch("SAPI.SpVoice") #creates the voice dispatcher object
        speak.speak(f"{x}") #send the text to be spoken to the dispatcher object