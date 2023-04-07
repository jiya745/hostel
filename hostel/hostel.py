from tkinter import*
from PIL import Image,ImageTk
from customer import customerwindow
from room import roombooking
from details import detailsroom



class hostelmanagenemtsystem:
    def __init__(self,root) :
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1450x700+0+0")
        
        
        
        img1=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\sidedown.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lb1img=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lb1img.place(x=0,y=0,width=1550,height=140)
        
        # ======================================
        
        img2=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lb1img=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lb1img.place(x=0,y=0,width=230,height=140)
        
        # =========================================
        
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Time New Roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        # =========================================
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        # ===========================================
        lbl_menu=Label(main_frame,text="Menu",font=("Time New Roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        # ===================================================
        btn_frame=Frame(self.root,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=235,width=230,height=190)
    #    1======================================== 
        cust_btn=Button(btn_frame,text="Customer",command=self.customer_detail,width=20,font=("Time New Roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        # 2=================================
        room_btn=Button(btn_frame,text="Room",command=self.Roombooking,width=20,font=("Time New Roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        # 3========================
        detail_btn=Button(btn_frame,text="Details",command=self.detailsroom,width=20,font=("Time New Roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        detail_btn.grid(row=2,column=0,pady=1)
        # =4============================
        report_btn=Button(btn_frame,text="Report",width=20,font=("Time New Roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        # 5==================================
        logout_btn=Button(btn_frame,text="Log Out",width=20,font=("Time New Roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        
        # image==================================
        img3=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\main.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lb1img1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lb1img1.place(x=225,y=0,width=1310,height=590)
        
        # ==================================
        img4=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\sideup.jpg")
        img4=img4.resize((200,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lb1img2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lb1img2.place(x=0,y=210,width=230,height=180)
        # =================================
        img5=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\sidedown.jpg")
        img5=img5.resize((200,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lb1img1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lb1img1.place(x=0,y=380,width=230,height=180)
        
        
    def customer_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=customerwindow(self.new_window)
        
    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)
        
        
    def detailsroom(self):
        self.new_window=Toplevel(self.root)
        self.app=detailsroom(self.new_window)
            
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=hostelmanagenemtsystem(root)
    root.mainloop()