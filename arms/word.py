import os
import win32com.client as win32
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def write_to_word_file():
    word = win32.Dispatch('Word.Application')
    word.Visible = True
    doc = word.Documents.Add()

    # get user input for filename and text to write
    filename = ""
    while not filename:
        print("What would you like to name the Word document?")
        filename = listen()
    filename = filename.lower().replace(" ", "_")

    text = ""
    while not text:
        print("What text would you like to write to the file?")
        text = listen()
    text = text.capitalize()

    # add text to document
    doc.Range().text = text

    # save the document
    path = os.path.join(os.path.expanduser('~'), 'Desktop', f'{filename}.docx')
    doc.SaveAs(path)

    # ask if user wants to edit the file
    edit = ""
    while edit not in ["yes", "no"]:
        print("Do you want to edit the file? (yes/no)")
        edit = listen().lower()
    if edit == "yes":
        # get user input for text to add
        additional_text = ""
        while not additional_text:
            print("What additional text would you like to add to the file?")
            additional_text = listen()
        additional_text = additional_text.capitalize()

        # add text to document
        doc.Range().InsertAfter(additional_text)

        # save the document
        doc.Save()

    # close the document
    doc.Close()


