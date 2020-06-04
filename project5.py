# MCS 260, Project Five, by Veronica Kalicki

from tkinter import *
import math

Window = Tk()
Window.title("Gravity Calculator")
label_1 = Label(Window, text='Give initial horizontal velocity of the projectile:')
entry_1 = Entry(Window)
label_1.grid(row=0, sticky=E)
entry_1.grid(row=0, column=1)

label_2 = Label(Window, text = 'Give initial vertical velocity of the projectile:')
entry_2 = Entry(Window)
label_2.grid(row=1, sticky=E)
entry_2.grid(row=1, column=1)

label_3 = Label(Window, text='Give the wind velocity:')
entry_3 = Entry(Window)
label_3.grid(row=2, sticky=E)
entry_3.grid(row=2, column=1)

label_4 = Label(Window, text='Give initial height of the projectile above ground:')
entry_4 = Entry(Window)
label_4.grid(row=3, sticky=E)
entry_4.grid(row=3, column=1)

entry_5 = Entry(Window, width=59)
entry_5.grid(row=6, column=1)


def horizontal_calculator():
    try:
        vx = float(entry_1.get())
        w = float(entry_3.get())
        vy = float(entry_2.get())
        y0 = float(entry_4.get())
        g = 9.80
    except ValueError:
        entry_5.delete(0, "end")
        entry_5.insert(0, "Missing number or there is a Non-Number Input")

    if vx < 0:
        entry_5.delete(0, "end")
        entry_5.insert(0, "Horizontal Velocity should be a positive number!")
        raise Exception("Negative Number1")
    if vy < 0:
        entry_5.delete(0, "end")
        entry_5.insert(0, "Vertical Velocity should be a positive number!")
        raise Exception("Negative Number2")
    if y0 < 0:
        entry_5.delete(0, "end")
        entry_5.insert(0, "Height should be a positive number!")
        raise Exception("Negative Number3")


    v = math.sqrt((float(vx) + float(w))**2 + float(vy)**2) # equation that determines velocity

    sine001 = (float(vy) / float(v))    # sin(0) equation

    cos01 = (float(vx) + float(w)) / float(v) # cos(0) equation

    d1 = (float(v)*float(cos01)/float(g)) # distance formula w/cos
    d2 = (float(v)*float(sine001) + math.sqrt((float(v)*float(sine001))**2 + 2*float(g)*float(y0))) # distance formula w/sin
    d3 = float(d1) * float(d2)     # distance answer


    tyards = float(d3) * 1.093 # yards conversion from meters total
    yards = math.floor(tyards) # round down yards
    ryards = tyards - yards # remaining yards

    tfeet = ryards * 3 # conversion to feet total
    feet = math.floor(tfeet) # feet round down
    rfeet = tfeet - feet # remaining feet

    inches = rfeet * 12 # inches from feet conversion total
    finalinches = math.floor(inches) # inches round down

    if (yards > 0) and (feet > 0):
        k1 = "The horizontal distance travelled by the projectile is: %s Yards %s Feet %s Inches " % (yards, feet,
        finalinches)
        entry_5.delete(0, "end")
        entry_5.insert(0, k1)
    elif yards > 0:
        k1 = "The horizontal distance travelled by the projectile is: %s Yards %s Inches " % (yards, finalinches)
        entry_5.delete(0, "end")
        entry_5.insert(0, k1)
    elif feet > 0:
        k1 = "The horizontal distance travelled by the projectile is: %s Feet %s Inches" % (feet, finalinches)
        entry_5.delete(0, "end")
        entry_5.insert(0, k1)
    else:
        k1 = "The horizontal distance travelled by the projectile is: %s Inches " % finalinches
        entry_5.delete(0, "end")
        entry_5.insert(0, k1)


CalculateButton = Button(Window, text='Calculate', command=horizontal_calculator)
CalculateButton.grid(row=5)
Window.mainloop()
