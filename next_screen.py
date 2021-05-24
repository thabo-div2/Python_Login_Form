from tkinter import *

window = Tk()
window.title("Second Form")
window.geometry("500x500")
window.config(bg="#555555")


def selection_sort():
    numbers = [42, 12, 13, 89, 63, 11]
    # sort nums into ascending order
    n = len(numbers)
    # For each position in the list (exc
    for a in range(n-1):
        # find the smallest item in the
        x = a
        for i in range(a+1, n):
            if numbers[i] < numbers[x]:
                x = i
        numbers[a], numbers[x] = numbers[x], numbers[a]
    label3.config(text=numbers)


label2 = Label(window, text="List of numbers: ", bg="#ed2d34")
label2.place(x=5, y=5)
label1 = Label(window, text="[42, 12, 13, 89, 63, 11]", bg="#ed2d34")
label1.place(x=180, y=5)
label3 = Label(window, text="", bg="#ed2d34")
label3.place(x=180, y=50)

mybutton = Button(window, text="Sort List", command=selection_sort, bg="#ed2d34")
mybutton.place(x=180, y=100)


window.mainloop()
