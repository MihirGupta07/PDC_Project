# import statements

from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import BruteForce as bru
import DivideConquer as DV
import Greedy as g
import Random as r
import NeedlemanWunschP as nw_p
import NeedlemanWunschS as nw_s
import time

# t0 = time.time()
# code_block
# t1 = time.time()

# total = t1-t0

# naming master
m = Tk()

m.title("19BCE0619 19BCE0806 19BCE0544 19BCE2186")

height = 450
width = 600

m.geometry("600x500+400+100")
# window width x window height + position right + position down

file1 = ""
file2 = ""
file_temp = ""
file_temp2 = ""

# button to get file
def callback():

    t.delete("1.0", END)
    textshow1.delete("1.0", END)

    global file1

    m.filename = filedialog.askopenfilename(
        initialdir="D:/Codes/NeedlemanWunsch-master/",
        title="Select File One",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")),
    )

    t.insert(END, m.filename)

    with open(m.filename, "r") as f:
        file_temp = f.read()

    textshow1.insert("1.0", file_temp)

    for i in file_temp:
        if i == "A" or i == "C" or i == "G" or i == "T":
            file1 = file1 + i
        else:
            file1 = file1 + "-"


# button to get files
def callback1():
    m.filename = filedialog.askopenfilename(
        initialdir="D:/Codes/NeedlemanWunsch-master/",
        title="Select File Two",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")),
    )

    t2.delete("1.0", END)
    textshow2.delete("1.0", END)

    global file2

    t2.insert(END, m.filename)

    with open(m.filename, "r") as f:
        file_temp2 = f.read()

    textshow2.insert("1.0", file_temp2)

    for i in file_temp2:
        if i == "A" or i == "C" or i == "G" or i == "T":
            file2 = file2 + i
        else:
            file2 = file2 + "-"


main_l = Label(m, text="Parallel and Distributed Computing", font=("Calibri", 16))
main_l.grid(row=0, sticky=N)

canvas_top = Canvas(m, width=600, height=3)
canvas_top.grid(row=3, sticky=N)
canvas_top.create_line(0, 3, width, 3)

l2 = Label(m, text="File Selection", font=("Calibri", 11))
l2.grid(row=5, sticky=W, column=0)

# label_side = Label(m, text="Welcome. Please choose two files to begin. Then select an algorithm from the drop down list.")
# label_side.grid(sticky=N, row=2)

# left hand side text field, buttons, created in order.
b = Button(m, text="Select", width=8, command=callback)
b2 = Button(m, text="Select", width=8, command=callback1)

t = Text(m, height=1, width=8)
t2 = Text(m, height=1, width=8)


# left hand side textfield, buttons for file openings
t.grid(row=6, sticky=W)
b.grid(row=7, sticky=W)
t2.grid(row=8, sticky=W)
b2.grid(row=9, sticky=W)

# list to hold options
op = ["Divide and Conquer", "Needleman Wunsch", "Brute Force", "Greedy", "Random"]
v = StringVar(m)
v.set("Brute Force")  # default value

l3 = Label(m, text="Algorithm", font=("Calibri", 12))
l3.grid(row=10, sticky=W)

w = OptionMenu(m, v, *op)
w.grid(row=11, sticky=W)

label_score = Label(m, text="Scoring", font=("Calibri", 12))
label_score.grid(row=12, sticky=W)

l4 = Label(m, text="Match:")
l4.grid(row=13, sticky=W)

t3 = Text(m, height=1, width=8)
t3.grid(row=14, sticky=W)
t3.insert("1.0", "1")

# label 5
l5 = Label(m, text="Mismatch:")
l5.grid(row=15, sticky=W)

t4 = Text(m, height=1, width=8)
t4.grid(row=16, sticky=W)
t4.insert("1.0", "-1")

l8 = Label(m, text="Gap:")
l8.grid(row=17, sticky=W)

t7 = Text(m, height=1, width=8)
t7.grid(row=18, sticky=W)
t7.insert("1.0", "-2")

# show file 1
fileshow1 = Label(m, text="File 1:")
fileshow1.grid(row=5, sticky=N)

textshow1 = Text(m, height=4, width=40)
textshow1.grid(row=6, sticky=N, columnspan=2, rowspan=2)

scroll2 = Scrollbar(m, command=textshow1.yview)
scroll2.grid(row=6, sticky=N + S + E)
textshow1["yscrollcommand"] = scroll2.set

# show file 2
fileshow2 = Label(m, text="File 2:")
fileshow2.grid(row=8, sticky=N)

textshow2 = Text(m, height=4, width=40)
textshow2.grid(row=9, sticky=N, columnspan=2, rowspan=2)

scroll3 = Scrollbar(m, command=textshow2.yview)
scroll3.grid(row=9, sticky=N + S + E)
textshow2["yscrollcommand"] = scroll3.set

# more labels
l6 = Label(m, text="Output Difference:")
l6.grid(row=11, sticky=N)

t5 = Text(m, height=5, width=40)
t5.grid(row=12, sticky=N, columnspan=2, rowspan=2)
# scrollbar
scroll = Scrollbar(m, command=t5.yview)
scroll.grid(row=12, sticky=N + S + E)
t5["yscrollcommand"] = scroll.set
# score
l7 = Label(m, text="Score:")
l7.grid(row=14, sticky=N)
# textbox Score
t6 = Text(m, height=1, width=8)
t6.grid(row=15, sticky=N)
# time box
l8 = Label(m, text="Time (Seconds):")
l8.grid(row=16, sticky=N)
t7 = Text(m, height=1, width=8)
t7.grid(row=17, sticky=N)
# function to execute each algorithm
def run():

    t6.delete("1.0", END)
    t7.delete("1.0", END)

    print("value is: " + v.get())

    try:
        score = int(t3.get("1.0", "end-1c"))
    except ValueError:
        messagebox.showerror(
            "Error", "A number was not entered or there was an empty field."
        )

    try:
        mismatch = int(t4.get("1.0", "end-1c"))
    except ValueError:
        messagebox.showerror(
            "Error", "A number was not entered or there was an empty field."
        )

    try:
        gap = int(t4.get("1.0", "end-1c"))
    except ValueError:
        messagebox.showerror(
            "Error", "A number was not entered or there was an empty field."
        )

    # timer
    t0 = time.time()

    # picking an algorithm to run
    if v.get() == "Needleman Wunsch":
        temp = nw_p.NeedlemanWunch(file1, file2, score, mismatch, gap)
        # print(bio.score)
        t5.insert(END, temp[0])
        t6.insert(END, temp[1])

    if v.get() == "Brute Force":
        temp = bru.brutForce(file1, file2, score, mismatch, gap)
        # print(bio.score)
        t5.insert(END, temp[0])
        t6.insert(END, temp[1])

    if v.get() == "Divide and Conquer":
        temp = DV.DivideConquer(file1, file2, score, mismatch, gap)
        t5.insert(END, temp[0])
        t6.insert(END, temp[1])
    if v.get() == "Random":

        # file 1, file 1 , match, mismatch, gap
        temp = r.Random(file1, file2, score, mismatch, gap)
        t5.insert(END, temp[0])
        t6.insert(END, temp[1])
    if v.get() == "Greedy":
        temp = g.Greedy(file1, file2, score, mismatch, gap)
        t5.insert(END, temp[0])
        t6.insert(END, temp[1])
    t1 = time.time()
    total = t1 - t0
    t7.insert(END, total)


# run button to actually run code
b3 = Button(m, text="Run", width=8, command=run)
b3.grid(row=19, sticky=W)
m.mainloop()
