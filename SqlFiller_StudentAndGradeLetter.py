import random

cuantos = 20
cuantosProfesores = 50
nombreslista = [
    "Liam", "Valentina", "Thiago","Emma", "Noah",
    "Victoria", "Mateo", "Luna", "Sebastián", "Aurora",
	"Lucas", "Amaia", "Dylan", "Catalina", "Ian",
    "Mía", "Nicolás", "Milena", "Ethan", "Gianna",
    "Liam", "Olivia", "Noah", "Emma", "Oliver",
    "Charlotte","James","Amelia","Elijah","Sophia",
	"William","Isabella","Henry","Ava","Lucas",
    "Mia","Benjamin","Evelyn","Theodore","Luna",
    "Santiago", "Kole", "Faith","Gelber"
]

callesNombres = [

    "LaSalle","St monica","Salento","Mound St", "Chapell Hill", 
    "Topacio", "Magnificent Mile","Spoti", "Mijo", "Banat",
    "Parce","Ibague","Bogota","Melgar","Illinois St",
    "Second", "Third", "First", "Fourth","Park", "Urshell",
    "Cazzo", "Duki", "Fifi", "Choconta", "Guajira", "Whisky"
    "Tumaco", "Mor","Cuisine", "Colorado","Top", "Pana"
    "Valpo"
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
    "Gutierrez", "Pugh","Bargwell"
]


random.seed(len(nombreslista))



def createStudentName():

    students = []

    for student in range(1,cuantos + 1):

        cual = int(len(nombreslista) * random.random())
        students.append(nombreslista[cual])

    return students


def createStudentLastName():

    studentsLastNames = []

    for student in range(1, cuantos + 1):

        cual = int(len(apellidolista) * random.random())
        studentsLastNames.append(apellidolista[cual])
        
    return studentsLastNames

def createStudentDate():

    dates = []
    for student in range(1, cuantos+1):

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

        date = (str(int(2019 + random.random() * 4)) + "-" + mes + "-" + dia)
        dates.append(date)
        
    return dates

import random

def createDirection():
    directions = []

    for x in range(cuantos):
        street_number = str(random.randint(1, 5000))

        if x % 7 == 0:
            directions.append("Cr " + street_number + " " + random.choice(callesNombres))
            if x % 14 == 0:
                directions.append("Road " + street_number + " " + random.choice(callesNombres))
        else:
            random.shuffle(callesNombres)  # Shuffle the list of street names
            directions.append(street_number + " " + callesNombres[0])

    return directions



###def printing(nombres, apellidos):

   # for student in range(1, cuantos ):
    #    print("Student #" + str(student) + ": "+ nombres[student] + " " + apellidos[student])
    #return 0


def printing(nombres, apellidos, date, direccion):

    print("Students table:\n")
    print("\nINSERT INTO projectschool.student (LastName, FirstName, Address, JoinDate, GradeID)\nVALUES \n   \n")

    for student in range(1, cuantos ):
       # print(" (" + str(student) +", '" + apellidos[student] + "', '" + nombres[student] + "','"  + direccion[student] + "', '" + date[student] + "', "+ str(student) +"),")
        print(" ('"  + apellidos[student] + "', '" + nombres[student] + "','"  + direccion[student] + "', '" + date[student] + "', " + str(student) + "),")
    
    print("\n;")

    print("Grades table:\n")
    print("\nINSERT INTO projectschool.gradeletter (GradeLetter, `Pass/Fail`)\nVALUES \n")
    for student in range(1,cuantos):
        grade = 'A'
        paso = "Pass"
        gpa  = random.random() * 5
        if (gpa < 3.6):
            grade = 'B'
            if (gpa < 2.8):
                grade = 'C'
                if (gpa < 1.7):
                     grade = 'D'
                     if (gpa < 0.8):
                        grade = 'F'
        if (gpa < 1.7):
            paso = "Fail"

        print(" ( '" + grade + "', '"+ paso + "'),")

    print("\n;")
   
    print("\nStudent/Class table:\n")
    print("\nINSERT INTO projectschool.studentclass(ClassID,StudentID)\nVALUES \n")

    generated_combinations = set()

    for p in range(1, cuantos):
        while True:
            y = random.randrange(1, cuantosProfesores + 1)
            x = random.randrange(1, cuantos + 1)
            new_combination = (y, x)

            if new_combination not in generated_combinations:
                generated_combinations.add(new_combination)
                print(f"({y}, {x}),")
                break
        #print(" ("+ str(y) + ", " + str(x) + "),")
    print("\n;")

    return 0

cuantos = int(input("How many students does your school want? \n"))+1

nombres = createStudentName()
apellidos = createStudentLastName()
dates = createStudentDate()
direccion = createDirection()

#print(nombreslista[34] + " " + str(len(nombreslista)))
printing(nombres,apellidos,dates,direccion)
