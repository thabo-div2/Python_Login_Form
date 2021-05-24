# Membership
from tkinter import *
from tkinter import messagebox

username = ["Apple", "Banana", "Orange", "Mango", "Kiwi"]
passwords = ["Lion", "Cheetah", "Tiger", "Panther", "Jaguar"]


def membership():
    for x in range(len(username)):
        if e1.get() == username[x] and e2.get() == passwords[x]:
            found = True
            if found == True:
               root.destroy()
               import next_screen
        else:
            return messagebox.showerror("Error", "Access Denied")


def clear_button():
    e1.delete(0, END)
    e2. delete(0, END)


def exit_button():
    return root.destroy()


root = Tk()

root.title("Membership")
root.geometry("1000x1000")
root.config(bg="#222222")

myframe = Frame(root, bg="#ed2d34")
myframe.place(x=0, y=0, width=500, height=500)

label_text = StringVar()
label1 = Label(myframe, text="Username: ", bg="#ed2d34")
label1.place(x=10, y=10)
label2 = Label(myframe, text="Password: ", bg="#ed2d34")
label2.place(x=10, y=50)
label3 = Label(myframe, text="", textvariable=label_text)

e1 = Entry(myframe)
e1.place(x=100, y=10)
e2 = Entry(myframe, show="*")
e2.place(x=100, y=50)

mybutton = Button(myframe, text="Enter", command=membership)
mybutton.place(x=155, y=155)
delete_button = Button(myframe, text="Del", command=clear_button)
delete_button.place(x=255, y=155)
but1 = Button(myframe, text="Exit", command=exit_button)
but1.place(x=355, y=155)

mainloop()







