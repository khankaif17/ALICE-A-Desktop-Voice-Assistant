# 🎙️ ALICE – A Desktop Voice Assistant

**ALICE (Artificial Linguistic Intelligence for Command Execution)** is a Python-based desktop voice assistant that helps users interact with their system using natural voice commands. It automates daily tasks such as searching the web, opening applications, fetching weather/news, and more — all through a conversational interface.

---

## 🧠 Project Description

ALICE is a lightweight and extensible voice-controlled assistant built using Python. It uses **speech recognition**, **text-to-speech**, and **natural language processing** to interpret voice commands and respond accordingly. The project demonstrates how voice assistants can be implemented on local machines without relying heavily on cloud services.

---

## 📌 Features

- 🎤 Voice Command Recognition (via microphone)
- 🗣️ Text-to-Speech Responses
- 🌐 Google Search Integration
- 📅 Tells date & time
- 📍 Weather and news updates
- 💻 Opens desktop applications (e.g., Notepad, Chrome)
- 📩 Sends emails via voice
- 📂 File operations (open folders, access drives)

---

## 🧰 Tech Stack

- **Python**
- `speech_recognition` – to convert speech to text  
- `pyttsx3` – for offline text-to-speech  
- `wikipedia` – to fetch summaries  
- `webbrowser`, `os`, `smtplib` – for various system functions  
- `datetime`, `time`, `random` – for task execution logic  

---


1. **Clone the repository:**
   ```bash
   git clone https://github.com/khankaif17/ALICE-A-Desktop-Voice-Assistant.git
   cd ALICE-A-Desktop-Voice-Assistant
2. Install dependencies:
pip install -r requirements.txt

3. Run the assistant:
python main.py

4. Speak after the prompt to interact with ALICE.

⚙️ Sample Commands
"What is the time?"

"Open YouTube"

"Search Python programming"

"Tell me the weather"

"Send email to John"

"Open Notepad"

💡 Future Enhancements
GUI integration using Tkinter or PyQt

Add wake-word functionality (e.g., "Hey Alice")

Improve NLP using spaCy or GPT APIs

Add more APIs for finance, calendar sync, etc.

