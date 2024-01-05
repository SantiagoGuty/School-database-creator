import random

cuantosProfesores = 40 + 1

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
    "Gutierrez", "Pugh"
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
    for professor in range(1, cuantosProfesores+1):
        cual = int(len(temas) * random.random())
        topics.append(temas[cual])

    return topics



#INSERT INTO projectschool.subject (SubjectID, SubjectName, Subjectcol)
#VALUES (1, 'Discrete Math', 'Nose');
def printing(apellidos, nombres, departamento, direcion, date, tema, nose):

    print("\nProfessors table:\n")

    for professor in range(1, cuantosProfesores ):
        print("(" + str(professor) + ", \"" + apellidos[professor] + "\", \"" + nombres[professor] + "\",'"+ departamento[professor] + "', '" + direcion[professor] + "', '" +  date[professor] + "' ),")
    
    print("\nSubjects table: ")

    for professor in range(1, cuantosProfesores ):
        print("(" + str(professor) + ", \""+ tema[professor] + "\", " + nose + "),")
    
    return 0




#professor
apellidos = createProfessorLastName()
nombres = createProfessorName()
departamento = createDepartment()
direcion = createDirection()
dates = createProfessorDate()

#subject
topic = createTopic()

printing(apellidos, nombres, departamento, direcion, dates, topic, "Nose")