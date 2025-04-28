class Course:
    name = ""
    average = None
    student_list  = []
  
    def show(self):
        print("{:<5}\taverage: {:>3}\n\tstudents: {}\n".format(self.name,self.average,self.student_list))

    ######################################################################
    # Task 1: define a method add_data(self, name, average, student_list)
    # that can assign data to the attributes name, average, studdent_list
    ######################################################################
    def add_data(self,in_name,in_average,in_student_list):
        self.name = in_name
        self.average = in_average
        self.student_list = in_student_list



file = open("data.csv", "r")

courses = []
line = file.readline()
while line:
    line_field = line.strip().split(",")

    ################################################################################
    # Task 2: create an object new_coure, and call the method add_data to
    # assign data to the attributes: name: 1st item in the line (course name),
    # average: 2nd item in the line (average score), student_list: the rest
    # of data in the line (student names)
    # NOTE: this is not a typical way to add data, we will learn the right way next week
    ################################################################################
    new_course = Course()
    new_course.add_data(line_field[0], line_field[1], line_field[2:])
      

    ####################################################################
    # Task 3: append the new_course object to the list courses
    ####################################################################



    line = file.readline()
file.close()

for course in courses:
    course.show()