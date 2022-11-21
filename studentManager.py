from tkinter import *

studentList = []

count = 5
root = Tk()


def onClicked(row=count):
    student = {
        'name': name.get(),
        'surname': surname.get(),
        'matricNo': matricNo.get(),
        'score': score.get(),
    }
    studentList.append(student)
    name.delete(0, END)
    surname.delete(0, END)
    matricNo.delete(0, END)
    score.delete(0, END)

    studentText = Label(
        root, text=f"Name: {student['name']} , Surname: {student['surname']} , MatricNo: {student['matricNo']} , Score: {student['score']}")
    studentText.grid(column=1, row=row)
    row += 1


nameText = Label(root, text="Name: ")
nameText.grid(column=0, row=0)
name = Entry(root)
name.grid(column=1, row=0)
surnameText = Label(root, text="Surname: ")
surnameText.grid(column=0, row=1)
surname = Entry(root)
surname.grid(column=1, row=1)
matricNoText = Label(root, text="MatricNo: ")
matricNoText.grid(column=0, row=2)
matricNo = Entry(root)
matricNo.grid(column=1, row=2)
scoreText = Label(root, text="Score: ")
scoreText.grid(column=0, row=3)
score = Entry(root)
score.grid(column=1, row=3)

button = Button(text="Compute", command=onClicked)
button.grid(column=1, row=count + 1)
button = Button(text="Done", command=onClicked)
button.grid(column=1, row=4)

root.mainloop()
