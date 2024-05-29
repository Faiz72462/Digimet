from django.shortcuts import render, HttpResponse, redirect
# from home.models import Contact
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
# from blog.models import Post
# Create your views here.
# signup view
def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse('password not match')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        





    return render(request,'signup.html')


# login view 

def Login(request):
    if request.method == 'POST':
        loginUname = request.POST.get('loginUsername')
        loginPass = request.POST.get('loginPassword')
        user = authenticate(username=loginUname, password=loginPass)
        if user is not None:
            login(request, user)
            messages.success(request, 'User successfully logged in')
            return redirect('base')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')  # Redirect back to the login page
    return render(request, 'login.html')



#base page
@login_required
def Base(request):
    return render(request,'base.html')



# homepage view
def Homepage(request):
    return render(request,'homepage.html')
    # return render(request,'homepage.html')