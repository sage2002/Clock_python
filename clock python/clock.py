from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from datetime import*
import time
from math import*
class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#DEA057")
        
        title=Label(self.root,text="Analog Clock",font=("times new roman",50,"bold"),bg="#F9EBC8").place(x=0,y=50,relwidth=1)
        
        self.lbl=Label(self.root,bg="chocolate",bd=20,relief=RAISED)
        self.lbl.place(x=450,y=150,height=400,width=400)
        # self.clock_image()
        self.working()
        
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        #=====For Clock Image
        bg=Image.open("clock.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        clock.save("clock_new.png")
        # Formula To Rotate the Clock
        # angle_in_radius = angle_in_degrees * math.pi / 180
        # line_length = 100
        # center_x = 250
        # center_y=250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)
        
 
        #=====Hour Line Image=====
        #         x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
         #=====Min Line Image=====
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="maroon",width=3)
         #=====Sec Line Image=====
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="red",width=2)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")
    
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second   
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(h,m,s)
        # print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
root=Tk()
obj=Clock(root)
root.mainloop()
        