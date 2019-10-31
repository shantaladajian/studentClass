class Assignment:

    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.grade = 0

    def __str__(self):
        return self.title + ": " + self.deadline + ": " + str(self.grade)

    def setGrade(self, grade):
        self.grade = grade

class Course:
    def __init__(self, ID):
        self.ID = ID
        self.assignments = []

    def __str__(self):
        return self.ID

    def addAssignment(self, title, deadline):
        assignment = Assignment(title, deadline)
        self.assignments.append(assignment)


    def getAssignment(self, title):
        for item in self.assignments:
            if item.title == title:
                return item
        return None

class Student:

    def __init__(self, Fname, Lname, ID):
        self.Fname = Fname
        self.Lname = Lname
        self.ID = ID
        self.courses = []

    def __str__(self):
        return self.getFullName() + ": " + self.ID

    def getFullName(self):
        return self.Fname + " " + self.Lname

    def addCourse(self, ID):
        course = Course(ID)
        self.courses.append(course)

    def addAssignment(self, cID, title, deadline):
        course = self.getCourse(cID)
        if course != None:
            course.addAssignment(title, deadline)
        else:
            print("The course", cID, "does not exist for this student")

    def getCourse(self, ID):
        for item in self.courses:
            if item.ID == ID:
                return item
        return None

    def getAssignment(self, cID, title):
        course = self.getCourse(cID)
        return course.getAssignment(title)

    def addGrade(self,cID,atitle,adeadline,grade):
        course=self.getCourse(cID)
        if course != None:
            assignment=self.getAssignment(cID,atitle)
            assignment.setGrade(grade)

def main():
    my_student = Student("Artur", "Sargsyan", "AUA234")
    print(my_student)

    #Adding Courses
    my_student.addCourse("ENGS115")
    print(my_student.getCourse("ENGS115"))
    print(my_student.getCourse("ENGS105"))

    #Adding assignment
    my_student.addAssignment("ENGS115", "Implement Browser History Using Stack", "2019-10-31")
    print(my_student.getAssignment("ENGS115", "Implement Browser History Using Stack"))

    #Adding grades
    my_student.addGrade("ENGS115","Implement Browser History Using Stack","2019-10-31","90")
    print(my_student.getAssignment("ENGS115", "Implement Browser History Using Stack"))
main()