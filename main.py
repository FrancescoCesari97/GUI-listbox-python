


def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    # print(f"You have ordered: {listbox.get(listbox.curselection())}")
    
    for i in food:
        print(f"You have ordered: {i} ")


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.curselection())
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


from tkinter import * 

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 30),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "burger")
listbox.insert(5, "cipolla")
listbox.insert(6, "spaghetti")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

entryButton = Button(window, text="add", command=add)
entryButton.pack()


submitButton = Button(window, text="submit", command=submit)
submitButton.pack()


deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()