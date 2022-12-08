from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    name = request.POST['height']
    students = ['inu', 'james', 'bob']

    if name in students:
        is_exist = True
    else:
        is_exist = False

    return render(request, 'index.html', {'user_name': name, 'is_exist':is_exist})

