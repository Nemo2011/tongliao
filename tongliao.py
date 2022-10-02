import tkinter
from tkinter import ttk
from tongliao import country2tongliao, COUNTRIES_DATA

root = tkinter.Tk()
root.resizable(0, 0)

combo = ttk.Combobox(root)
countries = list(COUNTRIES_DATA.keys())
countries.sort()
combo["value"] = countries
combo.pack()
area = tkinter.Label(root, text="面积")
area.pack()
people = tkinter.Label(root, text="人口")
people.pack()


def calc_tongliao(event):
    result = country2tongliao(combo.get())

    def set_value(a, p):
        area.configure(text=a)
        people.configure(text=p)

    if result == {}:
        set_value("???", "???")
    set_value(result["result"]["area_str"], result["result"]["people_str"])


combo.bind("<<ComboboxSelected>>", calc_tongliao)

root.mainloop()
