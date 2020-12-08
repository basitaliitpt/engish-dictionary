from tkinter import *
from backend import *

def execute_translate():
    """
    docstring
    """
    result_list.delete(0,END)
    output = translate(word_field.get())
    
    result_list.insert(1, output)


window=Tk()


    

label1 = Label(window, text = "Enter Word")
label1.grid(row=0, column=0)

label2 = Label(window,text ="Definations")
label2.grid(row=2, column=0)


word_text= StringVar()
word_field = Entry(window,textvariable = word_text)
word_field.grid(row = 0, column = 1)


result_list = Listbox(window, height=10, width = 200)
result_list.grid(row = 3, column = 1, columnspan = 6,rowspan=6)
#result_list.insert(1, "abcsasfsdfsd fs s df sd sd fesd s df sdf sdf sd sd sd sd sdfsdfs dw fdssd s ddadf")


search_btn = Button(window, text= "Search", command = execute_translate)
search_btn.grid(row = 0, column =2 )

scbar = Scrollbar(window)
scbar.grid(row=3,column=7, rowspan=6)

result_list.configure(yscrollcommand = scbar.set)
scbar.configure(command = result_list.yview)

#print(word_field.get())

window.mainloop()