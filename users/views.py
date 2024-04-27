from django.shortcuts import render,redirect
from users.forms import SignupForm
from  django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def my_profile(request):
    return render(request, 'my-profile.html')    

def services(request):
    return render(request, 'services.html')    



def shop_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'shop-login.html')    



def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

        # Direct login from Registration
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            return redirect('home')

        else:
            print('Invalid form data. Please try again.')


    return render(request, 'shop-registration.html')    
