from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.ttk as ttk
import GUI

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Furniture Store Management System")
        self.root.geometry("1000x580")
        self.root.resizable(False, False)
        #img
        self.IMAGE_WIDTH = 540
        self.IMAGE_HEIGHT = 580
        image = Image.open("images/bg.png")
        image = image.resize((self.IMAGE_WIDTH,self.IMAGE_HEIGHT), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)
        Label(self.root, image=self.image).place(x=0, y=0, width=self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)

        #------------Login frame------------
        self.loginFrame = Frame(self.root)
        self.loginFrame.place(x=self.IMAGE_WIDTH, y=0, width=1000-self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)

        self.loginLabel = ttk.Label(self.loginFrame)
        self.loginLabel.configure(
            compound="top",
            font="{Arial Rounded MT Bold} 30 {bold}",
            justify="center",
            padding="12",
            text="Login"
        )
        self.loginLabel.pack(anchor="center", pady="100", side="top")
        
        #Entry variables
        self.L_usernameEntryValue = StringVar()
        self.L_passwordEntryValue = StringVar()

        self.L_username = ttk.Label(self.loginFrame)
        self.L_username.configure(text="Username")
        self.L_username.place(anchor="nw", relwidth="0.17", relx="0.0", x="110", y="180")
        self.L_usernameEntry = ttk.Entry(self.loginFrame,textvariable=self.L_usernameEntryValue)
        self.L_usernameEntry.configure(width="40")
        self.L_usernameEntry.place(anchor="nw", x="110", y="205")

        self.L_password = ttk.Label(self.loginFrame)
        self.L_password.configure(text="Password")
        self.L_password.place(anchor="nw", relwidth="0.17", relx="0.0", x="110", y="240")
        self.L_passwordEntry = ttk.Entry(self.loginFrame, show="•",textvariable=self.L_passwordEntryValue)
        self.L_passwordEntry.configure(width="40")
        self.L_passwordEntry.place(anchor="nw", x="110", y="265")

        self.loginBtn = ttk.Button(self.loginFrame, command=self.login)
        self.loginBtn.configure(text="Login", width="40")
        self.loginBtn.place(anchor="nw", x="108", y="310")

        self.signupPageBtn = ttk.Button(self.loginFrame, command=self.openSignupPage)
        self.signupPageBtn.configure(text="Sign up page", width="40")
        self.signupPageBtn.place(anchor="nw", x="108", y="350")


        #------------Signup frame------------
        self.signupFrame = Frame(self.root)
        self.signupFrame.place(x=self.IMAGE_WIDTH, y=0, width=1000-self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)

        self.signupLabel = ttk.Label(self.signupFrame)
        self.signupLabel.configure(
            compound="top",
            font="{Arial Rounded MT Bold} 30 {bold}",
            justify="center",
            padding="12",
            text="Sign up"
        )
        self.signupLabel.pack(anchor="center", pady="100", side="top")
        
        #Entry variables
        self.S_usernameEntryValue = StringVar()
        self.S_passwordEntryValue = StringVar()
        self.S_confirmPasswordEntryValue = StringVar()

        self.S_username = ttk.Label(self.signupFrame)
        self.S_username.configure(text="Username")
        self.S_username.place(anchor="nw", relwidth="0.17", relx="0.0", x="110", y="180")
        self.S_usernameEntry = ttk.Entry(self.signupFrame,textvariable=self.S_usernameEntryValue)
        self.S_usernameEntry.configure(width="40")
        self.S_usernameEntry.place(anchor="nw", x="110", y="205")

        self.S_password = ttk.Label(self.signupFrame)
        self.S_password.configure(text="Password")
        self.S_password.place(anchor="nw", relwidth="0.17", relx="0.0", x="110", y="240")
        self.S_passwordEntry = ttk.Entry(self.signupFrame, show="•",textvariable=self.S_passwordEntryValue)
        self.S_passwordEntry.configure(width="40")
        self.S_passwordEntry.place(anchor="nw", x="110", y="265")

        self.S_confirmPassword = ttk.Label(self.signupFrame)
        self.S_confirmPassword.configure(text="Confirm password")
        self.S_confirmPassword.place(anchor="nw", relwidth="0.26", relx="0.0", x="110", y="300")
        self.S_confirmPasswordEntry = ttk.Entry(self.signupFrame, show="•",textvariable=self.S_confirmPasswordEntryValue)
        self.S_confirmPasswordEntry.configure(width="40")
        self.S_confirmPasswordEntry.place(anchor="nw", x="110", y="325")

        self.signupBtn = ttk.Button(self.signupFrame, command=self.signup)
        self.signupBtn.configure(text="Sign up", width="40")
        self.signupBtn.place(anchor="nw", x="108", y="365")

        self.loginPageBtn = ttk.Button(self.signupFrame, command=self.openLoginPage)
        self.loginPageBtn.configure(text="Login page", width="40")
        self.loginPageBtn.place(anchor="nw", x="108", y="405")

        #hide signup frame initially
        self.signupFrame.place_forget()

    def run(self):
        self.root.mainloop()

    def login(self):
        messagebox.showinfo("Login", "Login Successful!")
        self.root.withdraw()
        mainWindow = Toplevel(self.root)
        GUI.App(mainWindow,self.root).run()

    def signup(self):
        messagebox.showinfo("Sign up", "Sign up Successful!")

    def openSignupPage(self):
        self.loginFrame.place_forget()
        self.signupFrame.place(x=self.IMAGE_WIDTH, y=0, width=1000-self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)

    def openLoginPage(self):
        self.signupFrame.place_forget()
        self.loginFrame.place(x=self.IMAGE_WIDTH, y=0, width=1000-self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)

if __name__ == "__main__":
    root = Tk()
    Login(root).run()

