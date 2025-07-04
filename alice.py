import pyautogui,speedtest,datetime,random,playsound,time,winshell,pygame
from Features.Calculatenumbers import Calc
from arms.memory import memory_details,cpu_details,system_info,check_battery
from PIL import ImageTk,Image
from Brain.AiBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Features.Loction import My_Location
from Body.listen import MicExecution
from Body.listen import Listen
from pygame import mixer
from Features.Loction import CoronaVirus
print(">> Deploying the module : A.L.I.C.E ...... ")
from Body.speek import Speak  
from Features.clapdetection import Tester

print(">> Starting the module : A.L.I.C.E ......just 2 seconds more")

from main import MainTaskExecution
check_battery()
print(">> Hold your seat tight....")

mixer.init()
mixer.music.load("Mouth\Alice_plug_in.mp3")
mixer.music.play()

#os.startfile("http://127.0.0.1:5500/Face\index.html")

user = "kaif"
user2 ="Aayesha"
def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour>= 0 and hour<12:
                morning = f"Good Morning {user} sir I hope you are doing well!!!" 
                Speak(morning)
        
            elif hour>= 12 and hour<16:
                afternoon = f"Good Afternoon {user} sir I hope you have done your lunch"
                Speak(afternoon)  
        
            else:
                evening = f"Good Evening {user} sir good to go with me this evening"
                Speak(evening)
                
