from tkinter import *
from tkinter import ttk
import csv
# Main Canvas Definition
root = Tk()
root.title('Student Manager')
root.geometry('600x500')

# Global Variables
studentList = []
passStudentsList = []
failedStudentsList = []
bestStudentsList = []
meanScore = 0
row = 7
meanLabel = Label()
bestStudentLabelText = Label()
bestStudentLabel = Label()
nameLabel = Label()
matricNoLabel = Label()
scoreLabel = Label
passStudentLabel = Label()
passStudentLabelText = Label()
failedStudentLabel = Label()
failedStudentLabelText = Label()
seeMorePassButton = Button()
seeMoreFailedButton = Button()

# ScrollBar Functionality
# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(
    main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Important Functions


def nameField(student, row):
    global nameLabel
    nameLabel = Label(
        second_frame, text=f"Name: {student['name']} {student['surname']}")
    nameLabel.grid(column=0, row=row)


def matricNoField(student, row):
    global matricNoLabel
    matricNoLabel = Label(
        second_frame, text=f"MatricNo: {student['matricNo']}")
    matricNoLabel.grid(column=1, row=row)


def scoreField(student, row):
    global scoreLabel
    scoreLabel = Label(
        second_frame, text=f"Score: {student['score']}")
    scoreLabel.grid(column=2, row=row)


def meanScoreField(mean, row):
    global meanLabel
    meanLabel = Label(
        second_frame, text=f"MeanScore: {mean}")
    meanLabel.grid(column=0, row=row)


def bestStudentsField(bestStudents, maxScore, row):
    global bestStudentLabelText
    global bestStudentLabel
    column: int = 1
    students = ""
    bestStudentLabelText = Label(
        second_frame, text="BestStudents:")
    bestStudentLabelText.grid(column=0, row=row)
    for item in bestStudents:
        students = f"{students} {item}({maxScore})"
    bestStudentLabel = Label(
        second_frame, text=students)
    bestStudentLabel.grid(column=column, row=row)


def passStudentsField(passStudents, row, column):
    global passStudentLabelText
    global passStudentLabel
    global seeMoreButton
    students = ""
    passStudentLabelText = Label(
        second_frame, text="Students that passed: ")
    passStudentLabelText.grid(column=0, row=row)
    for i in range(len(passStudents)):
        students = f"{students} {passStudents[i]},"
        if (i >= 2):
            students = f"{students}..."
            break
    passStudentLabel = Label(
        second_frame, text=students)
    passStudentLabel.grid(column=column, row=row)
    seeMorePass(allPassStudents, column=column, row=row)


def failedStudentsField(failedStudents, row, column):
    global failedStudentLabelText
    global failedStudentLabel
    global seeMoreButton
    students = ""
    failedStudentLabelText = Label(
        second_frame, text="Students that failed: ")
    failedStudentLabelText.grid(column=0, row=row)
    for i in range(len(failedStudents)):
        students = f"{students} {failedStudents[i]},"
        if (i >= 2):
            students = f"{students}..."
            break
    failedStudentLabel = Label(
        second_frame, text=students)
    failedStudentLabel.grid(column=column, row=row)
    seeMoreFailed(allFailedStudents, column=column, row=row)


def seeMorePass(command, column, row):
    global seeMorePassButton
    seeMorePassButton = Button(second_frame, text="See all", command=command)
    seeMorePassButton.grid(column=column+1, row=row)


def seeMoreFailed(command, column, row):
    global seeMoreFailedButton
    seeMoreFailedButton = Button(second_frame, text="See all", command=command)
    seeMoreFailedButton.grid(column=column+1, row=row)


def allPassStudents():
    window = Toplevel()
    window.title('Students that Passed')
    window.geometry('300x200')
    scroll = Scrollbar(window)
    scroll.pack(side=RIGHT, fill=Y)
    count: int = 0
    myList = Listbox(window, yscrollcommand=scroll.set)
    for i in passStudentsList:
        myList.insert(END, f"{count+1}. {i}")
        count += 1
    myList.pack(side=LEFT, fill=BOTH)
    scroll.config(command=myList.yview)


