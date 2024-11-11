from tkinter import *
import calendar
from datetime import datetime

win = Tk()
win.title("GUI Calendar")

def display_calendar():
    year_str = year.get()
    month_str = month.get()
    
    # Check if the year and month are valid
    try:
        year_int = int(year_str)
    except ValueError:
        textfield.delete(0.0, END)
        textfield.insert(INSERT, "Invalid year!")
        return

    try:
        month_int = int(month_str)
        if month_int < 1 or month_int > 12:
            raise ValueError
    except ValueError:
        # If no valid month is provided, show the full year calendar
        cal = calendar.TextCalendar().formatyear(year_int)
    else:
        # Show the calendar for the specific month
        cal = calendar.month(year_int, month_int)

    # Display the current date
    current_date = f"Today's date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
    
    # Update the text field with the calendar
    textfield.delete(0.0, END)
    textfield.insert(INSERT, current_date + cal)

# Label for year and month inputs
label1 = Label(win, text='Year:')
label1.grid(row=0, column=0)
label2 = Label(win, text='Month (optional):')
label2.grid(row=0, column=1)

# Input fields for year and month
year = Spinbox(win, from_=1947, to=2150, width=24)
year.grid(row=1, column=0, padx=16)
month = Spinbox(win, from_=1, to=12, width=3)
month.grid(row=1, column=1)

# Button to generate the calendar
button = Button(win, text="GO", command=display_calendar)
button.grid(row=1, column=2)

# Text field to display the calendar
textfield = Text(win, height=20, width=50, foreground='brown')
textfield.grid(row=3, columnspan=3)

win.mainloop()
