from _ast import Pass
from email import message

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from main.models import Contacts, Blogs


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method=="POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        fPhoneno= request.POST.get("num")
        fdescription= request.POST.get("desc")
        query = Contacts(name = fname, email = femail, phonenumber = fPhoneno, description = fdescription)
        query.save()
        messages.success(request, "Thanks for contacting. I will get back to you soon!")
        return redirect('/contact')

    return render(request, 'contact.html')

def handleblog(request):
    posts = Blogs.objects.all()
    context= {'posts':posts}
    return render(request, 'handleblog.html', context)


def handleLogIn(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser = authenticate (username = get_email, password = get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")

    return render(request, 'LogIn.html')


def handleLogOut(request):
    logout(request)
    messages.success(request,"Logout success")
    return render(request, 'LogIn.html')


def signup(request, ):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request, 'Password not matching')
            return redirect('/SignUp/')


        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email is already Taken")
                return redirect('/SignUp/')

        except Exception as identifier:
            Pass

        myuser = User.objects.create_user(get_email, get_email, get_password)
        myuser.save()
        messages.success(request, "user created please login")
        return redirect('/LogIn/')
    return render(request, "signup.html")