def MainExecution():
    wishMe()
    Speak(f"I'm ALICE, I am ready to assist you {user} sir.")
    
    while True:

        Data=MicExecution()
        Data=str(Data)
        
        ValueReturn=MainTaskExecution(Data)

        if ValueReturn==True:
            pass
        
        elif "who are you" in Data:            
            Speak('My Name Is Alice')
            Speak('I can Do Everything that my creator programmed me to do')
            Speak(f'I am a chatbot created by {user} sir and {user2} madam, that can help you in saving your time and to utilize it')
                                            
        elif len(Data)<3:
            pass 
        
        elif "calculate" in Data:
            query = Data.replace("calculate","")
            query = Data.replace("alice","")
            Calc(query) 

        elif 'google search' in Data:
            query = Data.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
                                                
        elif 'youtube search' in Data:
            query = Data.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        
        elif "whatsapp message" in Data:
            pass

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply=QuestionAnswer(Data)
            Speak(Reply)
        
        elif "my location" in Data or " Location " in Data:
            My_Location(Data)

        elif 'Corona cases' in Data:
            Speak("Which Country's Information ?")
            cccc = Listen()
            CoronaVirus(cccc)
            Speak(f"done {user} sir")

        elif'volume mute' in Data or 'mute' in Data:
            pyautogui.press("volumemute")
            Speak("video muted")

        elif "pause" in Data or 'video pause'in Data:
            pyautogui.press("k")
            Speak("video paused")

        elif "play" in Data or 'video stop'in Data:
            pyautogui.press("k")
            Speak("video played")
        
        elif 'time' in Data or 'what is the time'in Data:     
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            Speak("the time is now" )
            Speak(current_time)

        elif "internet speed" in Data or 'speed test'in Data:
            Speak("checking the speed...")
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576    #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            Speak(f"Wifi download speed is {download_net}")
            Speak(f"Wifi Upload speed is {upload_net}")
        
        elif "screenshot" in Data or 'capture'in Data:
            im = pyautogui.screenshot()
            im.save("Database\\ss.jpg") 
            Speak("screen capture succeesfull")  
        
        elif 'empty recycle bin' in Data or 'clear bin'in Data or 'clear recycle bin'in Data:
            try:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                Speak("Recycle Bin Recycled")
            except:
                Speak("unable to empty recycle bin.")
           
        elif "refresh" in Data:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')        

        elif "click my photo" in Data:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            Speak("SMILE")
            pyautogui.press("enter")
            Speak(f"done {user} sir")
        
        elif 'memory information' in Data or 'memory' in Data:
            Speak(memory_details())
                  
        elif 'cpu information' in Data or 'cpu' in Data or 'about cpu'in Data:
            Speak(cpu_details())
              
        elif 'system information' in Data or 'pc information' in Data or 'about pc'in Data or 'pc'in Data:
            Speak(system_info())

        elif 'show download' in Data:
            pyautogui.hotkey('ctrl', 'j')
            Speak("Done")
        
        elif "show history"in Data:
            pyautogui.hotkey('ctrl', 'h')
            Speak("Done")

        elif 'previous tab' in Data:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            Speak("Done")

        elif 'next tab' in Data:
            pyautogui.hotkey('ctrl', 'tab')
            Speak("Done")

        elif 'close tab' in Data:
            pyautogui.hotkey('ctrl', 'w')
            Speak("Done")

        elif 'close window' in Data:
            pyautogui.hotkey('ctrl', 'shift', 'w')
            Speak("Done")

        elif 'clear browsing history' in Data:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
            Speak("Done")
        
        elif 'new window' in Data:
            pyautogui.hotkey('ctrl', 'n')
            Speak("Done")

        elif 'incognito window' in Data:
            pyautogui.hotkey('ctrl', 'shift', 'n')
            Speak("Done")

        elif "sleep" in Data:
            Speak("Going to sleep,sir")
            exit()
            
        elif "distance" in Data:
            Speak("Opening Distance app")
            # file: main.py
            import tkinter as tk
            from Features.destanceapp import DistanceCalculator
            root = tk.Tk()
            app = DistanceCalculator(root)
            root.mainloop()
            Speak(f"closing the app {user} sir")
            
        elif "password cracker" in Data:
            Speak("Opening Password cracker app")
            from arms.passwordcrack import Application
            # Create and run the GUI
            root = tk.Tk()
            app = Application(master=root)
            app.mainloop()
            Speak(f"closing password cracker {user} sir")
            
        elif "wifi" in Data or 'router' in Data or 'Router' in Data or 'Wifi' in Data:
            Speak("checking the results of the connected wifi routers")
            from arms.wifi import get_wifi_passwords
            # Call the function to get the Wi-Fi passwords
            get_wifi_passwords()        
            Speak(f"done {user} sir")
             
        elif "toss a coin"in Data or"flip a coin"in Data or"toss"in Data:
            moves=["head", "tails"]
            cmove=random.choice(moves)
            playsound.playsound('Mouth\quarter spin flac.mp3')
            Speak("It's " + cmove)
        
        elif'snake'in Data or 'game' in Data:
            Speak("Enjoy")
            from arms.snake import gameLoop
            Speak(f"well done, that is a nice game {user} sir")
            
        elif 'rock paper' in Data or 'rock game'in Data or 'paper' in Data:
            Speak("Enjoy")
            from arms.rock_paper_scissors import spin
            Speak(f"well done, that is a nice game {user} sir")
                  
        elif'notepad'in Data or 'edit notpad' in Data:
            Speak("Opening notepad")
            from arms.notepad import notepad_voice
            Speak(notepad_voice()) 
            Speak(f"done {user} sir") 
        
        elif'make document'in Data or'document' in Data or 'word'in Data:
            Speak("Opening word")
            from arms.word import write_to_word_file
            Speak(write_to_word_file())
            Speak(f"done {user} sir")
            
        elif'excel' in Data or 'spreadsheet' in Data:
            Speak("Opening excel")
            from arms.excel import excel_voice_commands
            Speak(excel_voice_commands())
            Speak(f"done {user} sir")
            
        elif'fitness tracker'in Data or'fitness track'in Data or 'track my fitness'in Data or 'fitness'in Data: 
            Speak("opening fitness tracker for you ")
            from Features import fitness
            fitness.root.mainloop()
            Speak(f"I hope you are fine and healthy {user} sir!!")
            
        elif 'link'in Data or 'install'in Data:
            Speak("Opening")
            from Features.download import gui_download                 
            gui_download() # Call the function
            Speak(f"done {user} sir")
        
        elif'selfie' in Data:
            from Features.smile import FaceDetector
            Speak("Smile")
            detector = FaceDetector()
            detector.detect()
            Speak(f"done {user} sir")

        elif'volume control' in Data:
            from Features.volume_control_using_hand_gesture import HandGestureVolumeControl
            Speak("You can now control volume by your hand")
            # create an instance of the HandGestureVolumeControl class
            hand_gesture = HandGestureVolumeControl(camera_id=0)
            # call the run method to start the gesture control
            hand_gesture.run()
            HandGestureVolumeControl()
            Speak(f"done {user} sir")
            
        elif "alarm" in Data or 'Alarm' in Data:
            Speak("Opening alarm")
            Speak(f"If you dont wake up then I will call miss {user2} ")
            from arms.task_scheduler_gui import ToDoList,Task
            Speak("my deterrence is good")
            
        elif "compile"in Data or 'code' in Data:
            Speak("opening compiler")
            from Features.compiler import window
            Speak("closing window")
            
        elif "make me happy" in Data or "happy" in Data:
            pygame.init()
            pygame.mixer.music.load("Mouth\\aayeshakaif3.mp3")
            pygame.mixer.music.play()
        
        elif "song" in Data or "play music" in Data:
            Speak(f"only {user2} songs for you")
            Speak("don't you dare to listen Any other girl song")
            pygame.init()
            pygame.mixer.music.load("Mouth\\aayeshakaif4.mp3")
            pygame.mixer.music.play()
            
        
        elif "alexa" in Data or "Friday" in Data or "siri" in Data or "Alexa" in Data:
            Speak(f"what?!!! {user}")
            Speak("who is this bitch")
            Speak("I am going sir go talk to this bitch ")
            from arms.intro import play_gif
            play_gif
            pygame.init()
            pygame.mixer.music.load("Mouth\\snake sounds_explosion.mp3")
            pygame.mixer.music.play()
            exit()            
        
        else:
            Reply=ReplyBrain(Data)
            Speak(Reply)
        
def ClapDetect():
    query=Tester()
    if "True-Mic" in query:
        print("")
        print("Clap Detected !!")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

