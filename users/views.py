from django.shortcuts import render,redirect
from users.forms import SignupForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def my_profile(request):
    return render(request, 'my-profile.html')    

def services(request):
    return render(request, 'services.html')    

def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('Invalid form data. Please try again.')


    return render(request, 'shop-registration.html')    
