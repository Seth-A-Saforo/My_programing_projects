# importing libraries

from tkinter import *
from csv import writer

# Creating the main window

window = Tk()

def register():
    global new_list
    element1 = first_name.get()
    element2 = last_name.get()
    element3 = nia_num.get()
    element4 = sim_num.get()

    new_list = [element1, element2, element3, element4]

# setting size and title to the main window
window.title("First_GUI_Program")
window.geometry("450x450")

# setting up labels used in GUI
Label(window, text="SIM REGISTRATION FORM", font=("arial", 16, "bold")).pack()
Label(window, text="Enter First Name:", font=("arial", 12)).place(x=10, y=70)
Label(window, text="Enter Last Name:", font=("arial", 12)).place(x=10, y=120)
Label(window, text="Enter NIA Card No.:", font=("arial", 12)).place(x=10, y=170)
Label(window, text="Enter SIM Number:", font=("arial", 12)).place(x=10, y=220)

# creating text boxes used in GUI

first_name = Entry(window, width=20, font=('Helvetica', 12))
last_name = Entry(window, width=20, font=('Helvetica', 12))
nia_num = Entry(window, width=20, font=('Helvetica', 12))
sim_num = Entry(window, width=20, font=('Helvetica', 12))

# positioning text boxes
first_name.place(x=200, y=70)
last_name.place(x=200, y=120)
nia_num.place(x=200, y=170)
sim_num.place(x=200, y=220)

# creating a button

button1 = Button(window, text="Register SIM", fg='white', bg='brown', command=register, font=("arial", 12, "bold"))
button1.place(x=1660, y=310)

# mainloop method runs the app and it tells the code to keep displaying


# clearing text boxes
def clear_text():
    first_name.delete(0, END)
    last_name.delete(0, END)
    nia_num.delete(0, END)
    sim_num.delete(0, END)


# saving to excel csv
def save(a_list):
    with open('regisster.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(a_list)

# initialising list
    new_list = []



    save(new_list)

    clear_text()

window.mainloop()
