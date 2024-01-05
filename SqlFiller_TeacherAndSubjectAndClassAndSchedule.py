import random

cuantosProfesores = 50 + 1

nombreslista = [
    "Liam", "Valentina", "Thiago","Emma", "Noah",
    "Victoria", "Mateo", "Luna", "Sebastián", "Aurora",
	"Lucas", "Amaia", "Dylan", "Catalina", "Ian",
    "Mía", "Nicolás", "Milena", "Ethan", "Gianna",
    "Liam", "Olivia", "Noah", "Emma", "Oliver",
    "Charlotte","James","Amelia","Elijah","Sophia",
	"William","Isabella","Henry","Ava","Lucas",
    "Mia","Benjamin","Evelyn","Theodore","Luna",
    "Santiago", "Kole"
]

departamentos = [
    "Arts","STEM","Engineering","PA","Theology","Computer Science","Business"
]

temas = [ 

    "Freshman Composition", "Principles","Advanced courses", "Electives", "Intermediate", "General", "Senior design"
]

colleges = [
    "Arts College", "Sciences College", "Engineering College"
]

numerosClase = [
    "101","102","103","131","201","205","350","490","370","493"
]

callesNombres = [
    "LaSalle","St monica","Salento","Mound St", "Chapell Hill", "Topacio", "Magnificent Mile"
]

apellidolista =  [

    "Smith","Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis" , "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Martin", "Lee", "Perez", "Thompson", "White",
    "Harris","Thomas", "Taylor", "Moore", "Jackson",
    "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", 
    "Walker", "Young", "Allen" ,"King", "Wright",
    "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall",
    "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gutierrez", "Pugh", "Rosassco", "Brossasco"
]

def createProfessorName():

    professors = []

    for professor in range(1,cuantosProfesores + 1):

        cual = int(len(nombreslista) * random.random())
        professors.append(nombreslista[cual])

    return professors


def createProfessorLastName():

    professorsLastNames = []

    for professor in range(1, cuantosProfesores + 1):

        cual = int(len(apellidolista) * random.random())
        professorsLastNames.append(apellidolista[cual])
        
    return professorsLastNames

def createProfessorDate():

    dates = []
    for professor in range(1, cuantosProfesores+1):

        mes = int(random.random() * 12)
        dia = int(random.random() * 28)

        if (dia == 0):
            dia = 1
        if (mes == 0):
            mes = 1
        if (dia < 10):
            dia = "0"+ str(dia)
        else:
            dia = str(dia)
        if (mes < 10):
            mes = "0"+ str(mes)
        else:
            mes = str(mes)

        date = (str(int(1990 + random.random() * 30)) + "-" + mes + "-" + dia)
        dates.append(date)
        
    return dates

def createDepartment():
    deparments = []
    for professor in range(1, cuantosProfesores+1):
        cual = int(len(departamentos) * random.random())
        deparments.append(departamentos[cual])

    return deparments

def createDirection():
    directions = []

    for professor in range(1, cuantosProfesores+1):

        cual = int(len(departamentos) * random.random())
        calle = str(int(random.random() * 1000))

        directions.append(calle + " " + callesNombres[cual])

    return directions

def createTopic():

    topics = []
    SubName = []
    SubjectCollege = []

    for professor in range(1, cuantosProfesores+1):

        cualt = int(len(temas) * random.random())
        #SubName.append(temas[cualt])

        cualC = int(len(colleges) * random.random())
        #SubjectCollege.append(colleges[cualC])

        topics.append([temas[cualt], colleges[cualC]])


    return topics

def createClassName():

    classNames = []
    for professor in range(1, cuantosProfesores+1):
        cual = int(len(numerosClase) * random.random())
        classNames.append(numerosClase[cual])

    return classNames

def createZoom():

    
    zooms = []
    for professor in range(1, cuantosProfesores+1):
        
        zooms.append("http://zoom.us/"+ str(int(random.random()*200)))

    return zooms

def createFechas():

    fechas = []

    for professor in range(1, cuantosProfesores+1):

        mes = int(random.random() * 12)
        dia = int(random.random() * 28)

        if (dia == 0):
            dia = 1
        if (mes == 0):
            mes = 1
        if (dia < 10):
            dia = "0"+ str(dia)
        else:
            dia = str(dia)
        if (mes < 10):
            mes = "0"+ str(mes)
        else:
            mes = str(mes)

        date1 = (str(2023) + "-" + mes + "-" + dia)

        dia = int(random.random() * 28)
        mes2 = (int(mes) + (random.random() * (12 - int(mes))))

        if (dia == 0):
            dia = 1
        if (mes2 == 0):
            mes2 = 1
        if (dia < 10):
            dia = "0"+ str(dia)
        else:
            dia = str(dia)
        if (mes2 < 10):
            mes2 = "0"+ str(int(mes2))
        else:
            mes2 = str(int(mes2))
                
        date2 = (str(2023) + "-" + mes2 + "-" + dia)
        fechas.append([date1, date2])
    
    return fechas




#INSERT INTO projectschool.gradeletter (GradeID, GradeLetter, `Pass/Fail`)
#VALUES (1, 'A', 1);

def printing(apellidos, nombres, departamento, direcion, date, tema, nose, classNum, zoom, fechas):

    print("\nProfessors table:\n")
    print("\nINSERT INTO projectschool.teacher (LastName, FirstName, Department, Address, JoinDate)\nVALUES\n")
    for professor in range(1, cuantosProfesores ):
        print(" ('" + apellidos[professor] + "', '" + nombres[professor] + "','"+ departamento[professor] + "', '" + direcion[professor] + "', '" +  date[professor] + "'),")
    print("\n;")

    print("\nSubjects table: \n")
    print("\nINSERT INTO projectschool.subject (SubjectName, SubjectCollege)\nVALUES \n")
    for professor in range(1, cuantosProfesores ):
        print(" ('"+ tema[professor][0] + "', '" + tema[professor][1] + "'),")
    print("\n;")

    print("\nClass table: \n")
    print("\nINSERT INTO projectschool.class (ClassName, TeacherID, SubjectID)\nVALUES\n")
    for professor in range(1, cuantosProfesores ):
        x = int(random.random() * cuantosProfesores)
        y = int(random.random() * cuantosProfesores)

        if (x == 0):
            x = 1
        if (y == 0):
            y = 1

        print(" ('"+ classNum[professor] + "', " + str(x) + ", " + str(y) + "),")
    print("\n;")

    print("\nSchedule table: \n")
    print("\nINSERT INTO projectschool.schedule (ZoomLink, DateStart, DateEnd, ClassID)\nVALUES \n")
    for professor in range(1, cuantosProfesores):
        classId = int(random.random() * 40)
        if (classId == 0):
            classId = 1
        
        print(" ('" + zoom[professor] + "', '" + fechas[professor][0] + "', '" + fechas[professor][1] + "', " + str(classId) + ")," )
    print("\n;")

    return 0




#professor
apellidos = createProfessorLastName()
nombres = createProfessorName()
departamento = createDepartment()
direcion = createDirection()
dates = createProfessorDate()

#subject
topic = createTopic()
Nose = "Nose"
#Class
ClassName = createClassName()
#Schedule
zooom = createZoom()
fechas = createFechas()


printing(apellidos, nombres, departamento, direcion, dates, topic, Nose, ClassName, zooom, fechas)