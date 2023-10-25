import os
import speech_recognition as sr
import pyttsx3


def speak(text):
    e = pyttsx3.init()
    e.say(text)
    e.runAndWait()

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command



def open_application(command):
    if ("don't" in command or "never" in command) and ("notepad" in command):
        print("OK")

    elif("run" in command or "launch" in command or "execute" in command or "open" in command) and ("notepad" in command):
        os.system("notepad")
        speak("Opening Notepad")
    else:
        print("Command not recognized.")

if __name__ == "__main__":
    print("HI I AM YOUR VOICE ASSISTANT")
    speak("HI I AM YOUR VOICE ASSISTANT")
    print()
    print("HOW CAN I HELP YOU ")
    speak("HOW CAN I HELP YOU ")
    while True:
        command = listen_for_command()
        if "exit" in command:
            speak("Exiting the program.")
            break
        else:
            open_application(command)