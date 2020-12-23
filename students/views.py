from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Schools, Students
from mydjango.forms import SchoolsForm, StudentsForm

# Create your views here.

def index(request):
    return render(request, 'master.html')

def students(request):
    students = Students.objects.all()
    return render(request, 'students.html', {"students": students})

def schools(request):
    schools = Schools.objects.all()
    return render(request, "schools.html", {'schools': schools})


def add_school(request):
    if request.method =="POST":
        form = SchoolsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/details')
            except():
                pass
    else:
        form = SchoolsForm()
    return render(request, 'schools/add-school.html', {'form': form, 'schools': schools})

def add_student(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except():
                pass
    else:
        form = StudentsForm()
    return render(request, 'students/add-student.html', {'students': Students.objects.all(), 'schools': Schools.objects.all(), 'form': form})