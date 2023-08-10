from datetime import datetime
from crud.models import *


# def run():
#     # Add instructors
#     # Create a user
#     user = User(first_name='Tichalla', last_name='Pather', dob=datetime(1962, 7, 16))
#     user.save()
#     instructor = Instructor(full_time=True, total_learners=30050)
#     # Update the user reference of instructor_john to be user_john
#     instructor.user = user
#     instructor.save()
    
#     instructor = Instructor(first_name='Hulk', last_name='Benner', dob=datetime(1962, 7, 16), full_time=True, total_learners=30050, country='U.S.A')
#     instructor.save()

#     instructor = Instructor(first_name='Charlie', last_name='Sheen', dob=datetime(1992, 1, 2), full_time=False, total_learners=10040, country='South Africa')
#     instructor.save()

#     instructor= Instructor(first_name='Peter', last_name='Griffein', dob=datetime(1982, 5, 2), full_time=True, total_learners=2002, country='U.S.A')
#     instructor.save()

#     instructor= Instructor(first_name='Django', last_name='Libre', dob=datetime(1976, 8, 9), full_time=True, total_learners=2002, country='Brazil')
#     instructor.save()
#     print("Instructor objects all saved... ")


# def run():
# # Add Courses
#     course = Course(name="Cloud Application Development with Database",
#                             description="Develop and deploy application on cloud")
#     course.save()
#     course = Course(name="Introduction to Python",
#                         description="Learn core concepts of Python and obtain hands-on "
#                                     "experience via a capstone project")
#     course .save()

#     print("Course objects all saved... ")


# def run():
#     # Add Learners
#     learner = Learner(first_name='Jimmy', last_name='Page', dob=datetime(1982, 7, 16),
#                             occupation='data_scientist',
#                             social_link='https://www.linkedin.com/jim/')
#     learner.save()
#     learner = Learner(first_name='Mary', last_name='Jane', dob=datetime(1991, 6, 12), occupation='dba',
#                            social_link='https://www.facebook.com/mary/')
#     learner.save()
#     learner = Learner(first_name='Bruce', last_name='Dickson', dob=datetime(1999, 1, 2), occupation='student',
#                              social_link='https://www.facebook.com/bd/')
#     learner.save()
#     learner = Learner(first_name='Ozzy', last_name='Osbourne', dob=datetime(1983, 7, 16),
#                             occupation='developer',
#                             social_link='https://www.linkedin.com/ozzy/')
#     learner.save()
#     learner = Learner(first_name='John', last_name='Wick', dob=datetime(1986, 3, 16),
#                            occupation='developer',
#                            social_link='https://www.linkedin.com/jw/')
#     learner.save()
#     print("Learner objects all saved... ")



# def run():
#     lesson = Lesson(title='Lesson 1', content="Object-relational mapping project")
#     lesson.save()
#     lesson = Lesson(title='Lesson 2', content="Django development project")
#     lesson.save()
#     print("Lesson objects all saved... ")

# def run():
#     #Delete all data to start from fresh
#     Enrollment.objects.all().delete()
#     User.objects.all().delete()
#     Learner.objects.all().delete()
#     Instructor.objects.all().delete()
#     Course.objects.all().delete()
#     Lesson.objects.all().delete()
#     print(f"All data was deleted...")
