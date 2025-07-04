import tkinter as tk
import hashlib


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Password Cracker")

        self.create_widgets()

    def create_widgets(self):
        # Create input fields and labels
        hash_label = tk.Label(self.master, text="Enter the hashed password:")
        hash_label.pack()
        self.hash_input = tk.Entry(self.master)
        self.hash_input.pack()

        pass_file_label = tk.Label(self.master, text="Enter passwords filename including path (root/home/):")
        pass_file_label.pack()
        self.pass_file_input = tk.Entry(self.master)
        self.pass_file_input.pack()

        # Create button to crack the password
        crack_button = tk.Button(self.master, text="Crack Password", command=self.crack_password)
        crack_button.pack()

        # Create text area to display results
        self.result_text = tk.StringVar()
        result_label = tk.Label(self.master, textvariable=self.result_text)
        result_label.pack()

    def crack_password(self):
        input_hash = self.hash_input.get()
        pass_doc = self.pass_file_input.get()
        pass_found = False

        try:
            pass_file = open(pass_doc, 'r')
        except:
            self.result_text.set(f"Error: {pass_doc} is not found.\nPlease give the path of file correctly.")
            return

        for word in pass_file:
            enc_word = word.encode('utf-8')
            hash_word = hashlib.md5(enc_word.strip())
            digest = hash_word.hexdigest()

            if digest == input_hash:
                self.result_text.set(f"Password found.\nThe password is: {word}")
                pass_found = True
                break

        if not pass_found:
            self.result_text.set(f"Password is not found in the {pass_doc} file")


# Create and run the GUI
root = tk.Tk()
app = Application(master=root)
app.mainloop()
