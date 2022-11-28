import customtkinter
import LoginScreen


customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

loginScreen = LoginScreen.LoginScreen()
loginScreen.mainloop()
