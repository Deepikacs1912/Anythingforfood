from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
# from .forms import UpdateProfileForm, UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

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