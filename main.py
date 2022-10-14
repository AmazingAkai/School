from tkinter import *
import tkinter.ttk as ttk 
import sqlite3
import tkinter.messagebox

db = sqlite3.connect('main.db')
cursor = db.cursor()

class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (HomePage, StudentLogin, TeacherLogin):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame(HomePage)

    def create_tables(self) -> None:
        cursor.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, rollno INTEGER, password TEXT);')
        cursor.execute('CREATE TABLE IF NOT EXISTS teachers (name TEXT, password TEXT);')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        self.cvs = Canvas(self, width="800", height="600", background="#7ce577")
        label = Label(self, text="eAttendance", font="Poppins 30", background="#7ce577")
        label.place(x=300, y=10)
        button = Button(self.cvs, text="Student", font="Arial 16",
                           command=lambda: self.controller.show_frame(StudentLogin),
                           bg="#a0ccda")
        button.place(x=100, y=100)
        button2 = Button(self.cvs, text="Teacher", font="Arial 16",
                           command=lambda: self.controller.show_frame(TeacherLogin),
                           bg="#a0ccda")
        button2.place(x=200, y=200)
        self.cvs.pack()


class StudentLogin(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller  
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def login(self):
        if not self.student_username.get():
            return tkinter.messagebox.showerror('Error', 'Please enter your username.')
        elif not self.student_password.get():
            return tkinter.messagebox.showerror('Error', 'Please enter your password.')
        cursor.execute('SELECT * FROM students WHERE name = ?', (self.student_username.get(),))
        data = cursor.fetchone()
        if data:
            if data[2] == self.student_password.get():
                print('Perfect')
            else:
                return tkinter.messagebox.showerror('Error', 'Invalid Password.')
        else:
            return tkinter.messagebox.showerror('Error', 'Invalid Username.')

    def make_widget(self):
        self.cvs = Canvas(self, width="800", height="600", background="#7ce577")
        label = Label(self, text="eAttendance", font="Poppins 30",  background="#7ce577")
        label.place(x=300, y=10)
        label_2 = Label(self, text="Username", font='Arial 10', background="#7ce577")
        label_2.place(x=300, y=250)
        self.student_username = Entry(self, bg="#F6F7F9",fg="#000716")
        self.student_username.place(x=300, y=270)
        label_2 = Label(self, text="Password", font='Arial 10', background="#7ce577")
        label_2.place(x=300, y=290)
        self.student_password = Entry(self, bg="#F6F7F9",fg="#000716", show='*')
        self.student_password.place(x=300, y=310)
        login = Button(self.cvs, text="Login", font="Arial 16",
                           command=self.login,
                           bg="#a0ccda")
        login.place(x=280, y=350)
        back = Button(self.cvs, text="Back", font="Arial 16",
                           command=lambda: self.controller.show_frame(HomePage),
                           bg="#a0ccda")
        back.place(x=370, y=350)
        self.cvs.pack()

class TeacherLogin(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller  
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def login(self):
        if not self.teacher_username.get():
            return tkinter.messagebox.showerror('Error', 'Please enter your username.')
        elif not self.teacher_password.get():
            return tkinter.messagebox.showerror('Error', 'Please enter your password.')
        cursor.execute('SELECT * FROM teachers WHERE name = ?', (self.teacher_username.get(),))
        data = cursor.fetchone()
        if data:
            if data[1] == self.teacher_password.get():
                print('Perfect')
            else:
                return tkinter.messagebox.showerror('Error', 'Invalid Password.')
        else:
            return tkinter.messagebox.showerror('Error', 'Invalid Username.')

    def make_widget(self):
        self.cvs = Canvas(self, width="800", height="600", background="#7ce577")
        label = Label(self, text="eAttendance", font="Poppins 30",  background="#7ce577")
        label.place(x=300, y=10)
        label_2 = Label(self, text="Username", font='Arial 10', background="#7ce577")
        label_2.place(x=300, y=250)
        self.teacher_username = Entry(self, bg="#F6F7F9",fg="#000716")
        self.teacher_username.place(x=300, y=270)
        label_2 = Label(self, text="Password", font='Arial 10', background="#7ce577")
        label_2.place(x=300, y=290)
        self.teacher_password = Entry(self, bg="#F6F7F9",fg="#000716", show='*')
        self.teacher_password.place(x=300, y=310)
        login = Button(self.cvs, text="Login", font="Arial 16",
                           command=self.login,
                           bg="#a0ccda")
        login.place(x=280, y=350)
        back = Button(self.cvs, text="Back", font="Arial 16",
                           command=lambda: self.controller.show_frame(HomePage),
                           bg="#a0ccda")
        back.place(x=370, y=350)
        self.cvs.pack()

if __name__ == '__main__':
    app = MyApp()
    app.title('Attendance Management Application')
    app.create_tables()
    app.resizable(False,False)
    app.mainloop()