from tkinter import *
from datetime import datetime
import json
import threading
import os
from playsound import playsound

class Task:
    def __init__(self, time, description):
        self.time = time
        self.description = description
    
    def is_due(self):
        return self.time <= datetime.now()
        
    def notify(self):
        threading.Thread(target=self.play_notification_sound).start()
        print(f"{self.time} - {self.description}")
    
    def play_notification_sound(self):
        playsound('Mouth\\snake sounds_beep.wav')
        
    
   
        

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("A.L.I.C.E To-Do List")
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.tasks = []
        self.load_tasks_from_file()
        
        self.time_label = Label(master, text="Time (format: hh:mm)")
        self.time_label.pack()
        
        self.time_entry = Entry(master)
        self.time_entry.pack()
        
        self.description_label = Label(master, text="Description")
        self.description_label.pack()
        
        self.description_entry = Entry(master)
        self.description_entry.pack()
        
        self.add_button = Button(master, text="Add", command=self.add_task)
        self.add_button.pack()
        
        self.quit_button = Button(master, text="Quit", command=self.on_closing)
        self.quit_button.pack()
        
        self.check_tasks()
        
    def add_task(self):
        time_str = self.time_entry.get()
        description_str = self.description_entry.get()
        
        try:
            time = datetime.strptime(time_str, "%H:%M").time()
            task = Task(datetime.combine(datetime.today(), time), description_str)
            self.tasks.append(task)
            self.save_tasks_to_file()
            
            self.time_entry.delete(0, END)
            self.description_entry.delete(0, END)
            
        except ValueError:
            print("Invalid time format. Please enter time in format hh:mm")
            
    def check_tasks(self):
        for task in self.tasks:
            if task.is_due():
                task.notify()
                
        self.master.after(60000, self.check_tasks)
        
    def load_tasks_from_file(self):
        try:
            with open("Data\\tasks1.json", "r") as f:
                tasks_json = json.load(f)
                for task_json in tasks_json:
                    time = datetime.strptime(task_json["time"], "%Y-%m-%d %H:%M:%S")
                    task = Task(time, task_json["description"])
                    self.tasks.append(task)
                    
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        
    def save_tasks_to_file(self):
        tasks_json = [{"time": task.time.strftime("%Y-%m-%d %H:%M:%S"), "description": task.description} for task in self.tasks]
        
        with open("Data\\tasks1.json", "w") as f:
            json.dump(tasks_json, f)
            
    def on_closing(self):
        with open("Data\\tasks1.json", "w") as f:
            f.write("")
        self.master.destroy()
        
root = Tk()

my_todo_list = ToDoList(root)
root.mainloop()
