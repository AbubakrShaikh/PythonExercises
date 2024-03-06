#Import
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

    #Define Student ID


    #Retrieve Student Name, Grade & ID


#Command to Input Student ID
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
    
#Command to Input Student Grade


#Command to Retrieve Student Grade


#Program Start
window = Tk()

#Create List to Input Student Names & ID
name_id_list = Listbox()

store_name_list=[]

store_id_list=[]

add_name_btn = Button(window, text="Add Name", command=add_id)
add_name_btn.pack()



name_id_list.pack()
window.mainloop()
#Create Button to Retrieve Student Grade 
