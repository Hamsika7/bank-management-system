#GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from time import gmtime,strftime
from tkinter import Toplevel

#Sign in-->name is valid or not
def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

#HOME
def home_return(master):
	master.destroy()
	Main_Menu()

#This fn is used in check_log_in fn
def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return
    
#After entering login details --> check if the file for a particular account is there or not
def check_log_in(master,name,ac_no,pin):
	if(check_acc_nmb(ac_no)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(ac_no,name)
    
#Sign in-->process
def write (master,name,pin,oc):
    if((is_number(name))or (is_number(oc)==0) or (is_number(pin)==0)or name=="" ):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1=open("ACCOUNT_RECORD.txt",'r')
    ac_no=int(f1.readline())
    ac_no+=1
    f1.close()

    f1=open("ACCOUNT_RECORD.txt",'w')
    f1.write(str(ac_no))
    f1.close()

    fdetail=open(str(ac_no)+".txt",'w')
    fdetail.write(pin+"\n")
    fdetail.write(oc+"\n")
    fdetail.write(str(ac_no)+"\n")
    fdetail.write(name+"\n")
    fdetail.close()

    frec=open(str(ac_no)+"-rec.txt",'w')
    frec.write("\tDATE\t\t|\t\tCREDIT\t\t|\t\tDEBIT\t\t|\t\tBALANCE\n")
    frec.write("_________________________________________________________________________________________________________________________________________\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S] |\t\t",gmtime()))+oc+"\t\t|\t\t\t\t|\t\t"+oc+"\n")
    frec.close()

    messagebox.showinfo("Details","Your Acccount Number is:"+str(ac_no))
    master.destroy()
    return
