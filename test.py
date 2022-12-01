import customtkinter as CTK

class App(CTK.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        # create navigation frame
        self.navigation_frame = CTK.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.home_button = CTK.CTkButton(self.navigation_frame, corner_radius=0, height=40, text="Home",
                                                    text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")


        
        self.frame_2_button = CTK.CTkButton(self.navigation_frame, corner_radius=0, height=40, text="Frame 2",
                                                       text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                        command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        

        
        self.frame_3_button = CTK.CTkButton(self.navigation_frame, corner_radius=0, height=40, text="Frame 3",
                                                       text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                        command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        


        # create home frame
        self.home_frame = CTK.CTkFrame(self, corner_radius=0)
        self.home_frame.grid_columnconfigure(0, weight=1)


        # create second frame
        self.second_frame = CTK.CTkFrame(self, corner_radius=0)

        # create third frame
        self.third_frame = CTK.CTkFrame(self, corner_radius=0)
        
        self.controls_label = CTK.CTkLabel(master=self.home_frame, text="- home -", text_font = ("",18))
        self.controls_label.place(relx=0.5, rely=0.5, anchor=CTK.CENTER)
        self.controls_label = CTK.CTkLabel(master=self.second_frame, text="- first -", text_font = ("",18))
        self.controls_label.place(relx=0.5, rely=0.5, anchor=CTK.CENTER)
        self.controls_label = CTK.CTkLabel(master=self.third_frame, text="second", text_font = ("",18))
        self.controls_label.place(relx=0.5, rely=0.5, anchor=CTK.CENTER)
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button


        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")


if __name__ == "__main__":
    app = App()
    app.mainloop()