class Cryptography():
      
    def __init__(self):
        return
    
    def EncryptString(self,inputString):
        self.output = ""
        
        for i in inputString:           
            self.output += chr(ord(i) + 3)
            
        return self.output              
     
    def DecryptString(self,inputString):  
        self.output = ""
        
        for i in inputString:           
            self.output += chr(ord(i) - 3)
            
        return self.output       
