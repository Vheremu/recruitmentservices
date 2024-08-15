from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from accounts.forms import UserForm,UserProfileInfoForm
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    print(request.POST)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors , profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'accounts/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def user_login(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('someone tried to login and failed')
            fail=1
            my_dict={'fail':fail}
            return render(request,'accounts/login.html',context=my_dict)


    else:
        return render(request,'accounts/login.html',{})
        print('hello')