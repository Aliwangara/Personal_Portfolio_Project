from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def handleLogIn(request):
    return render(request, 'LogIn.html')


def handleLogOut(request):
    return render(request, 'LogOut.html')


def signup(request):
    if request.method == "POST" :
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')

        print(get_email)
        print(get_password)
        print(get_confirm_password)


    return render(request, 'signup.html'),
