from .models import Schools, Student
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SchoolForm, StudentForm

# Create your views here.


def school(request):

    schools = Schools.objects.all()
    name=None

    if 'searchname' in request.GET:
        name = request.GET.get("searchname")
        if name:
            schools = Schools.objects.filter(name__icontains=name)

    context = {

        'school':schools
}
    
    return render(request, 'school/school.html',context)


def school_desc(request, school_id):
    all_schools = Schools.objects.all()
    school = get_object_or_404(Schools, pk=school_id)
    # students = Student.objects.filter(school=school)

    context = {
        'school': school,
        # 'students': students,
        'all_schools': all_schools,
    }

    # Render the 'school_desc.html' template and return it as an HttpResponse
    return render(request, 'school/school_desc.html', context)
    

def search(request):
    
    return render(request, 'school/search.html')


def all_schools(request):

    context = {
        'school':Schools.objects.all()
    }
    return render (request,'school/all_schools.html', context)

def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_schools')
    else:
        form = SchoolForm()

    context = {
        'form': form,
    }
    return render(request, 'school/create_school.html', context)


def school_students(request, school_id):
    school = get_object_or_404(Schools, pk=school_id)
    students = Student.objects.filter(school=school)  # Get students associated with the school

    context = {
        'school': school,
        'students': students,
    }

    return render(request, 'school/school_students.html', context)

def add_student(request, school_id):
    school = get_object_or_404(Schools, pk=school_id)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.school = school
            student.save()
            return redirect('school_students', school_id=school_id)

    else:
        form = StudentForm()
        # Filter the queryset for the 'school' field
        form.fields['school'].queryset = Schools.objects.filter(id=school_id)

    context = {
        'school': school,
        'form': form,
    }

    return render(request, 'school/add_student.html', context)





