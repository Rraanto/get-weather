import tkinter as tk
from PIL import ImageTk, Image
import pathlib
from os import path

# Path to the directory containing the file
WORKPATH = pathlib.Path(__file__).parent.absolute()

# styling constants
# headers
H1 = "Avenir 44 bold"
H2 = "Avenir 22 bold"
H3 = "Avenir 16"

# paragraph
P = "Avenir 14"

# color hex codes
FIRE_ENGINE_RED = "#C1292E"
QUEEN_BLUE = "#386FA4"
EERIE_BLACK = "#1C1C1C"
GAINSBORO = "#DADDD8"
CULTURED = "#EEF0F2"
ORANGE_RED_CRAYOLA = "#FF5A5F"
CAMBRIDGE_BLUE = "#A2C5AC"
GLAUCOUS = "#6E7DAB"
ROYAL_BLUE_LIGHT = "#5762D5"

# path constants


class Window(tk.Tk):
    def __init__(self, place, subtitle):
        super().__init__()
        # general configuration of the window
        self.geometry("600x500")

        self.main_frame = tk.Frame(
            master=self,
        )

        # main header of the window
        self.header = tk.Label(
            master=self.main_frame,
            text=place,
            font=H2
        )
        self.header.pack(
            ipady=10,
            ipadx=10,
            anchor="n"
        )

        # main title of the weather
        self.title = tk.Label(
            master=self.main_frame,
            text=subtitle,
            font=H1
        )

        self.title.pack(
            anchor="center",
            expand=True
        )

        # center frame of the window
        self.center_frame = tk.Frame(
            master=self.main_frame,
        )

        # test : add icon
        icon1 = Image.open("/users/rantonyainarakotondrajoa/requests/assets/icons/temperature.png")
        icon1 = icon1.resize((50, 50))
        self.icontk = ImageTk.PhotoImage(icon1, master=self.main_frame)
        self.label1 = tk.Label(image=self.icontk)
        self.label1.image = self.icontk

        self.label1.place(x=0, y=0)

        self.main_frame.pack()
        self.set_background(ROYAL_BLUE_LIGHT)
        self.set_foreground(CULTURED)
        self.mainloop()

    def set_background(self, color):
        self['bg'] = color
        self.main_frame.configure(bg=color)
        self.header.configure(bg=color)
        self.title.configure(bg=color)
        self.center_frame.configure(bg=color)

    def set_foreground(self, color):
        self.header.configure(fg=color)
        self.title.configure(fg=color)


if __name__ == "__main__":
    place = "Saint-Martin-D'Hères, France"
    main_weather = "Overcast clouds"
    draft_window = Window(place, main_weather)
