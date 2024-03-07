# Import module 
from tkinter import *

#Classes
#Class to hold different students
class Student:
    #Define Student Name
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no
    #Define Student Grade
    def grade_level(self, grade):
        self.grade = grade

# Change the label text 
def show(): 
    label.config( text = clicked.get() )
    
def add_id():
    no = int(input("Enter the student's position number on the list"))
    
    s_name = input("Enter the name of the Student ")
    store_name_list.insert(no, s_name)
    print(store_name_list)
    
    s_id = input("Enter the student's ID number")
    store_id_list.insert(no, s_id)
    print(store_id_list)

    s_name_id = s_name, s_id
    name_id_list.insert(no, s_name_id)
    print(name_id_list)


# Create object 
window = Tk()
  
# Adjust size 
window.geometry( "200x200" ) 
  
# Dropdown menu name_id_list 
name_id_list = ["No Selection"]

store_name_list=[]

store_id_list=[]


# datatype of menu text 
clicked = StringVar() 
  
# Create Dropdown menu 
drop = OptionMenu( window , clicked , *name_id_list ) 
drop.pack() 
  
# Create button, it will change label text
add_name_btn = Button(window, text="Add Name", command=add_id)
add_name_btn.pack()

button = Button( window , text = "Show Grade" , command = show ).pack() 


# Create Label 
label = Label( window , text="a" )#Add Grade 
label.pack() 
  
# Execute tkinter 
window.mainloop()

#https://www.geeksforgeeks.org/tkinter-optionmenu-widget/
