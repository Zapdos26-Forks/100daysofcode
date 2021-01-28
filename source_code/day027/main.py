import tkinter


def button_on_click(self):
    # print(f"{input1.get()=}")
    #self["text"] = input_.get()
    pass


def spin_on_use(self):
    print(self.get())


def scale_on_use(self):
    print(self)


def checkbox_on_change(self):
    print(self.get())


def radio_on_change(self):
    print(self.get())


def list_used(self):
    print(self.get(self.curselection()))


window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("My Window")
window.config(padx=10, pady=10)

label = tkinter.Label(text="Label1", font=("Trebuchet MS", 16, "normal"))
label.grid(column=1, row=1)
label.config(padx=0, pady=40)

input_ = tkinter.Entry(width=10)
input_.grid(column=2, row=2)


button = tkinter.Button(text="Click Me", command=button_on_click, )
button.grid(column=1, row=2)


spin = tkinter.Spinbox(from_=0, to=10, width=5, command=spin_on_use)
spin.grid(column=1, row=4)


scale = tkinter.Scale(from_=0, to=100, command=scale_on_use)
scale.grid(column=2, row=4)


checkbox_state = tkinter.IntVar()
checkbox = tkinter.Checkbutton(
    text="Break?", variable=checkbox_state, command=checkbox_on_change)
checkbox.grid(column=3, row=4)


radio_state = tkinter.IntVar()
radio_a = tkinter.Radiobutton(
    text="Male", value=1, variable=radio_state, command=radio_on_change('Male'))
radio_b = tkinter.Radiobutton(
    text="Female", value=2, variable=radio_state, command=radio_on_change())
radio_a.grid(column=4, row=4)
radio_b.grid(column=5, row=4)

fruit = tkinter.Listbox(height=3)

for index, item in enumerate(["apple", "banana", "pear"]):
    fruit.insert(index, item)

fruit.bind("<<ListboxSelect>>", list_used)
fruit.grid(column=1, row=5)

window.mainloop()
