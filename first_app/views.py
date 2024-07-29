from django.shortcuts import render,redirect
from first_app.forms import User_form,user_change_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash


# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = User_form(request.POST)
            if form.is_valid():
                messages.success(request,"Account Created Successfully!")
                form.save()
                print(form.cleaned_data)
        else:
            form = User_form()
        return render(request,'sign_up.html',{"form":form})
    else:
        return redirect("profile_page")

def home(request):
    return render(request,'base.html')



def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request , data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = name,password = password) # check kortesi user data base a ase kina
                if user is not None:
                    login(request,user)
                    return redirect('profile_page')
        else:
            form = AuthenticationForm()
        
        return render(request,'login.html',{'form':form})   
    else:
        return redirect("profile_page")         


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = user_change_data(request.POST,instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request,"Account Update successfully!")
        else:
            form = user_change_data(instance=request.user)
        return render(request,'profile.html',{'form':form})
    else:
        return redirect("sing_up_page")
    
    
def log_out(request):
    
    logout(request)
    return redirect ("log_in_page")

#old pass word change
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user , data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect("profile_page")
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request,'pass_change.html',{'form':form})
    else:
        return redirect('log_in_page')

#without old password change
def pass_change_2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile_page')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request,'pass_change.html',{'form':form})
    else:
        return redirect("log_in_page")
    

