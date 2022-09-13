from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# from .forms import UpdateProfileForm, UserRegistrationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')
@login_required(login_url='login')
def home(request):
    return render(request, 'users/home.html')
def registerpage(request):
    # form=UserCreationForm()
    form=CreateUserForm()
    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=CreateUserForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            user=form.cleaned_data.get('email')
            messages.success(request,"Account is craeted for "+user)
            return redirect('login')
    context={'form':form}
    return render(request,'users/register.html',context)
def loginpage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Email or password incorrect")
            return redirect('login')
    context={}
    return render(request,'users/login.html',context)

@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('logout')
# def Login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             form = login(request, user)
#             messages.success(request, f' welcome {username} !!')
            
#             return redirect('home')
#         else:
#             messages.info(request, f'account done not exit plz sign in')
#     form = AuthenticationForm()
#     return render(request, 'user/login.html', {'form':form, 'title':'log in'})

# def register(request):
#     if request.method=='POST':
#         form=UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your account has been created. You can log in now!') 
              
#             return redirect('login')
#     else:
#         form =UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'User/register.html', context)

# # @login_required
# def profile(request):
#     if request.method=='POST':
#         profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request,'Your profile is updated successfully')
#             return redirect('profile')
#     else:
#         profile_form=UpdateProfileForm(instance=request.user.profile)
#     return render(request,'User/profile.html',{'profile_form':profile_form})