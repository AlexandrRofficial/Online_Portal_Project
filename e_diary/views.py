from django.shortcuts import render, redirect , get_object_or_404
from .models import Student
from .forms import StudentForm

def students_list(request):
    students = Student.objects.all()
    return render(request, 'e_diary.html', {'students': students})



def add_logics(request):
    students = Student.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student")
        points_str = request.POST.get("points", "0")  # беремо рядок
        try:
            points = str(points_str)  # перетворюємо на int
        except ValueError:
            points = 0  # якщо введено некоректне число

        student = get_object_or_404(Student, id=student_id)

        if student.logics is None:
            student.logics = 0  # якщо поле пусте

        student.logics += points
        student.save()
        return redirect('students')

    return render(request, 'add_logics.html', {'students': students})
