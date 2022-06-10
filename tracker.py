from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def populate_list():
    spend_amount_list.delete(0, END)
    for row in db.fetch():
        spend_amount_list.insert(END, row)


def add_item():
    if place_text.get() == '' or total_text.get() == '' or date_text.get() == '' or checking_text.get() == '' or \
            savings_text.get() == '' or deposits_text.get() == '' or savings_deposits_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(place_text.get(), total_text.get(), date_text.get(), checking_text.get(), savings_text.get(),
              deposits_text.get(), savings_deposits_text.get())
    spend_amount_list.delete(0, END)
    spend_amount_list.insert(END, (place_text.get(), total_text.get(), date_text.get(), checking_text.get(),
                                   savings_text.get(), deposits_text.get(), savings_deposits_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = spend_amount_list.curselection()[0]
        selected_item = spend_amount_list.get(index)

        place_entry.delete(0, END)
        place_entry.insert(END, selected_item[1])
        total_entry.delete(0, END)
        total_entry.insert(END, selected_item[2])
        date_entry.delete(0, END)
        date_entry.insert(END, selected_item[3])
        checking_entry.delete(0, END)
        checking_entry.insert(END, selected_item[4])
        savings_entry.delete(0, END)
        savings_entry.insert(END, selected_item[5])
        deposits_entry.delete(0, END)
        deposits_entry.insert(END, selected_item[6])
        savings_deposits_entry.delete(0, END)
        savings_deposits_entry.insert(END, selected_item[7])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], place_text.get(), total_text.get(), date_text.get(), checking_text.get(),
              savings_text.get(), deposits_text.get(), savings_deposits_text.get())
    populate_list()


def clear_text():
    place_entry.delete(0, END)
    total_entry.delete(0, END)
    date_entry.delete(0, END)
    checking_entry.delete(0, END)
    savings_entry.delete(0, END)
    deposits_entry.delete(0, END)
    savings_deposits_entry.delete(0, END)


# Create window object
app = Tk()

# Daily spending list: Place of Purchase
place_text = StringVar()
place_label = Label(app, text="Place of Purchase", font=("bold", 10), pady=20)
place_label.grid(row=0, column=0, sticky=W)
place_entry = Entry(app, textvariable=place_text)
place_entry.grid(row=0, column=1)

# Daily spending list: Amount of Purchase
total_text = StringVar()
total_label = Label(app, text="Amount of Purchase", font=("bold", 10))
total_label.grid(row=0, column=2, sticky=W)
total_entry = Entry(app, textvariable=total_text)
total_entry.grid(row=0, column=3)

# Daily spending list: Time/Date
date_text = StringVar()
date_label = Label(app, text="Time/Date", font=("bold", 10))
date_label.grid(row=0, column=4, sticky=W)
date_entry = Entry(app, textvariable=date_text)
date_entry.grid(row=0, column=5)

# Daily spending list: Checking account Total
checking_text = StringVar()
checking_label = Label(app, text="Checking Account Total", font=("bold", 10), pady=20)
checking_label.grid(row=1, column=0, sticky=W)
checking_entry = Entry(app, textvariable=checking_text)
checking_entry.grid(row=1, column=1)

# Daily spending list: Savings account Total
savings_text = StringVar()
savings_label = Label(app, text="Savings Account Total", font=("bold", 10))
savings_label.grid(row=1, column=2, sticky=W)
savings_entry = Entry(app, textvariable=savings_text)
savings_entry.grid(row=1, column=3)

# Daily spending list: Deposits in Checking
deposits_text = StringVar()
deposits_label = Label(app, text="Deposits in Checking", font=("bold", 10))
deposits_label.grid(row=1, column=4, sticky=W)
deposits_entry = Entry(app, textvariable=deposits_text)
deposits_entry.grid(row=1, column=5)

# Daily spending list: Deposits in savings
savings_deposits_text = StringVar()
savings_deposits_label = Label(app, text="Deposits in Savings", font=("bold", 10), pady=20)
savings_deposits_label.grid(row=2, column=0, sticky=W)
savings_deposits_entry = Entry(app, textvariable=savings_deposits_text)
savings_deposits_entry.grid(row=2, column=1)

# spending list (Listbox)
spend_amount_list = Listbox(app, height=30, width=50, border=0)
spend_amount_list.grid(row=5, column=0, columnspan=3, rowspan=6, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=3)
# set scroll to listbox
spend_amount_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=spend_amount_list.yview)
# Bind select
spend_amount_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Expense', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

# Buttons
remove_btn = Button(app, text='Remove Expense', width=12, command=remove_item)
remove_btn.grid(row=3, column=1)

# Buttons
update_btn = Button(app, text='Update Expense', width=12, command=update_item)
update_btn.grid(row=3, column=2)

# Buttons
clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=3, column=3)

app.title("Finance Tracker")
app.geometry('1000x800')

# Populate data
populate_list()


# Start program
app.mainloop()
