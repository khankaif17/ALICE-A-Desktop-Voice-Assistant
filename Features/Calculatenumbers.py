import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolfRamAlpha(Data):
    apikey = "#8224AW-TGLP7KGHRX"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(Data)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(Data):
    Term = str(Data)
    Term = Term.replace("Alice","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")
      