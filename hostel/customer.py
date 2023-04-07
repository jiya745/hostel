from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class customerwindow:
    def __init__(self,root) :
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1290x500+190+190")
      #   ===================variablles
        
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()
      
        
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Time New Roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=50)
        # =========================================
        
                
        img2=Image.open( "C:\\Users\\bhutta\\Desktop\\hostel\\images\\logo.jpg")
        img2=img2.resize((140,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lb1img=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lb1img.place(x=0,y=0,width=140,height=100)
        # ==========================labelfram
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("Time New Roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=330,height=500)
        # =====================labelsandentires
        # =====1customerref
        lbl_cust_ref=Label(labelframeleft,text="Customer_ref",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=22,state="readonly",font=("Time New Roman",10,"bold"))
        entry_ref.grid(row=0,column=1)
        # ===================2customername
        lbl_cust_name=Label(labelframeleft,text="Customer_Name",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_name,width=22,font=("Time New Roman",10,"bold"))
        txtcname.grid(row=1,column=1)
        # ===================mothername
        lbl_cust_mother_name=Label(labelframeleft,text="Mother_Name",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_cust_mother_name.grid(row=2,column=0,sticky=W)
        
        txtcmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=22,font=("Time New Roman",10,"bold"))
        txtcmname.grid(row=2,column=1)
        # =====================genderconobox
        label_gender=Label(labelframeleft,text="Gender",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("Time New Roman",10,"bold"),width=20,state="readonly")
        # combo_gender.current(0)
        combo_gender["values"]=("male","female","other")
        combo_gender.grid(row=3,column=1)
        
        
        # ========================postcode
        lbl_postcode=Label(labelframeleft,text="Post_Code",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_postcode.grid(row=4,column=0,sticky=W)
        
        txtpost=ttk.Entry(labelframeleft,textvariable=self.var_post,width=22,font=("Time New Roman",10,"bold"))
        txtpost.grid(row=4,column=1)
        
          # ========================mobileno
        lbl_mobileno=Label(labelframeleft,text="Mobile_No",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_mobileno.grid(row=5,column=0,sticky=W)
        
        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=22,font=("Time New Roman",10,"bold"))
        txtmobile.grid(row=5,column=1)
           # ========================email
        lbl_email=Label(labelframeleft,text="Email",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_email.grid(row=6,column=0,sticky=W)
        
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=22,font=("Time New Roman",10,"bold"))
        txtemail.grid(row=6,column=1)
        
           # ========================nationality
        lbl_nationality=Label(labelframeleft,text="Nationality",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("Time New Roman",10,"bold"),width=20)
        # combo_gender.current(0)
        combo_nationality["values"]=("pakistan","india","turkey","american","bangladesh","japan")
        combo_nationality.grid(row=7,column=1)
           # ========================idproof
        lbl_idproof=Label(labelframeleft,text="Id Proof Type",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_idproof.grid(row=8,column=0,sticky=W)
        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("Time New Roman",10,"bold"),width=20)
        # combo_gender.current(0)
        combo_idproof["values"]=("cnic","driveing licences","passport")
        combo_idproof.grid(row=8,column=1)
        
           # ========================phone
        lbl_idnumber=Label(labelframeleft,text="Id number",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_idnumber.grid(row=9,column=0,sticky=W)
        
        txtidnumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=22,font=("Time New Roman",10,"bold"))
        txtidnumber.grid(row=9,column=1)
           # ========================address
        lbl_address=Label(labelframeleft,text="Address",font=("Time New Roman",10,"bold"),padx=2,pady=6)
        lbl_address.grid(row=10,column=0,sticky=W)
        
        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=22,font=("Time New Roman",10,"bold"))
        txtaddress.grid(row=10,column=1)
        
        
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
        
      #   =====================tabelframe
        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("Time New Roman",12,"bold"),padx=2)
        tabelframe.place(x=435,y=50,width=800,height=500)
        
        lblsearchby=Label(tabelframe,text="Search By :",font=("Time New Roman",10,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)
        self.serch_var=StringVar()
        
        combosearchby=ttk.Combobox(tabelframe,textvariable=self.serch_var,font=("Time New Roman",10,"bold"),width=20)
        # combo_gender.current(0)
        combosearchby["values"]=("mobile","ref")
        combosearchby.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtsearchby=ttk.Entry(tabelframe,textvariable=self.txt_search,width=22,font=("Time New Roman",10,"bold"))
        txtsearchby.grid(row=0,column=2,padx=2)
        
        btnsearch=Button(tabelframe,text="Search",command=self.search,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnsearch.grid(row=0,column=3,padx=2)
        
        btnshow=Button(tabelframe,text="Show All",command=self.fetch_data,bg="black",fg="gold",font=("arial",12,"bold"),width=7)
        btnshow.grid(row=0,column=4,padx=2)
      #   ==========================showdatatabel
        detailstabel=Frame(tabelframe,bd=2,relief=RIDGE)
        detailstabel.place(x=0,y=50,width=700,height=400)    
        scroll_x=ttk.Scrollbar(detailstabel,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailstabel,orient=VERTICAL)
        
        self.custdetailwin=ttk.Treeview(detailstabel,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.custdetailwin.xview)
        scroll_y.config(command=self.custdetailwin.yview)
        
        self.custdetailwin.heading("ref",text="Refer No")
        self.custdetailwin.heading("name",text="Name")
        self.custdetailwin.heading("mother",text="Mother Name")
        self.custdetailwin.heading("gender",text="Gender")
        self.custdetailwin.heading("post",text="Post Code")
        self.custdetailwin.heading("mobile",text="Mobile No")
        self.custdetailwin.heading("email",text="Email")
        self.custdetailwin.heading("nationality",text="nationality")
        self.custdetailwin.heading("idproof",text="ID Proof")
        self.custdetailwin.heading("idnumber",text="ID Number")
        self.custdetailwin.heading("address",text="Address")
        
        
        self.custdetailwin["show"]="headings"
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
        self.custdetailwin.pack(fill=BOTH,expand=1)
        self.custdetailwin.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self): 
      if self.var_mobile.get()=="" or self.var_mother.get()=="":
          messagebox.showerror("Error","sorry something want wrong",parent=self.root)
      else:
         try:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","customer has been added",parent=self.root)
         except Exception as es:
            messagebox.showwarning("warning",f"syntax error :{str(es)}",parent=self.root)
            
    def  fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
           self.custdetailwin.delete(*self.custdetailwin.get_children())
           for i in rows:
              self.custdetailwin.insert("",END,values=i)
        conn.commit()
        conn.close()
    def get_cursor(self,event=""):
       cursor_row=self.custdetailwin.focus()
       content=self.custdetailwin.item(cursor_row)
       row=content["values"]
       
       self.var_ref.set(row[0]),
       self.var_name.set(row[1]),
       self.var_mother.set(row[2]),
       self.var_gender.set(row[3]),
       self.var_post.set(row[4]),
       self.var_mobile.set(row[5]),
       self.var_email.set(row[6]),
       self.var_nationality.set(row[7]),
       self.var_idproof.set(row[8]),
       self.var_idnumber.set(row[9]),
       self.var_address.set(row[10])
       
       
    def update(self):
       if self.var_mobile.get()=="":
          mesagebox.showerror("Error","please enter mobile number",parent=self.root)
       else:
          
         conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get(),self.var_ref.get()))
         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("update","customer detail has been update",parent=self.root)
       
    def mdelete(self):
         mdelete=messagebox.askyesno("Hostel management system ","do you want to delete it",parent=self.root)
         if mdelete>0:
             conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
             my_cursor=conn.cursor() 
             query="delete from customer where ref=%s"
             value=(self.var_ref.get(),)
             my_cursor.execute(query,value)
         else:
            if not mdelete:
               return
         conn.commit()
         self.fetch_data()
         conn.close()
    def reset(self):
         # self.var_ref.set(""),
         self.var_name.set(""),
         self.var_mother.set(""),
         # self.var_gender.set(""),
         self.var_post.set(""),
         self.var_mobile.set(""),
         self.var_email.set(""),
         # self.var_nationality.set(""),
         # self.var_idproof.set(""),
         self.var_idnumber.set(""),
         self.var_address.set("")   
         x=random.randint(1000,9999)
         self.var_ref.set(str(x))
    def search(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor() 
            my_cursor.execute("select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
               self.custdetailwin.delete(*self.custdetailwin.get_children())
               for i in rows:
                  self.custdetailwin.insert("",END,values=i)
               conn.commit()
               conn.close()
         
if __name__ == "__main__":
    root=Tk()
    obj=customerwindow(root)
    root.mainloop()
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        