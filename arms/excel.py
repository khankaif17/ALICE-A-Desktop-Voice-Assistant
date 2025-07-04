import win32com.client as win32
import speech_recognition as sr

def excel_voice_commands():
    # Initialize Excel application
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    
    # Initialize speech recognition
    r = sr.Recognizer()
    
    while True:
        # Listen for voice command
        with sr.Microphone() as source:
            print("Listening for voice command...")
            audio = r.listen(source)
        
        # Recognize voice command
        try:
            command = r.recognize_google(audio)
            print("Command recognized: " + command)
        except sr.UnknownValueError:
            print("Command not recognized")
            continue
        
        # Process voice command
        if "open workbook" in command:
            # Open a workbook
            command_parts = command.split()
            if len(command_parts) < 3:
                print("Invalid command")
                continue
            filename = command_parts[2]
            workbook = excel.Workbooks.Open(filename)
            print("Workbook opened")
        elif "close workbook" in command:
            # Close the active workbook
            excel.ActiveWorkbook.Close()
            print("Workbook closed")
        elif "select cell" in command:
            # Select a cell
            command_parts = command.split()
            if len(command_parts) < 4:
                print("Invalid command")
                continue
            row = int(command_parts[2])
            column = int(command_parts[3])
            excel.ActiveSheet.Cells(row, column).Select()
            print("Cell selected")
        elif "enter value" in command:
            # Enter a value in the active cell
            command_parts = command.split()
            if len(command_parts) < 3:
                print("Invalid command")
                continue
            value = command_parts[2]
            excel.ActiveCell.Value = value
            print("Value entered")
        elif "save workbook" in command:
            # Save the active workbook
            excel.ActiveWorkbook.Save()
            print("Workbook saved")
        elif "quit excel" in command:
            # Quit Excel application
            excel.Application.Quit()
            break
        else:
            print("Command not recognized")
            
