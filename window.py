import tkinter as tk
from PIL import ImageTk, Image
import pathlib
from os import path

# Path to the directory containing the file
WORKPATH = pathlib.Path(__file__).parent.absolute()

# styling constants
# headers
H1 = "Avenir 44 bold"
H2 = "Avenir 30 bold"
H3 = "Avenir 25"

# paragraph
P = "Helvetica 22"

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


class Window(tk.Tk):
    def __init__(self, place, subtitle, temperature, humidity, pressure):
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

        self.temp_title = tk.Label(
            master=self.center_frame,
            text="Temperature : ",
            font=P
        ).grid(row=0, column=0, sticky="w")

        self.temp_res = tk.Label(
            master=self.center_frame,
            text=temperature,
            font=P
        ).grid(row=0, column=1)

        self.pres_title = tk.Label(
            master=self.center_frame,
            text="Pressure : ",
            font=P
        ).grid(row=1, column=0, sticky="w")

        self.pres_res = tk.Label(
            master=self.center_frame,
            text=pressure,
            font=P
        ).grid(row=1, column=1)

        self.hum_title = tk.Label(
            master=self.center_frame,
            text="Humidity : ",
            font=P
        ).grid(row=2, column=0, sticky="w")

        self.hum_res = tk.Label(
            master=self.center_frame,
            text=humidity,
            font=P
        ).grid(row=2, column=1)

        self.center_frame.pack(
            expand=True, anchor="w",
            pady=10,
            padx=0
        )
        self.main_frame.pack(
            expand=True,
            anchor="n"
        )
        self.set_background(CULTURED)
        self.set_foreground(EERIE_BLACK)

    def set_background(self, color):
        self['bg'] = color
        self.main_frame.configure(bg=color)
        for children in self.main_frame.winfo_children():
            children.configure(bg=color)
        for children in self.center_frame.winfo_children():
            children.configure(bg=color)

    def set_foreground(self, color):
        for children in self.main_frame.winfo_children():
            if type(children) == tk.Label:
                children.configure(fg=color)
        for children in self.center_frame.winfo_children():
            children.configure(fg=color)


if __name__ == "__main__":
    place = "Saint-Martin-D'Hères, France"
    main_weather = "Overcast clouds"
    temperature = "15°C"
    humidity = "85%"
    pressure = "1009"
    draft_window = Window(
        place=place,
        subtitle=main_weather,
        temperature=temperature,
        pressure=pressure,
        humidity=humidity
    )

    draft_window.mainloop()
