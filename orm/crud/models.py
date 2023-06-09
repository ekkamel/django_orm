from django.db import models


# Create your models here.

# User model 
class User(models.Model): 
    first_name = models.CharField(null=False, max_length=30, default='John')
    last_name = models.CharField(null=False, max_length=30, default='Doe')
    dob = models.DateField(null=True)

    # Create a toString method for objects string representation
    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Instructor model  (inherited from User an extension to it)
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for objects string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "is full time: " + str(self.full_time) + ", " + \
               "Total Learners: " + str(self.total_learners)

# Learner model - Inherited from User - Needs to be defined before Course
class Learner(User): 
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False, 
        max_length=20, 
        choices=OCCUPATION_CHOICES, 
        default=STUDENT
    )
    social_link = models.URLField(max_length=200)

    # Create a toString method for objects string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Date of Birth: " + str(self.dob) + ", " + \
               "Occupation: " + self.occupation + ", " + \
               "Social Link: " + self.social_link


# Course model Many-to-Many relationship with Instructor
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)

    # Many-to-many relationship with instructor 
    instructors = models.ManyToManyField(Instructor)

    # Many-to-Many relationship with Learner via Enrollment relationship
    Learners = models.ManyToManyField(Learner, through='Enrollment')

    # create a toString method for object string representation 
    def __str__(self):
        return "Name: " + self.name  + "," + \
            "Description: " + self.description

# Lesson model  One-to-Many relationship with Course
class Lesson(models.Model):
    title = models.CharField(max_length=200, default='title')
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()


# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODE = [
        (AUDIT, 'Audit'), 
        (HONOR, 'Honor'),
    ]

    # Add a learner foreign key 
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)

    # Add acourse foreign key 
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Enrollment Date 
    date_enrolled = models.DateField(auto_now_add=True)

    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODE, default=AUDIT)

    # Add Many-to-Many relationship between course and learner


