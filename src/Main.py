import customtkinter
import LoginScreen


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

loginScreen = LoginScreen.LoginScreen()
loginScreen.mainloop()

class Main():
    def __init__(self) -> None:
        super().__init__()
        
        
        
    def closeLoginWindow():
        loginScreen.destroy()