'''
create madlibs in python using tkinter
-input colour noun name adjective.
-display a button on clicking which, the madlibs appears
'''
from tkinter import *
from tkinter.font import BOLD
root=Tk()
root.title('Mad Libs in Python')
root.geometry('300x200')
root.config(bg='#33C0FF')


lbl1=Label(root,text='Name:',bg='#33C0FF',fg='#000000')
lbl1.grid(column=1,row=0,ipadx=10,)
box1=Entry(root,width=30)
box1.grid(column=2,row=0)

lbl2=Label(root,text='Colour:',bg='#33C0FF')
lbl2.grid(column=1,row=1,ipadx=8,padx=5)
box2=Entry(root,width=30)
box2.grid(column=2,row=1)

lbl3=Label(root,text=' Food:',bg='#33C0FF')
lbl3.grid(column=1,row=2,ipadx=11)
box3=Entry(root,width=30)
box3.grid(column=2,row=2)

lbl4=Label(root,text='Place:',bg='#33C0FF')
lbl4.grid(column=1,row=3,ipadx=12)
box4=Entry(root,width=30)
box4.grid(column=2,row=3)

lbl5=Label(root,text='Verb:',bg='#33C0FF')
lbl5.grid(column=1,row=4,ipadx=14)
box5=Entry(root,width=30)
box5.grid(column=2,row=4)

def clicked():
    print('Yesterday I met my old friend ',box1.get(),'.\nHe was wearing a ',box2.get()
    ,'shirt and black track pants , I greeted him with a smile and offered him some ',box3.get()
    ,'\n.When I asked him where he was off to? he replied ,\n"I am going to ',box4.get(),' to ',box5.get(),'there with my friends ,you should join us!."')
def clicked2():
    print('I am totally in love with ',box1.get(),'...\nHis ',box2.get()
    ,' eyes and his cute smile has had my heart eversince I met him...,\nwhenever I see his ',box3.get()
    ,'like cheeks I..I start dreaming...\nI first met him on the school trip to ',box4.get(),'where he was ',box5.get(),'\nwith his friends and his ',box2.get(),' eyes met mine...')
    

# button widget with red color text
# inside
btn = Button(root, text = "I met an old friend",width=20, command=clicked)
btn.grid(column=2, row=5,pady=10)
btn.configure(font=("Courier", 8, "bold"))
btn2=Button(root, text = "My crush",width=20, command=clicked2)
btn2.configure(font=("Courier", 8, "bold"))
btn2.grid(column=2, row=6)
root.mainloop()