def allFailedStudents():
    window = Toplevel()
    window.title('Students that Failed')
    window.geometry('300x200')
    scroll = Scrollbar(window)
    scroll.pack(side=RIGHT, fill=Y)
    count: int = 0
    myList = Listbox(window, yscrollcommand=scroll.set)
    for i in passStudentsList:
        myList.insert(END, f"{count+1}. {i}")
        count += 1
    myList.pack(side=LEFT, fill=BOTH)
    scroll.config(command=myList.yview)


def allBestStudents():
    window = Toplevel()
    window.geometry('300x200')
    frame = Frame(window)
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=window.yview)

    count: int = 0
    for i in bestStudentsList:
        Label(window, text=f"{count+1} {i}").grid(column=0, row=count)
        count += 1


def passStudents():
    scores = []
    for item in studentList:
        studentScore = int(item['score'])
        scores.append(studentScore)

    for item in studentList:
        intScore = int(item['score'])
        if (intScore >= 70):
            passStudentsList.append(f"{item['name']} ({intScore})")
    passStudentsField(passStudents=passStudentsList, column=1,
                      row=row + 4)


def failedStudents():
    scores = []
    for item in studentList:
        studentScore = int(item['score'])
        scores.append(studentScore)

    for item in studentList:
        intScore = int(item['score'])
        if (intScore < 50):
            failedStudentsList.append(f"{item['name']} ({intScore})")
    failedStudentsField(failedStudents=failedStudentsList, column=1,
                        row=row + 5)


def save(fileList):
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

    for item in studentList:
        studentScore = int(item['score'])
        scores.append(studentScore)

    maxScore = max(scores)
    for item in studentList:
        intScore = int(item['score'])
        if (intScore == maxScore):
            bestStudentsList.append(f"{item['name']} {item['surname']}")
    bestStudentsField(bestStudents=bestStudentsList,
                      maxScore=maxScore, row=row + 3)


def undo():
    global nameLabel
    global matricNoLabel
    global scoreLabel
    global bestStudentsList
    global passStudentsList

    bestStudentsList = []
    passStudentsList = []
    nameLabel.destroy()
    matricNoLabel.destroy()
    scoreLabel.destroy()
    meanLabel.destroy()
    bestStudentLabelText.destroy()
    bestStudentLabel.destroy()
    passStudentLabel.destroy()
    passStudentLabelText.destroy()
    seeMorePassButton.destroy()
    seeMoreFailedButton.destroy()


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
    seeMorePassButton.destroy()
    seeMoreFailedButton.destroy()

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
    failedStudents()

# User Interface


nameText = Label(second_frame, text="Name: ")
nameText.grid(column=0, row=0)

name = Entry(second_frame, width=30)
name.grid(column=1, row=0)

surnameText = Label(second_frame, text="Surname: ")
surnameText.grid(column=0, row=1)

surname = Entry(second_frame, width=30)
surname.grid(column=1, row=1)

matricNoText = Label(second_frame, text="MatricNo: ")
matricNoText.grid(column=0, row=2)

matricNo = Entry(second_frame, width=30)
matricNo.grid(column=1, row=2)

scoreText = Label(second_frame, text="Score: ")
scoreText.grid(column=0, row=3)

score = Entry(second_frame, width=30)
score.grid(column=1, row=3)

whiteSpace1 = Label(second_frame, text=" ")
whiteSpace1.grid(column=0, row=4)

button1 = Button(second_frame, text="Compute", command=compute)
button1.grid(column=0, row=5)

button2 = Button(second_frame, text="Next", command=onClicked)
button2.grid(column=1, row=5)

button3 = Button(second_frame, text="Undo", command=undo)
button3.grid(column=2, row=5)

button4 = Button(second_frame, text="Save", command=save)
button4.grid(column=3, row=5)

whiteSpace1 = Label(second_frame, text=" ")
whiteSpace1.grid(column=0, row=6)

root.mainloop()
