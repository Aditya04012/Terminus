import tkinter as tk
'''
        
                     Documentation



'get or show input'
def show_input():
    user_input = entry.get()  # Get text from the Entry widget

    label.config(text=f"{user_input}" ,fg="white", bg="black")

'initialization'
root=tk.Tk()
'title & bg-color'
root.title("GUI")
root.configure(bg="black") 

'label diled'
label=tk.Label(root, fg="white", bg="black", font=("Arial", 14),border=None)
label.pack(padx=100)

'inpyt field'
entry=tk.Entry(root,width=30, fg="white", bg="black", insertbackground="white",border=None)
entry.pack(pady=10)

'button type submit'
button=tk.Button(root,text="submit",command=show_input,fg="white", bg="black", activebackground="gray", activeforeground="white")
button.pack(pady=10)

'ending'
root.mainloop()
'''

'''
import tkinter as tk
from PIL import Image, ImageTk


root=tk.Tk()

root.title("Termio Shell")

root.geometry("800x600")
root.resizable(False, False)
  
bg_image=Image.open('t2.png')
bg_image=bg_image.resize((800,600))
bg=ImageTk.PhotoImage(bg_image)



bg_label=tk.Label(root,image=bg)
bg_label.place(x=0,y=0,relheight=1,relwidth=1)



root.mainloop()

'''
 

import tkinter as tk
from tkinter import scrolledtext
import os
import subprocess, threading



proc = subprocess.Popen(
    ["python", "commands.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)


def read_output():
    """Continuously read output from commands.py and display in terminal"""
    for line in proc.stdout:
        # Insert command output
        terminal.insert(tk.END, line)
        # Ensure output ends with newline
        if not line.endswith("\n"):
            terminal.insert(tk.END, "\n")  # <-- newline if missing
        # Insert prompt on new line
        terminal.insert(tk.END, os.getcwd() + " > ", "prompt")
        # Move cursor to end
        terminal.mark_set(tk.INSERT, tk.END)
        terminal.see(tk.END)

threading.Thread(target=read_output, daemon=True).start()

def on_enter(event=None):
    # Get user input (text after last prompt)
    command = terminal.get("insert linestart", "end-1c").replace(os.getcwd()+ " > ", "").strip()

    if command.startswith("cd "):
        path = command[3:].strip()
        try:
            os.chdir(path)
        except Exception as e:
            terminal.insert(tk.END, f"cd: {e}\n")
        # Always newline first, then prompt
        terminal.insert(tk.END, "\n" + os.getcwd() + " > ")
        terminal.mark_set(tk.INSERT, tk.END)
        return "break"

    if command == "exit":
        exit()

    # If no command, just print a new prompt
    if not command:
        terminal.insert(tk.END, "\n" + os.getcwd() + " > ", "#ED3694")
        terminal.mark_set(tk.INSERT, tk.END)
        return "break"

    # Insert newline before sending command to subprocess
    terminal.insert(tk.END, "\n")
    proc.stdin.write(command + "\n")
    proc.stdin.flush()

    # Move cursor to end
    terminal.mark_set(tk.INSERT, tk.END)
    return "break"



root = tk.Tk()
root.title("Terminus")
root.geometry("790x450")
root.configure(bg="#0C0C0C")  # CMD-like background
root.resizable(False, False)


terminal = scrolledtext.ScrolledText(
    root,
    bg="#0C0C0C",
    fg="#00FF00",
    insertbackground="white",
    font=("Consolas", 13),
    wrap=tk.WORD,
    borderwidth=0
)
terminal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Insert initial prompt
terminal.insert(tk.END, os.getcwd()+ " > ", "#ED3694")

# Bind Enter key
terminal.bind("<Return>", on_enter)

root.mainloop()
