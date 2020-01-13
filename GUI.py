import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 15)
path = "/Users/geraldine/PycharmProjects/FYP_ML_GUI/images/images.jpeg"

# start page image

with Image.open(path) as img:
    w, h = img.size


class MyGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self,width =w+100, height = h+100)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0)
            frame.pack_propagate(0)


        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=w+100, height=h+100,bg="RED")
        img = ImageTk.PhotoImage(Image.open(path))
        label = tk.Label(self, image=img)
        label.image = img
        label.pack()

        button1 = ttk.Button(self, text="Page One",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=w+100, height=h+100)

        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,width=w+100, height=h+100)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = MyGui()
app.mainloop()
