from tkinter import *
from backend import *
from tkinter import scrolledtext
from tkinter import messagebox
def execute_translate():
    """
    
    """
    #result_list.delete(0,END)
    
    output = translate(word_field.get())
    newbx.configure(state="normal")
    newbx.delete("1.0",END)
    #result_list.insert(1, output)
    #newbx.delete(0,END)
    newbx.insert(INSERT,output)
    newbx.configure(state="disabled")

window=Tk()

#wiget.pack()
    

label1 = Label(window, text = "Enter Word")
label1.grid(row=0, column=0)

label2 = Label(window,text ="Definations")
label2.grid(row=2, column=0)


word_text= StringVar()
word_field = Entry(window,textvariable = word_text)
word_field.grid(row = 0, column = 1)





search_btn = Button(window, text= "Search", command = execute_translate,bg="blue",padx = 10, pady = 10, fg="red")
search_btn.grid(row = 0, column =2 )

#scbar = Scrollbar(window)
#scbar.grid(row=3,column=7, rowspan=6)


#result_list = Listbox(window, height=10, width = 200)
#result_list.grid(row = 3, column = 1, columnspan = 6,rowspan=6)
#result_list.insert(1, "abcsasfsdfsd fs s df sd sd fesd s df sdf sdf sd sd sd sd sdfsdfs dw fdssd s ddadf")

#result_list.configure(yscrollcommand = scbar.set)
#scbar.configure(command = result_list.yview)

#print(word_field.get())
#bx = Entry(window,width = 55)
#bx.grid(row=4,column = 1)

newbx = text_area = scrolledtext.ScrolledText(window,  
                                      width = 100,  
                                      height = 10, state = "disabled") 
  
text_area.grid(row = 6,column = 0, pady = 10, padx = 10,columnspan=7) 

#messagebox.askquestion(title="info", message="bqa")
window.mainloop()