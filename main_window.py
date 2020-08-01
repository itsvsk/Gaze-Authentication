import tkinter as tk
from auth import register, login

def onPatternRegister():
    # This function is called when the register pattern button is clicked
    register()

def onLogin():
    # This function is called when the login button is clicked
    login()

root = tk.Tk()
root.title("Gaze Auth")
root.geometry('300x300+300+100')

# Creating the buttons
registerBtn = tk.Button(root, text="Register", command = onPatternRegister)
loginBtn = tk.Button(root, text="Login", command = onLogin)

registerBtn.pack()
loginBtn.pack()

print("Code initiated")
root.mainloop()
