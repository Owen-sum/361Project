import tkinter
import customtkinter

def startSearch():
    print("Search started!")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1920x1080")
app.title("TripCostCalculator")
loginPage = customtkinter.Frame(app)
searchPage = customtkinter.Frame(app)

dest_var = tkinter.StringVar()
title = customtkinter.CTkLabel(app, text="Enter a destination")
title.pack(padx=10, pady=10)

searchInput = customtkinter.CTkEntry(app, width=350, height=40, textvariable=dest_var)
searchInput.pack(pady=30)

search = customtkinter.CTkButton(app, text="search", command=startSearch)
search.pack(pady=10)

app.mainloop()