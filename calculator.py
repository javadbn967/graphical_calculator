import tkinter as tk

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + btn_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# پنجره اصلی
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)


entry = tk.Entry(window, font=("Arial", 20), borderwidth=3, relief="ridge", justify="right")
entry.pack(padx=10, pady=10, fill="x")


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(window)
frame.pack()

row, col = 0, 0
for btn in buttons:
    action = lambda x=btn: calculate() if x == "=" else click(x)
    tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1


tk.Button(window, text="Clear", width=30, height=2, font=("Arial", 12), command=clear).pack(pady=10)

window.mainloop()
