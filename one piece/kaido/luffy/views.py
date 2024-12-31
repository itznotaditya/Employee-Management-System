from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Employee
from django.shortcuts import get_object_or_404, redirect

def landing_page(request):
    return render(request, 'landing_page.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def employee_list(request):
    employees = Employee.objects.all()  
    return render(request, 'employee_list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        gender = request.POST['gender']
        designation = request.POST['designation']
        course = request.POST['course']
        image = request.FILES['image']


        fs = FileSystemStorage()
        image_name = fs.save(image.name, image)

        Employee.objects.create(
            name=name,
            email=email,
            mobile_number=mobile_number,
            gender=gender,
            designation=designation,
            course=course,
            image=image,
        )

        return redirect('employee_list')

    return render(request, 'add_employee.html')

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')
