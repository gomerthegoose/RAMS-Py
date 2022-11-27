import tkinter
import tkinter.messagebox
import customtkinter

class LoginScreen(customtkinter.CTk):
    
    defaultHeight = 150
    defaultWidth = 250
    
    def __init__(self):
        super().__init__()
        
        
        
        self.title("Login")
        self.geometry(f"{LoginScreen.defaultWidth}x{LoginScreen.defaultHeight}")
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #create frame to contain entry box and button
        self.Login_Frame = customtkinter.CTkFrame(master=self)
        self.Login_Frame.grid(row=0, column=1, sticky="nswe", padx=10 , pady=10)
        
              
        # - userName entry field -  
        self.username_Entry = customtkinter.CTkEntry(master=self.Login_Frame,
                                            width=200,
                                            placeholder_text="Usernmae")
        self.username_Entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        
        # - Password entry field - 
        self.password_Entry = customtkinter.CTkEntry(master=self.Login_Frame,
                                            width=200,
                                            placeholder_text="Password")
        self.password_Entry.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
        
        
        # - login Button -
        self.login_Button = customtkinter.CTkButton(master=self.Login_Frame,
                                                text="Login",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.LoginButtonHandle)
        self.login_Button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
        
        
        

        
    
    def HandleLogin(self, username, password):
        print ("-login Attempt-")
        print (username)
        print (password)      
          
    def LoginButtonHandle(self):
        self.HandleLogin(self.username_Entry.get(), self.password_Entry.get())
