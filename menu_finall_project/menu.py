# define a class to get users information 
class User :
    
    # a function to get data 
    def __init__ (self , name , number , adress):
        self.name = name 
        self.number = number
        self.adress = adress

    # a function to show welcome
    def welcome (self):
        print (f"weclome {self.name}")
# a parent class for foods 
class Food :
     
    # this function set all nececcery datas
    def __init__(self,name,cost,size,time_of_preparation,ingredients) :
        self.name = name 
        self.cost = cost
        self.size = size
        self.time_of_preparation = time_of_preparation
        self.ingredient = ingredients

    #this function show the datas about a food 
    def show (self):
        l = []
        l.append(f"the cost of {self.name} : {self.cost} $")
        l.append(f"the size of {self.name} : {self.size}")
        l.append(f"the time_of_preparation of {self.name} : {self.time_of_preparation} minutes")
        l.append(f"the ingredient of {self.name} : {self.ingredients}")
        return l 

    # this function set mount of food     
    def SetSize(self,size):
       self.choosen_size=size;

    # this function calculat the cost of food and show it     
    def CalcCost (self): 
        if self.choosen_size == "M" : 
            self.finall_cost = self.cost
            print(self.finall_cost + " $") 
        elif self.choosen_size == "L":
            self.finall_cost = str(int(self.cost)*1.5)
            print(self.finall_cost + " $")
        else :
            print ("invalid input")

class Kebab (Food):
    
    def __init__(self):
        self.name = "Kebab"
        self.cost = "50"
        self.size = "M,L"
        self.time_of_preparation = "35"
        self.ingredients= "meat,onion,tomato,bread"
        
        Food.__init__(self,self.name,self.cost,self.size,self.time_of_preparation,self.ingredients)
        
class ItalinPizza (Food):
    
    def __init__(self):
        self.name = "Italin Pizza"
        self.cost = "35"
        self.size = "M,L"
        self.time_of_preparation = "30"
        self.ingredients= "tomato,cheese,mushrooms"
        
        Food.__init__(self,self.name,self.cost,self.size,self.time_of_preparation,self.ingredients)
        
class Burger (Food):
    
    def __init__(self):
        self.name = "burger"
        self.cost = "20"
        self.size = "M,L"
        self.time_of_preparation = "25"
        self.ingredients= "tomato,cheese,mushrooms,meat,baguette"
        
        Food.__init__(self,self.name,self.cost,self.size,self.time_of_preparation,self.ingredients)
        
class SaladSezar (Food):
    
    def __init__(self):
        self.name = "SaladSezar"
        self.cost = "10"
        self.size = "M,L"
        self.time_of_preparation = "5"
        self.ingredients= "tomato,cucumber,lettuce,chicken"
        
        Food.__init__(self,self.name,self.cost,self.size,self.time_of_preparation,self.ingredients)

#a parent class for drinks 
class Drink :

    # this function set all nececcery datas
    def __init__(self,name,cost,size,kind) :
        self.name = name 
        self.cost = cost
        self.size = size
        self.kind = kind

    #this function show the datas about a food    
    def show (self):
        l2=[]
        l2.append(f"the cost of {self.name} : {self.cost} $")
        l2.append(f"the size of {self.name} : {self.size}")
        l2.append(f"the kind of {self.name} : {self.kind}")
        return l2

    # this function set mount of food
    def SetSize(self,size):
       self.choosen_size=size;

    # this function calculat the cost of food and show it     
    def CalcCost (self): 
        if self.choosen_size == "M" : 
            self.finall_cost = self.cost
            print(self.finall_cost + " $") 
        elif self.choosen_size == "L":
            self.finall_cost = str(int(self.cost)*1.5)
            print(self.finall_cost + " $")
        else :
            print ("invalid input")        

class Water (Drink):
    
    def __init__(self):
        self.name = "water"
        self.cost = "2"
        self.size = "M,L"
        self.kind= "bottle"
        
        Drink.__init__(self,self.name,self.cost,self.size,self.kind)
        
class Soda (Drink):
    
    def __init__(self):
        self.name = "soda"
        self.cost = "4"
        self.size = "M,L"
        self.kind= "Metal bottle"
        
        Drink.__init__(self,self.name,self.cost,self.size,self.kind)
'''
 # class tests 

user1 = User("Ali" , "09303195786"  , "Tabriz")
user1.welcome()
print ("-------------------------------------------------------------------------------------------------------------------------------")

food1 = ItalinPizza()
food1.show()
food1.SetSize("L")
food1.CalcCost()

print ("-------------------------------------------------------------------------------------------------------------------------------")

drink1 = Soda()
drink1.show()
drink1.SetSize("M")
drink1.CalcCost()

print ("-------------------------------------------------------------------------------------------------------------------------------")
 
'''        

#import packages
import tkinter as tk
from PIL import ImageTk , Image
from tkinter import ttk

#making an inctance of tk class that makes a window 
window = tk.Tk()

window.title("Menu")
window.resizable(0,0)
window.geometry("850x670")

