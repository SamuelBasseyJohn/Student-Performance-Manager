from tkinter import *

studentList = []

count = 6
root = Tk()


def nameField(student, row):
    nameText = Label(
        root, text=f"Name: {student['name']} {student['surname']}")
    nameText.grid(column=0, row=row)


def matricNoField(student, row):
    matricNoText = Label(
        root, text=f"MatricNo: {student['matricNo']}")
    matricNoText.grid(column=1, row=row)


def scoreField(student, row):
    scoreText = Label(
        root, text=f"Score: {student['score']}")
    scoreText.grid(column=2, row=row)


def onClicked():
    global count
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

    nameField(student=student, row=count)
    matricNoField(student=student, row=count)
    scoreField(student=student, row=count)

    count += 1


nameText = Label(root, text="Name: ")
nameText.grid(column=0, row=0)
name = Entry(root, width=30)
name.grid(column=1, row=0)
surnameText = Label(root, text="Surname: ")
surnameText.grid(column=0, row=1)
surname = Entry(root, width=30)
surname.grid(column=1, row=1)
matricNoText = Label(root, text="MatricNo: ")
matricNoText.grid(column=0, row=2)
matricNo = Entry(root, width=30)
matricNo.grid(column=1, row=2)
scoreText = Label(root, text="Score: ")
scoreText.grid(column=0, row=3)
score = Entry(root, width=30)
score.grid(column=1, row=3)
whiteSpace1 = Label(root, text=" ")
whiteSpace1.grid(column=0, row=4)


button = Button(text="Compute", command=onClicked)
button.grid(column=0, row=5)
button = Button(text="Done", command=onClicked)
button.grid(column=1, row=5)

root.mainloop()
