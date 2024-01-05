import random


#INSERT INTO projectschool.studentclass(ClassID,StudentID)
#VALUES(1, 1);

#INSERT INTO projectschool.exam (ExamID, ExamName, ClassID, ExamType)
#VALUES (1, 'Midterm', 1, 1);

cuantos = 80
examenes = [
    "starter", "midterm", "final","extracredit","quiz"
]


def createExams():

    Exams = []
    for exam in range(1, cuantos + 1):
        cual = int(len(examenes) * random.random())
        Exams.append(examenes[cual])
    return Exams

def printing(Exams):
    
#INSERT INTO projectschool.exam (ExamID, ExamName, ClassID, ExamType)
#VALUES (1, 'Midterm', 1, 1);
    
    print("\nProfessors table:\n")
    print("INSERT INTO projectschool.examtype(ExamType,TypeName)\nVALUES\n  (1, 'MultipleChoice'),\n  (2, 'Oral'),\n  (3, 'Reading'),\n  (4, 'Essay')\n;")
    
    print("\nExams table")
    print("\nINSERT INTO projectschool.exam ( ExamName, ClassID, ExamType)\nVALUES\n")
    for x in range(1, cuantos + 1 ):
        ClassID = int(random.random() * 50)
        if (ClassID == 0):
            ClassID = 1

        ExamType = int(random.random() * 4)
        if (ExamType == 0):
            ExamType = 1
        print(" ('"+ Exams[int(random.random() * 5)] + "', " + str(ClassID)  + ", "+ str(ExamType) + "),")
    print("\n;")
    


Exams = createExams()

printing(Exams)