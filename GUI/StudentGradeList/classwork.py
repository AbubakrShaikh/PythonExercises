from tkinter import *   

class Student:
    def __init__(self, name):
        self.name = name
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade

def show_grade():
    grade_label.config(text=csc2[0].grade)


csc2 = []

csc2.append(Student("Boaz"))
csc2[0].set_grade("Achieved")

window = Tk()
window.geometry("300x300")

grade_label = Label()
grade_label.pack

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack

window.mainloop()