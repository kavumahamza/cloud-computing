from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'tasks/home.html')

def login_user(request):
    return render(request, 'tasks/login.html')

def index(request):
    return render(request, 'tasks/dashboard.html')

def sign_up(request):
    return render(request, 'tasks/sign_up.html')

def create_task(request):
    return render(request, 'tasks/add_task.html')

def create_new_task(request):
    return render(request, 'tasks/add_task.html')

def updateTask(request):
    return render(request, 'tasks/update_task.html')

def updatePlan(request):
    return render(request, 'tasks/update_plan.html')

def deleteViewTask(request):
    return render(request, 'tasks/delete_task.html')

def deleteViewPlan(request):
    return render(request, 'tasks/delete_plan.html')

def deleteTask(request):
    return redirect('dashboard')

def deletePlan(request):
    return redirect('dashboard')

def statistics(request):
    return render(request, 'tasks/statistics.html')

def task_list(request):
    return render(request, 'tasks/task_list.html')

def createPlan(request):
    return render(request, 'tasks/add_plan.html')

def task_view(request):
    return render(request, 'tasks/task_view.html')

def logoutUser(request):
    return redirect('login')

def forgot_password(request):
    return render(request, 'tasks/forgot_password.html')