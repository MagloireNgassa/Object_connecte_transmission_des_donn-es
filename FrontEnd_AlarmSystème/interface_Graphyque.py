import tkinter as tk

root = tk.Tk()
root.geometry("340x300+30+30")

class Graphique:
    def __init__(self):
        self.colorZone_1 = 'grey'
        self.colorZone_2 = 'grey'
        self.colorZone_3 = 'grey'
        self.colorZone_4 = 'grey'
        self.colorActivate = 'grey'
        self.colorDesactivate = 'grey'
        self.colorReset = 'grey'
        self.colorOnOff = 'grey'
        
        
    
        
    def colorZone1_on(self):
        if (self.colorZone_1 == 'green' and self.colorActivate =='yellow'):
            self.colorZone_1 = 'red'
            self.colorReset = 'red'
 
        
        
    def colorZone2_on(self):
        if (self.colorZone_2 == 'green'and self.colorActivate =='yellow'):
            self.colorZone_2 = 'red'
            self.colorReset = 'red'
 

        
    def colorZone3_on(self):
        if (self.colorZone_3 == 'green'and self.colorActivate =='yellow'):
            self.colorZone_3 = 'red'
            self.colorReset = 'red'
 
        
    def colorZone4_on(self):
        if (self.colorZone_4 == 'green'and self.colorActivate =='yellow'):
            self.colorZone_4 = 'red'
            self.colorReset = 'red'
 

    
    def colorActivate_on(self):
        if self.colorActivate == 'grey':
            self.colorActivate = 'yellow'
            self.colorDesactivate = 'grey'
            self.colorZone_1 = 'green'
            self.colorZone_2 = 'green'
            self.colorZone_3 = 'green'
            self.colorZone_4 = 'green'
#         else:
#             self.colorActivate = 'grey'

    def colorReset_on(self):
        self.colorReset = 'grey'
        if self.colorActivate == 'yellow':
            self.colorZone_1 = 'green'
            self.colorZone_2 = 'green'
            self.colorZone_3 = 'green'
            self.colorZone_4 = 'green'

    def colorDesactivate_on(self):
        if self.colorDesactivate == 'grey':
            self.colorDesactivate = 'yellow'
            self.colorActivate = 'grey'
            self.colorZone_1 = 'grey'
            self.colorZone_2 = 'grey'
            self.colorZone_3 = 'grey'
            self.colorZone_4 = 'grey'
#         else:
#             self.colorDesactivate = 'grey'
            
    def colorOnOf_on(self):
        if self.colorOnOff == 'grey':
            self,colorOnOff = 'yellow'
        else:
            self.colorOnOff = 'grey'
            
    def on(self):
        print('systeme demarer')
        
    def counter_label(self, button): #cette fonction cree une boucle infin qui tourne sur elle meme avec un deconpte
        def count1():
            button.config(bg='grey')
            button.after(1000, count2)
        def count2():
            button.config(bg='red')
            button.after(1000, count1)
        count1()
        
    def construire(self):
        frame = tk.Frame(root)

        lz1 = tk.Label(root, 
                text='Zone 1', 
                fg= 'Black', 
                bg= self.colorZone_1)
        lz1.place(x = 20, y = 30, width=75, height=75)

        lz2 = tk.Label(root, 
                text='Zone 2', 
                fg= 'Black', 
                bg=self.colorZone_2)
        lz2.place(x = 100, y = 30, width=75, height=75)

        lz3 = tk.Label(root, 
                text='Zone 3', 
                fg= 'Black', 
                bg=self.colorZone_3)
        lz3.place(x = 20, y = 110, width=75, height=75)

        lz4 = tk.Label(root, 
                text='Zone 4', 
                fg= 'Black', 
                bg=self.colorZone_3)
        lz4.place(x = 100, y = 110, width=75, height=75)

        l = tk.Label(root, 
                text='start Alarm', 
                fg= 'Black')
        l.place(x = 50, y = 190, width=100, height=30)

        b = tk.Button(root, 
                text='On / Off', 
                fg= 'Black',bg=self.colorOnOff, command = self.on)
        #self.counter_label(b)
        b.place(x = 50, y = 225, width=120, height=50)

        lact = tk.Label(root, 
                text='Active', 
                fg= 'Black', 
                bg=self.colorActivate)
        lact.place(x = 190, y = 30, width=120, height=50)

        ldesact = tk.Label(root, 
                text='Desactive', 
                fg= 'Black', 
                bg=self.colorDesactivate)
        ldesact.place(x = 190, y = 83, width=120, height=50)

        lrest = tk.Label(root, 
                text='Reset', 
                fg= 'Black', 
                bg=self.colorReset)
        lrest.place(x = 190, y =136, width=120, height=50)
        

        
        
        
   
        
        
        