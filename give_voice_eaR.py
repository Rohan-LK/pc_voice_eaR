import pyttsx3
import speech_recognition as sr

# MACHINE_VOICE
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# SPEAK DEFINITIONS
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("CompteR: ", audio)

# TAKE COMMAND DEFINITION
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1.0
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
    except Exception as e:
        print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query

# ROHAN LAL KSHETRY