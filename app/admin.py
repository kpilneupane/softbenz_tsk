from django.contrib import admin
from .models import Course, Student, Enrollment


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


admin.site.register(Course, CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Student, StudentAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')


admin.site.register(Enrollment, EnrollmentAdmin)
