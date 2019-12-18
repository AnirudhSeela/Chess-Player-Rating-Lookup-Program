from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Text, messagebox
import requests
from bs4 import BeautifulSoup

class Search:

    def __init__(self, master):
        self.master = master
        master.title("Chess Player Rating Search")

        self.title = Label(master, text="Welcome to the Chess Player Rating Lookup!")
        self.dir = Label(master, text="Enter your info in the fields below.")

        self.firstname = Label(master, text="First Name:")
        self.lastname = Label(master, text="Last Name:")

        self.firstname_text = Entry(master)
        self.lastname_text = Entry(master)

        self.search_button = Button(master, text="Search", command=lambda: self.search())
        self.exit_button = Button(master, text="EXIT", command=master.quit)

        self.title.grid(row=0, column=0, sticky=W)
        self.dir.grid(row=1, column=0, sticky=W)

        self.firstname.grid(row=2, column=0, sticky=W)
        self.firstname_text.grid(row=2, column=1, sticky=W)

        self.lastname.grid(row=3, column=0, sticky=W)
        self.lastname_text.grid(row=3,column=1, sticky = W)

        self.search_button.grid(row=4, column=1)
        self.exit_button.grid(row=4, column=2, sticky=W)


    def search(self):

        try:
            firstName = self.firstname_text.get()
            lastName = self.lastname_text.get()

            url = 'http://www.uschess.org/datapage/player-search.php?name=' + firstName + "+" + lastName + '&state=ANY&ratingmin=&ratingmax=&order=N&rating=R&mode=Find'

            r = requests.get(url)

            rating = []

            soup = BeautifulSoup(r.content, 'html.parser')
            for form in soup.find_all("td"):
                rating.append(form)

            str1 = ''.join(rating[15])
            messagebox.showinfo('Rating', firstName.capitalize() + " " + lastName.capitalize() + '\'s rating is '
                                + str1.strip() + ".")
        except Exception:
            messagebox.showerror("Error!", "This person does not have a rating! Please check your input and try again!")


root = Tk()
my_gui = Search(root)
root.mainloop()
