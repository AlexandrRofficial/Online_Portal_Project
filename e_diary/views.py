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

        # Беремо введені бали
        points_str = request.POST.get("points", "0")

        # Перетворюємо у число — навіть якщо пусто або текст
        try:
            points = int(points_str)
        except (ValueError, TypeError):
            points = 0

        student = get_object_or_404(Student, id=student_id)

        # Переконуємось, що logics точно int
        try:
            current_logics = int(student.logics)
        except (ValueError, TypeError):
            current_logics = 0

        # Додаємо
        student.logics = current_logics + points
        student.save()

        return redirect('students')

    return render(request, 'add_logics.html', {'students': students})