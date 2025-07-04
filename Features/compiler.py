import tkinter as tk
from tkinter import ttk
import subprocess

# Create a new window
window = tk.Tk()
window.title("A.L.I.C.E Compiler")

# Create a text box for the user to enter code
code_box = tk.Text(window, width=80, height=20)
code_box.pack()

# Create a button to run the code
def run_code():
    # Get the user's code from the text box
    code = code_box.get("1.0", "end-1c")
    
    # Use the subprocess module to run the code in a Python interpreter
    result = subprocess.run(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Print the output to the user
    output_box.delete("1.0", "end")
    output_box.insert("end", result.stdout.decode("utf-8"))
    output_box.insert("end", result.stderr.decode("utf-8"))

run_button = tk.Button(window, text="Run", command=run_code)
run_button.pack()

# Create a text box to display the output
output_box = tk.Text(window, width=80, height=10)
output_box.pack()

# Create a button to rate the code
def rate_code():
    # Get the user's code from the text box
    code = code_box.get("1.0", "end-1c")
    
    # Split the code into lines
    lines = code.split("\n")
    
    # Count the number of lines of code, comments, and blank lines
    num_code_lines = 0
    num_comment_lines = 0
    num_blank_lines = 0
    
    for line in lines:
        line = line.strip()
        
        if not line:
            num_blank_lines += 1
        elif line.startswith("#"):
            num_comment_lines += 1
        else:
            num_code_lines += 1
    
    # Calculate the rating
    total_lines = len(lines)
    code_ratio = num_code_lines / total_lines
    comment_ratio = num_comment_lines / total_lines
    blank_ratio = num_blank_lines / total_lines
    
    rating = (code_ratio * 0.5) + (comment_ratio * 0.3) + (blank_ratio * 0.2)
    # Display the rating to the user
    rating_box.delete("1.0", "end")
    rating_box.insert("end", "Code rating: {:.2f}".format(rating))

rate_button = tk.Button(window, text="Rate", command=rate_code)
rate_button.pack()

# Create a text box to display the rating
rating_box = tk.Text(window, width=80, height=1)
rating_box.pack()

# Create a function to find errors in the code
def find_errors():
    # Get the user's code from the text box
    code = code_box.get("1.0", "end-1c")
    
    # TODO: Implement a function to find errors in the code
    
error_button = tk.Button(window, text="Find Errors", command=find_errors)
error_button.pack()

# Run the window
window.mainloop()
