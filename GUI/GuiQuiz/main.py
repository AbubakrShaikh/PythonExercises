from tkinter import *
import random

names = []
global questions_answers
asked = []

#Questions and answers
questions_answers = {
    1: ["What is the longest shark on average out of these?", 'Basking Shark', 'Great Hammerhead Shark', 'Greenland', 'Great White', 'Basking Shark', 1],
    2: ["What is the longest shark on average out of these?", 'Basking Shark', 'Great Hammerhead Shark', 'Greenland', 'Great White', 'Basking Shark', 1],
}

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

#Initial Page
class EntryPage:
    def __init__(self, parent):
    
    #Function for collecting username and destroy frame
    
        #Change the default background color
        back_color = "OldLace"

        #Setup initial frame for quiz
        self.initial_frame = Frame(parent, bg = back_color, padx = 150, pady = 150)
        self.initial_frame.grid()

        #Main heading for the quiz
        self.main_label = Label(self.initial_frame, text="GUI Quiz", font = ("Helvetica", 20, "bold"), bg = back_color)   
        self.main_label.grid(row = 0, padx = 10, pady = 20)

        #Holds the value of the inputs
        self.input1 = IntVar

        #This shows the user what to do on the initial page and enter their name
        self.user_name = Label(self.initial_frame, text = "Please enter your name", font = ("Times", 13), bg = back_color)
        self.user_name.grid(row = 1, padx = 20, pady = 20)

        self.name_entry = Entry(self.initial_frame)
        self.name_entry.grid(row = 2, padx = 20, pady = 20)

        
        #This is a button that enables the user to continue to next part of the quiz
        self.continue_button = Button(self.initial_frame, text = "Enter", font = ("bold"), bg="red", command=self.collect_name)
        self.continue_button.grid(row = 3, padx = 20, pady = 20)

    #This function collects the user's name then destroys the initial_frame frame
    def collect_name(self):
        name = self.name_entry.get()
        names.append(name)
        print(names)
        self.initial_frame.destroy()

#This is the main window which will hold all the instances/frames for the quiz    
randomiser()
window = Tk()
window.title("GUI Quiz")
first_instance = EntryPage(window)
window.mainloop()
