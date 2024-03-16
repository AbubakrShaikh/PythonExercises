from tkinter import *
import random

names = []
global questions_answers
asked = []

#Questions and answers
questions_answers = {
    1: ["What is the longest Shark on average out of these?", 'Basking Shark', 'Great Hammerhead Shark', 'Greenland', 'Great White', 'Basking Shark', 1],
    2: ["Which one of these is the fastest Shark?", 'Shortfin Mako', 'Blue', 'Great White', 'Thresher', 'Shortfin Mako', 1],
    3: ["What is the top speed achieved by a Shark (kph)?", '50', '75', '110', '64', '75', 2],
    4: ["Which animal has the strongest bite", 'Great White Shark', 'American Alligator', 'Saltwater Crocodile', 'Polar Bear', 'Saltwater Crocodile', 3],
    5: ["What is the tail fin of a Shark also known as?", 'Dorsal fin', 'Caudal Fin', 'Pectoral Fin', 'Adipose Fin', 'Caudal Fin', 1],
    6: ["Which Shark is not real?", 'Goblin', 'Ghost', 'Wobbegong', 'Abysstalon', 'Abysstalon', 4],
    7: ["What is the head of a Hammerhead Shark used for?", 'Detecting Enemies', 'Greater Speed', 'Finding Food', 'More Agility', 'Finding Food', 3],
    8: ["Which of these Sharks does a Killer Whale?", 'Basking Shark', 'Great Hammerhead Shark', 'Greenland', 'Great White', 'Basking Shark', 1],
    9: ["What is can a Shark sense apart from the 5 senses?", 'Blood', 'Urine', 'Weather', 'Electricity', 'Electricity', 4],
    10: ["Where in the world do people get attacked by Sharks the most?", 'Australia', 'South Carolina', 'Florida', 'Hawaii', 'Florida', 4],
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
        Quiz(window)

#Quiz Instance
class Quiz:
    def __init__(self, parent):
        #Change the default background color
        back_color = "OldLace"
        #Setup initial frame for quiz
        self.initial_frame = Frame(parent, bg = back_color, padx = 150, pady = 150)
        self.initial_frame.grid()

        randomiser()

        #Main question for the quiz
        self.question_label = Label(self.initial_frame, text= questions_answers[qnum][0], font = ("Helvetica", 20, "bold"), bg = back_color)   
        self.question_label.grid(row = 0, padx = 10, pady = 20)

        #Holds value of radio buton
        self.var1 = IntVar()

        #1st radio button
        self.rb1 = Radiobutton (self.initial_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg = back_color, value = 1, variable = self.var1, pady = 10)
        self.rb1.grid(row = 1, sticky=W)

        #2nd radio button
        self.rb2 = Radiobutton (self.initial_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg = back_color, value = 2, variable = self.var1, pady = 10)
        self.rb2.grid(row = 2, sticky=W)

        #3rd radio button
        self.rb3 = Radiobutton (self.initial_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg = back_color, value = 3, variable = self.var1, pady = 10)
        self.rb3.grid(row = 3, sticky=W)

        #4th radio button
        self.rb4 = Radiobutton (self.initial_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg = back_color, value = 4, variable = self.var1, pady = 10)
        self.rb4.grid(row = 4, sticky=W)

        self.confirm_button = Button(self.initial_frame, text ="Confirm", bg = "Red")
        self.confirm_button.grid(row = 5)
#This is the main window which will hold all the instances/frames for the quiz    

window = Tk()
window.title("Shark Quiz")
first_instance = EntryPage(window)
window.mainloop()
