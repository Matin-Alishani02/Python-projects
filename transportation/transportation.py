# define a class for drivers
class Driver :
    #a constructor to set a drivers info
    def __init__(self, id , name , number , age) :
        self.id=id
        self.name =name
        self.number =number
        self.age =age 

    #a funtion to show drivers info    
    def showDriver (self):
        print (f"the name of driver is : {self.name}" )
        print (f"the number of driver is : {self.number}")
        print (f"the age of driver is : {self.age}")

# define a class for vehicles
class Vehicle :
    #a constructor to set a vehicle info
    def __init__(self, name , kind , plaque , passenger):
        self.name = name 
        self.kind = kind
        self.plaque = plaque
        self.passenger_number= passenger

    #a funtion to show vehicle info     
    def showVehicle (self):
        list1=[]
        list1.append(f"the name of Vehicle is : {self.name}")
        list1.append(f"the kind of Vehicle is : {self.kind}")
        list1.append(f"the plaque of Vehicle is : {self.plaque}")
        return list1

# define a class for travels 
class Travel :
    #a constructor to set a travel info
    def __init__(self, vehicle , origin , destination, distance , time ):
        self.vehicle = vehicle
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.time = time 
        if self.vehicle=="Airplane":
            self.cost = str(int(self.distance)*1500)
        elif self.vehicle=="Bus":
            self.cost = str(int(self.distance)*150)
        elif self.vehicle=="Taxi":
            self.cost = str(int(self.distance)*80)
        elif self.vehicle=="Ship":
            self.cost = str(int(self.distance)*40)

    #a funtion to show  ticket 
    def showTicket(self):
        list2=[]
        list2.append(f"origin : {self.origin}")
        list2.append(f"destination : {self.destination}")
        list2.append(f"time : {self.time}")
        list2.append(f"cost : {self.cost} $")
        return list2

#define driven clases 
class Airplane (Vehicle):
    
    def __init__(self):
        self.name= "Airplane " 
        self.kind= "Passenger"
        self.plaque= "A23_58"
        self.passenger_number = "80"

        Vehicle.__init__(self,self.name,self.kind,self.plaque,self.passenger_number)
    
class Ship (Vehicle):
    
    def __init__(self):
        self.name= "Ship" 
        self.kind= "Freightage"
        self.plaque= "AAD_81"
        self.passenger_number = "0"

        Vehicle.__init__(self,self.name,self.kind,self.plaque,self.passenger_number)

class Bus (Vehicle):
    
    def __init__(self):
        self.name= "BUS " 
        self.kind= "Passenger"
        self.plaque= "A2SD_78"
        self.passenger_number = "40"

        Vehicle.__init__(self,self.name,self.kind,self.plaque,self.passenger_number)

class Taxi (Vehicle):
    
    def __init__(self):
        self.name= "Taxi " 
        self.kind= "Passenger"
        self.plaque= "A23DF_5875"
        self.passenger_number = "4"

        Vehicle.__init__(self,self.name,self.kind,self.plaque,self.passenger_number)

#Test clases and functions 
"""
driver1 = Driver("1273896858","Ali" , "09303195786","32")
driver1.showDriver()
print("--------------------------------------------------------------------------------------------------------")

vehicle1 = Ship()
vehicle2= Bus()
vehicle3 = Airplane()
vehicle4 = Taxi()

vehicle1.showVehicle()
print("--------------------------------------------------------------------------------------------------------")

vehicle2.showVehicle()
print("--------------------------------------------------------------------------------------------------------")

vehicle3.showVehicle()
print("--------------------------------------------------------------------------------------------------------")

vehicle4.showVehicle()
print("--------------------------------------------------------------------------------------------------------")

travel1 = Travel("Taxi","Tabriz", "Tehran", "800" ,"monday")
travel1.showTicket()
"""
#import packages
import tkinter as tk
from PIL import ImageTk , Image
from tkinter import ttk

#making an inctance of tk class that makes a window 
window = tk.Tk()

window.title("Transportation")
window.resizable(0,0)
window.geometry("900x700")

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


frm1 = tk.Frame(master=second_frame ,height=600, bg="#40E0D0")
lbl1= tk.Label(master = frm1,text = "enter your origin : " , height=1 , width=100 , font = 25 , bg="#40E0D0")
ent1 = tk.Entry(master = frm1, width=50 )
lbl2= tk.Label(master = frm1,text = "enter your destination : " , height=1, width=100 ,  font = 25 , bg="#40E0D0" )
ent2 = tk.Entry(master = frm1, width=50 )
lbl3= tk.Label(master = frm1,text = "enter the time you want to travel : " , height=1, width=100 ,  font = 25 , bg="#40E0D0" )
ent3 = tk.Entry(master = frm1 , width=50  )
lbl4= tk.Label(master = frm1,text = "enter the distance : " , height=1, width=100 ,  font = 25 , bg="#40E0D0" )
ent4 = tk.Entry(master = frm1 , width=50  )
lbl5 = tk.Label(master = frm1,text = "enter the vehicle : " , height=1, width=100 ,  font = 25 , bg="#40E0D0" )
ent5 = tk.Entry(master = frm1 , width=50  )

