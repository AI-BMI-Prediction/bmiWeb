from django.shortcuts import render

# Create your views here.

def index(request):

    if request.method =='GET':
        return render(request, 'index.html')

    elif request.method =='POST':

        height = request.POST['height']
        weight = request.POST['weight']
        step_count = request.POST['step_count']
        calorie_intake = request.POST['calorie_intake']
        burned_calorie = request.POST['burned_calorie']
        sleep = request.POST['sleep']

        context = {
            'height': height,
            'weight': weight,
            'step_count': step_count,
            'calorie_intake': calorie_intake,
            'burned_calorie': burned_calorie,
            'sleep': sleep,
        }

        return render(request, 'index.html', context)


