from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    name = request.POST['username']
    students = ['inu', 'james', 'bob']

    if name in students:
        is_exist = True
    else:
        is_exist = False

    return render(request, 'result.html', {'user_name': name, 'is_exist':is_exist})