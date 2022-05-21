import tkinter


class App(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.editcampo = tkinter.Entry()
        self.editcampo.pack()

        # Create the application variable.
        self.contents = tkinter.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.editcampo["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.editcampo.bind('<Key-Return>',
                            self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
        lbl = tkinter.Label(self, text=self.contents.get())
        lbl.pack(padx=10, pady=50)


root = tkinter.Tk()
myapp = App(root)
myapp.mainloop()
