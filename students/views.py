from django.shortcuts import render

# Create your views here.




def students_index(request):
    return render(request, 'stud_temp/students.html')


def students2_index(request):
    return render(request, 'stud_temp/students2.html')