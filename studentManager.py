from tkinter import *
import csv

studentList = []
meanScore = 0

row = 7
root = Tk()
root.title('Student Manager')
root.geometry('600x500')
meanLabel = Label()
bestStudentLabelText = Label()
bestStudentLabel = Label()
nameLabel = Label()
matricNoLabel = Label()
scoreLabel = Label
passStudentLabel = Label()
passStudentLabelText = Label()


def nameField(student, row):
    global nameLabel
    nameLabel = Label(
        root, text=f"Name: {student['name']} {student['surname']}")
    nameLabel.grid(column=0, row=row)


def matricNoField(student, row):
    global matricNoLabel
    matricNoLabel = Label(
        root, text=f"MatricNo: {student['matricNo']}")
    matricNoLabel.grid(column=1, row=row)


def scoreField(student, row):
    global scoreLabel
    scoreLabel = Label(
        root, text=f"Score: {student['score']}")
    scoreLabel.grid(column=2, row=row)


def meanScoreField(mean, row):
    global meanLabel
    meanLabel = Label(
        root, text=f"MeanScore: {mean}")
    meanLabel.grid(column=0, row=row)


def bestStudentsField(bestStudents, maxScore, row):
    global bestStudentLabelText
    global bestStudentLabel
    column: int = 1
    students = ""
    bestStudentLabelText = Label(
        root, text="BestStudents:")
    bestStudentLabelText.grid(column=0, row=row)
    for item in bestStudents:
        students = f"{students} {item}({maxScore})"
    bestStudentLabel = Label(
        root, text=students)
    bestStudentLabel.grid(column=column, row=row)


def passStudentsField(passStudents, row, column):
    global passStudentLabelText
    global passStudentLabel
    students = ""
    passStudentLabelText = Label(
        root, text="Students that passed: ")
    passStudentLabelText.grid(column=0, row=row)
    for item in passStudents:
        passStudentLabel = Label(
            root, text=item
        )
        passStudentLabel.grid(column=column, row=row)
        column += 1


def passStudents():
    scores = []
    passStudents = []
    for item in studentList:
        studentScore = int(item['score'])
        scores.append(studentScore)

    for item in studentList:
        intScore = int(item['score'])
        if (intScore >= 70):
            passStudents.append(f"{item['name']} ({intScore})")
    passStudentsField(passStudents=passStudents, column=1,
                      row=row + 4)


def save():
    with open("StudentResult.csv", 'a', newline="") as file:
        myFile = csv.writer(file)
        myFile.writerow()


def mean():
    global row
    global meanScore
    totalScore: int = 0
    length: int = len(studentList)

    for item in studentList:
        totalScore += int(item['score'])
    rawMean = totalScore/length
    meanScore = round(rawMean, 2)
    meanScoreField(mean=meanScore, row=row + 2)


def bestStudent():
    global row
    global studentList
    scores = []
    bestStudents = []
    for item in studentList:
        studentScore = int(item['score'])
        scores.append(studentScore)

    maxScore = max(scores)
    for item in studentList:
        intScore = int(item['score'])
        if (intScore == maxScore):
            bestStudents.append(f"{item['name']} {item['surname']}")
    bestStudentsField(bestStudents=bestStudents,
                      maxScore=maxScore, row=row + 3)


def undo():
    global nameLabel
    global matricNoLabel
    global scoreLabel

    nameLabel.destroy()
    matricNoLabel.destroy()
    scoreLabel.destroy()
    meanLabel.destroy()
    bestStudentLabelText.destroy()
    bestStudentLabel.destroy()
    passStudentLabel.destroy()
    passStudentLabelText.destroy()


def onClicked():
    global row
    global meanLabel
    global bestStudentLabel
    global bestStudentLabelText
    student = {
        'name': name.get(),
        'surname': surname.get(),
        'matricNo': matricNo.get(),
        'score': score.get(),
    }

    studentList.append(student)
    meanLabel.destroy()
    bestStudentLabelText.destroy()
    bestStudentLabel.destroy()

    name.delete(0, END)
    surname.delete(0, END)
    matricNo.delete(0, END)
    score.delete(0, END)

    nameField(student=student, row=row)
    matricNoField(student=student, row=row)
    scoreField(student=student, row=row)

    row += 1


def compute():
    mean()
    bestStudent()
    passStudents()


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

button1 = Button(text="Compute", command=compute)
button1.grid(column=0, row=5)

button2 = Button(text="Next", command=onClicked)
button2.grid(column=1, row=5)

button3 = Button(text="Undo", command=undo)
button3.grid(column=2, row=5)

button4 = Button(text="Save", command=save)
button4.grid(column=3, row=5)

whiteSpace1 = Label(root, text=" ")
whiteSpace1.grid(column=0, row=6)

root.mainloop()
