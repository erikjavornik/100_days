from tkinter import *

#Set up window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

#Entry window for Miles
entry = Entry(width=10)
entry.grid(column=1, row=0)

#Label for entry box
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

#Remaining Labels, Row 2
km = 0
label_list = []
for i in range(3):
    label = Label()
    if i == 0:
        label.config(text="is equal to")
    elif i == 1:
        label.config(text=km)
    elif i == 2:
        label.config(text="Km")
    label.grid(column=i, row=2)
    label_list.append(label)

#Calculate Button
def mile_to_km():
    con_km = int(entry.get()) * 1.61
    label_list[1].config(text=con_km)
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=3)

window.mainloop()