#Developer : Vivek Doshi
#password generator

#Fetching libraries 
import random as r
import string 
import tkinter
import pyperclip as pc



#-------------------  Main Logic -----------------------
def pass_gen_GUI(l):
    password = "".join(r.choice(string.ascii_letters + string.digits)for i in  range(l)) #this generates the password
    password_s = str(password)
    
    #show_generated_password
    # generated_pass.destroy()
    generated_pass=tkinter.Label(window, text= password_s, fg='Black', font=("Helvetica", 15))
    generated_pass.place(x=80, y=150)
    
    #button to copy password
    btn=tkinter.Button(window, text="copy", command= copy_pass)
    btn.place(x=250, y=150)

    #button to store password
    """
    btn=Button(window, text="store",command=store_it(password_s))
    btn.place(x=350, y=150)  """

    pass_gen_GUI.var = password_s

def copy_pass():
    pc.copy(pass_gen_GUI.var)          # problem to be solve (copy button)
    

def generate(): 
    value_entry = data.get()
    length_data = int(value_entry)
    pass_gen_GUI(length_data)

def store_it(password):
    with open("password.txt", 'a') as f:
        f.write(password+"\n")

#----------------------------------------------------------



# UI

#creating window
window=tkinter.Tk()

#variable that stores entered data in string
data = tkinter.StringVar()

#top_label
lbl=tkinter.Label(window, text="Password Generator", fg='Black', font=("Helvetica", 18))
lbl.place(x=80, y=20)

#instruct_label
lbl=tkinter.Label(window, text="Enter length below ", fg='Black', font=("Helvetica", 10))
lbl.place(x=80, y=80)

#length_of_password_entry
txtfld=tkinter.Entry(window, textvariable = data, bd=5)
txtfld.place(x=80, y=100)

#button to generate
btn=tkinter.Button(window, text="Generate",command= generate)
btn.place(x=250, y=100)

window.title('Password Generator')
window.geometry("500x200")
window.mainloop()

