import tkinter
from tkinter import messagebox as msg
import customtkinter
import Cryptography
import json
import os



class MainMenu(customtkinter.CTk):
    
    
    defaultWindowHeight = 1000
    defaultWindowWidth = 1000

    
    def __init__(self):
        super().__init__()
             
        self.title("Main Menu")
        self.geometry(f"{MainMenu.defaultWindowWidth}x{MainMenu.defaultWindowHeight}")

        
        
