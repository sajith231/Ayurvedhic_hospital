from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    return render(request, 'app1/index.html')

def about(request):
    return render(request, 'app1/about.html')

def gallery(request):
    return render(request,'app1/gallery.html')



def doctor(request):
    return render(request,'app1/doctor.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('doctor')  # Redirect to doctor.html page (doctor view)
        else:
            # Invalid login or non-superuser
            return render(request, 'login.html', {'error': 'Invalid login credentials or you are not a superuser.'})
    
    return render(request, 'login.html')



from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')  # Make sure this matches your home page URL name
    return redirect('index')  # Also redirect GET requests to home instead of returning 405