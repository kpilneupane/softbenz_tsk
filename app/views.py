from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Student, Course, Enrollment



class Home(TemplateView):
    template_name = 'home.html'


class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        students = Student.objects.all()[:3]
        student_info = []
        
        for student in students:
            course_enrolled = student.get_enrolled_courses()
            student_info.append({
                'name': student.name,
                'email': student.email,
                'course': ', '.join(course_enrolled) if course_enrolled else 'Not Enrolled',
            })
        context['students'] = student_info
        context['courses'] = Course.objects.all()[:3]
        return context


def course_list(request):
    return render(request, 'home.html')



class StudentView(TemplateView):
    template_name = 'students.html'

    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        students = Student.objects.all()
        student_info = []
        for student in students:
            course_enrolled = student.get_enrolled_courses()
            student_info.append({
                'name': student.name,
                'email': student.email,
                'course': ', '.join(course_enrolled) if course_enrolled else 'Not Enrolled',
            })
        context['students'] = self.student_info
        return context


class CourseView(TemplateView):
    template_name = 'courses.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['courses'] = Course.objects.all()
        return context