from tkinter import Tk,Label,Entry,StringVar
from PIL import Image,ImageTk


root=Tk()
root.title("Temperature Converter")
root.geometry("500x300")
root.config(bg="white")
root.resizable(False,False)

# function code
main_func="CTA"


def up(e):
    global main_func
    tab_main.place(x=15,y=80)
    main_func="CTA"
def mid(e):
    global main_func
   
    tab_main.place(x=15,y=140)
    main_func="FTA"
def down(e):
    global main_func
    
    tab_main.place(x=15,y=200)
    main_func="KTA"

def handleapp(e):
    try:
        if main_func=="CTA":
            celsius=float(celsius_value.get())
            farhenheit=(celsius*9/5)+32
            kelvin=celsius+273.15
            faren_value.set(f"{farhenheit}")
            kelvin_value.set(f"{kelvin}")
        elif main_func=="FTA":
            farhenheit=float(faren_value.get())
            celsius=(farhenheit-32)*5/9
            kelvin=celsius+273.15
            celsius_value.set(f"{celsius}")
            kelvin_value.set(f"{kelvin}")
        elif main_func=="KTA":
            kelvin=float(kelvin_value.get())
            celsius=kelvin-273.15
            farhenheit=(celsius*9/5)+32
            celsius_value.set(f"{celsius}")
            faren_value.set(f"{farhenheit}")
    except Exception as e:
        pass

# background image configure
background=Image.open("./assets/back.png").resize((200,200))
backgroundImage=ImageTk.PhotoImage(background)

title_text=Label(root,background="white",image=backgroundImage,font=("Microsoft YaHei UI Light",26))
title_text.place(x=300,y=50)
# background image configuration ends here

# testing entry background

entry_bg=ImageTk.PhotoImage(Image.open("./assets/enrect.png").resize((117,50)))
Label(root,background="white",image=entry_bg).place(x=50,y=65)
Label(root,background="white",image=entry_bg).place(x=50,y=125)
Label(root,background="white",image=entry_bg).place(x=50,y=185)


entry_bg1=ImageTk.PhotoImage(Image.open("./assets/celcius.png").resize((50,50)))
entry_bg2=ImageTk.PhotoImage(Image.open("./assets/farh.png").resize((50,50)))
entry_bg3=ImageTk.PhotoImage(Image.open("./assets/kelvin.png").resize((50,50)))

Label(root,background="white",image=entry_bg1).place(x=180,y=65)
Label(root,background="white",image=entry_bg2).place(x=180,y=125)
Label(root,background="white",image=entry_bg3).place(x=180,y=185)

# ------------------
# 140 80 200

toggle_image=ImageTk.PhotoImage(Image.open("./assets/tab.png").resize((20,20)))

tab_main=Label(root,background="white",image=toggle_image)
tab_main.place(x=15,y=80)

# making dynamic variables

celsius_value=StringVar()
faren_value=StringVar()
kelvin_value=StringVar()

celsius_value.set("0.0")
faren_value.set("32.0")
kelvin_value.set("273.15")



# making entries

celsius_input=Entry(root,font=("lucida", 20,"bold" ),textvariable=celsius_value,background="#e6e6e6",width=7,border=0)
celsius_input.place(x=60,y=75)

faren_input=Entry(root,font=("lucida", 20,"bold" ),background="#e6e6e6",width=7,border=0,textvariable=faren_value)
faren_input.place(x=60,y=135)

kelvin_input=Entry(root,font=("lucida", 20,"bold" ),background="#e6e6e6",width=7,border=0,textvariable=kelvin_value)
kelvin_input.place(x=60,y=195)

# move the ball

celsius_input.bind("<Button-1>",up)
faren_input.bind("<Button-1>",mid)
kelvin_input.bind("<Button-1>",down)




# button programming

btn_image=ImageTk.PhotoImage(Image.open("./assets/convert.png").resize((50,50)))

main_btn=Label(root,background="white",image=btn_image,cursor="hand2")

main_btn.place(x=250,y=185)

main_btn.bind("<Button-1>",handleapp)

root.mainloop()