def btn1Click ():
    #save users information in variables
    origin  = ent1.get()
    destination= ent2.get()
    time = ent3.get()
    distance = ent4.get()
    vehicle = ent5.get()

    obj = Travel(vehicle,origin ,destination ,distance ,time )
    ticket=obj.showTicket()
    btnlbl2 = tk.Label(master=frm1 ,text=ticket[0] , width= 50 ,font=40 , bg = "#F4DDD0" )
    btnlbl3 = tk.Label(master=frm1 ,text=ticket[1] , width= 50 ,font=40 , bg = "#F4DDD0")
    btnlbl4 = tk.Label(master=frm1 ,text=ticket[2] ,  width= 50 ,font=40, bg = "#F4DDD0")
    btnlbl5 = tk.Label(master=frm1 ,text=ticket[3] ,  width= 50 ,font=40, bg = "#F4DDD0")
    btnlbl2.pack()
    btnlbl3.pack()
    btnlbl4.pack()
    btnlbl5.pack()

    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    ent4.delete(0,tk.END)
    ent5.delete(0,tk.END)
    
btn1 = tk.Button(master = frm1,text="buy ticket" ,height=2, bg="#B0C4DE" , command=btn1Click)


frm1.pack(fill=tk.BOTH , expand=True)
lbl1.pack()
ent1.pack()
lbl2.pack()
ent2.pack()
lbl3.pack()
ent3.pack()
lbl4.pack()
ent4.pack()
lbl5.pack()
ent5.pack()
btn1.pack()

frm2 = tk.Frame(master=second_frame,width=200,height=1100 ,bg="#40E0D0")

img1 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/transportation/Airplane.jpg"))
Airpalnelbl = tk.Label(master = frm2 , image=img1 )

vehicle1 = Airplane()
show1 = vehicle1.showVehicle()

Airpalnelbl2 = tk.Label(master=frm2 ,text=show1[0] , bg = "#DDA0DD", font=32 )
Airpalnelbl3 = tk.Label(master=frm2 ,text=show1[1] , bg = "#DDA0DD", font=32)
Airpalnelbl4 = tk.Label(master=frm2 ,text=show1[2] , bg = "#DDA0DD", font=32)

frm2.pack(fill=tk.BOTH , expand=True)
Airpalnelbl.place(x=20,y=5)
Airpalnelbl2.place(x=400,y=40)
Airpalnelbl3.place(x=400,y=70)
Airpalnelbl4.place(x=400,y=100)

vehicle2= Taxi()
show2 = vehicle2.showVehicle()

img2 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/transportation/taxi.jpg"))
Taxilbl = tk.Label(master = frm2 , image=img2 )

Taxilbl2 = tk.Label(master=frm2 ,text=show2[0] , bg = "#DDA0DD", font=32)
Taxilbl3 = tk.Label(master=frm2 ,text=show2[1] , bg = "#DDA0DD", font=32)
Taxilbl4 = tk.Label(master=frm2 ,text=show2[2] , bg = "#DDA0DD", font=32)

frm2.pack(fill=tk.BOTH , expand=True)
Taxilbl.place(x=20,y=250)
Taxilbl2.place(x=400,y=280)
Taxilbl3.place(x=400,y=310)
Taxilbl4.place(x=400,y=340)

vehicle3= Ship()
show3 = vehicle3.showVehicle()

img3 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/transportation/ship.jpg"))
Shiplbl = tk.Label(master = frm2 , image=img3 )

Shiplbl2 = tk.Label(master=frm2 ,text=show3[0] , bg = "#DDA0DD", font=32)
Shiplbl3 = tk.Label(master=frm2 ,text=show3[1] , bg = "#DDA0DD", font=32)
Shiplbl4 = tk.Label(master=frm2 ,text=show3[2] , bg = "#DDA0DD", font=32)

frm2.pack(fill=tk.BOTH , expand=True)
Shiplbl.place(x=20,y=550)
Shiplbl2.place(x=400,y=580)
Shiplbl3.place(x=400,y=610)
Shiplbl4.place(x=400,y=640)

vehicle4= Bus()
show4 = vehicle4.showVehicle()

img4 = ImageTk.PhotoImage(Image.open("C:/Users/Matin/Desktop/transportation/bus.jpg"))
Buslbl = tk.Label(master = frm2 , image=img4 )

Buslbl2 = tk.Label(master=frm2 ,text=show4[0] , bg = "#DDA0DD", font=32)
Buslbl3 = tk.Label(master=frm2 ,text=show4[1] , bg = "#DDA0DD", font=32)
Buslbl4 = tk.Label(master=frm2 ,text=show4[2] , bg = "#DDA0DD", font=32)

frm2.pack(fill=tk.BOTH , expand=True)
Buslbl.place(x=20,y=850)
Buslbl2.place(x=400,y=880)
Buslbl3.place(x=400,y=910)
Buslbl4.place(x=400,y=940)


#keep window open
window.mainloop()