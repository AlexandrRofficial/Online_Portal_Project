from django.shortcuts import render, redirect , get_object_or_404
from .models import Student
from .forms import StudentForm

def students_list(request):
    students = Student.objects.all()
    return render(request, 'e_diary.html', {'students': students})

def add_logic(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.logic_points += 1
    student.save()
    return redirect('students')