#CREDIT WRITE FN
def crdt_write(master,amt,ac_no,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(ac_no+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(ac_no+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(ac_no+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(ac_no)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S] |\t\t",gmtime()))+str(amti)+"\t\t|\t\t\t\t|\t\t"+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

#DEBIT WRITE FN
def debit_write(master,amt,ac_no,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(ac_no+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(ac_no+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(ac_no+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(ac_no)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S] |\t\t",gmtime()))+"\t\t|\t\t"+str(amti)+"\t\t|\t\t"+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return

#LOGOUT FN
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

#CREDIT AMOUNT
def Cr_Amt(ac_no,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x300")
	creditwn.title("Credit Amount")
	creditwn.configure(bg="#DD6892")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="Summit Capital Bank",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Times New Roman","20","bold"))
	l_title.pack(side="top")
	l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be credited: ",fg="white",bg="#DD6892")
	l1.config(font=("Times New Roman","15","bold"))
	e1=tk.Entry(creditwn,relief="raised")
	e1.config(font=("Times New Roman","15"))
	l1.place(x=50,y=50)
	e1.place(x=350,y=50)
	b=tk.Button(creditwn,text="Credit",font=("Times New Roman","15","bold"),relief="raised",command=lambda:crdt_write(creditwn,e1.get(),ac_no,name))
	b.place(x=290,y=100)
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),ac_no,name))

#DEBIT AMOUNT
def De_Amt(ac_no,name):
    debitwn=tk.Tk()
    debitwn.geometry("600x300")
    debitwn.title("Debit Amount")	
    debitwn.configure(bg="#35C191")

    fr1=tk.Frame(debitwn,bg="blue")
	
    l_title=tk.Message(debitwn,text="Summit Capital Bank",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Times New Roman","20","bold"))
    l_title.pack(side="top")
	
    l1=tk.Label(debitwn,relief="raised",text="Enter Amount to be debited: ",fg="white",bg="#35C191")
    l1.config(font=("Times New Roman","15","bold"))

    e1=tk.Entry(debitwn,relief="raised")
    e1.config(font=("Times New Roman","15"))
        
    l1.place(x=50,y=50)
    #l1.pack(side="top")
    e1.place(x=350,y=50)
    #e1.pack(side="top")
	
    b=tk.Button(debitwn,text="Debit",font=("Times New Roman","15","bold"),relief="raised",command=lambda:debit_write(debitwn,e1.get(),ac_no,name))
    b.place(x=290,y=100)
    #b.pack(side="top")
	
    debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),ac_no,name))
	
#DISPLAY BALANCE 

def disp_bal(ac_no):
	fdet=open(ac_no+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)

#TRANSACTION HISTROY

def disp_tr_hist(ac_no):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x700")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="#B190CC")
	
	fr1=tk.Frame(disp_wn,bg="blue")
	
	l_title=tk.Message(disp_wn,text="Summit Capital Bank",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Times New Roman","20","bold"))
	l_title.pack(side="top")
	
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="#503468",fg="white",relief="raised")
	l1.pack(side="top")
	
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	
	frec=open(ac_no+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
		
	b=tk.Button(disp_wn,text="Quit",font=("Times New Roman","20"),relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

#LOGIN-->MENU
def logged_in_menu(ac_no,name):
    y1=Tk()
    y1.geometry("620x620")
    y1.title("Show Page")
    y1.configure(background="#2594E7")
    
    l1=Label(y1,text="***USER DETAILS***",font=("Times New Roman",20),fg="white",bg="#2594E7")
    l1.place(x=200,y=50)
    #CREDIT IMG
    c1=PhotoImage(file="images/CREDIT.gif")
    c2=c1.subsample(2,2)
    cb1=Button(y1,image=c2,command=lambda: Cr_Amt(ac_no,name))
    cb1.image=c2
    cb1.place(x=150,y=300)
    #DEBIT IMG
    d1=PhotoImage(file="images/DEBIT.gif")
    d2=d1.subsample(2,2)
    db1=Button(y1,image=d2,command=lambda: De_Amt(ac_no,name))
    db1.image=d2
    db1.place(x=350,y=300)
    #TRANSACTION_IMG
    t1=PhotoImage(file="images/TRAN_HIS.gif")
    t2=t1.subsample(2,2)
    tb1=Button(y1,image=t2,command=lambda: disp_tr_hist(ac_no))
    tb1.image=t2
    tb1.place(x=150,y=350)
    #BALANCE_IMG
    ba1=PhotoImage(file="images/BALANCE.gif")
    ba2=ba1.subsample(2,2)
    b1=Button(y1,image=ba2,command=lambda: disp_bal(ac_no))
    b1.image=ba2
    b1.place(x=350,y=350)
    #LOGOUT_IMG
    lo1=PhotoImage(file="images/logout.gif")
    lo2=lo1.subsample(2,2)
    lob1=Button(y1,image=lo2,command=lambda: logout(y1))
    lob1.image=lo2
    lob1.place(x=250,y=420)
    

#LOGIN_FN
def Login(master):
    master.destroy()
    y=Tk()
    y.geometry("620x620")
    y.title("Login Page")
    y.configure(background="#2594E7")
    
    l1=Label(y,text="***USER DETAILS***",font=("Times New Roman",20),fg="white",bg="#2594E7")
    l1.place(x=200,y=50)
    l1=Label(y,text="USER NAME",font=("Times New Roman",20),fg="white",bg="#2594E7")
    l1.place(x=50,y=120)
    e1=Entry(y,font=("Times New Roman",20))
    e1.place(x=310,y=120)
    l1=Label(y,text="ACCOUNT NUMBER",font=("Times New Roman",20),fg="white",bg="#2594E7")
    l1.place(x=50,y=180)
    e2=Entry(y,font=("Times New Roman",20))
    e2.place(x=310,y=180)
    l1=Label(y,text="PIN NUMBER",font=("Times New Roman",20),fg="white",bg="#2594E7")
    l1.place(x=50,y=240)
    e3=Entry(y,font=("Times New Roman",20),show="*")
    e3.place(x=310,y=240)
    b1=Button(y,text="Submit",font=("Times New Roman",20),command=lambda: check_log_in(y,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b1.place(x=200,y=500)
    
    b2=Button(y,text="Home",font=("Times New Roman",20),relief="raised",command=lambda: home_return(y))
    b2.place(x=310,y=500)
    y.bind("<Return>",lambda b:check_log_in(y,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    
    

#SIGNIN_FN
def Signup():
    z=Tk()
    z.geometry("620x620")
    z.title("Sign Up Page")
    z.configure(background="#2594E7")

    lb1=Label(z,text="***CREATE NEW ACCOUNT***",font=("Times New Roman",20),fg="white",bg="#2594E7")
    lb1.place(x=110,y=50)
    lb1=Label(z,text="NAME",font=("Times New Roman",20),fg="white",bg="#2594E7")
    lb1.place(x=50,y=120)
    en1=Entry(z,font=("Times New Roman",20))
    en1.place(x=310,y=120)
    lb1=Label(z,text="CREATE PIN",font=("Times New Roman",20),fg="white",bg="#2594E7")
    lb1.place(x=50,y=180)
    en2=Entry(z,font=("Times New Roman",20))
    en2.place(x=310,y=180)
    lb1=Label(z,text="OPENING CREDIT",font=("Times New Roman",20),fg="white",bg="#2594E7")
    lb1.place(x=50,y=240)
    en3=Entry(z,font=("Times New Roman",20))
    en3.place(x=310,y=240)
    bu1=Button(z,text="Submit",font=("Times New Roman",20),command=lambda:write(z,en1.get().strip(),en2.get().strip(),en3.get().strip()))
    bu1.place(x=275,y=500)
    z.bind("<Return>",lambda a:write(z,en1.get().strip(),en2.get().strip(),en3.get().strip()))
    return


#MY PROJECT-->MAIN PAGE
def Main_Menu():
    x=tk.Tk()
    x.title("My Project")
    x.geometry("1680x1050")
    x.configure(background="black")

    """im=ImageTk.PhotoImage(Image.open("bg.jpg"))
    lb2=Label(x,image=im,height="300",width="300")
    lb2.place(x=200,y=300)"""

    bg_img=Image.open('images/bg_1.jpg')
    bg_img2=bg_img.resize((1680,1050))
    bg_img3=ImageTk.PhotoImage(bg_img2)
    
    f1=Frame(x,height="1050",width="1680")
    f1.pack(side="top")
    
    lb2=tk.Label(f1,image=bg_img3)
    lb2.place(x=0,y=0)

    lb1=tk.Label(x,text="***WELCOME TO MAIN MENU***",bg="#005DA9",fg="white",font=("Times New Roman",25))
    #lb.pack() to place in top centre
    lb1.place(x=425,y=130)
    
    lb3=tk.Label(x,text="SUMMIT CAPITAL BANK",bg="#2594E7",fg="white",font=("Times New Roman",23))
    lb3.place(x=500,y=50)
    
    #LOGIN_IMG
    login_img=Image.open("images/login.jpg")
    login_img2=login_img.resize((90,60))
    login_img3=ImageTk.PhotoImage(login_img2)
    
    #SIGN IN_IMG
    sign_img=Image.open("images/Sign.jpg")
    sign_img2=sign_img.resize((90,60))
    sign_img3=ImageTk.PhotoImage(sign_img2)

    b1=tk.Button(x,image=login_img3,command=lambda:Login(x))
    b1.place(x=1220, y=400)

    b2=tk.Button(x,image=sign_img3,command=Signup)
    b2.place(x=220, y=400)

    # #QUIT_IMG
    # quit_img=Image.open("Quit.jpg")
    # quit_img2=quit_img.resize((90,60))
    # quit_img3=ImageTk.PhotoImage(quit_img)

    #QUIT_IMG
    quit_img=Image.open("images/Quit.jpg")
    quit_img2=quit_img.resize((90,60))
    quit_img3=ImageTk.PhotoImage(quit_img)

    b3=tk.Button(x,image=quit_img3,command=x.destroy)
    b3.place(x=650, y=600)
    
    x.mainloop()

Main_Menu()
   


    

