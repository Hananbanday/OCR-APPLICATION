from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import transformers
from transformers import pipeline
import  PIL
from PIL import Image ,ImageTk
import cv2
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe"

DATA = []



def showImage():
    global img_input
    img = Tk()
    img.config(bg="red")
    img.geometry("400x400")
    img_lable = Label(img,text="IMAGE NAME",bg = "black",fg="white",padx =10,pady =10)
    img_lable.pack()
    
    img_input = Entry(img,width=50)
    img_input.pack(ipady=6,pady=(1,15))
    btton = Button(img,text = "ENTER",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command = display)
    btton.pack()
    
    img.mainloop()
    
    
    
def display():
    img_name = img_input.get()
    image_name = img_name +".png"
    print(image_name)
    dis = cv2.imread(image_name)
    dis = cv2.cvtColor(dis,cv2.COLOR_BGR2RGB)
    
    cv2.imshow("IMAGE",dis)
    cv2.release()
    cv2.destroyAllWindows()

def summary():
    
    summary_extraction = pipeline("summarization")
    summary = summary_extraction(content,max_length = 150,min_length = 60,do_sample = False)
    messagebox.showinfo("Result",summary)

def show():
    global show_input
    show = Tk()
    show.config(bg="blue")
    show.geometry("400x400")
    show_lable = Label(show,text="DATA file name ",bg = "black",fg="white",padx =10,pady =10)
    show_lable.pack()
    
    show_input = Entry(show,width=50)
    show_input.pack(ipady=6,pady=(1,15))
    bton = Button(show,text = "ENTER",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command = showText)
    bton.pack()
    
    show.mainloop()


def showText():
    global content
    
    search = show_input.get()
    st = Tk()
    st.config(bg="voilet")
    st.geometry("900x1100")
    st_lable = Label(st,text="DATA",bg = "black",fg="white",padx =10,pady =10)
    st_lable.pack()
    f1 = LabelFrame(st,bg= "white")
    f1.pack()
    l1 = Label(f1,bg="grey",fg = "black",font= "Helvetica 14 bold",wraplength= 900)
    l1.pack()
    bton = Button(st,text = "summerize",bg="white",fg='black',padx=4,pady=4,borderwidth=6, command = summary)
    bton.pack()
    

    with open("DATA.txt","r") as file :
        for item in file:
            if item == search:
                ans = item+".txt"
                with open(ans,"r") as answer:
                    content = answer.read()
                    
                    l1["text"] = content
                    
            else:
                
                l1["text"] = "DATA NOT PRESENT"
                
    st.mainloop()



def heading():
    global head_input 
    
    head = Tk()
    head.config(bg="brown")
    head.geometry("400x400")
    head_lable = Label(head,text="HEADING",bg = "black",fg="white",padx =10,pady =10)
    head_lable.pack()
    
    head_input = Entry(head,width=50)
    head_input.pack(ipady=6,pady=(1,15))
    btn = Button(head,text = "ENTER",bg="white",fg='black',padx=4,pady=4,borderwidth=6,command = upload)
    btn.pack()
    
    head.mainloop()
             
    


def upload():
    heading = head_input.get()
    
    file_location = filedialog.askopenfilename(title = "Select image")
    name = filedialog.asksaveasfilename()
    name = name.split("/")
    n =len(name)
    naam = name[n-1]  
    img2 = Image.open(file_location,"r")
    img2.load()
    img2.save(naam+".png")
    
    text = pt.image_to_string(naam+".png")
   
    if heading in DATA :
        with open(heading+".txt","a") as file:
            file.write(text)
            
    else:
        with open(heading+".txt","a") as file:
            DATA.append(heading)
            file.write(text)
            
    with open("DATA.txt","a") as data:
        for a in DATA :
            data.write("\n"+a)
        

root = Tk()
root.config(bg="purple")
root.geometry("500x400")
root_lable = Label(root,text="Hello",bg = "black",fg="white",padx =10,pady =10)
root_lable.pack()

b1=Button(root,text='Upload',bg ="white",fg="black",command= heading)
b1.pack(side=LEFT)
b2=Button(root,text='Show Data',bg ="white",fg="black",command= show)
b2.pack(side=RIGHT)
b3=Button(root,text='SHOW IMAGE',bg ="white",fg="black",command= showImage)
b3.pack(side = BOTTOM)
root.mainloop()