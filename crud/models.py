from django.db import models


class User(models.Model):
    first_name = models.CharField(null=False, max_length=30)
    last_name = models.CharField(null=False, max_length=30)
    dob = models.DateTimeField(null=True, blank=True)
    country = models.CharField(null=True, max_length=20)
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    # class Meta:
    #     abstract = True


# Instructor model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return (
            f"First name: {self.first_name}, "
            f"Last name: {self.last_name}, "
            f"Is full time: {self.full_time}, "
            f"Total Learners: {self.total_learners},"
            f"Country: {self.country} "
        )

# Learner model
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

    def __str__(self):
        return (
            f"First name: {self.first_name}, "
            f"Last name: {self.last_name}, "
            f"Date of Birth: {self.dob}, "
            f"Occupation: {self.occupation}, "
            f"Social Link: {self.social_link}"
        )

# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    instructors = models.ManyToManyField(Instructor)
    learners = models.ManyToManyField(Learner, through='Enrollment')

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description} "

# Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)
