from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from django.contrib import messages
from .models import Student
from django.views.decorators.http import require_POST

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_edit.html', {'form': form, 'student': student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'student_create.html', {'form': form})

@require_POST
def student_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        messages.success(request, 'Student deleted successfully.')
    except Student.DoesNotExist:
        messages.error(request, 'Student not found.')
    return redirect('student_list')