from tkinter import *

import calendar

#function for showing the calender of the given year
def showCal():
    new_gui = Tk()

    new_gui.config(background="white")

    new_gui.title("CALENDER")

    new_gui.geometry("550x600")

    fetch_year= int(year_field.get())
    # calendermethode of calender module return
    # the calender of the given year
    cal_content=calendar.calendar(fetch_year)
    # create a label for showing the content of the calender
    cal_year = Label(new_gui, text=cal_content, font="consolas 10 bold")
    # grid methode is used for placing the widgets at respective positions in table like structure
    cal_year.grid(row=5, column=1,padx=20)

    # start the GUI
    new_gui.mainloop()

# Driver code
if __name__ =="__main__":
    gui = Tk()

    gui.config(background="white")

    gui.title('CALENDER')

    gui.geometry("250x140")

    # create a CALENDER :label with specified font a size
    cal= Label(gui , text="CALENDER", bg="darkgrey",font=("times",28,'bold'))

    #create a Enter year : label
    year = Label(gui,text="Enter Year", bg="light green")

    year_field=Entry(gui)

    show = Button(gui,text="Show calender", fg="Black", bg="Red", command=showCal)

    #creat a Exit button and attached top exit function
    Exit = Button(gui, text="EXIT", fg="Black", bg="red", command=exit)

    #grid method is used for placing the widgets at respective positions in table like structure
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)

    gui.mainloop()