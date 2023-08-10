from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)

# class LessonInline(admin.StackedInline):
#     model = Lesson 
#     extra = 5

# class CourseAdmin(admin.ModelAdmin):
#     fields = ['name', 'description']
#     inlines = [LessonInline]
# admin.site.register(Course, CourseAdmin)


# class InstructorAdmin(admin.ModelAdmin):
#     fields = ['user', 'full_time']
# admin.site.register(Instructor, InstructorAdmin)
