from models import * 

# Course has instructors reference field so can be used directly via forward access
courses = Course.objects.filter(instructors__first_name='Yan')
print("1. Get courses taught by Instructor `Yan`, forward")
print(courses)

print("\n")
# For each instructor, Django creates a implicit course_set. This is caleld backward access
instructor_yan = Instructor.objects.get(first_name='Yan')
print("1. Get courses taught by Instructor `Yan`, backward")
print(instructor_yan.course_set.all())

print("\n")
instructors = Instructor.objects.filter(course__name__contains='Cloud')
print("2. Get the instructors of Cloud app dev course")
print(instructors)

print("\n")
courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print("3. Check the occupations of the courses taught by instructor Yan'")
print(occupation_list)

# Results

# 1. Get courses taught by Instructor `Yan`, forward
# <QuerySet [<Course: Name: Cloud Application Development with Database,Description: Develop and deploy application on cloud>]>

# 1. Get courses taught by Instructor `Yan`, backward
# <QuerySet [<Course: Name: Cloud Application Development with Database,Description: Develop and deploy application on cloud>]>

# 2. Get the instructors of Cloud app dev course
# <QuerySet [<Instructor: First name: Yan, Last name: Luo, Is full time: True, Total Learners: 30050>, <Instructor: First name: Joy, Last name: Li, Is full time: False, Total Learners: 10040>]>

# 3. Check the occupations of the courses taught by instructor Yan'
# {'dba', 'data_scientist', 'developer'}

print("1. Get the user information about learner `David`")
learner_david = Learner.objects.get(first_name="David")
print( #<HINT> use the usr_ptr field created by Django for the Inheritance relationship# )

print("2. Get learner `David` information from user")
user_david = User.objects.get(first_name="David")
print( #<HINT> use the learner field created by Django# )

print("3. Get all learners for `Introduction to Python` course")
course = Course.objects.get(name='Introduction to Python')
learners = #<HINT> use the learners field in Course model# 
print(learners)

print("4. Check the occupation list for the courses taught by instructor `Yan`")
courses = Course.objects.filter( #<HINT> query the first name of instructor# )
occupation_list = set()
for course in courses:
    for learner in #<HINT>use the learners field in Course Model#  :
        occupation_list.add(learner.occupation)
print(occupation_list)

print("5. Check which courses developers are enrolled in Aug, 2020")  
enrollments = Enrollment.objects.filter(date_enrolled__month=8,
                                            date_enrolled__year=2020,
                                            #<HINT>use the occupation field from learner #)
courses_for_developers = set()
for enrollment in enrollments:
    course = enrollment.course
    courses_for_developers.add(course.name)
print(courses_for_developers)

learner_david = Learner.objects.get(first_name="David")
print("1. Get the user information about learner `David`")
print(learner_david.user_ptr)
user_david = User.objects.get(first_name="David")
print("2. Get learner `David` information from user")
print(user_david.learner)

course = Course.objects.get(name='Introduction to Python')
learners = course.learners.all()
print("3. Get all learners for `Introduction to Python` course")
print(learners)

courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print("4. Check the occupation list for the courses taught by instructor `Yan`")
print(occupation_list)

enrollments = Enrollment.objects.filter(date_enrolled__month=8,
                                            date_enrolled__year=2020,
                                            learner__occupation='developer')
courses_for_developers = set()
for enrollment in enrollments:
    course = enrollment.course
    courses_for_developers.add(course.name)
print("5. Check which courses developers are enrolled in Aug, 2020")    
print(courses_for_developers)

# Results 

# 1. Get the user information about learner `David`
# David Smith

# 2. Get learner `David` information from user
# First name: David, Last name: Smith, Date of Birth: 1983-07-16, Occupation: developer, Social Link: https://www.linkedin.com/david/

# 3. Get all learners for `Introduction to Python` course
# <QuerySet [<Learner: First name: Robert, Last name: Lee, Date of Birth: 1999-01-02, Occupation: student, Social Link: https://www.facebook.com/robert/>]>
# 4. Check the occupation list for the courses taught by instructor `Yan`
# {'data_scientist', 'developer', 'dba'}

# 5. Check which courses developers are enrolled in Aug, 2020
# {'Cloud Application Development with Database'}