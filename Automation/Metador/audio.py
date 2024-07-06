import pyttsx3

engine = pyttsx3.init()

text = "I am married to Saleha Noorie and my son name is Arsalaan"

engine.say(text)

engine.runAndWait()