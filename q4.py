class Course:
    name = ""
    average = None
    student_list = []

courses = []
file = open("data.csv", "r")
line = file.readline()
while line:
    line_field = line.strip().split(",")
    print(line_field)

    ####################################################################
    # Task 1: create an object new_course with the name attribute being
    # the first item in the line (course name), the average attribute being
    # the second item in the line (average score) but as a float number, the 
    # student_list attribute storing the rest of data in the line (student names)
    ####################################################################
    new_course = Course()
    new_course.name= line_field[0]
    new_course.average = line_field[1]
    new_course.student_list = line_field[2:]

     

    ####################################################################
    # Task 2: append the new_course object to courses
    ####################################################################
    courses.append(new_course)


    # continue to read the next line
    line = file.readline()
file.close()


#######################################################################
# Task 3: print data in the format below using the list courses
# Math 	  average:75.3
#         students: ['Bill', 'Alan']
#
# Java 	  average:88.9
#         students: ['Joe']
#
# Python  average:95.0
#         students: ['Mary', 'Alan', 'Jack']
#
# C++  	  average:78.0
#         students: ['Mark', 'Yohan']
#######################################################################
for course in courses:
    print('{:7}\taverage:{:>3}\n\t{}'.format(course.name, course.average, course.average, course.student_list))


