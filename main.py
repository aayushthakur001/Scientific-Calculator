from tkinter import *
import tkinter.messagebox
import math

# Initialize the main application window
root = Tk()
root.geometry("650x400+300+300")
root.title("Scientific Calculator by Pramoth")

switch = None  # Switch between radians and degrees

# Functions for button clicks
def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')

def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')

def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')

# Add similar functions for buttons 4-9 and 0 following the same format as above...

def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)

def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')

def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')

def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')

def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')

def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

def sin_clicked():
    try:
        ans = float(disp.get())
        ans = math.sin(math.radians(ans)) if switch else math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# Define similar trigonometric functions (cos, tan, arcsin, arccos, arctan) as above

def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')

def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(int(ans))
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')

def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')

def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')

def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display != '0' and display:
        disp.delete(0, END)
        disp.insert(0, display[:-1])

def conv_clicked():
    global switch
    switch = not switch
    conv_btn['text'] = "Deg" if switch else "Rad"

def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')

def btneq_clicked(*args):
    try:
        ans = eval(disp.get())
        disp.delete(0, END)
        disp.insert(0, ans)
    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# Setup display entry
disp = Entry(root, font="Verdana 20", fg="black", bg="mistyrose", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
for i in range(10):
    disp.bind(f"<Key-{i}>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=True, fill=BOTH)

# Setup buttons (Example shown for Row 1)
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill=BOTH)
pi_btn = Button(btnrow1, text="π", font="Segoe 18", relief=GROOVE, bd=0, command=pi_clicked, fg="white", bg="#333333")
pi_btn.pack(side=LEFT, expand=True, fill=BOTH)

# Define all other buttons for rows 1-4 in a similar fashion...

root.mainloop()
