import pyttsx3
from config.settings import VOICE_RATE, VOICE_LANGUAGE

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', VOICE_RATE)
    engine.say(text)
    engine.runAndWait()