# making scrollbar 
main_frame = tk.Frame()
main_frame.pack(fill=tk.BOTH,expand=True)
my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
my_scrolbar = ttk.Scrollbar(main_frame,orient=tk.VERTICAL,command=my_canvas.yview)
my_scrolbar.pack(side=tk.RIGHT,fill=tk.Y)
my_canvas.configure(yscrollcommand=my_scrolbar.set)
my_canvas.bind('<Configure>',lambda e : my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = tk.Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")

frm1 = tk.Frame(master=second_frame , bg="#ffe4c4")
lbl1= tk.Label(master = frm1,text = "enter your name " , height=1 , width=100 , font = 25 , bg="#ffe4c4")
ent1 = tk.Entry(master = frm1, width=50 )
lbl2= tk.Label(master = frm1,text = "enter your number" , height=1, width=100 ,  font = 25 , bg="#ffe4c4" )
ent2 = tk.Entry(master = frm1, width=50 )
lbl3= tk.Label(master = frm1,text = "enter your adress" , height=1, width=100 ,  font = 25 , bg="#ffe4c4" )
ent3 = tk.Entry(master = frm1 , width=50  )

def btn1Click ():
    btnlbl= tk.Label(text="successfully registered")
    btnlbl.pack()
    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    
btn1 = tk.Button(master = frm1,text="registered" , command=btn1Click)


frm1.pack(fill=tk.BOTH , expand=True)
lbl1.pack()
ent1.pack()
lbl2.pack()
ent2.pack()
lbl3.pack()
ent3.pack()
btn1.pack()

#save users infrmation in variables
name = ent1.get()
number = ent2.get()
adress = ent3.get()

frm2 = tk.Frame(master=second_frame,width=200,height=1700 ,bg="#ffe4c4")

img1 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/menu_finall_project/kebab.jpg"))
kebablbl = tk.Label(master = frm2 , image=img1 )

food1= Kebab()
show1 = food1.show()

kebablbl2 = tk.Label(master=frm2 ,text=show1[0] )
kebablbl3 = tk.Label(master=frm2 ,text=show1[1] )
kebablbl4 = tk.Label(master=frm2 ,text=show1[2] )
kebablbl5 = tk.Label(master=frm2 ,text=show1[3] )

frm2.pack(fill=tk.BOTH , expand=True)
kebablbl.place(x=20,y=5)
kebablbl2.place(x=400,y=40)
kebablbl3.place(x=400,y=70)
kebablbl4.place(x=400,y=100)
kebablbl5.place(x=400,y=130)

food2=ItalinPizza()
show2 = food2.show()

img2 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/menu_finall_project/pizza.jpg"))
ItalinPizzalbl = tk.Label(master = frm2 , image=img2 )

ItalinPizzalbl2 = tk.Label(master=frm2 ,text=show2[0] )
ItalinPizzalbl3 = tk.Label(master=frm2 ,text=show2[1] )
ItalinPizzalbl4 = tk.Label(master=frm2 ,text=show2[2] )
ItalinPizzalbl5 = tk.Label(master=frm2 ,text=show2[3] )

frm2.pack(fill=tk.BOTH , expand=True)
ItalinPizzalbl.place(x=20,y=250)
ItalinPizzalbl2.place(x=400,y=280)
ItalinPizzalbl3.place(x=400,y=310)
ItalinPizzalbl4.place(x=400,y=340)
ItalinPizzalbl5.place(x=400,y=370)

food3=Burger()
show3 = food3.show()

img3 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/menu_finall_project/burger.jpg"))
Burgerlbl = tk.Label(master = frm2 , image=img3 )

Burgerlbl2 = tk.Label(master=frm2 ,text=show3[0] )
Burgerlbl3 = tk.Label(master=frm2 ,text=show3[1] )
Burgerlbl4 = tk.Label(master=frm2 ,text=show3[2] )
Burgerlbl5 = tk.Label(master=frm2 ,text=show3[3] )

frm2.pack(fill=tk.BOTH , expand=True)
Burgerlbl.place(x=20,y=550)
Burgerlbl2.place(x=400,y=580)
Burgerlbl3.place(x=400,y=610)
Burgerlbl4.place(x=400,y=640)
Burgerlbl5.place(x=400,y=670)

food4=SaladSezar()
show4 = food4.show()

img4 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/menu_finall_project/SaladSezar.jpg"))
SaladSezarlbl = tk.Label(master = frm2 , image=img4 )

SaladSezarlbl2 = tk.Label(master=frm2 ,text=show4[0] )
SaladSezarlbl3 = tk.Label(master=frm2 ,text=show4[1] )
SaladSezarlbl4 = tk.Label(master=frm2 ,text=show4[2] )
SaladSezarlbl5 = tk.Label(master=frm2 ,text=show4[3] )

frm2.pack(fill=tk.BOTH , expand=True)
SaladSezarlbl.place(x=20,y=850)
SaladSezarlbl2.place(x=400,y=880)
SaladSezarlbl3.place(x=400,y=910)
SaladSezarlbl4.place(x=400,y=940)
SaladSezarlbl5.place(x=400,y=970)

drink1 = Water()
show5 = drink1.show()

img5 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/menu_finall_project/water.jpg"))
Waterlbl = tk.Label(master = frm2 , image=img5 )

Waterlbl2 = tk.Label(master=frm2 ,text=show5[0] )
Waterlbl3 = tk.Label(master=frm2 ,text=show5[1] )
Waterlbl4 = tk.Label(master=frm2 ,text=show5[2] )

frm2.pack(fill=tk.BOTH , expand=True)
Waterlbl.place(x=20,y=1150)
Waterlbl2.place(x=400,y=1180)
Waterlbl3.place(x=400,y=1210)
Waterlbl4.place(x=400,y=1240)

drink2= Soda()
show6 = drink2.show()

img6 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/menu_finall_project/soda.jpg"))
Sodalbl = tk.Label(master = frm2 , image=img6 )

Sodalbl2 = tk.Label(master=frm2 ,text=show6[0] )
Sodalbl3 = tk.Label(master=frm2 ,text=show6[1] )
Sodalbl4 = tk.Label(master=frm2 ,text=show6[2] )

frm2.pack(fill=tk.BOTH , expand=True)
Sodalbl.place(x=20,y=1450)
Sodalbl2.place(x=400,y=1480)
Sodalbl3.place(x=400,y=1510)
Sodalbl4.place(x=400,y=1540)

#keep window open
window.mainloop()