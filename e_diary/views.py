from django.shortcuts import render, redirect , get_object_or_404
from .models import Student
from .forms import StudentForm

def students_list(request):
    students = Student.objects.all()
    return render(request, 'e_diary.html', {'students': students})


def add_logics(request):
    students = Student.objects.all()

    if request.method == "POST":
        student_ids = request.POST.getlist("students")  # <-- getlist для мультивибору
        points_str = request.POST.get("points", "0")

        try:
            points = int(points_str)
        except (ValueError, TypeError):
            points = 0

        for sid in student_ids:
            student = Student.objects.filter(id=sid).first()
            if student:
                try:
                    current_logics = int(student.logics)
                except (ValueError, TypeError):
                    current_logics = 0
                student.logics = current_logics + points
                student.save()

        return redirect('students')

    return render(request, 'add_logics.html', {'students': students})



def add_new_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    return render(request, 'add_new_student.html', {'form': form})



def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')  # назад до списку
    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {"form": form, "student": student})