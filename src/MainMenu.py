import tkinter
from tkinter import messagebox as msg
import customtkinter
import Cryptography
import json
import os




class MainMenu(customtkinter.CTk):
    
    
    defaultWindowHeight = 1000
    defaultWindowWidth = 1000
    controlsWidth = 190

    
    def __init__(self):
        super().__init__()
             
        self.title("Main Menu")
        self.geometry(f"{MainMenu.defaultWindowWidth}x{MainMenu.defaultWindowHeight}")
               
        # configure grid layout (2x1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        

        #create frame to contain entry box and button
        self.Controls_Frame = customtkinter.CTkFrame(master=self)
        self.Controls_Frame.grid(row=0, column=1, sticky="nsw", padx=10 , pady=10)
        
        self.View_Frame = customtkinter.CTkFrame(master=self)
        self.View_Frame.grid(row=0,column=2,sticky="nswe",padx=10,pady=10)

        self.ControlsSub_Frame = customtkinter.CTkFrame(master=self.Controls_Frame,border_color="default_theme",border_width="default_theme")
        self.ControlsSub_Frame.grid(row=0,column=2,sticky="nwe",padx=2,pady=2)
        
        
        #create buttons for controls frame 
        
        self.quit_button = customtkinter.CTkButton(master=self.Controls_Frame,
                                                    text="Exit",
                                                    border_width=2,  # <- custom border_width
                                                    width=self.controlsWidth,
                                                    command=self.quitApplication,
                                                    fg_color="red",
                                                    hover_color="darkRed")
        self.quit_button.place(relx=0.5, rely=0.99, anchor=customtkinter.S)
        
        self.staff_button = customtkinter.CTkButton(master=self.ControlsSub_Frame,
                                                    text="Staff",
                                                    border_width=2,  # <- custom border_width
                                                    width=self.controlsWidth,
                                                    command=self.quitApplication)
        self.staff_button.place(relx=0.5, rely=0.15, anchor=customtkinter.N)
        
        self.stock_button = customtkinter.CTkButton(master=self.ControlsSub_Frame,
                                                    text="Stock",
                                                    border_width=2,  # <- custom border_width
                                                    width=self.controlsWidth,
                                                    command=self.quitApplication)
        self.stock_button.place(relx=0.5, rely=0.30, anchor=customtkinter.N)
        
        self.thursdayBook_button = customtkinter.CTkButton(master=self.ControlsSub_Frame,
                                                    text="Thursday Bookings",
                                                    border_width=2,  # <- custom border_width
                                                    width=self.controlsWidth,
                                                    command=self.quitApplication)
        self.thursdayBook_button.place(relx=0.5, rely=0.45, anchor=customtkinter.N)
        
        self.sundayBook_button = customtkinter.CTkButton(master=self.ControlsSub_Frame,
                                                    text="Sunday Bookings",
                                                    border_width=2,  # <- custom border_width
                                                    width=self.controlsWidth,
                                                    command=self.quitApplication)
        self.sundayBook_button.place(relx=0.5, rely=0.60, anchor=customtkinter.N)     
        
        
        # create label for controls frame
        
        self.controls_label = customtkinter.CTkLabel(master=self.ControlsSub_Frame, text="- Options -", text_font = ("",18))
        self.controls_label.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)
        
        
    def quitApplication(self):
        print ("totaly functional")

        
        
