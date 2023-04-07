from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox



class roombooking:
    def __init__(self,root) :
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1290x500+190+190")
        
              #   ===================variablles
        

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtax=StringVar()
        self.var_total=StringVar()
         
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Time New Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=50)
        # =========================================
        
                
        img2=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\logo.jpg")
        img2=img2.resize((140,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lb1img=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lb1img.place(x=0,y=0,width=140,height=100)
        
         # ==========================labelfram
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking Details",font=("Time New Roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=330,height=500)
        
        # =====1customercontact
        lbl_cust_contact=Label(labelframeleft,text="Customer_Connect",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=15,font=("Time New Roman",10,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        
        # ===================featchdatabtn
        btnfetchdata=Button(labelframeleft,command=self.fetch_contact,text="fetch data",bg="black",fg="gold",font=("arial",8,"bold"),width=7)
        btnfetchdata.place(x=243,y=4)
         
          # ===================2check in date
        lbl_cust_checkindate=Label(labelframeleft,text="Check in date",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_cust_checkindate.grid(row=1,column=0,sticky=W)
        
        txt_checkindate=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=22,font=("Time New Roman",10,"bold"))
        txt_checkindate.grid(row=1,column=1)
        # ===================check out date
        lbl_cust_checkoutdate=Label(labelframeleft,text="Check out date",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_cust_checkoutdate.grid(row=2,column=0,sticky=W)
        
        txtcheckoutdate=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=22,font=("Time New Roman",10,"bold"))
        txtcheckoutdate.grid(row=2,column=1)
        # =====================room type
        label_roomtype=Label(labelframeleft,text="Room Type",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)
        
        
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from details")
        row=my_cursor.fetchall()
        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("Time New Roman",10,"bold"),width=20,state="readonly")
        # combo_gender.current(0)
        combo_roomtype["values"]=row
        combo_roomtype.grid(row=3,column=1)
        
        
        # ========================avaiableroom
        lbl_avaiableroom=Label(labelframeleft,text="Available Room",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_avaiableroom.grid(row=4,column=0,sticky=W)
        
        
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()
        
        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("Time New Roman",10,"bold"),width=20,state="readonly")
        # combo_gender.current(0)
        combo_roomno["values"]=rows
        combo_roomno.grid(row=4,column=1)
        # txtavaiableroom=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=22,font=("Time New Roman",10,"bold"))
        # txtavaiableroom.grid(row=4,column=1)
        
          # ========================meal
        lbl_meal=Label(labelframeleft,text="Meal",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)
        
        txtmeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=22,font=("Time New Roman",10,"bold"))
        txtmeal.grid(row=5,column=1)
        
           # ========================no of days
        lbl_noofdays=Label(labelframeleft,text="NO of Days",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_noofdays.grid(row=6,column=0,sticky=W)
        
        txtnoofdays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=22,font=("Time New Roman",10,"bold"))
        txtnoofdays.grid(row=6,column=1)

        # ========================paidtax
        lbl_paidtax=Label(labelframeleft,text="Paid Tax",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_paidtax.grid(row=7,column=0,sticky=W)
        
        txtpaidtax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=22,font=("Time New Roman",10,"bold"))
        txtpaidtax.grid(row=7,column=1)

        # ========================sub tax
        lbl_sabtax=Label(labelframeleft,text="Sab Tax",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_sabtax.grid(row=8,column=0,sticky=W)
        
        txtsabtax=ttk.Entry(labelframeleft,textvariable=self.var_actualtax,width=22,font=("Time New Roman",10,"bold"))
        txtsabtax.grid(row=8,column=1)
        
                # ========================total cost
        lbl_totalcost=Label(labelframeleft,text="Tota; Cost",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_totalcost.grid(row=9,column=0,sticky=W)
        
        txttotalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=22,font=("Time New Roman",10,"bold"))
        txttotalcost.grid(row=9,column=1)
        # ===================billbutton
        btnbill=Button(labelframeleft,text="Bill",command=self.total,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)
        
         
          #   ==========================button
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=320,height=40)    
        
        
        # btnadd=Button(btn_frame,text="Add",font=("Time New Roman",10,"bold"),bd="black",fg="gold",width=4)
        # btnadd.grid(row=0,column=0,padx=1)  
        btnadd=Button(btn_frame,text="Add",command=self.add_data,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnadd.grid(row=0,column=0)
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnupdate.grid(row=0,column=2)
        
        btndelete=Button(btn_frame,text="Delete",command=self.mdelete,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btndelete.grid(row=0,column=3)
        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnreset.grid(row=0,column=4)
        
        # ===================setimagerightside
        
        img3=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\room.jpg")
        img3=img3.resize((330,230),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lb1img=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lb1img.place(x=900,y=55,width=330,height=230)
        
        
         #   =====================tabelframe
        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("Time New Roman",12,"bold"),padx=2)
        tabelframe.place(x=435,y=280,width=800,height=260)
        
        lblsearchby=Label(tabelframe,text="Search By :",font=("Time New Roman",10,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)
        self.serch_var=StringVar()
        
        combosearchby=ttk.Combobox(tabelframe,font=("Time New Roman",10,"bold"),width=20)
        # combo_gender.current(0)
        combosearchby["values"]=("contact","roomavailable")
        combosearchby.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtsearchby=ttk.Entry(tabelframe,width=22,font=("Time New Roman",10,"bold"))
        txtsearchby.grid(row=0,column=2,padx=2)
        
        btnsearch=Button(tabelframe,text="Search",command=self.search,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnsearch.grid(row=0,column=3,padx=2)
        
        btnshow=Button(tabelframe,text="Show All",command=self.fetch_data,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnshow.grid(row=0,column=4,padx=2)
        
        
        
        #   ==========================showdatatabel
        detailstabel=Frame(tabelframe,bd=2,relief=RIDGE)
        detailstabel.place(x=0,y=50,width=700,height=180)    
        scroll_x=ttk.Scrollbar(detailstabel,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailstabel,orient=VERTICAL)
        
        self.rooom_table=ttk.Treeview(detailstabel,column=("contact","checkindate","checkoutdate","roomtype","roomavailable","meal","noofdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.rooom_table.xview)
        scroll_y.config(command=self.rooom_table.yview)
        
        self.rooom_table.heading("contact",text="Contact")
        self.rooom_table.heading("checkindate",text="Check-in-date")
        self.rooom_table.heading("checkoutdate",text="Check=out-date")
        self.rooom_table.heading("roomtype",text="Room-type")
        self.rooom_table.heading("roomavailable",text="Roomavailable")
        self.rooom_table.heading("meal",text="Meal")
        self.rooom_table.heading("noofdays",text="No of Days")
        
        
        self.rooom_table["show"]="headings"
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
        self.rooom_table.pack(fill=BOTH,expand=1)
        self.rooom_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
                    
        # ==========fetchdata
    def  fetch_data(self):
          conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from room")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
             self.rooom_table.delete(*self.rooom_table.get_children())
             for i in rows:
                 self.rooom_table.insert("",END,values=i)
             conn.commit()
             conn.close()        
        
        
    def add_data(self): 
      if self.var_contact.get()=="" or self.var_checkin.get()=="":
          messagebox.showerror("Error","sorry something want wrong",parent=self.root)
      else:
         try:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
            self.var_contact.get(),
            self.var_checkin.get(),
            self.var_checkout.get(),
            self.var_roomtype.get(),
            self.var_roomavailable.get(),
            self.var_meal.get(),
            self.var_noofdays.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","room booked....!",parent=self.root)
         except Exception as es:
            messagebox.showwarning("warning",f"syntax error :{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.rooom_table.focus()
        content=self.rooom_table.item(cursor_row)
        row=content["values"]
       
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
        
    def update(self):
       if self.var_contact.get()=="":
          mesagebox.showerror("Error","please enter contact number",parent=self.root)
       else:
         conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("update room set checkindate=%s,checkoutdate=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get(),self.var_contact.get()))
      
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("update","room detail has been update",parent=self.root)
    
    
    def mdelete(self):
         mdelete=messagebox.askyesno("Hostel management system ","do you want to delete it",parent=self.root)
         if mdelete>0:
             conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
             my_cursor=conn.cursor() 
             query="delete from room where contact=%s"
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
         else:
            if not mdelete:
               return
         conn.commit()
         self.fetch_data()
         conn.close()
    def reset(self):            
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtax.set(""),
        self.var_total.set("")
   
        
        
    def  fetch_contact(self):
         if self.var_contact.get()=="":
             messagebox.showerror("Error","plz enter contact number",parent=self.root)
         else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","this number is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=455,y=55,width=340,height=180)
                lblname=Label(showdataframe,text="name",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)
                
                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)     
                
                
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()      
               
                lblgender=Label(showdataframe,text="gender",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)
                
                lbl2=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)  
                
                # =================email
                                
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()      
               
                lblemail=Label(showdataframe,text="email",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)
                
                lbl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)   
                
                # ====================nationality
                                
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()      
               
                lblnationality=Label(showdataframe,text="nationality",font=("arial",12,"bold"))
                lblnationality.place(x=0,y=90)
                
                lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)
                
                # ====================address
                                
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
                my_cursor=conn.cursor()
                query=("select address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()      
               
                lbladdress=Label(showdataframe,text="address",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)
                
                lbl5=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)               
                
    #  serachsystem
    def search(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor() 
            my_cursor.execute("select * from room where "+str(self.serch_var.get())+
            " LIKE'%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
               self.rooom_table.delete(*self.room_table.get_children())
               for i in rows:
                  self.rooom_table.insert("",END,values=i)
               conn.commit()
               conn.close()
           
                
    def total(self):
      inDate=self.var_checkin.get()       
      outDate=self.var_checkout.get()
      inDate=datetime.strptime(inDate,"%d/%m/%Y")       
      outDate=datetime.strptime(outDate,"%d/%m/%Y")       
      self.var_noofdays.set(abs(outDate-inDate).days)
      
      if(self.var_meal.get()=="dinner" and self.var_roomtype.get()=="laxary"):
        q1=float(300)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(Tax)
        self.var_actualtax.set(ST)
        self.var_total.set(TT)
      elif(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="single"):
        q1=float(300)
        q2=float(500)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(Tax)
        self.var_actualtax.set(ST)
        self.var_total.set(TT)
      elif(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="double"):
        q1=float(300)
        q2=float(600)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(Tax)
        self.var_actualtax.set(ST)
        self.var_total.set(TT)
          
        
      
if __name__ == "__main__":
    root=Tk()
    obj=roombooking(root)
    root.mainloop()