import tkinter as tk
import random
def generate_password():
    k=int(lengthentry.get())
    x=[]
    for i in range(33,126):
        x.append(chr(i))
    paswd=''
    for i in range(k):
        paswd+=random.choice(x)
    passwordlabel.config(text="Generated Password: " + paswd)

root = tk.Tk()
root.geometry("1000x1000")
root.title("Password Generator")

lengthlabel = tk.Label(root, text="Password Length:")
lengthlabel.pack()

lengthentry = tk.Entry(root)
lengthentry.pack()

generatebutton = tk.Button(root, text="Generate Password", command=generate_password)
generatebutton.pack()

passwordlabel = tk.Label(root, text="")
passwordlabel.pack()

root.mainloop()
