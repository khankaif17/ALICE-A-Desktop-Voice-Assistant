#target
#hindi and english command
#say english and hindi both and it will listen in english and give the ans


###commands to run
# step 1 
# pip install googletrans==3.1.0a0 install it in your cmd
# step 2
# three function 
# listen function
# # english function 
# # connect


import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator

# function 1
def Listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source,0,5) #listening mode .....stuck... type the number 

        try:
            print("Recognizing....")
            query=r.recognize_google(audio,language="hi")
        except:
            return""
        
        query=str(query).lower()
        return query

# function 2
def TranslationHintoEng(Text):
    line=str(Text)
    translate=Translator()
    result=translate.translate(line)
    data=result.text
    print(f"you :{data}.")
    return data

#function 3
def MicExecution():
    query=Listen()
    data=TranslationHintoEng(query)
    return data

