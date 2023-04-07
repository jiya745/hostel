from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox



class detailsroom:
    def __init__(self,root) :
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1290x500+190+190")
        
        lbl_title=Label(self.root,text="DETAILS OF ROOMS",font=("Time New Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=50)
        # =========================================
        
                
        img2=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\logo.jpg")
        img2=img2.resize((140,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lb1img=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lb1img.place(x=0,y=0,width=140,height=100)
        
         # ==========================labelfram
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("Time New Roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)
            
        # =====1floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=22,font=("Time New Roman",10,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #====================room no
        lbl_roomno=Label(labelframeleft,text="Room NO",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)
        self.var_roomno=StringVar()
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=22,font=("Time New Roman",10,"bold"))
        entry_roomno.grid(row=1,column=1,sticky=W)
        
        # =====room type
        lbl_roomtype=Label(labelframeleft,text="Room Type",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)
        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=22,font=("Time New Roman",10,"bold"))
        entry_roomtype.grid(row=2,column=1,sticky=W)
        
        
        
           #   ==========================button
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=450,height=40)    
        
        
        # btnadd=Button(btn_frame,text="Add",font=("Time New Roman",10,"bold"),bd="black",fg="gold",width=4)
        # btnadd.grid(row=0,column=0,padx=1)  
        btnadd=Button(btn_frame,text="Add",command=self.add_data,bg="black",fg="gold",font=("arial",12,"bold"),width=9)
        btnadd.grid(row=0,column=0)
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,bg="black",fg="gold",font=("arial",12,"bold"),width=9)
        btnupdate.grid(row=0,column=2)
        
        btndelete=Button(btn_frame,text="Delete",command=self.mdelete,bg="black",fg="gold",font=("arial",12,"bold"),width=9)
        btndelete.grid(row=0,column=3)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,bg="black",fg="gold",font=("arial",12,"bold"),width=9)
        btnreset.grid(row=0,column=4)
        
         #   =====================tabelframe
        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("Time New Roman",12,"bold"),padx=2)
        tabelframe.place(x=600,y=55,width=600,height=360)
        
        
        
        scroll_x=ttk.Scrollbar(tabelframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabelframe,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(tabelframe,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room NO")
        self.room_table.heading("roomtype",text="Room Type")

        
        self.room_table["show"]="headings"
      #   self.custdetailwin.heading("ref",width=100)
      #   self.custdetailwin.column("name",width=100)
      #   self.custdetailwin.column("mother",width=100)
      #   self.custdetailwin.column("gender",width=100)
      #   self.custdetailwin.column("post",width=100)
      #   self.custdetailwin.column("mobile",width=100)
      #   self.custdetailwin.column("email",width=100)
      #   self.custdetailwin.column("nationality",width=100)
      #   self.custdetailwin.column("idproof",width=100)
      #   self.custdetailwin.column("idnumber",width=100)
      #   self.custdetailwin.column("address",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
        
    def add_data(self): 
      if self.var_floor.get()=="" or self.var_roomtype.get()=="":
          messagebox.showerror("Error","sorry something want wrong",parent=self.root)
      else:
         try:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),
                                                                      self.var_roomno.get(),
                                                                      self.var_roomtype.get()
                                                                      ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","details added....!",parent=self.root)
         except Exception as es:
            messagebox.showwarning("warning",f"syntax error :{str(es)}",parent=self.root)
            # ==========fetchdata
    def  fetch_data(self):
          conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from details")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                 self.room_table.insert("",END,values=i)
             conn.commit()
             conn.close()        
    
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
       
        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])
    
    
    def update(self):
       if self.var_floor.get()=="":
          mesagebox.showerror("Error","please enter floor number",parent=self.root)
       else:
         conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("update details set floor=%s,roomtype=%s where roomno=%s",
                         (self.var_floor.get(),
                          self.var_roomtype.get(),
                          self.var_roomno.get()
                          ))
         
         
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("update","room detail has been update",parent=self.root)
    
    def mdelete(self):
         mdelete=messagebox.askyesno("Hostel management system ","do you want to delete it",parent=self.root)
         if mdelete>0:
             conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
             my_cursor=conn.cursor() 
             query="delete from details where roomno=%s"
             value=(self.var_roomno.get(),)
             my_cursor.execute(query,value)
         else:
            if not mdelete:
               return
         conn.commit()
         self.fetch_data()
         conn.close()
     
                    
    def reset(self): 
         self.var_floor.set(""),
         self.var_roomtype.set(""),
         self.var_roomno.set("")
if __name__ == "__main__":
    root=Tk()
    obj=detailsroom(root)
    root.mainloop()