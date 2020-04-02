from tkinter import *
from autocomplete_entry import AutocompleteEntry
import tkinter as tk
import tkinter.ttk as ttk
from db_conn import DBConnect


# info for connect to db
server = 's-kv-center-s59'
db = 'AnalyticReports'


def check_connect():
    with DBConnect(server, db) as sql:
        return sql.get_user_info()


row = check_connect()
for i in row:
    print(i)


def _get_users():
    with DBConnect(server, db) as sql:
        return sql.get_users()


users = dict(_get_users())
users.values()


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Payment Access")
        # self.wm_iconbitmap("icon.ico")

        self.tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="Add user")

        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text="Таб 2")
        self.tabControl.pack(expand=1, fill="both")


        self._tab1()
        self._tab2()

    def center_window(self, width, height):
        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def _tab1(self):
        # Frame for tab1
        labelFrame = ttk.LabelFrame(self.tab1, text="Новый пользователь", pad=10)
        labelFrame.grid(row=0, column=0,  padx=0, pady=10)




        label = ttk.Label(labelFrame, text="UserName:")
        label.grid(row=0, column=0, sticky='W')
        # self.get_user = ttk.Combobox(self.labelFrame, width=20, state='readonly')
        get_user = AutocompleteEntry(list(users.values()), labelFrame, width=30, listboxLength=6)
        get_user.grid(row=0, column=1, padx=5, pady=10)
        label2 = ttk.Label(labelFrame, text="ShortUserName:")
        label2.grid(row=1, column=0)
        textEdit = ttk.Entry(labelFrame, width=30)
        textEdit.grid(row=1, column=1)




    def _tab2(self):
        # Frame for tab2
        pass

        self.center_window(600, 400)



class TabFrame(MainApp):
    def __init__(self, **kw):
        super().__init__(**kw)



        print(users)



root = MainApp()
root.mainloop()
