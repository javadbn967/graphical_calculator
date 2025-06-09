import customtkinter as ctk

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("280x300")
app.title("Calculator")

entry = ctk.CTkEntry(app, width=240, font=("Arial", 16))
entry.pack(pady=20)



def click(char):
    entry.insert("end", char)

def clear():
    entry.delete(0, "end")

def calc():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, "end")
        entry.insert(0, result)
    except:
        entry.delete(0, "end")
        entry.insert(0, "Error")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = ctk.CTkFrame(app)
frame.pack()

row = col = 0
for b in buttons:
    cmd = lambda x=b: calc() if x == "=" else click(x)
    btn = ctk.CTkButton(frame, text=b, width=60, command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1


ctk.CTkButton(app, text="Clear", command=clear).pack(pady=10)

app.mainloop()
