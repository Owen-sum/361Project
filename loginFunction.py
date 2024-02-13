import tkinter as tk
from tkinter import Frame, Entry, Label, Button, messagebox

def search():
    input = Search.get_input_field()
    if len(input) > 1: 
            print("Searched for " + input)
    else:
            messagebox.showerror("Error", "Please enter a value in the login field.")

class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master,  bg="#404040")
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        button_style = {"font": ("Helvetica", 16), "bg": "#333333", "fg": "white", "width": 10}

        self.title_label = Label(self, text="Travel Calculator", font=("Helvetica", 20), bg="#404040", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5))

        self.input_field = Entry(self, width=20)  
        self.input_field.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 10))

        self.switch_button = Button(self, text="Login", command=self.switch_to_search, **button_style)
        self.switch_button.grid(row=2, column=0, padx=5, pady=10)

        self.quit_button = Button(self, text="Quit", command=self.quit, **button_style)
        self.quit_button.grid(row=2, column=1, padx=5, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        return self.input_field

    def switch_to_search(self):
        if self.input_field.get().strip(): 
            self.grid_forget()  
            app_search.grid()  
        else:
            messagebox.showerror("Error", "Please enter a value in the login field.")

    def get_input_field(self):
        return self.input_field.get().strip()

class Search(Frame):
    def __init__(self, master):
        Frame.__init__(self, master,  bg="#404040")
        self.create_widgets()

    def create_widgets(self):
        button_style = {"font": ("Helvetica", 16), "bg": "#333333", "fg": "white", "width": 10}

        self.title_label = Label(self, text="Enter a destination", font=("Helvetica", 20), bg="#404040", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5))

        self.input_field = Entry(self, width=20)  
        self.input_field.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 10))

        self.logout_button = Button(self, text="Logout", command=self.switch_to_login, **button_style)
        self.logout_button.grid(row=2, column=0, padx=5, pady=10)

        self.search_button = Button(self, text="Search", command=search, **button_style)
        self.search_button.grid(row=2, column=1, padx=5, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        return self.input_field

    def switch_to_login(self):
        self.grid_forget()
        app_login.grid()
    
    def get_input_field(self):
        return self.input_field.get().strip()

root = tk.Tk()
root.title("Login")
root.geometry("300x250")  

app_login = Login(root)
app_search = Search(root)

app_login.configure(bg="#404040")  
app_search.configure(bg="#404040") 

app_login.grid()

root.mainloop()