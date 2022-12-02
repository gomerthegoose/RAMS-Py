import customtkinter


class MainMenu(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("1000,800")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        mainFrame = customtkinter.CTkFrame()
        mainFrame.grid(row=0,column=0,sticky="nsew")
        
        
        self.pages = {}
        for page in (MainMenuPage,testPage):
            pageName = page.__name__
            frame = page(MainFrame=mainFrame)
            self.pages[pageName] = frame

    def openPage(self,pageName):
        self.pages[pageName].grid(row=0,column=0,sticky="nsew")



class MainMenuPage(customtkinter.CTkFrame):
    def __init__(self,MainFrame):
        # load images with light and dark mode image
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, text="Home",
                                                     command=self.home_button_event)
        self.home_button.grid(row=1, column=1, sticky="ew")

    def home_button_event(self):
        print("fully functional")

class testPage(customtkinter.CTkFrame):
    def __init__(self,MainFrame):
        pass