import os
import speech_recognition as sr

def notepad_voice():
    r = sr.Recognizer()

    # Open Notepad
    os.system("start notepad")

    # Listen for the text to write to the file
    with sr.Microphone() as source:
        print("Speak the text you want to write to the file.")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"Text: {text}")
    except Exception as e:
        print("Error: " + str(e))
        return

    # Get the file name from the user
    while True:
        with sr.Microphone() as source:
            print("Speak the file name you want to give to the file.")
            audio = r.listen(source)

        try:
            file_name = r.recognize_google(audio)
            print(f"File name: {file_name}")
            break
        except Exception as e:
            print("Error: " + str(e))
            continue

    # Save the text to the specified file
    with open(file_name, "w") as f:
        f.write(text)

    # Open the file in Notepad
    os.system(f"start notepad {file_name}")

    # Listen for edits to the file
    while True:
        with sr.Microphone() as source:
            print("Do you want to make edits to the file? Say 'yes' or 'no'.")
            audio = r.listen(source)

        try:
            response = r.recognize_google(audio)
            print(f"You said: {response}")
            if "yes" in response.lower():
                with sr.Microphone() as source:
                    print("What do you want to add to the file?")
                    audio = r.listen(source)
                try:
                    new_text = r.recognize_google(audio)
                    with open(file_name, "a") as f:
                        f.write("\n" + new_text)
                    os.system(f"start notepad {file_name}")
                except Exception as e:
                    print("Error: " + str(e))
                    continue
            elif "no" in response.lower():
                os.system(f"taskkill /f /im notepad.exe")
                break
        except Exception as e:
            print("Error: " + str(e))
            continue

notepad_voice()
