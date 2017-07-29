''' Application GUI '''
import Tkinter as tk
from PIL import Image, ImageTk

class Login(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=0, **kwargs)
        usr = tk.StringVar()
        password = tk.StringVar()
        im = Image.open('/home/solus/twilio/pink.jpg')
        image1 = ImageTk.PhotoImage(im)
        button1 = tk.Button(self, text="Login",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0,
                            command=lambda: self.callback())
        button2 = tk.Button(self, text="Register",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0)
        button3 = tk.Button(self, text="Forgot Password",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=1, width=10, borderwidth=0)
        button1.place(x=200, y=200, relwidth=.1, relheight=.1,)
        button2.place(x=500, y=200, relwidth=.1, relheight=.1)
        button3.place(x=200, y=500, relwidth=.1, relheight=.1)
        label_usrname = tk.Label(self, text="Username")
        label_password = tk.Label(self, text="Password")
        label_password.place(x=100, y=100, relwidth=.1, relheight=.1)
        label_usrname.place(x=100, y=200, relwidth=.1, relheight=.1)
        usrname_field = tk.Entry(self, textvariable=usr)
        usrname_field.place(x=300, y=300, relwidth=.1, relheight=.05)
        password_field = tk.Entry(self, textvariable=password)
        password_field.place(x=600, y=300, relwidth=.1, relheight=.05, )
        print usrname_field.get(), password_field.get()

    def onlift(self):
        print "nuker"
        self.lift()

class Register(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=0, **kwargs)
        usr = tk.StringVar()
        password = tk.StringVar()
        im = Image.open('/home/solus/twilio/purple.jpg')
        image1 = ImageTk.PhotoImage(im)
        button1 = tk.Button(self, text="Login",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0)
        button2 = tk.Button(self, text="Register",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0,
                            command=lambda: self.callback())
        button3 = tk.Button(self, text="Forgot Password",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=1, width=10, borderwidth=0)
        button2.place(x=500, y=200, relwidth=.1, relheight=.1)
        button3.place(x=200, y=500, relwidth=.1, relheight=.1)
        label_usrname = tk.Label(self, text="Username")
        label_password = tk.Label(self, text="Password")
        label_password.place(x=100, y=100, relwidth=.1, relheight=.1)
        label_usrname.place(x=100, y=200, relwidth=.1, relheight=.1)
        usrname_field = tk.Entry(self, textvariable=usr)
        usrname_field.place(x=300, y=300, relwidth=.1, relheight=.05)
        password_field = tk.Entry(self, textvariable=password)
        password_field.place(x=600, y=300, relwidth=.1, relheight=.05, )
        print usrname_field.get(), password_field.get()

    def onlift(self):
        print "not nuker"
        self.lift()

class MainPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=0, **kwargs)
        button2 = tk.Button(self, text="MainPage",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0,
                            command=lambda: self.callback())
        button2.place(x=500, y=200, relwidth=.1, relheight=.1)
    def onlift(self):
        self.lift()

class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        p1 = Login(self)
        p2 = Register(self)
        p3 = MainPage(self)
        p1.callback = p2.onlift
        p2.callback = p3.onlift
        p3.callback = p1.onlift
        p1.place(x=0, y=0, relwidth=1, relheight=1)
        p2.place(x=0, y=0, relwidth=1, relheight=1)
        p3.place(x=0, y=0, relwidth=1, relheight=1)
        p1.onlift()

class Settings(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=0, **kwargs)
        button2 = tk.Button(self, text="MainPage",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0,
                            command=lambda: self.callback())
        button2.place(x=500, y=200, relwidth=.1, relheight=.1)
    def onlift(self):
        self.lift()

class Update(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=0, **kwargs)
        button2 = tk.Button(self, text="MainPage",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0,
                            command=lambda: self.callback())
        button2.place(x=500, y=200, relwidth=.1, relheight=.1)
    def onlift(self):
        self.lift()

class History(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=0, **kwargs)
        button2 = tk.Button(self, text="MainPage",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0,
                            command=lambda: self.callback())
        button2.place(x=500, y=200, relwidth=.1, relheight=.1)
    def onlift(self):
        self.lift()


class Upgrade(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=0, **kwargs)
        button2 = tk.Button(self, text="MainPage",
                            fg="white", activeforeground="yellow",
                            activebackground="black", bg="black",
                            height=2, width=3, borderwidth=0,
                            command=lambda: self.callback())
        button2.place(x=500, y=200, relwidth=.1, relheight=.1)
    def onlift(self):
        self.lift()

root = tk.Tk()
app = App(root)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Trying Tinker")
root.mainloop()